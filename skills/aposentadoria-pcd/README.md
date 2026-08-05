# Aposentadoria PCD — Skill (Claude Code / Cowork)

Skill de **Aposentadoria da Pessoa com Deficiência (PCD)** para Claude Code e Claude Cowork.
Atua como auxiliar jurídico sênior — experiente, com raciocínio crítico e analítico — em todo
o ciclo do caso: **triagem → enquadramento de grau (IF-BrA) → prova → perícia biopsicossocial
→ redação de peças → revisão de benefícios**.

Base legal: **LC 142/2013**, **Decreto 3.048/1999**, **CF art. 201 §1º (EC 103/2019)**,
**Portaria IF-BrA (nº 1/2014)**.

## Instalação

Copie a pasta `aposentadoria-pcd/` para o diretório de skills:

```
~/.claude/skills/aposentadoria-pcd/
```

A skill fica disponível automaticamente no Claude Code e no Cowork.

## Gatilhos (slash)

| Comando | Fluxo |
|---|---|
| `/atendimentopcd` | Atendimento, entrevista, enquadramento de grau e pontuação IF-BrA |
| `/peticaopcd` | Redação de peça a partir dos modelos da biblioteca |
| `/ifbra` | Enquadramento / pontuação IF-BrA de um caso |
| `/aposentadoriapcd`, `/pcd` | Roteia entre atendimento, peça ou dúvida |

Variantes aceitas: `/peticao-pcd`, `/atendimento-pcd`, `/peticaopcs`, `/petiçãopcd`.

## Estrutura

```
aposentadoria-pcd/
├── SKILL.md                          # Persona, gatilhos e fluxos (A: atendimento, B: peça)
└── references/
    ├── if-bra-metodologia.md         # Motor 25/50/75/100, faixas de grau, 41 atividades/7 domínios, barreiras, Fuzzy
    ├── roteiros-atendimento.md       # Roteiros Leve / Moderado / Grave + Roteiro Específico (intake)
    └── biblioteca/                   # 39 documentos + INDEX (acervo dos 44 PDFs incorporados)
        ├── INDEX.md
        ├── 01..04  → metodologia IF-BrA e perícia
        ├── 05..06  → roteiros de entrevista
        ├── 07..12  → petições iniciais (por tipo de deficiência/benefício)
        ├── 13..19  → ED, manifestações, impugnação e nulidade de perícia
        ├── 20..23  → quesitos
        ├── 24..28  → réplica e revisão
        ├── 29..37  → administrativo, teses e peças diversas
        ├── 38       → fluxograma LC 142 (transcrito)
        └── 39       → síntese doutrinária do curso PCD PRO
```

## Faixas de enquadramento (IF-BrA)

| Grau | Pontuação total | Tempo H | Tempo M |
|------|-----------------|---------|---------|
| Grave | ≤ 5.739 | 25 anos | 20 anos |
| Moderado | 5.740 – 6.354 | 29 anos | 24 anos |
| Leve | 6.355 – 7.584 | 33 anos | 28 anos |
| Insuficiente (não é PCD) | ≥ 7.585 | — | — |

Aposentadoria por idade PCD: Homem 60 / Mulher 55 + 15 anos como PCD. Cálculo: **100% da média**
(sem coeficiente 60%+2% da EC 103/19). Carência: 180.

## Aviso

Conteúdo **proprietário** (Cortex / Vértika), derivado do acervo do curso *Aposentadoria da PCD
PRO* (AJ&G). Os documentos da biblioteca são **modelos/base de trabalho**: toda peça gerada é
**minuta** — o advogado revisa e assina. Não use dados de exemplo dos modelos como se fossem do
cliente.
