# 📖 Bíblia de Prompts — Direito Previdenciário

Prompts prontos para colar direto no Claude (Code, Cowork ou app). Copie, troque o que
está entre `[colchetes]` pelos dados do seu caso, e envie.

> **Como usar:** cada prompt é autossuficiente. Para os fluxos completos (cálculo de CNIS,
> petição, recurso, decisão), use os comandos das skills: `/cnis`, `/peticionar`, `/recurso`,
> `/decisor`. Os prompts abaixo são para tarefas pontuais do dia a dia.

> **Regra de ouro anti-invenção:** sempre termine pedindo à IA que sinalize o que ela NÃO
> tem certeza. Nunca protocole nada sem conferir jurisprudência e dispositivos legais.

---

## 1. ANÁLISE DE DOCUMENTOS

### 1.1 — Resumir CNIS (rápido)
```
Anexei o CNIS do meu cliente. Faça:
1. Tabela de todos os vínculos (empregador, início, fim, tempo).
2. Lista de lacunas/gaps de contribuição.
3. Competências com contribuição abaixo do mínimo.
4. Indicadores (PEXT, PREC, IREC, IEAN) e o que cada um significa para o caso.
5. Tempo total de contribuição até hoje.
Não invente nada — se algum dado estiver ilegível, me pergunte.
```

### 1.2 — Ler laudo médico/pericial
```
Anexei um laudo médico. Extraia:
- CID(s) e descrição
- Conclusão pericial e grau de incapacidade
- Data de início da doença/incapacidade (DID/DII), se constar
- Prognóstico
Depois me diga: esse laudo favorece um pedido de [auxílio-doença / aposentadoria por
invalidez / BPC por deficiência]? Aponte os pontos fortes e fracos para esse benefício.
```

### 1.3 — Resumir contestação/decisão do INSS
```
Anexei a [contestação do INSS / decisão / carta de indeferimento]. Faça:
1. Resumo em 5 linhas do que o INSS alegou/decidiu.
2. Lista dos argumentos principais usados pelo INSS.
3. Jurisprudência/dispositivos que o INSS citou (apenas os que aparecem no documento).
4. Roteiro de como rebater cada argumento.
```

### 1.4 — Extrair dados de documentos para planilha
```
Anexei [CTPS / holerites / carnês]. Extraia em formato de tabela:
competência (mês/ano) | empregador/tipo | valor | observação.
Liste também o que falta para comprovar o período.
```

---

## 2. PESQUISA E TESES (sempre com verificação)

### 2.1 — Linhas de argumentação (sem citar processo)
```
Quais são as principais teses e linhas de argumentação para defender [benefício] no caso
de [situação resumida]? Liste os FUNDAMENTOS (princípios, dispositivos da Lei 8.213/91 e
da EC 103/2019). NÃO cite números de processo nem ementas — quero só as teses, que vou
validar depois.
```

### 2.2 — Checar uma tese
```
Existe fundamento legal para [tese, ex: "reconhecer tempo rural antes dos 12 anos de idade"]?
Me explique o estado atual do entendimento, citando apenas dispositivos legais e súmulas
que você tem CERTEZA que existem. Para qualquer ponto incerto, escreva [VERIFICAR] em vez
de afirmar.
```

### 2.3 — Diferença entre regras
```
Explique, em linguagem simples, a diferença entre [regra A] e [regra B] de aposentadoria
após a EC 103/2019: requisitos, quem se beneficia de cada uma, e a principal armadilha de
cada regra.
```

---

## 3. ATENDIMENTO E COMUNICAÇÃO COM CLIENTE

### 3.1 — Traduzir juridiquês
```
Reescreva o texto abaixo em português simples, que um cliente leigo entenda, mantendo a
precisão. Tom acolhedor, sem prometer resultado:

[colar a decisão/explicação técnica]
```

### 3.2 — Explicar o indeferimento ao cliente
```
O INSS negou o benefício do meu cliente com este motivo: [motivo].
Escreva uma mensagem de WhatsApp para o cliente explicando, em linguagem simples:
(1) o que significa essa negativa, (2) que ainda há caminhos (recurso/ação),
(3) próximos passos. Tom tranquilizador, sem prometer ganho de causa.
```

### 3.3 — Lista de documentos para o cliente
```
Meu cliente quer dar entrada em [benefício]. Gere uma lista clara, em formato de checklist,
de todos os documentos que ele precisa providenciar, com uma frase explicando para que serve
cada um. Linguagem simples.
```

