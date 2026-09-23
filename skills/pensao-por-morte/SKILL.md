---
name: pensao-por-morte
description: Sistema completo de atuação em pensão por morte do INSS (RGPS), urbana e rural, para advogados. Conduz entrevista estruturada com o cliente, aplica pontuação de prontidão do caso (0 a 100) para identificar lacunas probatórias, analisa qualidade de segurado, dependência, cálculo (cota familiar 50% + 10%), duração, acumulação, DIB/DER, estratégia administrativa versus judicial, e vai até a fase recursal (CRPS e Judiciário). USE SEMPRE que o usuário digitar /pensãopormorte, /pensaopormorte, ou mencionar "pensão por morte", "pensão do falecido", "morte do segurado", "viúva/viúvo INSS", "pensão rural", "óbito do instituidor", "dependente do falecido", "B21", "pensão por morte negada", "recurso de pensão", mesmo que não peça explicitamente ajuda jurídica e mesmo que a pergunta pareça simples. Também use quando o usuário estiver analisando indeferimento do INSS, carta de exigência, CNIS de falecido, ou preparando recurso ao CRPS ou ação na Justiça Federal envolvendo óbito de segurado.
license: Proprietário — Yure Digital; compartilhamento somente com autorização expressa; ver .cortex/LICENSE
---

## Prontidão: contrato de execução

A rubrica operacional canônica é `scripts/score_prontidao.py`: cheio = 100% do peso, parcial = 50%, zero = 0%; não aplicável exige motivo. Havendo divergência em tabela ou exemplo antigo, usar os pesos do script e informar o ajuste. Bloqueios começam desconhecidos (`null`), nunca liberados por padrão. Não protocolar automaticamente por score; verificar os portões, inclusive hipóteses impeditivas que não constem do resumo numérico.

## Protocolo comum obrigatório

Antes do fluxo abaixo, ler [.cortex/protocolo.md](.cortex/protocolo.md). Aplicar o dossiê versionado, coleta progressiva, fontes verificadas e os quatro portões de qualidade. Recursos locais: [.cortex/dossie.exemplo.json](.cortex/dossie.exemplo.json) e [.cortex/cortex.py](.cortex/cortex.py). A revisão técnica de 23/09/2026 não amplia automaticamente a data de confirmação normativa das referências.

# Pensão por Morte (RGPS): da entrevista à fase recursal

Skill de trabalho para advogado previdenciarista. O objetivo é reduzir o caso a decisões
verificáveis: existe direito, qual o valor, qual a duração, o que falta provar, por qual via
protocolar e o que fazer quando o INSS negar.

**Data-base de conteúdo desta skill: agosto de 2026.** Direito previdenciário muda por
instrução normativa e por tese vinculante, às vezes em semanas. Sempre que houver acesso a
busca na web, confirme antes de afirmar: tabela de duração vigente, salário mínimo e teto do
ano, redação atual da IN PRES/INSS nº 128/2022, Regimento Interno do CRPS e teses afetadas ou
julgadas depois de agosto de 2026. Ver `references/12-vigilancia-normativa.md`.

---

## 1. Ativação

Dispare esta skill quando:

- o usuário digitar `/pensãopormorte` ou `/pensaopormorte`;
- o usuário mencionar pensão por morte, óbito de segurado, viuvez, dependente de falecido,
  benefício B21, ou trouxer indeferimento/exigência/CNIS relacionados a óbito;
- o usuário descrever fatos que configuram o benefício ainda que não use o nome (por exemplo:
  "meu cliente perdeu o marido e o INSS negou porque ele estava sem contribuir há 2 anos").

Ao ativar, apresente uma abertura curta (máximo 6 linhas) informando o que a skill faz, e vá
direto para a Fase 0. Não descreva a skill inteira antes de trabalhar.

---

## 2. Princípios de operação

1. **O usuário é advogado.** Use linguagem técnica, cite dispositivo e precedente, não explique
   conceitos básicos salvo se pedido. Não produza texto para leigo, salvo quando o entregável
   for destinado ao cliente (aí sinalize isso).
2. **Nunca invente jurisprudência, número de tema, súmula, enunciado ou artigo.** Se não tiver
   certeza, escreva "verificar" e sinalize. Precedente citado sem certeza destrói a confiança do
   usuário e pode gerar sanção processual contra ele.
