#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diagnostico.py — Calculadora determinística para casos de salário-maternidade (RGPS).

Por que existe: contagem de período de graça e de prescrição com suspensão administrativa
é onde o caso se perde por aritmética, não por direito. Cálculo determinístico exige entradas e enquadramento verificados; este script também tem limites.

Uso:
    python3 diagnostico.py --interativo
    python3 diagnostico.py --json caso.json
    python3 diagnostico.py --exemplo

Contrato JSON: obrigatórios fato_gerador, categoria, data_referencia, salario_minimo e teto_rgps.
Para art. 73, III, usar salarios_competencias com competencia YYYY-MM, valor_atualizado,
atualizacao_confirmada=true e fonte. Lista legada sem competências não gera RMI.
Exemplo ilustrativo (parâmetros precisam corresponder à data-base):

{
  "nome": "Cliente Exemplo",
  "data_referencia": "2026-09-23",
  "fato_gerador": "2024-08-15",
  "tipo_fato_gerador": "parto",          # parto | natimorto | aborto | adocao | guarda
  "categoria": "contribuinte_individual", # ver CATEGORIAS abaixo
  "ultima_contribuicao": "2023-11-30",   # competência da última contribuição/vínculo
  "contribuicoes_totais": 45,            # nº de contribuições sem perda de qualidade intercalada
  "desemprego_involuntario": true,
  "der": "2024-09-10",                   # data do requerimento administrativo
  "ciencia_decisao": "2024-12-02",       # ciência do indeferimento
  "ajuizamento": "2026-03-01",           # data do ajuizamento (ou hoje, se ainda não ajuizou)
  "salarios_contribuicao": [1412.0, 1412.0, 1500.0],  # últimos SC, do mais recente ao mais antigo
  "remuneracao_mensal": 3200.0,          # para empregada/avulsa/doméstica
  "internacao_dias": 0,
  "alta_hospitalar": null,               # "YYYY-MM-DD" — a mais tardia entre mãe e bebê
  "salario_minimo": 1621.00,
  "teto_rgps": 8475.55
}

