# Skill: auxilio-acidente (Programa Cortex)

Sistema de atuação em auxílio-acidente do RGPS, urbano e rural, para advogado. Cobre da
entrevista com o cliente até a fase recursal administrativa e judicial, com nexo técnico,
pontuação de lacunas e cálculo automatizado.

Data-base do conteúdo: agosto de 2026. Incorpora a Portaria Conjunta MPS/INSS nº 15/2026, que
instituiu a análise documental prévia como etapa obrigatória, anterior à perícia presencial.

## Instalação no Claude Code

Opção 1, skill de projeto:
```
mkdir -p .claude/skills
cp -r auxilio-acidente .claude/skills/
```

Opção 2, skill pessoal (vale para todos os projetos):
```
mkdir -p ~/.claude/skills
cp -r auxilio-acidente ~/.claude/skills/
```

Comandos de atalho (opcional, para habilitar `/auxilioacidente`):
```
mkdir -p .claude/commands
cp auxilio-acidente/commands/*.md .claude/commands/
```

Se o Cortex já tiver estrutura própria de plugin, coloque a pasta em `skills/` do plugin e os
arquivos de `commands/` em `commands/`.

## Estrutura

```
auxilio-acidente/
├── SKILL.md                    ponto de entrada, fluxo em 10 fases
├── references/                 17 arquivos de conteúdo técnico
├── assets/                     13 modelos de documentos e peças
├── scripts/                    calculadora e índice de prontidão
└── commands/                   atalhos /auxilioacidente e /auxílio-acidente
```

## Uso

Digite `/auxilioacidente` ou apenas mencione auxílio-acidente. A skill:

1. Pergunta se o caso é urbano (empregado, avulso, doméstico) ou rural (segurado especial), e
   valida a classificação por conta própria, incluindo o alerta sobre contribuinte individual e
   facultativo, que em regra ficam fora do rol de beneficiários.
2. Conduz entrevista estruturada em blocos curtos, cobrindo o evento, o nexo técnico, o
   tratamento e a consolidação da lesão.
3. Mapeia o nexo técnico: CAT, NTEP, acidente de trajeto e doença ocupacional, com o que fazer
   quando não há CAT.
4. Calcula o Índice de Prontidão Probatória (0 a 100) e lista as lacunas com o ganho de cada
   diligência.
5. Analisa qualidade de segurado, enquadramento do beneficiário e sequela, independentemente do
   grau da lesão.
6. Calcula o valor (50% do salário de benefício), a DIB e trata a cumulação com aposentadoria
   (Súmula 507/STJ) e com auxílio-doença.
7. Monta o requerimento já pensado para a análise documental prévia da Portaria 15/2026,
   acompanha exigências e prepara o cliente para a perícia.
8. Vai até recurso ordinário e especial no CRPS, ação no JEF, quesitos periciais judiciais e
   recurso inominado.
9. Roda uma varredura de oportunidades conexas ao final de toda análise: cessação de
   auxílio-doença sem exame de sequela, revisão de aposentadoria rural pelo Tema 322/TNU,
   estabilidade acidentária, indenização civil, erros de cálculo em benefício já concedido.

## Scripts

```
python scripts/calculadora_auxilio_acidente.py rmi --base 3200
python scripts/calculadora_auxilio_acidente.py dib --cessacao-auxilio-doenca 2026-03-15
python scripts/calculadora_auxilio_acidente.py cumulacao --lesao 2015-04-10 --aposentadoria 2026-01-05
python scripts/calculadora_auxilio_acidente.py prazos --ciencia 2026-07-01
python scripts/score_prontidao.py --exemplo > caso.json
python scripts/score_prontidao.py caso.json
```

Use o interpretador `python`. Em ambiente Windows sem `python3` configurado, `python3` falha.

## Aviso

Ferramenta de apoio ao trabalho do advogado. Não substitui conferência normativa. Antes de
protocolar qualquer peça, rode `references/14-vigilancia-normativa.md`.
