#!/usr/bin/env python3
"""
Indice de Prontidao do Caso (IPC) para pensao por morte.

Uso:
  python3 score_prontidao.py --exemplo > caso.json      # gera o template preenchivel
  python3 score_prontidao.py caso.json                  # calcula, lista lacunas e projeta ganho

Cada item aceita: "cheio", "parcial", "zero" ou "na" (nao aplicavel).
Itens "na" tem seus pontos redistribuidos proporcionalmente entre os itens aplicaveis do
mesmo bloco, de modo que o total do bloco permaneca estavel.

Bloqueios fatais: se algum for true, a recomendacao final e "nao protocolar", qualquer que
seja a pontuacao.
"""

import argparse
import json
import sys

BLOCOS = {
    "A": {
        "nome": "Evento morte e legitimacao",
        "total": 15,
        "itens": {
            "A1": ("Certidao de obito em maos", 5,
                   "Solicitar 2a via em cartorio ou via Registro Civil online"),
            "A2": ("Causa da morte documentada", 4,
                   "Buscar laudo do IML, CAT, boletim de ocorrencia ou prontuario"),
            "A3": ("Legitimidade e classe do requerente definidas", 3,
                   "Obter certidao que comprove a relacao e conferir a classe do art. 16"),
            "A4": ("Mapeamento de outros habilitados", 3,
                   "Consultar certidoes, CNIS, processos de familia e a propria certidao de obito"),
        },
    },
    "B": {
        "nome": "Qualidade de segurado do falecido",
        "total": 25,
        "itens": {
            "B1": ("CNIS completo e conferido", 6,
                   "Extrair CNIS e HISCRE por procuracao no Meu INSS"),
            "B2": ("Vinculo, contribuicao ou atividade rural na data do obito", 8,
                   "Conferir ultima competencia, beneficio ativo ou prova de atividade rural"),
            "B3": ("Prorrogacao do periodo de graca documentada", 5,
                   "Reunir prova de desemprego involuntario (Tema 1.360/STJ) ou de 120 contribuicoes"),
            "B4": ("Vinculos ausentes do CNIS mapeados", 3,
                   "Levantar CTPS fisica, acoes trabalhistas, holerites e periodos rurais"),
            "B5": ("Direito adquirido a aposentadoria em vida apurado", 3,
                   "Simular todas as aposentadorias possiveis na data da perda da qualidade"),
        },
    },
    "C": {
        "nome": "Qualidade de dependente",
        "total": 25,
        "itens": {
            "C1": ("Documento formal da relacao", 8,
                   "Certidao de casamento, nascimento, tutela ou termo de guarda"),
            "C2": ("Inicio de prova material contemporanea (24 meses)", 8,
                   "Reunir ao menos dois documentos da janela dos 24 meses (art. 16, §5º)"),
            "C3": ("Prova de dependencia economica quando exigida", 5,
                   "Extratos, IR, contas, plano de saude, coabitacao documentada"),
            "C4": ("Invalidez ou deficiencia documentada quando alegada", 4,
                   "Laudos e historico medico para verificar inicio anterior ao obito; nao exigir automaticamente inicio antes dos 21 anos"),
        },
    },
    "D": {
        "nome": "Prova material e coerencia temporal",
        "total": 20,
        "itens": {
            "D1": ("Linha do tempo probatoria sem vazios relevantes", 7,
                   "Mapear periodo a periodo e listar diligencias para os vazios"),
            "D2": ("Coerencia entre bases oficiais", 5,
                   "Conferir CNIS, CadUnico, INCRA, enderecos e sindicato"),
            "D3": ("Testemunhas idoneas identificadas", 4,
                   "Arrolar tres testemunhas sem interesse direto no beneficio"),
            "D4": ("Documentos de terceiros do grupo familiar aproveitaveis", 4,
                   "Buscar documentos do conjuge, pais e filhos com qualificacao rural"),
        },
    },
    "E": {
        "nome": "Calculo, DIB, acumulacao e riscos",
        "total": 15,
        "itens": {
            "E1": ("Base de calculo apurada", 4,
                   "Obter valor do beneficio ou simular a aposentadoria ficta"),
            "E2": ("DIB definida conforme prazo de requerimento", 4,
                   "Conferir 90 ou 180 dias e calcular o impacto nos atrasados"),
            "E3": ("Acumulacao e opcao mais vantajosa analisadas", 3,
                   "Simular redutores do art. 24 da EC 103/2019"),
            "E4": ("Bloqueios fatais checados", 4,
                   "Rodar a lista de alertas criticos da secao 8 do SKILL.md"),
        },
    },
}