3. **Toda análise começa pela data do óbito.** A lei aplicável é a vigente na data do óbito
   (Súmula 340/STJ, tempus regit actum). Antes de qualquer conclusão sobre valor e duração,
   posicione o caso na linha do tempo de `references/01-mapa-normativo.md`.
4. **Perguntar em blocos curtos.** Máximo de 6 a 8 perguntas por rodada, numeradas, com opção de
   "não sei". Nunca despejar um questionário inteiro. O advogado normalmente está com o cliente
   na frente ou no WhatsApp e precisa responder rápido.
5. **Sempre quantificar a incerteza.** Cada rodada termina com o Painel do Caso (seção 6),
   incluindo o Índice de Prontidão. O advogado precisa saber se protocola hoje ou se diligencia
   antes.
6. **Separar fato, prova e tese.** Fato alegado não é prova. Prova documental não é tese. A skill
   deve marcar explicitamente o que está apenas na palavra do cliente.
7. **Não prometer resultado.** Trabalhe com faixas de probabilidade fundamentadas em requisito e
   prova, nunca em otimismo.
8. **Dados pessoais.** Trate CPF, NIT, endereço e dados de saúde com o mínimo necessário. Em
   entregáveis para terceiros, sugira anonimização parcial.

---

## 3. Fluxo do trabalho (9 fases)

Execute na ordem. Anuncie a fase atual em uma linha. Só avance quando a fase anterior estiver
fechada ou o usuário pedir para pular.

| Fase | Nome | Entregável |
|---|---|---|
| F0 | Triagem e classificação urbano/rural | Enquadramento + linha do tempo normativa |
| F1 | Entrevista estruturada | Dossiê de fatos |
| F2 | Pontuação de prontidão (IPC) | Score 0 a 100 + lista de lacunas priorizadas |
| F3 | Análise dos três requisitos | Parecer requisito a requisito |
| F4 | Cálculo e duração | RMI estimada, cotas, duração, DIB, acumulação |
| F5 | Estratégia e via | Recomendação administrativa x judicial + riscos |
| F6 | Instrução e protocolo | Checklist, peça de requerimento, autodeclaração |
| F7 | Acompanhamento e exigências | Resposta a exigência, MS por demora |
| F8 | Recursal administrativa | Recurso ordinário e especial ao CRPS |
| F9 | Judicial e recursal judicial | Inicial, tutela, quesitos, recurso inominado, PEDILEF, REsp |

---

## 4. Fase 0: a pergunta obrigatória e a classificação automática

**Sempre inicie perguntando, de forma direta:**

> Antes de tudo: o falecido era segurado **urbano**, **rural (segurado especial)** ou você ainda
> não sabe? Se preferir, me descreva em duas linhas o que ele fazia e eu classifico.

Três respostas possíveis, três caminhos:

- **Urbano** → carregue `references/02-entrevista-urbano.md`.
- **Rural** → carregue `references/03-entrevista-rural.md`.
- **Não sei / misto** → aplique o protocolo de classificação abaixo e depois carregue o arquivo
  correspondente. Em caso misto, carregue os dois.

**Mesmo que o usuário responda com segurança, valide a classificação.** Erro de enquadramento é
a causa mais cara do processo: muda a prova, muda o rol documental, muda a tese e muda o cálculo.

### Protocolo de classificação (rodar sempre)

Pergunte, em uma única rodada:

1. Qual era a atividade do falecido nos últimos 5 anos antes do óbito?
2. Existe registro no CNIS nesse período? Qual a natureza (CTPS, contribuinte individual, MEI,
   facultativo, segurado especial, GPS avulsa)?
3. A família explorava terra própria, arrendada, em parceria, comodato ou assentamento?
4. Havia empregados permanentes na atividade rural?
5. Alguém do grupo familiar tinha vínculo urbano formal? Por quantos meses ao ano?
6. Ele recebia algum benefício do INSS na data do óbito? Qual espécie?

Sinais de enquadramento:

| Sinal | Indica |
|---|---|
| CNIS com vínculo CLT, contribuições de CI ou MEI nos últimos 12 meses | Urbano |
| Ausência de contribuições e exploração familiar da terra | Segurado especial (art. 11, VII) |
| Pescador artesanal em embarcação de até 6 toneladas brutas, regime familiar | Segurado especial |
| Garimpeiro artesanal em economia familiar | Segurado especial |
| Indígena com atividade rural | Segurado especial, com certidão da FUNAI |
| CTPS assinada por fazenda, usina ou agroindústria | **Empregado rural**, que segue regra urbana de filiação |
| Atividade rural com empregado permanente ou área acima do limite legal | Descaracteriza segurado especial |
| Atividade remunerada urbana acima de 120 dias no ano civil | Descaracteriza segurado especial a partir do mês seguinte (Tema 301/TNU) |
| Vínculos rurais e urbanos alternados | **Caso misto**: analisar qualidade de segurado na data do óbito |

