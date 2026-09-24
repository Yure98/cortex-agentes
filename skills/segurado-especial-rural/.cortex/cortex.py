#!/usr/bin/env python3
"""Núcleo determinístico Cortex. Python 3.10+, sem dependências externas."""
import argparse
import calendar
import json
import re
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from urllib.parse import urlparse


def numero(value, *, minimo=0):
    if isinstance(value, bool):
        raise ValueError('booleano não é valor numérico')
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError('número inválido') from exc
    if not result.is_finite() or result < Decimal(str(minimo)):
        raise ValueError('valor não finito ou abaixo do mínimo')
    return result


def moeda(value):
    return str(numero(value).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


def soma_meses(dt, meses):
    if type(meses) is not int:
        raise ValueError('meses deve ser inteiro')
    y, m = divmod(dt.year * 12 + dt.month - 1 + meses, 12)
    return date(y, m + 1, min(dt.day, calendar.monthrange(y, m + 1)[1]))


def validar(d, final=False):
    erros = []
    if not isinstance(d, dict):
        return ['dossiê deve ser objeto']
    for k in ('versao_schema', 'caso_id', 'revisao_numero', 'data_referencia', 'objetivo',
              'fatos', 'fontes', 'calculos', 'pendencias', 'revisao', 'historico'):
        if k not in d:
            erros.append('campo ausente: ' + k)
    if d.get('versao_schema') != 1:
        erros.append('versao_schema deve ser 1')
    if not re.fullmatch(r'[a-zA-Z0-9_-]{1,80}', str(d.get('caso_id', ''))):
        erros.append('caso_id inválido')
    if type(d.get('revisao_numero')) is not int or d['revisao_numero'] < 1:
        erros.append('revisao_numero inválido')
    try:
        date.fromisoformat(d.get('data_referencia', ''))
    except (TypeError, ValueError):
        erros.append('data_referencia inválida')
    for k in ('fatos', 'fontes', 'calculos', 'pendencias', 'historico'):
        if not isinstance(d.get(k), list):
            erros.append(k + ' deve ser lista')
    if erros:
        return erros
    ids = set()
    for f in d['fatos']:
        if not isinstance(f, dict):
            erros.append('fato deve ser objeto')
            continue
        if not f.get('id') or f['id'] in ids:
            erros.append('id de fato ausente/duplicado')
        ids.add(f.get('id'))
        if f.get('estado') not in ('confirmado', 'relatado', 'inferido', 'desconhecido'):
            erros.append('estado de fato inválido')
        if f.get('estado') == 'confirmado' and (not f.get('origem') or f.get('valor') is None):
            erros.append('fato confirmado sem valor/proveniência')
        if final and (f.get('estado') != 'confirmado' and f.get('essencial', True)):
            erros.append('fato essencial não confirmado: ' + str(f.get('id')))
    for f in d['fontes']:
        if not isinstance(f, dict):
            erros.append('fonte deve ser objeto')
            continue
        if f.get('estado') not in ('confirmado', 'pendente', 'superado'):
            erros.append('estado de fonte inválido')
        if f.get('estado') == 'confirmado':
            for key in ('orgao', 'titulo', 'url', 'trecho', 'publicacao', 'consulta', 'regime_temporal'):
                if not f.get(key):
                    erros.append('fonte sem ' + key)
            if urlparse(f.get('url', '')).scheme != 'https':
                erros.append('fonte sem URL HTTPS')
        if final and f.get('estado') != 'confirmado':
            erros.append('fonte não confirmada utilizada')
    for p in d['pendencias']:
        if not isinstance(p, dict) or type(p.get('essencial')) is not bool or not p.get('descricao'):
            erros.append('pendência inválida')
        elif final and p['essencial']:
            erros.append('pendência essencial: ' + p['descricao'])
    for c in d['calculos']:
        if not isinstance(c, dict) or any(not c.get(k) for k in ('script', 'versao', 'entradas', 'saida', 'parametros_fonte')):
            erros.append('cálculo sem memória reproduzível')
    r = d.get('revisao')
    if not isinstance(r, dict):
        erros.append('revisao deve ser objeto')
    else:
        for k in ('fatos', 'prova_calculo', 'contraditorio', 'final'):
            if r.get(k) not in ('pendente', 'bloqueado', 'aprovado'):
                erros.append('portão inválido: ' + k)
            elif final and r[k] != 'aprovado':
                erros.append('portão não aprovado: ' + k)
    if final and (not d['fatos'] or not d['fontes'] or '[CONFERIR]' in str(d['objetivo'])):
        erros.append('entrega final sem fatos, fontes ou objetivo confirmado')
    return erros


def coeficiente(modalidade, anos, sexo):
    """Somente coeficientes. Não decide elegibilidade nem regra da média."""
    anos = numero(anos)
    if sexo not in ('F', 'M'):
        raise ValueError('sexo deve ser F ou M para a regra informada')
    if modalidade == 'pcd-tempo' or modalidade == 'pedagio100':
        return Decimal(1)
    if modalidade == 'pcd-idade':
        return min(Decimal(1), Decimal('.70') + Decimal('.01') * int(anos))
    if modalidade == 'geral-ec103':
        limite = 15 if sexo == 'F' else 20
        return Decimal('.60') + Decimal('.02') * max(0, int(anos) - limite)
    raise ValueError('modalidade não suportada; exige enquadramento específico')


def comparar(d):
    """Fluxos reais mensais, 13º provisionado em 1/12. Não é liquidação de atrasados."""
    if d.get('unidade') != 'reais-constantes':
        raise ValueError('informar unidade=reais-constantes e taxa real mensal')
    taxa = numero(d['taxa_real_mensal'])
    horizonte = d['horizonte_meses']
    if type(horizonte) is not int or not 1 <= horizonte <= 1200:
        raise ValueError('horizonte deve ser inteiro entre 1 e 1200 meses')
    cenarios = d['cenarios']
    if len(cenarios) < 2:
        raise ValueError('informar pelo menos dois cenários')
    saida = []
    nomes = set()
    for c in cenarios:
        if c.get('elegibilidade_confirmada') is not True or not c.get('fonte_calculo'):
            raise ValueError('cenário sem elegibilidade/memória de cálculo confirmada')
        nome = c['nome']
        if not isinstance(nome, str) or not nome or nome in nomes:
            raise ValueError('nome de cenário ausente/duplicado')
        nomes.add(nome)
        rmi = numero(c['rmi'], minimo='.01')
        espera = c['espera_meses']
        if type(espera) is not int or not 0 <= espera <= horizonte:
            raise ValueError('espera inválida')
        custo = numero(c['contribuicao_adicional_mensal'])
        fluxos = [-custo * 12 if t <= espera else rmi * Decimal(13)
                  for t in range(1, horizonte + 1)]
        vpl = sum(f / (1 + taxa) ** t for t, f in enumerate(fluxos, 1)) / 12
        saida.append({'nome': nome, 'vpl': str(vpl.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),
                      'fluxos': fluxos})
    a, b = saida[:2]
    diferenca = Decimal(0)
    cruzamentos = []
    esteve_atras = False
    for t, (fa, fb) in enumerate(zip(a['fluxos'], b['fluxos']), 1):
        anterior = diferenca
        diferenca += fb - fa
        esteve_atras |= diferenca < 0
        if esteve_atras and anterior < 0 <= diferenca:
            cruzamentos.append(t)
    for s in saida:
        del s['fluxos']
    return {'cenarios': saida, 'cruzamentos_b_sobre_a_meses': cruzamentos,
            'equilibrio': cruzamentos[0] if cruzamentos else None,
            'limite': 'Sem cruzamento não prova ausência fora do horizonte. Valores reais; 13º provisionado; '
                      'sem probabilidade individual de sobrevivência. Custos somente incrementais.'}


def pedagio50(tempo_reforma, tempo_atual, sexo, carencia):
    """Anos já apurados externamente, sem arredondar para cruzar a fronteira legal."""
    if sexo not in ('F', 'M') or type(carencia) is not int or carencia < 0:
        raise ValueError('sexo/carência inválidos')
    reforma, atual = numero(tempo_reforma), numero(tempo_atual)
    if atual < reforma:
        raise ValueError('tempo atual inferior ao da reforma')
    minimo = Decimal(30 if sexo == 'F' else 35)
    falta = max(Decimal(0), minimo - reforma)
    exigido = minimo + falta / 2
    return {'acesso_regra': reforma > minimo - 2,
            'tempo_exigido': str(exigido),
            'requisitos_numericos': reforma > minimo - 2 and atual >= exigido and carencia >= 180,
            'limite': 'Tempos previamente apurados, sem arredondar. Não valida filiação, prova ou fator previdenciário.'}


def ifbra(d):
    """Conferência aritmética de formulários; não aplica Fuzzy nem emite grau oficial."""
    totais = {}
    for avaliador in ('medica', 'social'):
        notas = d.get(avaliador)
        if not isinstance(notas, list) or len(notas) != 41:
            raise ValueError('exigidas 41 atividades em cada avaliação')
        if any(type(n) is not int or n not in (25, 50, 75, 100) for n in notas):
            raise ValueError('notas inválidas')
        totais[avaliador] = sum(notas)
    return {'totais': totais, 'total_bruto': sum(totais.values()),
            'limite': 'Soma bruta de dois formulários. Fuzzy, barreiras, DID e grau exigem revisão própria.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='cmd', required=True)
    v = sub.add_parser('validar'); v.add_argument('arquivo'); v.add_argument('--final', action='store_true')
    c = sub.add_parser('comparar'); c.add_argument('arquivo')
    c = sub.add_parser('ifbra'); c.add_argument('arquivo')
    c = sub.add_parser('pedagio50'); c.add_argument('arquivo')
    r = sub.add_parser('coeficiente'); r.add_argument('modalidade'); r.add_argument('--anos', required=True); r.add_argument('--sexo', required=True)
    a = p.parse_args()
    try:
        if a.cmd == 'coeficiente':
            result = {'coeficiente': str(coeficiente(a.modalidade, a.anos, a.sexo)), 'limite': 'Não valida direito, média, piso ou teto.'}
        else:
            with open(a.arquivo, encoding='utf-8') as f:
                d = json.load(f)
            if a.cmd == 'validar': result = {'erros': validar(d, a.final)}
            elif a.cmd == 'ifbra': result = ifbra(d)
            elif a.cmd == 'pedagio50': result = pedagio50(d['tempo_reforma'], d['tempo_atual'], d['sexo'], d['carencia'])
            else: result = comparar(d)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2 if result.get('erros') else 0
    except (ValueError, TypeError, KeyError, OSError) as e:
        p.exit(2, '[CONFERIR] ' + str(e) + '\n')

if __name__ == '__main__':
    raise SystemExit(main())
