# Skill: pensao-por-morte (Programa Cortex)

Sistema de atuação em pensão por morte do RGPS, urbana e rural, para advogado. Cobre da entrevista
com o cliente até a fase recursal administrativa e judicial, com pontuação de lacunas e cálculo
automatizado.

Data-base do conteúdo: agosto de 2026.

## Instalação no Claude Code

Opção 1, skill de projeto:
```
mkdir -p .claude/skills
cp -r pensao-por-morte .claude/skills/
```

Opção 2, skill pessoal (vale para todos os projetos):
```
mkdir -p ~/.claude/skills
cp -r pensao-por-morte ~/.claude/skills/
```

Comandos de atalho (opcional, para habilitar `/pensãopormorte`):
```
mkdir -p .claude/commands
cp pensao-por-morte/commands/*.md .claude/commands/
```

Se o Cortex já tiver estrutura própria de plugin, coloque a pasta em `skills/` do plugin e os
arquivos de `commands/` em `commands/`.

## Estrutura

```
pensao-por-morte/
├── SKILL.md                    ponto de entrada, fluxo em 9 fases
├── references/                 17 arquivos de conteúdo técnico
├── assets/                     14 modelos de documentos e peças
├── scripts/                    calculadora e índice de prontidão
└── commands/                   atalhos /pensãopormorte e /pensaopormorte
```

## Uso

Digite `/pensãopormorte` ou apenas mencione pensão por morte. A skill:

1. Pergunta se o caso é urbano ou rural e valida a classificação por conta própria.
2. Conduz entrevista estruturada em blocos curtos.
3. Calcula o Índice de Prontidão do Caso (0 a 100) e lista as lacunas com o ganho de cada
   diligência.
4. Analisa os três requisitos (morte, qualidade de segurado, dependência) pelo regime da data do
   óbito.
5. Calcula valor, cotas, duração, DIB, atrasados e acumulação.
6. Recomenda a via, monta o requerimento instruído e acompanha exigências.
7. Vai até recurso ordinário e especial no CRPS, ação no JEF, recurso inominado e uniformização.

## Scripts

```
python3 scripts/calculadora_pensao.py rmi --base 4000 --dependentes 3 --obito 2024-05-10
python3 scripts/calculadora_pensao.py duracao --obito 2024-05-10 --idade-dependente 43 --contribuicoes 22 --uniao-meses 60
python3 scripts/calculadora_pensao.py dib --obito 2025-01-02 --der 2026-04-15
python3 scripts/calculadora_pensao.py acumulacao --beneficio-a 4200 --beneficio-b 1900
python3 scripts/calculadora_pensao.py prazos --ciencia 2026-07-01
python3 scripts/score_prontidao.py --exemplo > caso.json
python3 scripts/score_prontidao.py caso.json
```

## Aviso

Ferramenta de apoio ao trabalho do advogado. Não substitui conferência normativa. Antes de
protocolar qualquer peça, rode `references/12-vigilancia-normativa.md`.