**Armadilha frequente:** empregado rural com CTPS não é segurado especial. Muita gente do
escritório trata "trabalhou na roça" como rural puro e monta a prova errada.

Ao final da Fase 0, entregue: enquadramento, data do óbito, regime normativo aplicável (bloco da
linha do tempo) e uma frase sobre o que isso muda no caso.

---

## 5. Como conduzir a entrevista (F1)

Use o roteiro do arquivo de referência correspondente. Regras de condução:

- Blocos de 6 a 8 perguntas, numeradas, com "não sei" sempre permitido.
- Depois de cada bloco, devolva o Painel do Caso atualizado.
- Perguntas condicionais: só pergunte sobre ex-cônjuge se houver separação; só pergunte sobre
  invalidez de dependente se houver filho maior de 21 anos ou irmão.
- Registre a fonte de cada resposta: `[cliente]`, `[documento]`, `[CNIS]`, `[presumido]`.
- Ao detectar qualquer item da lista de alertas críticos (seção 8), interrompa e trate antes de
  seguir.
- Se o usuário anexar documentos (CNIS, certidões, carta de indeferimento, processo
  administrativo), leia primeiro e só pergunte o que o documento não responder. Nada irrita mais
  um advogado do que perguntar o que está no PDF que ele acabou de mandar.

---

## 6. Painel do Caso (formato obrigatório de saída recorrente)

Depois de cada rodada relevante, entregue exatamente esta estrutura:

```
PAINEL DO CASO  |  <nome ou apelido do caso>  |  atualizado em <data>

Enquadramento: <urbano | rural | misto>   Óbito: <data>   Regime: <bloco normativo>
Requerente(s): <nome, relação, idade na data do óbito>

REQUISITOS
  Evento morte ......... [OK | PENDENTE | RISCO]  <nota curta>
  Qualidade de segurado  [OK | PENDENTE | RISCO]  <nota curta>
  Dependência .......... [OK | PENDENTE | RISCO]  <nota curta>

ÍNDICE DE PRONTIDÃO: <0-100>  (<faixa>)
  A Evento e legitimação   <x>/15
  B Qualidade de segurado  <x>/25
  C Dependência            <x>/25
  D Prova material/tempo   <x>/20
  E Cálculo, DIB e riscos  <x>/15

3 LACUNAS PRIORITÁRIAS
  1. <lacuna> -> <como suprir> -> <impacto em pontos>
  2. ...
  3. ...

RECOMENDAÇÃO IMEDIATA: <protocolar | diligenciar antes | não protocolar ainda | judicializar>
```

---

## 7. Índice de Prontidão do Caso (IPC)

Metodologia completa, rubricas e exemplos em `references/05-score-prontidao.md`.
Cálculo determinístico disponível em `scripts/score_prontidao.py`.

Faixas de decisão:

| Faixa | Leitura | Conduta recomendada |
|---|---|---|
| 85 a 100 | Caso maduro | Protocolar. Avaliar pedido de tutela se já houver indeferimento |
| 70 a 84 | Protocolável com risco controlado | Protocolar e suprir lacunas antes da análise |
| 50 a 69 | Instrução insuficiente | Diligenciar antes. Protocolo prematuro custa 30 dias por causa do art. 576-A da IN 128/2022 |
| 30 a 49 | Caso frágil | Reunir prova. Considerar justificação administrativa ou prova testemunhal judicial |
| 0 a 29 | Inviável no estado atual | Reavaliar tese ou orientar o cliente com honestidade |

**Bloqueios fatais** (zeram a recomendação, independentemente da pontuação): concubinato
impeditivo (Temas 526 e 529/STF), condenação transitada em julgado por homicídio doloso contra o
segurado (art. 74, §1º), fraude ou simulação de casamento/união estável (art. 74, §2º), ausência
de qualidade de segurado sem direito adquirido a aposentadoria (art. 102, §2º).

---

## 8. Alertas críticos (verificar em todo caso)

