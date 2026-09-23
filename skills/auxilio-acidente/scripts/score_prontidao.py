#!/usr/bin/env python3
"""
Indice de Prontidao Probatoria (IPP) para auxilio-acidente.

Uso:
  python score_prontidao.py --exemplo > caso.json      # gera o template preenchivel
  python score_prontidao.py caso.json                  # calcula, lista lacunas e projeta ganho

Cada item aceita: "cheio", "parcial", "zero" ou "na" (nao aplicavel).
Itens "na" tem seus pontos redistribuidos proporcionalmente entre os itens aplicaveis do
mesmo bloco, de modo que o total do bloco permaneca estavel.

Bloqueios fatais: se algum for true, a recomendacao final e "nao protocolar", qualquer que
seja a pontuacao.
"""

import argparse
import json

BLOCOS = {
    "A": {
        "nome": "Qualidade de segurado e enquadramento",
        "total": 20,
        "itens": {
            "A1": ("Categoria dentro do rol do art. 18, par. 1o, na data do evento", 8,
                   "Confirmar categoria (empregado, avulso, domestico, especial) por documento"),
            "A2": ("Qualidade de segurado documentada na data do evento", 7,
                   "Extrair CNIS, CTPS ou cadastro rural do periodo do evento"),
            "A3": ("Teste do periodo de graca de vinculo anterior, se fora do rol hoje", 3,
                   "Levantar data de rescisao do ultimo vinculo elegivel e comparar com a data do evento"),
            "A4": ("Coerencia entre CNIS e categoria alegada", 2,
                   "Conferir e explicar qualquer divergencia"),
        },
    },
    "B": {
        "nome": "Nexo tecnico e fato gerador",
        "total": 25,
        "itens": {
            "B1": ("CAT emitida e coerente com o relato", 8,
                   "Obter CAT, ou emitir por via alternativa (sindicato, medico, proprio segurado)"),
            "B2": ("Nexo demonstrado por outros meios, se nao ha CAT", 7,
                   "Reunir NTEP, PPP ou laudo tecnico relacionando atividade e lesao"),
            "B3": ("Categoria do fato gerador definida", 5,
                   "Classificar acidente de qualquer natureza ou ocupacional; documentar nexo entre evento e sequela em ambos"),
            "B4": ("Testemunhas do evento ou da atividade", 5,
                   "Identificar duas ou mais testemunhas idoneas"),
        },
    },
    "C": {
        "nome": "Sequela, prova medica e reducao",
        "total": 30,
        "itens": {
            "C1": ("Lesao consolidada, com data definida", 10,
                   "Obter laudo ou relatorio medico que confirme a consolidacao e a data"),
            "C2": ("Laudos, exames e prontuarios reunidos", 8,
                   "Reunir conjunto documental cobrindo diagnostico e evolucao"),
            "C3": ("Descricao funcional especifica da reducao de capacidade", 7,
                   "Nova entrevista focada em tarefas concretas do trabalho habitual"),
            "C4": ("Compatibilidade com o Anexo III ou fundamentacao fora dele", 5,
                   "Verificar o Anexo III do Decreto 3.048/99 e fundamentar caso a sequela nao conste"),
        },
    },
    "D": {
        "nome": "Prova documental complementar",
        "total": 15,
        "itens": {
            "D1": ("Historico de auxilio-doenca com datas", 6,
                   "Confirmar datas de inicio e cessacao por extrato do CNIS"),
            "D2": ("PPP, PCMSO, PGR ou laudos ambientais, se doenca ocupacional", 5,
                   "Solicitar documentos a empresa ou ao sindicato"),
            "D3": ("Prova rural complementar, se aplicavel", 4,
                   "Reunir autodeclaracao, CAF ou cadastro do art. 38-A"),
        },
    },
    "E": {
        "nome": "Calculo, cumulacao e riscos",
        "total": 10,
        "itens": {
            "E1": ("Base de calculo apurada", 4,
                   "Estimar o salario de beneficio com CNIS ou HISCRE"),
            "E2": ("Cumulacao analisada", 3,
                   "Aplicar o teste da Sumula 507/STJ se houver aposentadoria no horizonte"),
            "E3": ("Bloqueios fatais checados", 3,
                   "Rodar a lista de alertas criticos da secao 8 do SKILL.md"),
        },
    },
}

