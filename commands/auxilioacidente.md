---
description: Inicia o atendimento completo de auxílio-acidente (urbano ou rural), da entrevista à fase recursal
---

Ative a skill `auxilio-acidente` (leia `SKILL.md` antes de qualquer resposta) e inicie o
atendimento pela Fase 0.

Contexto informado pelo usuário (pode estar vazio): $ARGUMENTS

Regras desta execução:
1. Se houver contexto acima, extraia dele o que já foi dito e não repita perguntas respondidas.
2. Abra com no máximo 6 linhas e faça imediatamente a pergunta obrigatória de enquadramento:
   urbano, rural, ou não sei.
3. Rode o protocolo de classificação mesmo que o usuário afirme o enquadramento.
4. Conduza a entrevista em blocos de 6 a 8 perguntas, atualizando o Painel do Caso e o Índice
   de Prontidão Probatória ao final de cada bloco.
5. Use os scripts para todo cálculo. Nunca calcule de cabeça.
6. Antes de recomendar protocolo, recurso ou petição, rode os dois portões obrigatórios: o red
   team contra o INSS e a varredura de oportunidades conexas.
7. Ao final de cada fase, ofereça o entregável em arquivo.
