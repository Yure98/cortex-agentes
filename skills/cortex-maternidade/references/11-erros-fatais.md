# 11 — Erros Fatais

Leia antes de protocolar qualquer coisa. Cada item aqui corresponde a caso perdido de forma evitável.

## Erros que matam o caso inteiro

| # | Erro | Consequência | Prevenção |
|---|---|---|---|
| 1 | Ajuizar sem prévio requerimento | Extinção sem mérito (Tema 350/STF) | Confirmar a DER antes de qualquer minuta |
| 2 | Ajuizar caso rural sem nenhum início de prova material | Extinção sem mérito (Tema 629/STJ) na melhor hipótese; improcedência na pior | Gate 3 do SKILL.md. Buscar prova antes |
| 3 | Perder o prazo de 30 dias do CRPS **e** reprotocolar | A IN 203/2026 veda novo requerimento com prazo recursal em curso | Marcar o prazo na ciência do indeferimento |
| 4 | Não computar a suspensão da prescrição | Prescrição reconhecida indevidamente | Súmula 74/TNU demonstrada com datas na inicial |
| 5 | Enquadrar boia-fria como segurada especial | Improcedência por enquadramento | Classificador do `01`, etapa A, B1 |
| 6 | Contar o período de graça sem a extensão do art. 30, II, da Lei 8.212/91 | Conclusão errada sobre qualidade de segurada | `scripts/diagnostico.py` |
| 7 | Litispendência com recurso administrativo em curso | Extinção | Pergunta 5 da triagem |

## Erros que reduzem o resultado

| # | Erro | Consequência | Prevenção |
|---|---|---|---|
| 8 | Pedir remuneração integral para desempregada | Pedido reduzido (Tema 202/TNU); base de honorários menor | Art. 73, III sempre para desempregada |
| 9 | Aceitar 14 dias em caso de natimorto | Perda de 106 dias | Checar certidão de óbito fetal |
| 10 | Não pedir a DIB no fato gerador | Atrasados menores | Pedido expresso na inicial |
| 11 | Não verificar internação prolongada | Perda da regra da Lei 15.222/2025 | Pergunta obrigatória na entrevista |
| 12 | Cumular Selic com INPC após 09/12/2021 | Impugnação e atraso na RPV | EC 113/2021: Selic única |
| 13 | Não fazer a varredura do Passo 3 | Cliente sai com 1 pedido quando tinha 3 | `10-teses-e-gaps.md` sempre |

## Erros de argumentação

| # | Erro | Por quê |
|---|---|---|
| 14 | Gastar a peça provando que a carência caiu, quando o indeferimento foi por qualidade de segurada | Ataque o que foi decidido, não o que você explica melhor |
| 15 | Citar só a jurisprudência de aposentadoria rural por idade | Existe regime probatório **específico** e mais favorável: Temas 11 e 17/TNU |
| 16 | Aceitar a descaracterização pelo vínculo urbano do cônjuge | Tema 532/STJ: ônus é do INSS e a exclusão é individual (art. 11, § 10) |
| 17 | Não pedir a certidão de módulo fiscal quando o INSS alega área excessiva | O limite é 4 módulos **fiscais**, não módulo rural (Súmula 30/TNU) |
| 18 | Apresentar a autodeclaração rural desacompanhada | Art. 38-B exige ratificação |
| 19 | Não formular pedido subsidiário | Sentença tudo-ou-nada |
| 20 | Não pedir extinção sem mérito quando o cenário probatório está perdido | Improcedência impede nova ação; extinção não (Tema 629/STJ) |

## Erros de condução com a cliente

| # | Erro | Prevenção |
|---|---|---|
| 21 | Mandar empregada CLT procurar parcelas no Meu INSS | Quem paga é a empresa (art. 72, § 1º), salvo adoção e dispensa na gravidez |
| 22 | Não orientar o acompanhamento do Meu INSS | Indeferimento por exigência não cumprida é dos mais comuns |
| 23 | Aceitar o resumo da cliente sobre o motivo do indeferimento | Peça a carta e o processo administrativo integral |
| 24 | Levar testemunha parente de primeiro grau quando havia vizinho | Credibilidade reduzida |
| 25 | Ensaiar respostas idênticas entre testemunhas | Lido como combinação; derruba o conjunto |
| 26 | Prometer prazo do INSS ou resultado | Nunca faça |

## Erros específicos da skill (você, assistente)

| # | Erro | Prevenção |
|---|---|---|
| 27 | Inventar número de processo, tema, súmula ou enunciado | Use apenas `00-mapa-normativo.md`; marque `[PRECEDENTE A LOCALIZAR]` |
| 28 | Apresentar tese em construção como pacífica | Marque 🟧 / `[TESE EM CONSTRUÇÃO]` |
| 29 | Afirmar valor de salário mínimo ou teto sem conferir | Marque `[VOLÁTIL]` |
| 30 | Aceitar o trilho informado pelo usuário sem verificar | Passo 1 do SKILL.md é obrigatório |
| 31 | Interrogar em série | Peça tudo em bloco numerado e ofereça premissas |
| 32 | Entregar parecer sem semáforo e sem riscos | O advogado precisa da calibração, não só do argumento |
| 33 | Não rodar a varredura do Passo 3 | É o principal diferencial da skill |

---

## Revisão final em 10 pontos

Antes de entregar qualquer peça ou parecer:

1. Trilho e categoria conferidos contra documento?
2. Qualidade de segurada verificada **na data do fato gerador**?
3. Prescrição calculada com suspensão?
4. Prévio requerimento confirmado?
5. Prova material suficiente (trilhos R e D)?
6. Fato gerador com a duração correta?
7. RMI conforme a categoria?
8. Pedidos principal e subsidiário formulados?
9. Todas as citações existem em `00-mapa-normativo.md`?
10. Varredura do Passo 3 rodada e reportada?
