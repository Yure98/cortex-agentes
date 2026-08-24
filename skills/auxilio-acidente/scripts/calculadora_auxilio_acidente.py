#!/usr/bin/env python3
"""
Calculadora de auxilio-acidente (RGPS).

Subcomandos:
  rmi         Valor do auxilio-acidente: 50% do salario de beneficio
  dib         Data de inicio do beneficio quando precedido de auxilio-doenca
  cumulacao   Testa a Sumula 507/STJ: cumulacao com aposentadoria
  prazos      Contagem de prazos recursais administrativos (CRPS)

Uso:
  python calculadora_auxilio_acidente.py rmi --base 3200
  python calculadora_auxilio_acidente.py dib --cessacao-auxilio-doenca 2026-03-15
  python calculadora_auxilio_acidente.py cumulacao --lesao 2015-04-10 --aposentadoria 2026-01-05
  python calculadora_auxilio_acidente.py prazos --ciencia 2026-07-01

Valores de referencia de 2026 (confirmar antes de usar):
  salario minimo R$ 1.621,00   teto do RGPS R$ 8.475,55
"""

import argparse
from datetime import date, timedelta

SM_PADRAO = 1621.00
TETO_PADRAO = 8475.55

CORTE_LEI_9528 = date(1997, 11, 11)


def parse_data(s):
    return date.fromisoformat(s)


def fmt_data(d):
    return d.strftime("%d/%m/%Y")


def fmt_moeda(v):
    s = f"{v:,.2f}"
    s = s.replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {s}"


def cmd_rmi(args):
    base = args.base
    teto = args.teto or TETO_PADRAO

    if base > teto:
        print(f"AVISO: salario de beneficio informado (R$ {base:.2f}) excede o teto do RGPS "
              f"({fmt_moeda(teto)}). Aplicando teto.")
        base = teto

    rmi = base * 0.5

    print("CALCULO DO VALOR DO AUXILIO-ACIDENTE")
    print("-" * 48)
    print(f"Salario de beneficio informado: {fmt_moeda(args.base)}")
    print(f"Teto do RGPS considerado: {fmt_moeda(teto)}")
    print()
    print("Percentual aplicado: 50% (art. 86, caput e paragrafos, Lei 8.213/91)")
    print(f"RMI (valor mensal) do auxilio-acidente: {fmt_moeda(rmi)}")
    print()
    print("Observacao: nao ha piso de um salario minimo garantido para este beneficio,")
    print("diferente de outros beneficios do RGPS. O valor pode ser inferior ao minimo.")
    if args.decimo_terceiro:
        print(f"\nDecimo terceiro proporcional (1/12 por competencia recebida no ano):")
        print(f"  Um doze avos do valor mensal: {fmt_moeda(rmi / 12)}")


def cmd_dib(args):
    cessacao = parse_data(args.cessacao_auxilio_doenca) if args.cessacao_auxilio_doenca else None
    requerimento = parse_data(args.requerimento) if args.requerimento else None

    print("DEFINICAO DA DATA DE INICIO DO BENEFICIO (DIB)")
    print("-" * 48)

    if cessacao:
        dib = cessacao + timedelta(days=1)
        print(f"Cessacao do auxilio-doenca (mesmo fato gerador): {fmt_data(cessacao)}")
        print(f"DIB do auxilio-acidente (dia seguinte, art. 86, par. 2o; Tema 862/STJ): {fmt_data(dib)}")
    elif requerimento:
        print(f"Sem auxilio-doenca precedente pelo mesmo fato gerador.")
        print(f"DIB projetada na data do requerimento administrativo: {fmt_data(requerimento)}")
        print("Confirme que a lesao ja estava consolidada nessa data.")
    else:
        print("Informe --cessacao-auxilio-doenca OU --requerimento para calcular a DIB.")
        return

    print()
    print("Prescricao quinquenal (art. 103, paragrafo unico): atinge parcelas vencidas ha mais")
    print("de 5 anos contados da DER ou do ajuizamento, ressalvados menores, incapazes e ausentes.")


