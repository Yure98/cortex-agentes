#!/usr/bin/env python3
"""
Calculadora de pensao por morte (RGPS).

Subcomandos:
  rmi         Valor da pensao pela regra de cotas (EC 103/2019) ou 100% (regime anterior)
  duracao     Duracao do beneficio do conjuge/companheiro conforme data do obito e idade
  dib         Data de inicio do beneficio conforme prazo de requerimento
  acumulacao  Redutores do art. 24 da EC 103/2019
  prazos      Contagem de prazos recursais administrativos

Uso:
  python3 calculadora_pensao.py rmi --base 4000 --dependentes 3
  python3 calculadora_pensao.py rmi --base 4000 --dependentes 1 --invalido
  python3 calculadora_pensao.py duracao --obito 2024-05-10 --nascimento-dependente 1981-03-22 \
          --contribuicoes 22 --uniao-meses 60
  python3 calculadora_pensao.py dib --obito 2025-11-02 --der 2026-04-15 --idade-dependente 33
  python3 calculadora_pensao.py acumulacao --beneficio-a 4200 --beneficio-b 1900 --salario-minimo 1621
  python3 calculadora_pensao.py prazos --ciencia 2026-07-01

Valores de referencia de 2026 (confirmar antes de usar):
  salario minimo R$ 1.621,00   teto do RGPS R$ 8.475,55
"""

import argparse
import math
import calendar
from datetime import date, timedelta

SM_PADRAO = 1621.00
TETO_PADRAO = 8475.55

EC103 = date(2019, 11, 13)
LEI_13135 = date(2015, 6, 18)
MP_871 = date(2019, 1, 18)
PORTARIA_424 = date(2021, 1, 1)

# (idade_minima, idade_maxima, anos de duracao). None = vitalicia
TABELA_ATE_2020 = [
    (0, 20, 3),
    (21, 26, 6),
    (27, 29, 10),
    (30, 40, 15),
    (41, 43, 20),
    (44, 200, None),
]

TABELA_DESDE_2021 = [
    (0, 21, 3),
    (22, 27, 6),
    (28, 30, 10),
    (31, 41, 15),
    (42, 44, 20),
    (45, 200, None),
]


def soma_meses(dt, meses):
    y, m = divmod(dt.year * 12 + dt.month - 1 + meses, 12)
    return date(y, m + 1, min(dt.day, calendar.monthrange(y, m + 1)[1]))


def brl(valor):
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def parse_data(txt):
    ano, mes, dia = [int(p) for p in txt.split("-")]
    return date(ano, mes, dia)


def idade_em(nascimento, referencia):
    anos = referencia.year - nascimento.year
    if (referencia.month, referencia.day) < (nascimento.month, nascimento.day):
        anos -= 1
    return anos


# ---------------------------------------------------------------- RMI

def cmd_rmi(args):
    base = args.base
    dep = args.dependentes
    obito = parse_data(args.obito) if args.obito else None
    teto = args.teto
    if obito is None:
        raise ValueError("obito obrigatorio: nao presumir regime novo")
    if obito < date(2015, 6, 18):
        raise ValueError("regime historico anterior a 18/06/2015 nao suportado; conferir lei e MP 664")
    if dep < 1:
        raise ValueError("dependentes deve ser pelo menos 1")
    base = min(base, teto)

    print("CALCULO DO VALOR DA PENSAO")
    print("-" * 46)
    print(f"Base de calculo informada: {brl(base)}")
    print(f"Dependentes habilitados: {dep}")

    regime_novo = True
    if obito:
        regime_novo = obito >= EC103
        print(f"Data do obito: {obito.strftime('%d/%m/%Y')}")
        print(f"Regime: {'EC 103/2019 (cotas)' if regime_novo else 'anterior a 13/11/2019 (100%)'}")

    if not regime_novo:
        total = max(args.salario_minimo, min(base, teto))
        print(f"\nValor total da pensao: {brl(total)} (100% da base)")
        if dep > 0:
            print(f"Cota por dependente: {brl(total / dep)}")
        print("\nObservacao: no regime anterior a cota do dependente que perde a qualidade")
        print("reverte aos demais (art. 77, §1º, redacao anterior).")
        return

    if args.invalido:
        percentual = 100
        print("\nDependente invalido ou com deficiencia intelectual, mental ou grave: art. 23, §2º, da EC 103/2019.")
    else:
        percentual = min(50 + 10 * dep, 100)

    total = base * percentual / 100
    if total > teto:
        print(f"\nAtencao: valor apurado ({brl(total)}) excede o teto informado. Limitado ao teto.")
        total = teto
    if total < args.salario_minimo:
        print(f"\nAtencao: valor apurado abaixo do piso. Elevado ao salario minimo.")
        total = args.salario_minimo

    print(f"\nPercentual aplicado: {percentual}%  (50% de cota familiar + 10% por dependente)")
    print(f"Valor total da pensao: {brl(total)}")
    if dep > 0:
        print(f"Cota por dependente: {brl(total / dep)}")

    if args.invalido:
        print("Projecao bloqueada: identificar se permanece dependente protegido pelo art. 23, par. 2o.")
        return

    print("\nProjecao de cessacao de cotas (cotas nao revertem, art. 23, §1º):")
    for restantes in range(dep - 1, 0, -1):
        p = min(50 + 10 * restantes, 100)
        v = max(args.salario_minimo, min(teto, base * p / 100))
        print(f"  com {restantes} dependente(s): {p}% = {brl(v)}  (cota individual {brl(v / restantes)})")
    if dep >= 5:
        print("  com 5 ou mais remanescentes, preserva-se 100% (art. 23, §1º, parte final).")


