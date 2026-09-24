#!/usr/bin/env python3
"""Confronto ARITMÉTICO de renda BPC já classificada e auditada; não decide direito."""
import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


def dinheiro(valor):
    if isinstance(valor, bool) or not isinstance(valor, str):
        raise ValueError('valores monetários precisam ser strings decimais em reais')
    try:
        n = Decimal(valor)
    except InvalidOperation as e:
        raise ValueError('valor monetário inválido') from e
    if not n.is_finite() or n < 0 or n.as_tuple().exponent < -2:
        raise ValueError('valor negativo, não finito ou com mais de dois decimais')
    return n


def texto(valor, nome):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(nome + ' exige fonte/documento explícito')
    return valor


def classificar(registro, campo, fonte):
    if type(registro.get(campo)) is not bool:
        raise ValueError(campo + ' precisa de classificação jurídica explícita (true/false)')
    texto(registro.get(fonte), fonte)
    return registro[campo]


def calcular(d):
    if not isinstance(d, dict):
        raise ValueError('JSON deve conter objeto')
    competencia = texto(d.get('competencia'), 'competencia')
    if len(competencia) != 7 or competencia[4] != '-' or not competencia[:4].isdigit() or not competencia[5:].isdigit() or not 1 <= int(competencia[5:]) <= 12:
        raise ValueError('competencia deve ser AAAA-MM')
    texto(d.get('fonte_salario_minimo'), 'fonte_salario_minimo')
    minimo = dinheiro(d.get('salario_minimo'))
    if minimo <= 0:
        raise ValueError('salario_minimo deve ser positivo')
    pessoas = d.get('pessoas')
    if not isinstance(pessoas, list) or not pessoas:
        raise ValueError('informar ao menos uma pessoa')
    incluidos = 0
    total = Decimal('0')
    ids = set()
    memoria = []
    for pessoa in pessoas:
        if not isinstance(pessoa, dict):
            raise ValueError('pessoa precisa ser objeto')
        identificador = texto(pessoa.get('id'), 'id')
        if identificador in ids:
            raise ValueError('id de pessoa duplicado')
        ids.add(identificador)
        grupo = classificar(pessoa, 'grupo_legal', 'fonte_grupo')
        rendimentos = pessoa.get('rendimentos')
        if not isinstance(rendimentos, list) or not rendimentos:
            raise ValueError('renda zero deve ser documentada expressamente por pessoa')
        subtotal = Decimal('0')
        for item in rendimentos:
            if not isinstance(item, dict):
                raise ValueError('rendimento precisa ser objeto')
            valor = dinheiro(item.get('valor'))
            inclui = classificar(item, 'inclui', 'fonte_classificacao')
            texto(item.get('fonte_valor'), 'fonte_valor')
            if grupo and inclui:
                subtotal += valor
        if grupo:
            incluidos += 1
            total += subtotal
        memoria.append({'id': identificador, 'grupo_legal': grupo, 'renda_incluida': str(subtotal)})
    if incluidos == 0:
        raise ValueError('grupo legal vazio')
    deducoes = d.get('deducoes')
    if not isinstance(deducoes, list):
        raise ValueError('deducoes precisa de lista explícita, mesmo se vazia')
    abatimento = Decimal('0')
    for item in deducoes:
        if not isinstance(item, dict):
            raise ValueError('dedução precisa ser objeto')
        texto(item.get('fonte_classificacao'), 'fonte_classificacao')
        texto(item.get('fonte_valor'), 'fonte_valor')
        abatimento += dinheiro(item.get('valor'))
    if abatimento > total:
        raise ValueError('deduções maiores que a renda incluída: verificar classificações')
    per_capita = (total - abatimento) / incluidos
    limite = minimo / 4
    cent = lambda valor: str(valor.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
    return {'competencia': competencia, 'pessoas_grupo_legal': incluidos,
            'renda_bruta_incluida': cent(total), 'deducoes_validadas_pelo_advogado': cent(abatimento),
            'renda_per_capita': cent(per_capita), 'referencia_um_quarto_minimo': cent(limite),
            'comparacao_puramente_aritmetica': 'ate_1_4' if per_capita <= limite else 'acima_1_4',
            'memoria': memoria,
            'limite': 'NÃO verifica grupo, exceções, prova, vulnerabilidade, limite alternativo, direito ou RMI. Revisão humana obrigatória.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arquivo', type=Path, required=True)
    args = parser.parse_args()
    try:
        data = json.loads(args.arquivo.read_text(encoding='utf-8'))
        print(json.dumps(calcular(data), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError, TypeError, json.JSONDecodeError) as exc:
        parser.exit(2, '[CONFERIR] ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