def cmd_cumulacao(args):
    lesao = parse_data(args.lesao)
    aposentadoria = parse_data(args.aposentadoria)

    print("TESTE DE CUMULACAO COM APOSENTADORIA (SUMULA 507/STJ)")
    print("-" * 48)
    print(f"Data da lesao incapacitante (consolidacao, ou art. 23 da Lei 8.213/91 se doenca "
          f"profissional/do trabalho): {fmt_data(lesao)}")
    print(f"Data de concessao da aposentadoria: {fmt_data(aposentadoria)}")
    print(f"Marco divisor (Lei 9.528/97): {fmt_data(CORTE_LEI_9528)}")
    print()

    lesao_anterior = lesao < CORTE_LEI_9528
    aposentadoria_anterior = aposentadoria < CORTE_LEI_9528

    print(f"Lesao anterior ao marco? {'SIM' if lesao_anterior else 'NAO'}")
    print(f"Aposentadoria anterior ao marco? {'SIM' if aposentadoria_anterior else 'NAO'}")
    print()

    if lesao_anterior and aposentadoria_anterior:
        print("RESULTADO: CUMULACAO POSSIVEL.")
        print("As duas condicoes da Sumula 507/STJ estao presentes: lesao e aposentadoria")
        print("ambas anteriores a 11/11/1997.")
    else:
        print("RESULTADO: CUMULACAO NAO PERMITIDA.")
        print("Pelo menos uma das datas e posterior a 11/11/1997. O auxilio-acidente e extinto")
        print("na data de inicio da aposentadoria (art. 86, par. 2o, Lei 9.528/97; art. 26, par. 3o,")
        print("II, EC 103/2019).")


def cmd_prazos(args):
    ciencia = parse_data(args.ciencia)
    prazo_recurso = ciencia + timedelta(days=30)
    prazo_especial = prazo_recurso + timedelta(days=30)

    print("PRAZOS RECURSAIS ADMINISTRATIVOS (CRPS)")
    print("-" * 48)
    print(f"Ciencia da decisao: {fmt_data(ciencia)}")
    print(f"Prazo final para Recurso Ordinario a Junta de Recursos "
          f"(30 dias, art. 305, par. 1o, Decreto 3.048/99): {fmt_data(prazo_recurso)}")
    print(f"Se a Junta manter a negativa, prazo estimado para Recurso Especial a Camara de")
    print(f"Julgamento (30 dias da ciencia da decisao da Junta): confirme a data de ciencia")
    print(f"real dessa decisao; a data acima ({fmt_data(prazo_especial)}) e apenas ilustrativa,")
    print(f"somando 30 + 30 dias a partir da ciencia original.")
    print()
    print("Sempre confirme a data de ciencia exata registrada no processo administrativo,")
    print("nao a data de emissao da decisao.")


def main():
    p = argparse.ArgumentParser(description="Calculadora de auxilio-acidente (RGPS)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("rmi", help="valor do auxilio-acidente (50% do salario de beneficio)")
    s.add_argument("--base", type=float, required=True, help="salario de beneficio")
    s.add_argument("--teto", type=float, default=None, help="teto do RGPS (padrao: valor de 2026)")
    s.add_argument("--decimo-terceiro", action="store_true", help="tambem calcula 1/12 do decimo terceiro")
    s.set_defaults(func=cmd_rmi)

    s = sub.add_parser("dib", help="data de inicio do beneficio")
    s.add_argument("--cessacao-auxilio-doenca", default=None, help="data de cessacao do auxilio-doenca (AAAA-MM-DD)")
    s.add_argument("--requerimento", default=None, help="data do requerimento, se nao houve auxilio-doenca precedente")
    s.set_defaults(func=cmd_dib)

    s = sub.add_parser("cumulacao", help="testa a Sumula 507/STJ para cumulacao com aposentadoria")
    s.add_argument("--lesao", required=True, help="data da lesao incapacitante / consolidacao (AAAA-MM-DD)")
    s.add_argument("--aposentadoria", required=True, help="data de concessao da aposentadoria (AAAA-MM-DD)")
    s.set_defaults(func=cmd_cumulacao)

    s = sub.add_parser("prazos", help="prazos recursais administrativos no CRPS")
    s.add_argument("--ciencia", required=True, help="data de ciencia da decisao (AAAA-MM-DD)")
    s.set_defaults(func=cmd_prazos)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