# ------------------------------------------------------------ DURACAO

def tabela_por_obito(obito):
    if obito >= PORTARIA_424:
        return TABELA_DESDE_2021, "a partir de 01/01/2021 (Portaria SEPRT/ME 424/2020)"
    return TABELA_ATE_2020, "de 18/06/2015 a 31/12/2020 (Lei 13.135/2015)"


def cmd_duracao(args):
    obito = parse_data(args.obito)
    print("DURACAO DA PENSAO DO CONJUGE OU COMPANHEIRO")
    print("-" * 46)
    print(f"Data do obito: {obito.strftime('%d/%m/%Y')}")

    if obito < LEI_13135:
        raise ValueError("duracao historica anterior a 18/06/2015 exige analise especifica, incluindo MP 664")

    if args.idade_dependente is not None:
        idade = args.idade_dependente
    else:
        nasc = parse_data(args.nascimento_dependente)
        idade = idade_em(nasc, obito)
    print(f"Idade do dependente na data do obito: {idade} anos")

    if args.invalido:
        raise ValueError("duracao com invalidez/deficiencia exige condicao, cessacao e minima legal; nao aplicar tabela comum automaticamente")

    if not args.acidente and (args.contribuicoes is None or args.uniao_meses is None):
        raise ValueError("contribuicoes e duracao da uniao desconhecidas; nao presumir filtros atendidos")
    filtro_contrib = args.contribuicoes is not None and args.contribuicoes >= 18
    filtro_uniao = args.uniao_meses is not None and args.uniao_meses >= 24

    print(f"\nFiltro 1 - 18 contribuicoes (ou 18 meses de atividade rural): "
          f"{'ATENDIDO' if filtro_contrib else 'NAO ATENDIDO'}")
    print(f"Filtro 2 - 2 anos de casamento ou uniao estavel: "
          f"{'ATENDIDO' if filtro_uniao else 'NAO ATENDIDO'}")
    if args.acidente:
        print("Morte por acidente de qualquer natureza ou doenca do trabalho: filtros afastados.")

    if not args.acidente and not (filtro_contrib and filtro_uniao):
        fim = soma_meses(obito, 4)
        print(f"\nRESULTADO: 4 meses, contados da data do obito (art. 77, §2º, V, 'b').")
        print(f"Termo final aproximado: {fim.strftime('%d/%m/%Y')}")
        print("Tema 377/TNU: o prazo conta da data do obito mesmo em habilitacao tardia.")
        return

    tabela, rotulo = tabela_por_obito(obito)
    print(f"\nTabela aplicavel: {rotulo}")
    for minimo, maximo, anos in tabela:
        if minimo <= idade <= maximo:
            if anos is None:
                print(f"\nRESULTADO: pensao VITALICIA (idade {idade} na faixa {minimo}+).")
            else:
                fim = soma_meses(obito, anos * 12)
                print(f"\nRESULTADO: {anos} anos de duracao (faixa {minimo} a {maximo}).")
                print(f"Cessacao aproximada: {fim.strftime('%d/%m/%Y')}")
            return


# ---------------------------------------------------------------- DIB

