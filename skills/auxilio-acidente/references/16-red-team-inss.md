# 16. Red team: escreva a defesa do INSS antes dele

Passo obrigatório antes de recomendar protocolo, entregar recurso ou petição inicial. O
objetivo é encontrar o ponto por onde o caso vai ser atacado e blindar antes, especialmente
porque a análise documental prévia da Portaria 15/2026 pode indeferir sem sequer agendar
perícia, sem chance de o cliente "se explicar" pessoalmente.

Método: para cada ataque aplicável, produza três linhas. Ataque, como o caso está exposto,
blindagem concreta. Nunca liste o ataque sem a blindagem, e nunca declare blindagem sem apontar
a prova que a sustenta.

---

## 1. Ataques ao enquadramento do beneficiário

| # | Ataque | Blindagem |
|---|---|---|
| A1 | "Requerente é contribuinte individual, fora do rol do art. 18, §1º" | Testar a exceção do período de graça de vínculo anterior. Documentar a data da rescisão do último vínculo elegível e a data do evento dentro da janela do art. 15. Sinalizar que é tese não pacificada |
| A2 | "Categoria alegada não confere com o CNIS" | Reunir prova adicional da categoria, como CTPS física, registro sindical, cadastro de segurado especial, e explicar a divergência |
| A3 | "Empregado doméstico, mas o evento é anterior a 01/06/2015" | Verificar se a doença é ocupacional com consolidação posterior a essa data, o que pode reabrir a análise sobre qual data rege o direito |

## 2. Ataques ao nexo técnico

| # | Ataque | Blindagem |
|---|---|---|
| B1 | "Não há CAT" | Demonstrar que a CAT não é requisito. Reunir NTEP, PPP, laudo técnico, prontuário do atendimento, testemunhas |
| B2 | "Doença não consta da lista de doenças profissionais" | Reclassificar como doença do trabalho (art. 20, II), que não depende de lista fechada, e provar o nexo causal ou concausal com as condições concretas de trabalho |
| B3 | "Acidente de trajeto com desvio de rota" | Demonstrar que o desvio foi pequeno e justificável, dentro das necessidades cotidianas normais, sem quebra do nexo com o deslocamento habitual |
| B4 | "Doença também existe fora do ambiente de trabalho, não é exclusiva da profissão" | Sustentar o nexo concausal do art. 20, II, que não exige exclusividade, apenas relação com as condições especiais em que o trabalho é realizado |

## 3. Ataques à sequela e à redução de capacidade

| # | Ataque | Blindagem |
|---|---|---|
| C1 | "Lesão não consolidada, ainda em tratamento" | Reconhecer, se for o caso, e orientar sobre o momento correto de protocolar. Se houver divergência médica, buscar relatório atualizado do médico assistente afirmando estabilização |
| C2 | "Grau da lesão é mínimo, não gera direito" | Tema 416/STJ e Súmula 88/TNU: grau mínimo não afasta o direito, desde que exista redução real |
| C3 | "Sequela não consta do Anexo III do Decreto 3.048/99" | Sustentar o caráter exemplificativo do rol, com fundamentação da redução funcional concreta e específica |
| C4 | "Segurado continua exercendo a mesma função sem alteração perceptível" | Levantar prova de adaptação, esforço adicional, redução de rendimento, ou ajuda de terceiros, mesmo sem mudança formal de função |
| C5 | "Relato do cliente é genérico, sem especificidade funcional" | Refazer a entrevista com foco em tarefas concretas: o que fazia antes, o que não consegue mais fazer do mesmo jeito |

## 4. Ataques na análise documental prévia (Portaria 15/2026)

| # | Ataque | Blindagem |
|---|---|---|
| D1 | "Documentação médica insuficiente para caracterizar a sequela" | Antes de protocolar, reunir relatório médico específico sobre consolidação e repercussão funcional, não apenas exames de imagem isolados |
| D2 | "Documentação não demonstra nexo" | Incluir CAT ou documento equivalente, NTEP, PPP, conforme o caso, já no requerimento inicial |
| D3 | "Indeferimento sem perícia presencial" | Recurso administrativo reforçando exatamente o ponto apontado como ausente, com novo documento específico |

## 5. Ataques de cumulação e vedação

| # | Ataque | Blindagem |
|---|---|---|
| E1 | "Já recebe aposentadoria, vedada a cumulação" | Testar as duas datas da Súmula 507/STJ: lesão e aposentadoria ambas anteriores a 11/11/1997. Se uma for posterior, reconhecer a vedação com honestidade |
| E2 | "Já recebe auxílio-doença pela mesma lesão" | Demonstrar que são sequenciais, não simultâneos: o auxílio-acidente nasce quando o auxílio-doença cessar, não antes |
| E3 | "Pede conversão em aposentadoria por invalidez automaticamente" | Explicar que essa conversão automática não existe desde a Lei 9.528/97. Orientar sobre o requerimento novo e autônomo, se aplicável |

## 6. Ataques processuais

| # | Ataque | Blindagem |
|---|---|---|
| F1 | "Ausência de prévio requerimento administrativo" | Tema 350/STF: protocolar antes de ajuizar, salvo hipóteses de dispensa |
| F2 | "Decadência" | ADI 6096/STF e Súmula 81/TNU: não há decadência para indeferimento, cancelamento e cessação |
| F3 | "Prescrição quinquenal" | Limitar o pedido às parcelas dentro do quinquênio, ou invocar a ressalva de menores, incapazes e ausentes |
| F4 | "Incompetência do juízo" | Conferir valor da causa, teto de 60 salários mínimos e a regra do Tema 820/STF |

---

## 7. Saída do red team

```
RED TEAM · [caso]
Ataques provaveis, em ordem de risco
1. [codigo] · Exposicao: ....................
   Blindagem adotada: ....................
   Prova que sustenta: ....................
   Risco residual: [alto | medio | baixo]
2. ...

Ataques que nao temos como neutralizar hoje
· ....................  -> decisao: [aguardar prova | assumir o risco | recusar o caso]

Alteracoes feitas na peca em razao deste exercicio
· ....................
```

Se sobrar um ataque de risco alto sem blindagem, não protocole sem antes registrar a decisão
por escrito com o cliente. Isso vale com força redobrada aqui, porque a análise documental
prévia pode indeferir sem chance de correção pessoal na perícia.
