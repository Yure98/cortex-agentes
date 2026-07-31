# Skill: salario-maternidade

Skill de operação completa de casos de salário-maternidade no RGPS, da entrevista à fase recursal.
Construída para uso por advogado previdenciarista dentro do programa **Cortex**.

## Instalação no Claude Code

Copie a pasta inteira para o diretório de skills:

```bash
# escopo do projeto
cp -r salario-maternidade .claude/skills/

# ou escopo do usuário (disponível em todos os projetos)
cp -r salario-maternidade ~/.claude/skills/
```

A skill dispara sozinha quando a conversa envolve salário-maternidade, INSS e maternidade, benefício
B80, segurada especial com filho, gestante desempregada, adoção, natimorto ou indeferimento do INSS.
Também pode ser invocada pelo nome.

## Estrutura

```
salario-maternidade/
├── SKILL.md                      ← ponto de entrada; pipeline de 9 fases e varredura de passivo
├── references/                   ← carregadas sob demanda
│   ├── 00-mapa-normativo.md      ← ÚNICA fonte autorizada para citações (antialucinação)
│   ├── 01-triagem-e-entrevista.md
│   ├── 02-urbano.md
│   ├── 03-rural.md
│   ├── 04-fatos-geradores-especiais.md
│   ├── 05-fase-administrativa.md
│   ├── 06-recurso-crps.md
│   ├── 07-fase-judicial.md
│   ├── 08-fase-recursal-judicial.md
│   ├── 09-calculo-e-valores.md
│   ├── 10-teses-e-gaps.md        ← varredura de passivo; o diferencial
│   └── 11-erros-fatais.md
├── assets/
│   ├── ficha-de-entrevista.md
│   ├── checklists-documentais.md
│   ├── modelo-recurso-crps.md
│   ├── modelo-peticao-inicial-jef.md
│   └── modelo-quesitos-testemunhas.md
└── scripts/
    └── diagnostico.py            ← prazos, período de graça, prescrição, RMI, art. 73-A
```

## Calculadora

```bash
python3 scripts/diagnostico.py --exemplo
python3 scripts/diagnostico.py --interativo
python3 scripts/diagnostico.py --json caso.json
```

Sem dependências externas. Python 3.10+.

Saída: semáforo de viabilidade, contagem do período de graça com a extensão do art. 30, II, da
Lei 8.212/91, prescrição com suspensão administrativa (Súmula 74/TNU), duração com a regra da
Lei 15.222/2025, RMI por categoria e checagem do prazo do art. 73-A.

## Como a skill trabalha

1. Pergunta se o caso é urbano ou rural.
2. **Classifica por conta própria**, em quatro trilhos (U, R, H, D), e avisa quando diverge da resposta.
3. Percorre o pipeline de 9 fases, com quatro gates de segurança.
4. Ao final, roda a **varredura de passivo**: identifica as pretensões adicionais que o mesmo fato
   gerador abre.

## Manutenção

- **Anual (janeiro):** salário mínimo, teto do RGPS, alçada do JEF — em `09-calculo-e-valores.md` e
  em `scripts/diagnostico.py`.
- **Semestral:** novas INs do INSS, resoluções do CRPS, temas do STF/STJ/TNU — em `00-mapa-normativo.md`.
- **Quando julgado:** Tema 1.274/STF (cota da segurada) — atualizar `10-teses-e-gaps.md` §5.

Itens marcados `[VOLÁTIL]` são os que envelhecem. Base consolidada até **30/07/2026**.

## Aviso

Ferramenta de apoio ao trabalho do advogado. Não substitui análise do caso concreto nem dispensa a
conferência das fontes primárias antes do protocolo de qualquer peça.