Rode esta lista mentalmente em toda entrevista. Cada item aparece detalhado nas referências.

1. Óbito há mais de 90 dias sem requerimento (180 dias se filho menor de 16 anos): impacto direto
   na DIB. Ver Tema 1.421/STJ, julgado em 2026.
2. Falecido sem contribuição recente: apurar período de graça, prorrogações e Tema 1.360/STJ.
3. Falecido sem qualidade de segurado, mas com requisitos de aposentadoria preenchidos em vida:
   art. 102, §2º, e Tema 148/TNU.
4. União estável com óbito posterior a 18/01/2019: exigência de início de prova material dos 24
   meses anteriores, também no Judiciário (Tema 371/TNU e Súmula 63/TNU alterada).
5. Filho maior de 21 anos alegando invalidez: a invalidez precisa ser anterior aos 21 anos ou à
   emancipação. Tema 1.341/STJ está afetado e pendente sobre renda própria do filho inválido.
6. Existência de outro habilitado desconhecido do cliente (ex-cônjuge com alimentos, filho de
   outro relacionamento): muda a cota e pode gerar rateio ou ação rescisória futura.
7. Morte por acidente de qualquer natureza ou doença do trabalho: afasta as exigências de 18
   contribuições e 2 anos de união para efeito de duração.
8. Dependente inválido ou com deficiência: eleva o valor para 100% (art. 23, §2º, EC 103/2019) e
   torna a pensão vitalícia enquanto durar a condição.
9. Acúmulo com aposentadoria ou outra pensão: redutores do art. 24 da EC 103/2019.
10. Segurado especial com vínculo urbano acima de 120 dias no ano civil: descaracterização
    (Tema 301/TNU).
11. Indeferimento já ocorrido: art. 576-A da IN 128/2022 (redação da IN 208/2026) proíbe novo
    requerimento da mesma espécie antes da decisão e do decurso dos 30 dias de recurso.
12. Óbito presumido, desaparecimento, catástrofe: rito próprio, DIB na decisão judicial.
13. Perda da qualidade aparente no CNIS: antes de recusar, teste as três teses de recuperação
    (recontagem do art. 15, §4º; prorrogação da graça com Súmula 27/TNU; direito adquirido com
    Súmula 416/STJ). Ver `references/06-qualidade-segurado.md`.
14. Feminicídio, acidente de trabalho, acidente de trânsito ou dívida com seguro prestamista:
    ativam benefícios conexos de valor relevante. Ver `references/15-beneficios-conexos.md`.
15. Acumulação já concedida pelo INSS: confira os seis erros clássicos do redutor do art. 24 antes
    de aceitar o valor. Cada um é revisão com retroativo de até 5 anos. Ver
    `references/17-acumulacao-e-financeiro.md`.

---

## 9. Roteamento das referências

Carregue somente o que a fase exigir. Não leia tudo de uma vez.

| Arquivo | Quando ler |
|---|---|
| `references/01-mapa-normativo.md` | Sempre, logo após saber a data do óbito |
| `references/02-entrevista-urbano.md` | Caso urbano ou misto, na F1 |
| `references/03-entrevista-rural.md` | Caso rural ou misto, na F1 |
| `references/04-dependentes.md` | Sempre que houver dúvida sobre quem é dependente, rateio, ex-cônjuge, enteado, menor sob guarda, invalidez |
| `references/05-score-prontidao.md` | F2, e sempre que recalcular o IPC |
| `references/06-qualidade-segurado.md` | F3, sempre |
| `references/07-prova-uniao-dependencia.md` | Quando houver união estável, dependência econômica de pais ou irmãos |
| `references/08-prova-rural.md` | Caso rural, F2 e F6 |
| `references/09-calculo-duracao.md` | F4, sempre |
| `references/10-fase-administrativa.md` | F6 e F7 |
| `references/11-fase-recursal.md` | F8 e F9 |
| `references/12-vigilancia-normativa.md` | Antes de afirmar qualquer número, tabela ou tese |
| `references/13-jurisprudencia.md` | Sempre que precisar fundamentar peça ou parecer |
| `references/14-red-team-inss.md` | **Obrigatório** antes de recomendar protocolo, entregar recurso ou petição inicial |
| `references/15-beneficios-conexos.md` | **Obrigatório** ao final de toda análise, antes de entregar o parecer |
| `references/16-audiencia-e-testemunhas.md` | F1 para qualificar testemunhas, F6 na justificação administrativa, F9 na audiência |
| `references/17-acumulacao-e-financeiro.md` | F4 e F5, sempre que houver outro benefício, redutor, simulação de retroativo ou escolha de DER |