### 3.4 — Roteiro de primeira reunião
```
Vou atender um cliente que quer [benefício]. Monte um roteiro de perguntas que eu devo
fazer na primeira reunião para entender o caso e já identificar pontos críticos
(qualidade de segurado, carência, tempo especial, etc.).
```

---

## 4. PEÇAS E DOCUMENTOS (rascunho rápido)

> Para a petição completa com jurisprudência real, use `/peticionar`. Os prompts abaixo são
> para rascunhos rápidos de trechos.

### 4.1 — Rascunho da seção "DOS FATOS"
```
Escreva a seção "DOS FATOS" de uma petição inicial previdenciária com base nesta narrativa:
[narrativa do caso]
Linguagem forense, objetiva, cronológica. Deixe [PREENCHER] onde faltar dado.
```

### 4.2 — Quesitos para perícia médica
```
Vou ter uma perícia médica judicial em um caso de [benefício por incapacidade].
Gere uma lista de quesitos estratégicos para apresentar ao perito, focados em comprovar
[incapacidade total/parcial, permanente/temporária, data de início]. Considere as
condições pessoais e sociais do segurado: [idade, profissão, escolaridade].
```

### 4.3 — Requerimento administrativo
```
Escreva um requerimento administrativo ao INSS para [benefício], com base em:
[dados do segurado e fatos]. Estrutura formal, fundamentação na Lei 8.213/91.
Deixe [PREENCHER] em dados que faltam.
```

---

## 5. ESTRATÉGIA E DECISÃO

> Para a análise de decisão completa (break-even, VPL), use `/decisor`.

### 5.1 — Vale a pena judicializar?
```
Meu cliente teve [benefício] negado por [motivo]. Considerando [resumo das provas que tenho],
faça uma análise de viabilidade: pontos fortes, pontos fracos, probabilidade aproximada de
êxito (alta/média/baixa com justificativa) e se recomenda recurso administrativo, ação
judicial, ou reunir mais provas antes.
```

### 5.2 — Parecer de viabilidade para o cliente
```
Com base na análise acima, escreva um parecer curto (1 página) em linguagem acessível para
o cliente, explicando se vale a pena seguir com o caso e por quê. Sem prometer resultado.
```

---

## 6. GESTÃO E PRODUTIVIDADE DO ESCRITÓRIO

### 6.1 — Resumo de processo para audiência
```
Anexei os autos / colei o resumo do processo. Gere uma "ficha de audiência" com:
- Partes e benefício
- Síntese do caso em 5 linhas
- Pontos controvertidos
- Provas a meu favor e contra
- Perguntas-chave para testemunhas
```

### 6.2 — Conteúdo para Instagram (autoridade)
```
Crie um roteiro de Reels (gancho + conteúdo + CTA) explicando, para leigos, o tema
[ex: "revisão da vida toda" / "quem tem direito ao BPC"]. Tom didático, sem prometer
resultado, respeitando as regras da OAB para publicidade.
```

### 6.3 — Resposta a dúvida frequente
```
Um seguidor perguntou: "[pergunta]". Responda de forma clara e curta, como um advogado
previdenciário responderia nos comentários — informativo, sem dar consulta jurídica
individual, convidando a procurar atendimento para o caso concreto.
```

---

## 7. REVISÃO E CONFERÊNCIA

### 7.1 — Revisar minha petição
```
Revise a petição abaixo como um advogado sênior faria. Verifique: coerência entre fatos e
pedidos, fundamentação, citações (aponte qualquer ementa/súmula que pareça inventada ou
que eu deva conferir), campos faltando, e erros. Liste os problemas em ordem de gravidade.

[colar a petição]
```

### 7.2 — Conferir cálculo
```
Confira a lógica deste cálculo de tempo de contribuição / RMI. Aponte qualquer erro de
contagem, regra mal aplicada ou premissa duvidosa. Não refaça o cálculo do zero — só
audite o que está aqui:

[colar o cálculo]
```

---

## ⚠️ DISCLAIMER PARA TODOS OS PROMPTS

A IA é ferramenta de apoio, não substitui o advogado. **Sempre:**
- Confira jurisprudência e dispositivos legais antes de usar (a IA pode inventar).
- Revise valores e cálculos em software homologado.
- Adapte ao caso concreto e às regras da OAB.
- A peça/parecer gerado é minuta — você revisa, assina e se responsabiliza.

---

*Bíblia de Prompts — Cortex / Vértika · IA aplicada à advocacia previdenciária*