BLOQUEIOS = {
    "fora_do_rol_sem_excecao": "Categoria fora do rol do art. 18, par. 1o, sem excecao aplicavel (V1)",
    "sem_qualidade_de_segurado": "Ausencia de qualidade de segurado na categoria elegivel, na data do evento (V2)",
    "lesao_nao_consolidada": "Lesao ainda nao consolidada (V3)",
    "sem_reducao_constatavel": "Ausencia de qualquer reducao de capacidade constatavel (V4)",
    "nexo_inexistente": "Nexo tecnico inexistente ou fortemente contestavel (V5)",
}

VALORES = {"cheio": 1.0, "parcial": 0.5, "zero": 0.0}


def template():
    caso = {
        "caso": "Nome ou apelido do caso",
        "enquadramento": "urbano | rural | avulso | domestico",
        "natureza": None,
        "data_evento": "AAAA-MM-DD",
        "data_consolidacao": "AAAA-MM-DD ou 'em curso'",
        "itens": {},
        "justificativas_na": {},
        "bloqueios": {k: None for k in BLOQUEIOS},
    }
    for bloco in BLOCOS.values():
        for cod in bloco["itens"]:
            caso["itens"][cod] = "zero"
    return caso


def validar_caso(caso):
    if not isinstance(caso.get("itens"), dict):
        raise ValueError("itens deve ser objeto")
    conhecidos = {cod for b in BLOCOS.values() for cod in b["itens"]}
    if set(caso["itens"]) - conhecidos:
        raise ValueError("codigo de item desconhecido")
    for cod, estado in caso["itens"].items():
        if estado not in (*VALORES, "na"):
            raise ValueError("estado invalido: " + cod)
        if estado == "na" and (cod in ['A1', 'A2', 'C1', 'C3'] or not caso.get("justificativas_na", {}).get(cod)):
            raise ValueError("na exige justificativa e nao pode excluir requisito essencial: " + cod)
    bloqueios = caso.get("bloqueios", {})
    if not isinstance(bloqueios, dict) or set(bloqueios) - set(BLOQUEIOS):
        raise ValueError("bloqueios invalidos")
    if any(v is not None and type(v) is not bool for v in bloqueios.values()):
        raise ValueError("bloqueios aceitam apenas true, false ou null")


def pontuar(caso):
    validar_caso(caso)
    if caso.get("natureza") not in ("comum", "ocupacional"):
        raise ValueError("definir natureza comum ou ocupacional")
    if caso["natureza"] == "comum":
        caso = dict(caso, itens=dict(caso["itens"]))
        caso["itens"]["B1"] = "na"
        caso["itens"]["B2"] = "na"
    resultado = {}
    lacunas = []
    for letra, bloco in BLOCOS.items():
        aplicaveis = {}
        for cod, (nome, peso, acao) in bloco["itens"].items():
            estado = caso["itens"].get(cod, "zero")
            if estado == "na":
                continue
            aplicaveis[cod] = (nome, peso, acao, estado)
        peso_total = sum(v[1] for v in aplicaveis.values()) or 1
        fator = bloco["total"] / peso_total
        obtido = 0.0
        for cod, (nome, peso, acao, estado) in aplicaveis.items():
            peso_ajustado = peso * fator
            ganho = peso_ajustado * VALORES.get(estado, 0.0)
            obtido += ganho
            if estado != "cheio":
                lacunas.append({
                    "codigo": cod,
                    "nome": nome,
                    "estado": estado,
                    "pontos_atuais": round(ganho, 1),
                    "pontos_possiveis": round(peso_ajustado, 1),
                    "ganho": round(peso_ajustado - ganho, 1),
                    "acao": acao,
                })
        resultado[letra] = (round(obtido, 1), bloco["total"], bloco["nome"])
    total = round(sum(v[0] for v in resultado.values()), 1)
    lacunas.sort(key=lambda x: x["ganho"], reverse=True)
    return total, resultado, lacunas