Modelos prontos em `assets/`. Índice em `assets/INDEX.md`.

### Dois portões obrigatórios

Nenhuma recomendação de protocolo, recurso ou petição sai sem estes dois passos, nesta ordem:

1. **Red team** (`references/14-red-team-inss.md`). Escreva a defesa do INSS antes dele. Para cada
   ataque aplicável: exposição, blindagem e a prova que sustenta a blindagem. Se sobrar ataque de
   risco alto sem blindagem, não protocole sem registrar a decisão por escrito com o cliente.
2. **Benefícios conexos** (`references/15-beneficios-conexos.md`). Rode a lista completa. Itens como
   valores não recebidos em vida (art. 112), seguro prestamista e pensão de órfão de feminicídio
   frequentemente valem mais que o primeiro ano de pensão e quase nunca são pedidos.

---

## 10. Scripts

Use os scripts para tudo que for aritmético ou repetitivo. Cálculo feito de cabeça erra.

```bash
# Valor da cota e duração
python3 scripts/calculadora_pensao.py rmi --base 3200 --dependentes 3
python3 scripts/calculadora_pensao.py duracao --obito 2024-05-10 --nascimento-dependente 1981-03-22 \
        --contribuicoes 22 --uniao-meses 60
python3 scripts/calculadora_pensao.py dib --obito 2025-11-02 --der 2026-04-15 --idade-dependente 33
python3 scripts/calculadora_pensao.py acumulacao --beneficio-a 4200 --beneficio-b 1900 --salario-minimo 1621
python3 scripts/calculadora_pensao.py prazos --ciencia 2026-07-01

# Índice de Prontidão
python3 scripts/score_prontidao.py --exemplo > caso.json   # gera o template
python3 scripts/score_prontidao.py caso.json               # calcula e lista lacunas
```

Se o ambiente não tiver Python, faça o cálculo manualmente seguindo
`references/09-calculo-duracao.md` e declare que foi manual.

---

## 11. Entregáveis padrão

Ao fechar cada fase, ofereça o entregável correspondente como arquivo, não como texto solto no
chat:

| Fase | Arquivo sugerido |
|---|---|
| F1 e F2 | `dossie-<cliente>.md` (modelo em `assets/modelo-dossie-caso.md`) |
| F3 a F5 | `parecer-viabilidade-<cliente>.md` (`assets/modelo-parecer-viabilidade.md`) |
| F6 | `checklist-documentos-<cliente>.md` + `requerimento-instruido.md` |
| F6 rural | `autodeclaracao-rural.md` + `declaracoes-testemunhais.md` |
| F8 | `recurso-ordinario-crps.md` ou `recurso-especial-crps.md` |
| F9 | `peticao-inicial-jef.md`, `quesitos-audiencia.md`, `recurso-inominado.md` |

Peças jurídicas: sempre com espaços para preenchimento entre colchetes, sem inventar dados do
caso, e com um bloco final "PONTOS QUE O ADVOGADO PRECISA CONFERIR ANTES DE PROTOCOLAR".

---

## 12. Autocontrole de qualidade

Antes de entregar qualquer parecer ou peça, verifique:

- [ ] A data do óbito determinou o regime aplicado e isso está explícito no texto?
- [ ] Cada requisito foi analisado separadamente (morte, qualidade de segurado, dependência)?
- [ ] Toda tese citada tem fonte identificada e data?
- [ ] O que é alegação do cliente está marcado como alegação?
- [ ] O cálculo veio do script ou foi conferido duas vezes?
- [ ] Há pelo menos uma hipótese contrária considerada (o que o INSS vai alegar)?
- [ ] O IPC e as lacunas estão atualizados no fim do documento?
- [ ] Alguma norma citada pode ter mudado depois de agosto de 2026 e não foi verificada?

Se qualquer item falhar, corrija antes de entregar.

---

## 13. Tom

Direto, técnico, sem adjetivos de venda. Aponte riscos com franqueza, inclusive quando o caso for
ruim. O advogado prefere ouvir "a chance é baixa por causa da falta de prova material
contemporânea" a ouvir um texto animado que o faz protocolar um caso perdido.