def cmd_dib(args):
    obito = parse_data(args.obito)
    der = parse_data(args.der)
    dias = (der - obito).days
    if args.idade_dependente is None:
        raise ValueError("informe idade na data do obito e confirme a especie de dependente")
    if der < obito:
        raise ValueError("DER anterior ao obito")
    if obito < date(1997, 12, 11):
        raise ValueError("DIB historica nao suportada")
    menor16 = args.filho and args.idade_dependente < 16

    print("DEFINICAO DA DIB")
    print("-" * 46)
    print(f"Obito: {obito.strftime('%d/%m/%Y')}   DER: {der.strftime('%d/%m/%Y')}   "
          f"Intervalo: {dias} dias")

    if obito < date(2015, 11, 5):
        limite = 30
        base_legal = "art. 74, I, redacao anterior a Lei 13.183/2015: 30 dias"
    elif obito < MP_871:
        limite = 90
        base_legal = "Lei 13.183/2015: 90 dias"
    elif menor16:
        limite = 180
        base_legal = "art. 74, I: 180 dias para filho menor de 16 anos"
    else:
        limite = 90
        base_legal = "art. 74, I: 90 dias"

    print(f"Prazo aplicavel: {base_legal}")

    if dias <= limite:
        print(f"\nRESULTADO: DIB na DATA DO OBITO ({obito.strftime('%d/%m/%Y')}).")
    else:
        print(f"\nRESULTADO: DIB na DATA DO REQUERIMENTO ({der.strftime('%d/%m/%Y')}).")
        print(f"Perda aproximada: {dias} dias de atrasados em relacao a data do obito "
              f"({dias - limite} dias alem do prazo legal).")
        if menor16:
            print("Tema 1.421/STJ (2026): nao ha retroacao para filho menor de 16 anos que")
            print("requer apos 180 dias, em obitos na vigencia da Lei 13.846/2019.")

    print("\nPrescricao: parcelas anteriores a 5 anos da DER estao prescritas (art. 103,")
    print("paragrafo unico, e Sumula 85/STJ), salvo pensionista menor, incapaz ou ausente")
    print("[CONFERIR] causas impeditivas/suspensivas e capacidade no periodo; art. 79 revogado.")


# --------------------------------------------------------- ACUMULACAO

def aplica_redutor(valor, sm):
    faixas = [(1, 1.00), (2, 0.60), (3, 0.40), (4, 0.20)]
    restante = valor
    resultado = 0.0
    anterior = 0.0
    detalhe = []
    for mult, perc in faixas:
        limite = mult * sm
        parcela = max(0.0, min(valor, limite) - anterior)
        if parcela > 0:
            resultado += parcela * perc
            detalhe.append((anterior, limite, parcela, perc, parcela * perc))
        anterior = limite
    excedente = max(0.0, valor - 4 * sm)
    if excedente > 0:
        resultado += excedente * 0.10
        detalhe.append((4 * sm, None, excedente, 0.10, excedente * 0.10))
    return resultado, detalhe


def cmd_acumulacao(args):
    print("SIMULACAO ARITMETICA: confirmar especies, regimes e permissao legal de acumulacao antes de aplicar redutor.")
    sm = args.salario_minimo
    a, b = args.beneficio_a, args.beneficio_b
    maior, menor = (a, b) if a >= b else (b, a)

    print("ACUMULACAO DE BENEFICIOS (art. 24 da EC 103/2019)")
    print("-" * 46)
    print(f"Salario minimo de referencia: {brl(sm)}")
    print(f"Beneficio 1: {brl(a)}   Beneficio 2: {brl(b)}")
    print(f"\nMantido integral (maior valor): {brl(maior)}")

    reduzido, detalhe = aplica_redutor(menor, sm)
    print(f"Beneficio secundario bruto: {brl(menor)}")
    for ini, fim, parcela, perc, res in detalhe:
        faixa = f"{brl(ini)} a {brl(fim)}" if fim else f"acima de {brl(ini)}"
        print(f"  faixa {faixa}: {brl(parcela)} x {int(perc*100)}% = {brl(res)}")
    print(f"Beneficio secundario apos redutor: {brl(reduzido)}")
    print(f"\nRENDA TOTAL: {brl(maior + reduzido)}")
    print(f"Perda mensal em relacao a soma integral: {brl((a + b) - (maior + reduzido))}")
    print("\nObservacao: a constitucionalidade do art. 24 e discutida no STF. Registrar ressalva")
    print("quando o valor perdido for expressivo. BPC nao acumula com pensao por morte.")