def faixa(total):
    if total >= 85:
        return "caso maduro", "Submeter a revisao juridica antes de definir a via"
    if total >= 70:
        return "protocolavel com risco controlado", "Revisar lacunas e requisitos essenciais antes de protocolar"
    if total >= 50:
        return "instrucao insuficiente", "Diligenciar antes. A analise documental previa (Portaria 15/2026) pode indeferir sem pericia"
    if total >= 30:
        return "caso fragil", "Reunir prova medica e de nexo. Avaliar se a lesao ainda nao consolidou"
    return "inviavel no estado atual", "Reavaliar a tese e informar o cliente com clareza"


def main():
    ap = argparse.ArgumentParser(description="Indice de Prontidao Probatoria - auxilio-acidente")
    ap.add_argument("arquivo", nargs="?", help="JSON do caso")
    ap.add_argument("--exemplo", action="store_true", help="imprime o template JSON")
    args = ap.parse_args()

    if args.exemplo or not args.arquivo:
        print(json.dumps(template(), indent=2, ensure_ascii=False))
        return

    with open(args.arquivo, encoding="utf-8") as fh:
        caso = json.load(fh)

    total, resultado, lacunas = pontuar(caso)
    rotulo, conduta = faixa(total)

    print("=" * 62)
    print(f"INDICE DE PRONTIDAO PROBATORIA  |  {caso.get('caso', 'sem nome')}")
    print(f"Enquadramento: {caso.get('enquadramento', 'nao informado')}   "
          f"Evento: {caso.get('data_evento', 'nao informado')}   "
          f"Consolidacao: {caso.get('data_consolidacao', 'nao informado')}")
    print("=" * 62)
    print(f"\nIPP: {total}/100  ({rotulo})\n")
    for letra in "ABCDE":
        obtido, maximo, nome = resultado[letra]
        barra = "#" * int(round(obtido / maximo * 20)) if maximo else ""
        print(f"  {letra} {nome:<38} {obtido:>5}/{maximo:<3} {barra}")

    desconhecidos = [k for k in BLOQUEIOS if caso.get("bloqueios", {}).get(k) is None]
    ativos = [BLOQUEIOS[k] for k, v in caso.get("bloqueios", {}).items() if v and k in BLOQUEIOS]
    if desconhecidos:
        print("\nBLOQUEADO PARA USO FINAL: verificar " + ", ".join(desconhecidos))
    if ativos:
        print("\n*** BLOQUEIOS FATAIS DETECTADOS ***")
        for b in ativos:
            print(f"  - {b}")
        print("\nRECOMENDACAO: NAO PROTOCOLAR. Reavaliar a tese antes de qualquer providencia.")
    elif not desconhecidos:
        print(f"\nRECOMENDACAO: {conduta}. Score nao autoriza protocolo nem tutela; aplicar os quatro portoes.")

    if lacunas:
        print("\nLACUNAS PRIORITARIAS")
        projecao = total
        for i, l in enumerate(lacunas[:5], 1):
            print(f"  {i}. [{l['codigo']}] {l['nome']}  "
                  f"({l['pontos_atuais']}/{l['pontos_possiveis']}, ganho +{l['ganho']})")
            print(f"     Como suprir: {l['acao']}")
            if i <= 3:
                projecao += l["ganho"]
        print(f"\nIPP projetado apos as 3 primeiras diligencias: {round(projecao, 1)} "
              f"({faixa(projecao)[0]})")
    else:
        print("\nSem lacunas. Caso completo.")


if __name__ == "__main__":
    main()
