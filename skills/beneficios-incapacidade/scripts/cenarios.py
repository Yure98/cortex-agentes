#!/usr/bin/env python3
"""Cenários condicionados de incapacidade; nunca apura CNIS ou concede benefício."""

import argparse
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import json
from pathlib import Path
import re
import sys

CENT = Decimal('0.01')
EXEMPLO = Path(__file__).resolve().parents[1] / 'assets' / 'casos-exemplo.json'


def falha(message):
    raise ValueError(message)


def pares_sem_repeticao(pares):
    objeto = {}
    for chave, valor in pares:
        if chave in objeto:
            falha('chave duplicada: ' + chave)
        objeto[chave] = valor
    return objeto


def dinheiro(valor, campo):
    if isinstance(valor, bool) or not isinstance(valor, (str, int)):
        falha(f'{campo}: usar valor positivo decimal como string, com ate 2 casas')
    if not re.fullmatch(r'[0-9]+(?:\.[0-9]{1,2})?', str(valor)):
        falha(f'{campo}: formato decimal invalido')
    try:
        n = Decimal(str(valor))
    except InvalidOperation:
        falha(f'{campo}: numero invalido')
    if not n.is_finite() or n <= 0:
        falha(f'{campo}: exige valor positivo finito')
    return n


def data_iso(valor):
    if not isinstance(valor, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', valor):
        falha('data_inicio: exige YYYY-MM-DD')
    try:
        return date.fromisoformat(valor)
    except ValueError:
        falha('data_inicio: data inexistente')


def calcular(dados):
    if not isinstance(dados, dict):
        falha('entrada deve ser objeto JSON')
    obrigatorios = {'especie', 'data_inicio', 'salario_beneficio',
                    'fonte_salario_beneficio', 'competencia_base'}
    especie = dados.get('especie')
    if especie == 'temporaria':
        obrigatorios |= {'media_ultimos_ate_12', 'fonte_media_12',
                         'quantidade_salarios', 'regra_2015_aplicavel'}
    elif especie == 'permanente':
        obrigatorios |= {'sexo_regra', 'anos_completos', 'nexo_ocupacional_comprovado'}
    else:
        falha('especie deve ser temporaria ou permanente')
    faltantes = sorted(obrigatorios - dados.keys())
    extras = sorted(dados.keys() - obrigatorios)
    if faltantes or extras:
        falha(f'campos faltantes: {faltantes}; inesperados: {extras}')
    inicio = data_iso(dados['data_inicio'])
    # Recorte explícito: cálculo de média e alterações entre regimes não são resolvidos aqui.
    if inicio < date(2019, 11, 13):
        falha('cenario anterior a 13/11/2019 exige estudo historico fora deste script')
    competencia = dados['competencia_base']
    if (not isinstance(competencia, str)
            or not re.fullmatch(r'\d{4}-(0[1-9]|1[0-2])', competencia)
            or competencia > inicio.strftime('%Y-%m')):
        falha('competencia_base: YYYY-MM valido e nao posterior a data_inicio')
    for campo in ('fonte_salario_beneficio',) + (('fonte_media_12',) if especie == 'temporaria' else ()):
        if not isinstance(dados[campo], str) or not dados[campo].strip() or dados[campo].strip() == '[CONFERIR]':
            falha(f'{campo}: informar origem auditavel da media')
    sb = dinheiro(dados['salario_beneficio'], 'salario_beneficio')
    if especie == 'temporaria':
        if dados['regra_2015_aplicavel'] is not True:
            falha('regra_2015_aplicavel deve ser true; revisar regime historico')
        quantidade = dados['quantidade_salarios']
        if isinstance(quantidade, bool) or not isinstance(quantidade, int) or not 1 <= quantidade <= 12:
            falha('quantidade_salarios: inteiro de 1 a 12')
        limite_12 = dinheiro(dados['media_ultimos_ate_12'], 'media_ultimos_ate_12')
        percentual = Decimal('0.91')
        base = min(sb * percentual, limite_12)
        fundamento = 'Lei 8.213/1991, arts. 61 e 29 paragrafo 10'
    else:
        sexo = dados['sexo_regra']
        if sexo not in ('F', 'M'):
            falha('sexo_regra: F ou M conforme enquadramento juridico conferido')
        anos = dados['anos_completos']
        if isinstance(anos, bool) or not isinstance(anos, int) or anos < 0:
            falha('anos_completos: inteiro nao negativo e auditado')
        nexo = dados['nexo_ocupacional_comprovado']
        if type(nexo) is not bool:
            falha('nexo_ocupacional_comprovado: true ou false explicitos')
        percentual = (Decimal('1') if nexo else
                      Decimal('0.60') + Decimal('0.02') * max(0, anos - (15 if sexo == 'F' else 20)))
        base = sb * percentual
        fundamento = 'EC 103/2019, art. 26 paragrafos 2 III, 3 II e 5'
    return {
        'especie': especie,
        'data_inicio_declarada': inicio.isoformat(),
        'competencia_base_declarada': competencia,
        'coeficiente': str(percentual),
        'base_teorica_antes_piso_teto': str(base.quantize(CENT, rounding=ROUND_HALF_UP)),
        'fundamento': fundamento,
        'limites_e_direito': 'pendentes: piso/teto, media auditada, elegibilidade, especie, DIB, revisao humana',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument('--arquivo', type=Path, help='JSON local sem dados pessoais')
    grupo.add_argument('--exemplo', action='store_true', help='usar cenario ficticio do pacote')
    args = parser.parse_args()
    try:
        arquivo = EXEMPLO if args.exemplo else args.arquivo
        dados = json.loads(arquivo.read_text(encoding='utf-8'), object_pairs_hook=pares_sem_repeticao)
        print(json.dumps(calcular(dados), ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        print('Cenario recusado: ' + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