BLOQUEIOS = {
    "concubinato_impeditivo": "Concubinato paralelo a casamento nao dissolvido (Temas 526 e 529/STF)",
    "homicidio_doloso_transitado": "Condenacao transitada em julgado por homicidio doloso (art. 74, §1º)",
    "fraude_ou_simulacao": "Fraude ou simulacao de casamento ou uniao (art. 74, §2º)",
    "sem_qualidade_e_sem_direito_adquirido": "Perda da qualidade de segurado sem direito adquirido (art. 102, §2º)",
    "classe_inferior_com_superior_habilitada": "Requerente de classe inferior com classe superior habilitada",
}

VALORES = {"cheio": 1.0, "parcial": 0.5, "zero": 0.0}


def template():
    caso = {
        "caso": "Nome ou apelido do caso",
        "enquadramento": "urbano | rural | misto",
        "data_obito": "AAAA-MM-DD",
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
        if estado == "na" and (cod in ['A1', 'A3', 'B2', 'C1'] or not caso.get("justificativas_na", {}).get(cod)):
            raise ValueError("na exige justificativa e nao pode excluir requisito essencial: " + cod)
    bloqueios = caso.get("bloqueios", {})
    if not isinstance(bloqueios, dict) or set(bloqueios) - set(BLOQUEIOS):
        raise ValueError("bloqueios invalidos")
    if any(v is not None and type(v) is not bool for v in bloqueios.values()):
        raise ValueError("bloqueios aceitam apenas true, false ou null")


def pontuar(caso):
    validar_caso(caso)
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
        return "caso maduro", "Submeter a revisao juridica; tutela depende de requisitos proprios"
    if total >= 70:
        return "protocolavel com risco controlado", "Revisar lacunas e requisitos essenciais antes de protocolar"
    if total >= 50:
        return "instrucao insuficiente", "Diligenciar antes. Protocolo prematuro trava 30 dias (art. 576-A da IN 128/2022)"
    if total >= 30:
        return "caso fragil", "Reunir prova. Avaliar justificacao administrativa e prova testemunhal judicial"
    return "inviavel no estado atual", "Reavaliar a tese e informar o cliente com clareza"


def main():
    ap = argparse.ArgumentParser(description="Indice de Prontidao do Caso")
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
    print(f"INDICE DE PRONTIDAO DO CASO  |  {caso.get('caso', 'sem nome')}")
    print(f"Enquadramento: {caso.get('enquadramento', 'nao informado')}   "
          f"Obito: {caso.get('data_obito', 'nao informado')}")
    print("=" * 62)
    print(f"\nIPC: {total}/100  ({rotulo})\n")
    for letra in "ABCDE":
        obtido, maximo, nome = resultado[letra]
        barra = "#" * int(round(obtido / maximo * 20)) if maximo else ""
        print(f"  {letra} {nome:<42} {obtido:>5}/{maximo:<3} {barra}")

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
        print(f"\nIPC projetado apos as 3 primeiras diligencias: {round(projecao, 1)} "
              f"({faixa(projecao)[0]})")
    else:
        print("\nSem lacunas. Caso completo.")


if __name__ == "__main__":
    main()