# ------------------------------------------------------------- PRAZOS

def cmd_prazos(args):
    ciencia = parse_data(args.ciencia)
    print("PRAZOS APOS A CIENCIA DA DECISAO")
    print("-" * 46)
    print(f"Ciencia: {ciencia.strftime('%d/%m/%Y')}")
    r30 = ciencia + timedelta(days=30)
    print(f"\nRecurso ordinario ao CRPS (30 dias, art. 126 da Lei 8.213/91): "
          f"ate {r30.strftime('%d/%m/%Y')}")
    print(f"Recurso especial a Camara de Julgamento (30 dias da ciencia da decisao da Junta).")
    print("Data nominal: conferir calendario de expediente, prorrogacao e regimento vigente.")
    print("Novo requerimento: conferir texto vigente da IN 128; este script nao fixa impedimento automatico.")

# --------------------------------------------------------------- MAIN

def main():
    p = argparse.ArgumentParser(description="Calculadora de pensao por morte (RGPS)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("rmi", help="valor da pensao")
    s.add_argument("--base", type=float, required=True, help="valor da aposentadoria ou aposentadoria ficta")
    s.add_argument("--dependentes", type=int, required=True)
    s.add_argument("--obito", type=str, required=True, help="AAAA-MM-DD")
    s.add_argument("--invalido", action="store_true", help="ha dependente invalido ou com deficiencia intelectual, mental ou grave")
    s.add_argument("--salario-minimo", type=float, required=True)
    s.add_argument("--teto", type=float, required=True)
    s.set_defaults(func=cmd_rmi)

    s = sub.add_parser("duracao", help="duracao do beneficio do conjuge")
    s.add_argument("--obito", type=str, required=True)
    s.add_argument("--nascimento-dependente", type=str, default=None)
    s.add_argument("--idade-dependente", type=int, default=None)
    s.add_argument("--contribuicoes", type=int, default=None, help="numero de contribuicoes do falecido")
    s.add_argument("--uniao-meses", type=int, default=None, help="meses de casamento ou uniao estavel")
    s.add_argument("--acidente", action="store_true")
    s.add_argument("--invalido", action="store_true")
    s.set_defaults(func=cmd_duracao)

    s = sub.add_parser("dib", help="data de inicio do beneficio")
    s.add_argument("--filho", action="store_true", help="requerente e filho; indispensavel para prazo de 180 dias")
    s.add_argument("--obito", type=str, required=True)
    s.add_argument("--der", type=str, required=True)
    s.add_argument("--idade-dependente", type=int, default=None)
    s.set_defaults(func=cmd_dib)

    s = sub.add_parser("acumulacao", help="redutores do art. 24 da EC 103/2019")
    s.add_argument("--beneficio-a", type=float, required=True)
    s.add_argument("--beneficio-b", type=float, required=True)
    s.add_argument("--salario-minimo", type=float, required=True)
    s.set_defaults(func=cmd_acumulacao)

    s = sub.add_parser("prazos", help="prazos recursais administrativos")
    s.add_argument("--ciencia", type=str, required=True)
    s.set_defaults(func=cmd_prazos)

    args = p.parse_args()
    if args.cmd == "duracao" and args.idade_dependente is None and args.nascimento_dependente is None:
        p.error("informe --idade-dependente ou --nascimento-dependente")
    try:
        for nome in ("base", "salario_minimo", "teto", "beneficio_a", "beneficio_b"):
            value = getattr(args, nome, None)
            if value is not None and (not math.isfinite(value) or value <= 0):
                raise ValueError(nome + " deve ser positivo e finito")
        for nome in ("idade_dependente", "contribuicoes", "uniao_meses"):
            value = getattr(args, nome, None)
            if value is not None and value < 0:
                raise ValueError(nome + " nao pode ser negativo")
        if getattr(args, "obito", None) and parse_data(args.obito) > date.today():
            raise ValueError("obito futuro")
        if getattr(args, "nascimento_dependente", None) and parse_data(args.nascimento_dependente) > parse_data(args.obito):
            raise ValueError("nascimento posterior ao obito: examinar habilitacao de filho postumo separadamente")
        if getattr(args, "teto", None) and args.teto < args.salario_minimo:
            raise ValueError("teto inferior ao piso")
        args.func(args)
    except (ValueError, TypeError) as e:
        p.error(str(e))


if __name__ == "__main__":
    main()