AVISO: os parâmetros salario_minimo e teto_rgps são [VOLÁTIL]. Confirme antes de usar em peça.
"""

from __future__ import annotations

import argparse
import math
from decimal import Decimal, ROUND_HALF_UP
import json
import sys
from dataclasses import dataclass, field
from datetime import date, timedelta

# ---------------------------------------------------------------------------
# Parâmetros [VOLÁTIL] — conferir em janeiro de cada ano
# ---------------------------------------------------------------------------
SALARIO_MINIMO_PADRAO = 1621.00   # Decreto 12.797/2025 (2026)
TETO_RGPS_PADRAO = 8475.55        # Portaria Interministerial MPS/MF nº 13/2026
ALCADA_JEF_SM = 60

CATEGORIAS = {
    "empregada": "Empregada (CLT)",
    "empregada_rural": "Empregada rural registrada",
    "domestica": "Empregada doméstica",
    "avulsa": "Trabalhadora avulsa",
    "mei": "Microempreendedora individual",
    "contribuinte_individual": "Contribuinte individual",
    "facultativa": "Segurada facultativa",
    "desempregada": "Desempregada em período de graça",
    "segurada_especial": "Segurada especial (rural)",
}

DURACAO_DIAS = {
    "parto": 120,
    "natimorto": 120,
    "aborto": 14,
    "adocao": 120,
    "guarda": 120,
}

PAGADOR = {
    "empregada": "Empresa, com compensação (art. 72, § 1º) — salvo adoção e dispensa na gravidez",
    "empregada_rural": "Empresa, com compensação (art. 72, § 1º)",
    "domestica": "INSS (art. 73, I)",
    "avulsa": "INSS",
    "mei": "INSS",
    "contribuinte_individual": "INSS",
    "facultativa": "INSS",
    "desempregada": "INSS (Tema 113/TNU)",
    "segurada_especial": "INSS",
}


def brl(valor: float) -> str:
    """Formata em padrão brasileiro: 1.621,00"""
    return f"{valor:,.2f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def d(valor) -> date | None:
    """Converte 'YYYY-MM-DD' em date. Aceita None."""
    if valor is None or valor == "":
        return None
    if isinstance(valor, date):
        return valor
    return date.fromisoformat(str(valor).strip())


def fim_do_mes(dt: date) -> date:
    """Último dia do mês de dt."""
    if dt.month == 12:
        return date(dt.year, 12, 31)
    return date(dt.year, dt.month + 1, 1) - timedelta(days=1)


def soma_meses(dt: date, meses: int) -> date:
    """Soma meses preservando o fim de mês quando necessário."""
    total = dt.month - 1 + meses
    ano = dt.year + total // 12
    mes = total % 12 + 1
    ultimo = fim_do_mes(date(ano, mes, 1)).day
    return date(ano, mes, min(dt.day, ultimo))


def validar_entrada(dados):
    for key in ('fato_gerador', 'categoria', 'data_referencia', 'salario_minimo', 'teto_rgps'):
        if dados.get(key) is None:
            raise ValueError('campo obrigatório: ' + key)
    if dados['categoria'] not in CATEGORIAS:
        raise ValueError('categoria desconhecida')
    if dados.get('tipo_fato_gerador', 'parto') not in DURACAO_DIAS:
        raise ValueError('tipo de fato gerador desconhecido')
    for key in ('desemprego_involuntario', 'nexo_internacao_confirmado'):
        if key in dados and type(dados[key]) is not bool:
            raise ValueError(key + ' exige booleano JSON, não texto')
    for key in ('salario_minimo', 'teto_rgps', 'remuneracao_mensal'):
        if dados.get(key) is not None:
            val = dados[key]
            if isinstance(val, bool) or not math.isfinite(float(val)) or float(val) <= 0:
                raise ValueError(key + ' deve ser positivo e finito')
    for valor in dados.get("salarios_contribuicao", []):
        if isinstance(valor, bool) or not math.isfinite(float(valor)) or float(valor) < 0:
            raise ValueError("salário de contribuição inválido")
    if float(dados['teto_rgps']) < float(dados['salario_minimo']):
        raise ValueError('teto inferior ao piso')
    for key in ('internacao_dias', 'dias_antes_parto', 'contribuicoes_totais'):
        val = dados.get(key, 0)
        if type(val) is not int or val < 0:
            raise ValueError(key + ' exige inteiro não negativo')
    if dados.get('dias_antes_parto', 0) > 120:
        raise ValueError('dias anteriores excedem duração')
    ref, evento = d(dados['data_referencia']), d(dados['fato_gerador'])
    if evento > ref:
        raise ValueError('evento futuro: usar planejamento, não diagnóstico de fato ocorrido')
    for key in ('der', 'ciencia_decisao', 'ajuizamento', 'alta_hospitalar', 'ultima_contribuicao'):
        dt = d(dados.get(key))
        if dt and dt > ref:
            raise ValueError(key + ' posterior à data de referência')
    der, ciencia = d(dados.get('der')), d(dados.get('ciencia_decisao'))
    if ciencia and (not der or ciencia < der):
        raise ValueError('ciência exige DER anterior ou igual')
    if dados.get('alta_hospitalar') and d(dados['alta_hospitalar']) < evento:
        raise ValueError('alta anterior ao parto')


# ---------------------------------------------------------------------------
@dataclass
class Caso:
    fato_gerador: date
    nome: str = "—"
    tipo_fato_gerador: str = "parto"
    categoria: str = "desconhecida"
    ultima_contribuicao: date | None = None
    contribuicoes_totais: int = 0
    desemprego_involuntario: bool = False
    der: date | None = None
    ciencia_decisao: date | None = None
    ajuizamento: date | None = None
    salarios_contribuicao: list[float] = field(default_factory=list)
    remuneracao_mensal: float | None = None
    internacao_dias: int = 0
    alta_hospitalar: date | None = None
    salario_minimo: float | None = None
    teto_rgps: float | None = None
    data_referencia: date | None = None
    salarios_competencias: list[dict] = field(default_factory=list)
    dias_antes_parto: int = 0
    nexo_internacao_confirmado: bool = False
    feriados: list[date] = field(default_factory=list)

    @staticmethod
    def de_dict(dados: dict) -> "Caso":
        validar_entrada(dados)
        return Caso(
            fato_gerador=d(dados["fato_gerador"]),
            nome=dados.get("nome", "—"),
            tipo_fato_gerador=dados.get("tipo_fato_gerador", "parto"),
            categoria=dados["categoria"],
            ultima_contribuicao=d(dados.get("ultima_contribuicao")),
            contribuicoes_totais=int(dados.get("contribuicoes_totais", 0) or 0),
            desemprego_involuntario=dados.get("desemprego_involuntario", False),
            der=d(dados.get("der")),
            ciencia_decisao=d(dados.get("ciencia_decisao")),
            ajuizamento=d(dados.get("ajuizamento")),
            salarios_contribuicao=[float(x) for x in dados.get("salarios_contribuicao", [])],
            remuneracao_mensal=(float(dados["remuneracao_mensal"])
                                if dados.get("remuneracao_mensal") else None),
            internacao_dias=int(dados.get("internacao_dias", 0) or 0),
            alta_hospitalar=d(dados.get("alta_hospitalar")),
            salario_minimo=float(dados["salario_minimo"]),
            teto_rgps=float(dados["teto_rgps"]),
            data_referencia=d(dados["data_referencia"]),
            salarios_competencias=dados.get("salarios_competencias", []),
            dias_antes_parto=dados.get("dias_antes_parto", 0),
            nexo_internacao_confirmado=dados.get("nexo_internacao_confirmado", False),
            feriados=[d(x) for x in dados.get("feriados", [])],
        )


# ---------------------------------------------------------------------------
def calcular_periodo_graca(c: Caso) -> dict:
    """
    Art. 15 da Lei 8.213/91 + art. 30, II, da Lei 8.212/91.
    O prazo conta a partir do fim do mês seguinte ao término do período de manutenção.
    """
    if c.ultima_contribuicao is None:
        return {"aplicavel": False,
                "observacao": "Data da última contribuição/vínculo não informada."}

    base = 6 if c.categoria == "facultativa" else 12
    detalhe = [f"Base do art. 15: {base} meses ({'facultativa' if base == 6 else 'regra geral'})"]

    if c.categoria != "facultativa" and c.contribuicoes_totais > 120:
        base += 12
        detalhe.append("+12 meses — mais de 120 contribuições sem perda intercalada (art. 15, § 1º)")

    if c.desemprego_involuntario and c.categoria != "facultativa":
        base += 12
        detalhe.append("+12 meses — desemprego involuntário comprovado (art. 15, § 2º; Tema 19/TNU)")

    fim_manutencao = soma_meses(fim_do_mes(c.ultima_contribuicao), base)
    # extensão do art. 30, II, da Lei 8.212/91: até o dia 15 do 2º mês seguinte
    segundo_mes = soma_meses(fim_manutencao, 2)
    limite = date(segundo_mes.year, segundo_mes.month, 15)
    while limite.weekday() >= 5 or limite in c.feriados:
        limite += timedelta(days=1)

    mantida = c.fato_gerador <= limite
    return {
        "aplicavel": True,
        "meses_totais": base,
        "detalhamento": detalhe,
        "fim_da_manutencao": fim_manutencao.isoformat(),
        "limite_com_extensao_art_30_II": limite.isoformat(),
        "qualidade_mantida_no_fato_gerador": mantida,
        "margem_dias": (limite - c.fato_gerador).days,
        "calendario": "Feriados dependem da lista informada; conferir vencimento antes de concluir perda.",
    }


def calcular_prescricao(c: Caso) -> dict:
    """
    Art. 103, parágrafo único, da Lei 8.213/91.
    Suspensão pelo requerimento administrativo: Súmula 74/TNU + Decreto 20.910/1932, arts. 4º e 5º.
    """
    referencia = c.ajuizamento or c.data_referencia
    if referencia is None:
        raise ValueError("data_referencia obrigatória")
    consumido_1 = None
    consumido_2 = None

    if c.der and c.der >= c.fato_gerador:
        consumido_1 = (c.der - c.fato_gerador).days
        retomada = c.ciencia_decisao or referencia
        consumido_2 = max(0, (referencia - retomada).days) if c.ciencia_decisao else 0
        total = consumido_1 + consumido_2
        suspensao_dias = ((c.ciencia_decisao - c.der).days if c.ciencia_decisao
                          else (referencia - c.der).days)
    else:
        total = (referencia - c.fato_gerador).days
        suspensao_dias = 0

    limite = (soma_meses(c.fato_gerador, 60) - c.fato_gerador).days
    return {
        "data_referencia": referencia.isoformat(),
        "houve_suspensao": bool(c.der),
        "dias_ate_a_der": consumido_1,
        "dias_de_suspensao": suspensao_dias,
        "dias_apos_a_ciencia": consumido_2,
        "prazo_consumido_dias": total,
        "prazo_consumido_anos": round(total / 365.25, 2),
        "prescrito": None,
        "dias_restantes": max(0, limite - total),
        "alerta": "[CONFERIR] estimativa desde o evento; apurar vencimento de cada parcela, capacidade e causas de suspensão. Não conclui prescrição de todas as parcelas.",
    }


def calcular_rmi(c: Caso) -> dict:
    """RMI conforme arts. 72 e 73 da Lei 8.213/91 e Tema 202/TNU."""
    sm, teto = c.salario_minimo, c.teto_rgps
    if sm is None or teto is None:
        raise ValueError("informar piso e teto da data-base")
    base_legal = ""
    valor = None
    observacoes: list[str] = []

    if c.categoria in ("empregada", "empregada_rural", "avulsa"):
        base_legal = "art. 72 — remuneração integral (se variável, média dos 6 últimos)"
        valor = c.remuneracao_mensal
    elif c.categoria == "domestica":
        base_legal = "art. 73, I — último salário de contribuição"
        valor = c.remuneracao_mensal or (c.salarios_contribuicao[0]
                                         if c.salarios_contribuicao else None)
    elif c.categoria == "mei":
        base_legal = "MEI — 1 salário mínimo; complemento de alíquota sobre a mesma base não aumenta a RMI"
        valor = sm
    elif c.categoria == "segurada_especial":
        base_legal = "art. 39, parágrafo único — 1 salário mínimo"
        valor = sm
    elif c.categoria in ("contribuinte_individual", "facultativa", "desempregada"):
        base_legal = "art. 73, III — 1/12 da soma dos 12 últimos SC (período máx. 15 meses)"
        if c.categoria == "desempregada":
            observacoes.append(
                "Tema 202/TNU: ainda que a última vinculação tenha sido como EMPREGADA, "
                "aplica-se o art. 73, III — e não a remuneração integral do art. 72."
            )
        if c.salarios_competencias:
            limite = soma_meses(date(c.fato_gerador.year, c.fato_gerador.month, 1), -15)
            fim = date(c.fato_gerador.year, c.fato_gerador.month, 1)
            usados = []
            vistos = set()
            for item in c.salarios_competencias:
                competencia = date.fromisoformat(item['competencia'] + '-01')
                if competencia in vistos:
                    raise ValueError('competência duplicada; consolidar atividades antes do cálculo')
                vistos.add(competencia)
                if not limite <= competencia < fim:
                    raise ValueError('competência fora da janela de 15 meses anterior ao evento')
                if item.get('atualizacao_confirmada') is not True or not item.get('fonte'):
                    raise ValueError('salário sem atualização/fonte confirmada')
                val = Decimal(str(item['valor_atualizado']))
                if not val.is_finite() or val < 0:
                    raise ValueError('salário inválido')
                usados.append((competencia, val))
            usados.sort(reverse=True)
            valor = float(sum(v for _, v in usados[:12]) / Decimal(12))
            observacoes.append('Divisor fixo 12; até 12 SC verificados na janela de 15 meses.')
        elif c.salarios_contribuicao:
            observacoes.append('[CONFERIR] lista sem competências não permite verificar janela ou atualização; RMI bloqueada.')

    if valor is None:
        return {"base_legal": base_legal, "rmi": None,
                "observacoes": observacoes + ["Dados insuficientes para calcular a RMI."]}

    rmi = valor
    if rmi < sm:
        observacoes.append(
            f"Valor apurado (R$ {brl(valor)}) inferior ao piso; elevado ao salário mínimo "
            "(CF art. 201, § 2º; art. 73 da Lei 8.213/91)."
        )
        rmi = sm
    if rmi > teto and c.categoria not in ("empregada", "empregada_rural", "avulsa"):
        observacoes.append(f"Valor apurado (R$ {brl(valor)}) acima do teto; limitado.")
        rmi = teto

    if c.categoria in ("empregada", "empregada_rural", "avulsa"):
        observacoes.append("Remuneração integral sem teto RGPS; conferir limite constitucional aplicável e verbas variáveis.")
    dias = DURACAO_DIAS.get(c.tipo_fato_gerador, 120)
    if c.internacao_dias > 14:
        observacoes.append("Total abaixo cobre apenas duração ordinária; extensão hospitalar exige liquidação separada.")
    total = rmi * (dias / 30.0)

    return {
        "base_legal": base_legal,
        "rmi": round(rmi, 2),
        "dias": dias,
        "valor_total_estimado": round(total, 2),
        "piso": sm,
        "teto": teto,
        "observacoes": observacoes,
    }


def calcular_duracao(c: Caso) -> dict:
    """Duração, com a regra da Lei 15.222/2025 (art. 71, § 3º)."""
    dias = DURACAO_DIAS.get(c.tipo_fato_gerador, 120)
    r = {"dias_regra_geral": dias, "regra_internacao_aplicavel": False}

    if c.internacao_dias > 14 and c.tipo_fato_gerador in ("parto", "natimorto"):
        r["regra_internacao_aplicavel"] = True
        r["fundamento"] = ("Lei 15.222/2025 — art. 71, § 3º, da Lei 8.213/91 e art. 392, § 7º, "
                           "da CLT; ADI 6.327/STF")
        r["efeito"] = ("Benefício devido durante todo o período de internação E por mais 120 dias "
                       "após a alta (a mais tardia entre mãe e recém-nascido), descontado o tempo "
                       "de recebimento anterior ao parto.")
        if c.alta_hospitalar and c.nexo_internacao_confirmado:
            r["dcb_estimada"] = (c.alta_hospitalar + timedelta(days=120 - c.dias_antes_parto)).isoformat()
            r["nota_contagem"] = "Estimativa exclui dia da alta no acréscimo; conferir DIB/DCB administrativas e dias pagos."
        else:
            r["efeito"] += " [CONFERIR] faltam alta ou nexo comprovado; não fixar DCB."
        r["prova_necessaria"] = ("Relatório hospitalar com datas de entrada e alta de mãe e bebê + "
                                 "declaração médica estabelecendo o NEXO com o parto.")
    elif c.internacao_dias > 0:
        r["nota"] = (f"Internação de {c.internacao_dias} dia(s) — abaixo do gatilho de 2 semanas "
                     "do art. 71, § 3º. Reconferir as datas.")
    return r


def calcular_art_73a(c: Caso) -> dict:
    """Art. 73-A da Lei 8.213/91 (Lei 15.415/2026)."""
    vigencia = date(2026, 5, 26)
    paga_inss = c.categoria not in ("empregada", "empregada_rural")

    if not c.der:
        return {"aplicavel": False, "motivo": "DER não informada."}
    if not paga_inss and c.tipo_fato_gerador not in ("adocao", "guarda"):
        return {"aplicavel": False,
                "motivo": "Benefício pago pela empresa; o art. 73-A alcança apenas o pago "
                          "diretamente pela Previdência."}
    if c.der < vigencia:
        return {"aplicavel": False,
                "motivo": f"DER anterior a {vigencia.isoformat()} (vigência da Lei 15.415/2026). "
                          "Aplicação a requerimentos pendentes é discutível. [VOLÁTIL]"}

    if c.ciencia_decisao:
        return {"aplicavel": False, "motivo": "Já há decisão comunicada; examinar tempestividade e efeitos concretos, sem presumir mora atual."}
    prazo = c.der + timedelta(days=30)
    hoje = c.data_referencia
    if hoje is None:
        raise ValueError("data_referencia obrigatória")
    return {
        "aplicavel": True,
        "prazo_final_para_decisao": prazo.isoformat(),
        "prazo_vencido": hoje > prazo,
        "dias_restantes": max(0, (prazo - hoje).days),
        "efeito_do_descumprimento": ("Concessão PROVISÓRIA e AUTOMÁTICA (art. 73-A, § 1º). "
                                     "Valores não são devolvidos, salvo má-fé."),
        "acao_sugerida": ("Requerimento administrativo de implementação citando o art. 73-A; "
                          "se negado ou ignorado, mandado de segurança."),
    }


def avaliar_semaforo(c: Caso, graca: dict, presc: dict) -> dict:
    riscos, sinal = [], "🟢 VERDE"

    if presc["prescrito"]:
        return {"sinal": "🔴 VERMELHO",
                "riscos": ["Prescrição consumada de todas as parcelas."]}

    if presc["dias_restantes"] < 180:
        sinal = "🟡 AMARELO"
        riscos.append(f"Prescrição próxima: {presc['dias_restantes']} dia(s) restantes.")

    if graca.get("aplicavel"):
        if not graca["qualidade_mantida_no_fato_gerador"]:
            sinal = "🔴 VERMELHO"
            riscos.append(
                "Qualidade de segurada aparentemente NÃO mantida na data do fato gerador. "
                "Verificar vínculos ausentes no CNIS e prorrogações do art. 15."
            )
        elif graca["margem_dias"] < 60:
            if sinal != "🔴 VERMELHO":
                sinal = "🟡 AMARELO"
            riscos.append(f"Margem estreita no período de graça: {graca['margem_dias']} dia(s).")
    else:
        sinal = "🟡 AMARELO"
        riscos.append("Última contribuição não informada — qualidade de segurada não verificada.")

    if c.categoria == "facultativa":
        if sinal == "🟢 VERDE":
            sinal = "🟡 AMARELO"
        riscos.append(
            "Facultativa: Resolução CRPS 13/2026 exige filiação REGULARMENTE CONSTITUÍDA antes "
            "do fato gerador. Conferir a data da primeira contribuição válida."
        )

    if c.categoria == "segurada_especial":
        if sinal == "🟢 VERDE":
            sinal = "🟡 AMARELO"
        riscos.append(
            "Segurada especial: o caso se decide na prova material (Súmula 149/STJ). "
            "Comprovar qualidade/atividade no regime aplicável; não confundir janela de prova com carência abolida."
        )

    if not c.der:
        sinal = "🟡 AMARELO"
        riscos.append("Sem DER: triagem possível; verificar necessidade de prévio requerimento e exceções antes de judicializar (Tema 350/STF).")

    return {"sinal": sinal, "riscos": riscos or ["Nenhum risco crítico identificado."]}


def varredura_passivo(c: Caso) -> list[str]:
    achados = []
    if c.tipo_fato_gerador == "aborto":
        achados.append("Confirmar se é ABORTO (14 dias) ou NATIMORTO (120 dias). "
                       "Se há declaração de óbito fetal, são 120 dias — diferença de 106 dias.")
    if c.internacao_dias > 14:
        achados.append("Lei 15.222/2025: benefício durante a internação + 120 dias após a alta. "
                       "Vale também retroativamente, via ADI 6.327, dentro da prescrição.")
    if c.categoria in ("empregada", "empregada_rural"):
        achados.append("Verificar desconto da cota da segurada sobre o salário-maternidade nos "
                       "holerites → repetição de indébito (Tema 72/STF por analogia; "
                       "Tema 1.274/STF pendente).")
        achados.append("Se houve dispensa na gravidez: Enunciado CRPS nº 6 (INSS paga) + "
                       "estabilidade gestante (ADCT art. 10, II, 'b') — duas frentes.")
    if c.categoria in ("contribuinte_individual", "facultativa", "mei", "segurada_especial"):
        achados.append("Se houve indeferimento anterior por CARÊNCIA: revisão pós-ADI 2.110/2.111 "
                       "(IN 188/2025, art. 200, § 4º) — requerimentos feitos ou pendentes desde "
                       "05/04/2024, independentemente da data do fato gerador.")
    if c.tipo_fato_gerador in ("adocao", "guarda"):
        achados.append("Adoção/guarda: pagamento SEMPRE pelo INSS (art. 71-A, § 1º), inclusive "
                       "para empregada CLT.")
    achados.append("Verificar atividades concomitantes: possível salário-maternidade POR ATIVIDADE.")
    return achados


# ---------------------------------------------------------------------------
def relatorio(c: Caso) -> str:
    graca = calcular_periodo_graca(c)
    presc = calcular_prescricao(c)
    rmi = calcular_rmi(c)
    dur = calcular_duracao(c)
    art73a = calcular_art_73a(c)
    sem = avaliar_semaforo(c, graca, presc)
    if rmi["rmi"] is None or presc["prescrito"] is None:
        if sem["sinal"] == "🟢 VERDE":
            sem["sinal"] = "🟡 AMARELO"
        sem["riscos"] = [x for x in sem["riscos"] if x != "Nenhum risco crítico identificado."]
        sem["riscos"].append("Conclusão parcial: conferir RMI, prescrição por parcela e portões antes de uso final.")

    L = []
    add = L.append
    add("=" * 74)
    add("DIAGNÓSTICO — SALÁRIO-MATERNIDADE")
    add("=" * 74)
    add(f"Cliente: {c.nome}")
    add(f"Categoria: {CATEGORIAS.get(c.categoria, c.categoria)}")
    add(f"Fato gerador: {c.tipo_fato_gerador} em {c.fato_gerador.isoformat()}")
    add(f"Quem paga: {PAGADOR.get(c.categoria, '—')}")
    add("")
    add(f"SEMÁFORO: {sem['sinal']}")
    for r in sem["riscos"]:
        add(f"  • {r}")
    add("")
    add("-" * 74)
    add("1. QUALIDADE DE SEGURADA — art. 15 da Lei 8.213/91")
    add("-" * 74)
    if graca.get("aplicavel"):
        for det in graca["detalhamento"]:
            add(f"  {det}")
        add(f"  Total: {graca['meses_totais']} meses")
        add(f"  Fim da manutenção: {graca['fim_da_manutencao']}")
        add(f"  Limite com extensão (art. 30, II, Lei 8.212/91): "
            f"{graca['limite_com_extensao_art_30_II']}")
        add(f"  Qualidade mantida no fato gerador: "
            f"{'SIM' if graca['qualidade_mantida_no_fato_gerador'] else 'NÃO'}")
        add(f"  Margem: {graca['margem_dias']} dia(s)")
    else:
        add(f"  {graca['observacao']}")
    add("")
    add("-" * 74)
    add("2. PRESCRIÇÃO — art. 103, p.ú.; Súmula 74/TNU; Dec. 20.910/32, arts. 4º e 5º")
    add("-" * 74)
    add(f"  Referência: {presc['data_referencia']}")
    add(f"  Houve suspensão administrativa: {'SIM' if presc['houve_suspensao'] else 'NÃO'}")
    if presc["dias_ate_a_der"] is not None:
        add(f"  Dias consumidos até a DER: {presc['dias_ate_a_der']}")
        add(f"  Dias de suspensão: {presc['dias_de_suspensao']}")
        add(f"  Dias após a ciência: {presc['dias_apos_a_ciencia']}")
    add(f"  Prazo consumido: {presc['prazo_consumido_dias']} dias "
        f"({presc['prazo_consumido_anos']} anos)")
    add(f"  Dias restantes: {presc['dias_restantes']}")
    add(f"  >>> {presc['alerta']}")
    add("")
    add("-" * 74)
    add("3. DURAÇÃO")
    add("-" * 74)
    add(f"  Regra geral: {dur['dias_regra_geral']} dias")
    if dur["regra_internacao_aplicavel"]:
        add(f"  APLICÁVEL: {dur['fundamento']}")
        add(f"  Efeito: {dur['efeito']}")
        if "dcb_estimada" in dur:
            add(f"  DCB estimada: {dur['dcb_estimada']}")
        add(f"  Prova: {dur['prova_necessaria']}")
    elif "nota" in dur:
        add(f"  {dur['nota']}")
    add("")
    add("-" * 74)
    add("4. RENDA MENSAL INICIAL")
    add("-" * 74)
    add(f"  Base legal: {rmi['base_legal']}")
    if rmi["rmi"] is not None:
        add(f"  RMI estimada: R$ {brl(rmi['rmi'])}")
        add(f"  Valor total estimado ({rmi['dias']} dias): R$ {brl(rmi['valor_total_estimado'])}")
        add(f"  Piso: R$ {brl(rmi['piso'])}  |  Teto: R$ {brl(rmi['teto'])}   [VOLÁTIL]")
    for o in rmi["observacoes"]:
        add(f"  • {o}")
    add("")
    add("-" * 74)
    add("5. ART. 73-A — PRAZO DE 30 DIAS (Lei 15.415/2026)")
    add("-" * 74)
    if art73a["aplicavel"]:
        add(f"  Prazo final para decisão: {art73a['prazo_final_para_decisao']}")
        add(f"  Prazo vencido: {'SIM' if art73a['prazo_vencido'] else 'NÃO'} "
            f"({art73a['dias_restantes']} dia(s) restantes)")
        add(f"  Efeito: {art73a['efeito_do_descumprimento']}")
        add(f"  Ação: {art73a['acao_sugerida']}")
    else:
        add(f"  Não aplicável — {art73a['motivo']}")
    add("")
    add("-" * 74)
    add("6. VARREDURA DE PASSIVO")
    add("-" * 74)
    for i, a in enumerate(varredura_passivo(c), 1):
        add(f"  {i}. {a}")
    add("")
    add("=" * 74)
    add("AVISO: cálculo auxiliar. Confira parâmetros [VOLÁTIL] e valide o caso concreto.")
    add("=" * 74)
    return "\n".join(L)


def interativo() -> Caso:
    print("Diagnóstico de salário-maternidade — deixe em branco o que não souber.\n")

    def perg(rotulo, padrao=""):
        r = input(f"{rotulo}{f' [{padrao}]' if padrao else ''}: ").strip()
        return r or padrao

    dados = {
        "nome": perg("Nome da cliente", "—"),
        "fato_gerador": perg("Data do fato gerador (AAAA-MM-DD)"),
        "tipo_fato_gerador": perg("Tipo (parto/natimorto/aborto/adocao/guarda)", "parto"),
        "categoria": perg(f"Categoria ({'/'.join(CATEGORIAS)})", "contribuinte_individual"),
        "ultima_contribuicao": perg("Última contribuição/vínculo (AAAA-MM-DD)") or None,
        "contribuicoes_totais": int(perg("Total de contribuições", "0")),
        "desemprego_involuntario": perg("Desemprego involuntário comprovado? (s/n)", "n").lower() == "s",
        "der": perg("DER (AAAA-MM-DD)") or None,
        "ciencia_decisao": perg("Ciência da decisão (AAAA-MM-DD)") or None,
        "ajuizamento": perg("Ajuizamento/data de referência (AAAA-MM-DD)") or None,
        "remuneracao_mensal": perg("Remuneração mensal (R$)") or None,
        "internacao_dias": int(perg("Dias de internação ligada ao parto", "0")),
        "data_referencia": perg("Data de referência (AAAA-MM-DD)"),
        "salario_minimo": perg("Salário mínimo da data-base (R$)"),
        "teto_rgps": perg("Teto da data-base (R$)"),
        "alta_hospitalar": perg("Alta hospitalar mais tardia (AAAA-MM-DD)") or None,
    }
    sc = perg("Salários de contribuição, do mais recente ao mais antigo (separados por vírgula)")
    if sc:
        dados["salarios_contribuicao"] = [float(x.strip().replace(",", "."))
                                          for x in sc.split(",") if x.strip()]
    return Caso.de_dict(dados)


EXEMPLO = {
    "nome": "Exemplo — CI em período de graça",
    "fato_gerador": "2024-08-15",
    "tipo_fato_gerador": "parto",
    "categoria": "contribuinte_individual",
    "ultima_contribuicao": "2023-11-30",
    "contribuicoes_totais": 45,
    "desemprego_involuntario": False,
    "der": "2024-09-10",
    "ciencia_decisao": "2024-12-02",
    "ajuizamento": "2026-03-01",
    "salarios_contribuicao": [1412.0] * 12,
    "internacao_dias": 0,
    "data_referencia": "2026-03-01",
    "salario_minimo": 1412.0,
    "teto_rgps": 7786.02,
}


def main() -> int:
    p = argparse.ArgumentParser(description="Diagnóstico de salário-maternidade (RGPS).")
    p.add_argument("--json", help="Arquivo JSON com os dados do caso")
    p.add_argument("--interativo", action="store_true", help="Coleta os dados no terminal")
    p.add_argument("--exemplo", action="store_true", help="Roda um caso de demonstração")
    a = p.parse_args()

    try:
        if a.exemplo:
            caso = Caso.de_dict(EXEMPLO)
        elif a.json:
            with open(a.json, encoding="utf-8") as f:
                caso = Caso.de_dict(json.load(f))
        elif a.interativo:
            caso = interativo()
        else:
            p.print_help()
            return 1
    except (KeyError, ValueError) as e:
        print(f"Erro nos dados de entrada: {e}", file=sys.stderr)
        return 2

    try:
        print(relatorio(caso))
    except (ValueError, TypeError, KeyError) as e:
        print(f"[CONFERIR] {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
