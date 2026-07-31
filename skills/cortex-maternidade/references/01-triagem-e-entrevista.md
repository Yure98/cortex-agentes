# 01 — Triagem, Entrevista e Classificação

## 1. Triagem em 5 perguntas (60 segundos)

Antes de investir tempo, resolva isto. Se alguma resposta for bloqueante, diga logo.

| # | Pergunta | Resposta bloqueante |
|---|---|---|
| 1 | Quando foi o fato gerador (parto, adoção, guarda, natimorto, aborto)? | Mais de 5 anos, sem requerimento administrativo no meio → prescrição de todas as parcelas |
| 2 | Já houve requerimento no INSS? Qual a DER e o resultado? | Nunca requereu → não ajuizar (Tema 350/STF); requerer primeiro |
| 3 | A cliente tinha alguma contribuição, vínculo ou atividade rural nos 3 anos anteriores? | Nenhuma, jamais → sem qualidade de segurada, sem caso |
| 4 | Ela se afastou do trabalho/atividade? | Não se afastou → art. 71-C; verificar antes de prosseguir |
| 5 | Já existe processo judicial ou recurso administrativo em curso sobre isso? | Sim → litispendência / vedação do art. 576-A da IN 128/2022 |

**Sobre a pergunta 5:** desde a IN 203/2026, é vedado novo requerimento administrativo enquanto
houver processo em curso da mesma espécie — inclusive durante o prazo recursal ainda aberto. A
vedação **não** alcança pedido de revisão. Erro comum: reprotocolar em vez de recorrer, e perder o
prazo dos 30 dias.

---

## 2. Classificador de trilho

Rode na ordem. Pare no primeiro trilho confirmado.

### Etapa A — Perguntas discriminantes

```
A1. Nos 12 meses anteriores ao fato gerador, de onde vinha o sustento dela e da família?
    → Da terra, da pesca, do extrativismo, consumido e vendido pela própria família ...... vá para B
    → De salário, prestação de serviço, comércio, aplicativo, autônoma .................. vá para C
    → Dos dois, em momentos diferentes ................................................. TRILHO H
    → Ela não trabalhava e alguém contribuía por ela / ela pagava GPS sem trabalhar ..... TRILHO U (facultativa)

B1. Ela trabalhava na terra da própria família (ou em parceria/comodato/arrendamento),
    com o trabalho de todos, sem empregado permanente?
    → Sim ................................................................ TRILHO R (segurada especial)
    → Não: trabalhava por diária, para vários donos, sem vínculo ......... TRILHO D (boia-fria/volante)
    → Não: tinha carteira assinada em fazenda/usina/agroindústria ........ TRILHO U (empregada rural)

C1. Qual era o vínculo na data do fato gerador?
    → CTPS ativa ......................................... U-empregada (paga pela empresa)
    → CTPS doméstica / eSocial Doméstico ................. U-doméstica (paga pelo INSS)
    → Sindicato/OGMO .................................... U-avulsa
    → CNPJ MEI com DAS .................................. U-MEI
    → GPS 1007/1163 como autônoma ....................... U-contribuinte individual
    → GPS como facultativa (1406/1473) .................. U-facultativa
    → Nenhum vínculo ativo, mas houve antes ............. U-desempregada em período de graça
```

### Etapa B — Confirmação por evidência

A resposta da cliente é hipótese. Confirme contra documento. Ordem de confiabilidade:

1. **CNIS** — o que o INSS enxerga. Categoria, competências, indicadores de pendência.
2. **CTPS / eSocial** — vínculos, inclusive rurais.
3. **Autodeclaração + CAF/DAP, CadÚnico, ITR, notas de produtor** — indicadores de rural.
4. **Carta de indeferimento** — revela em que categoria o INSS a enquadrou. Muitas vezes o
   indeferimento existe porque o INSS enquadrou errado, e a peça correta é de **reenquadramento**,
   não de prova adicional.
5. Narrativa da cliente — última, porque leiga confunde "trabalhava na roça" com segurada especial.

### Etapa C — Sinais de erro de trilho

| Sinal | O que costuma significar |
|---|---|
| Cliente diz "rural", CNIS mostra GPS de autônoma | Contribuinte individual. Trilho U. Valor pela média, não pelo piso |
| Cliente diz "urbana", certidão de casamento diz "lavrador" | Investigar trilho R ou H — pode haver período rural aproveitável |
| Cliente diz "rural", trabalha em usina com carteira | Empregada rural. Trilho U, sem carência, valor pela remuneração |
| Cliente diz "rural", trabalha por diária para vários | Trilho D. **Não** é segurada especial. Súmula 149 + Tema 554/STJ se aplicam |
| Marido tem vínculo urbano estável e alta renda | Risco de descaracterização do regime de economia familiar (Tema 532/STJ) |
| CNPJ MEI aberto e ativo | Verificar art. 11, § 12 — pode não descaracterizar, se agrícola/agroindustrial/agroturístico |
| Município pequeno, CadÚnico rural, sem nenhum documento | Trilho R com risco alto de prova. Ver `03-rural.md` §5 |

### Etapa D — Saída do classificador

```
TRILHO: <U | R | H | D>
CATEGORIA: <empregada | doméstica | avulsa | MEI | CI | facultativa | desempregada | segurada especial | empregada rural | boia-fria>
BASE: <o que sustenta a classificação>
DIVERGE DO INFORMADO: <sim/não — se sim, explique a consequência prática>
CONFIANÇA: <alta | média | baixa — se baixa, diga qual documento resolve>
```

---

## 3. Entrevista estruturada

Objetivo: sair com o caso classificado, os riscos mapeados e a lista de documentos fechada.
Ficha completa em `assets/ficha-de-entrevista.md`.

### Bloco 1 — Identificação e fato gerador
- Nome, CPF, NIT/PIS, data de nascimento, endereço (**rural ou urbano?** anote o zoneamento, não só o CEP)
- Estado civil / união estável — **e profissão do cônjuge na certidão** (é prova material no trilho R)
- Fato gerador: parto / natimorto / aborto não criminoso / adoção / guarda para fins de adoção
- Data exata do fato gerador
- Documento que comprova (certidão de nascimento, certidão de óbito do natimorto, atestado médico,
  termo de guarda, sentença de adoção)
- Houve internação da mãe ou do bebê? Quantos dias? Havia nexo com o parto? → dispara Lei 15.222/2025
- Parto múltiplo? Prematuro? UTI neonatal?

### Bloco 2 — Vida contributiva (12 a 36 meses antes do fato gerador)
- Última atividade remunerada antes do fato gerador — qual, quando começou, quando terminou
- Vínculos CLT: datas, empregador, se houve baixa na CTPS
- Contribuições próprias: código da GPS, competências, se pagas em dia ou em atraso
- **Se pagou em atraso: quando efetivamente pagou?** — competência recolhida depois do parto tende a
  ser rejeitada; a Resolução CRPS 13/2026 endureceu isso para a facultativa
- MEI: data de abertura, DAS pagos, se houve desenquadramento
- Recebeu seguro-desemprego? Quando? → prova de desemprego involuntário, prorroga o período de graça
- Recebeu outro benefício no período? Auxílio por incapacidade, BPC, outro salário-maternidade?
- **Tinha mais de uma atividade ao mesmo tempo?** → possibilidade de benefício por atividade

### Bloco 3 — Se houver qualquer indício rural
- Onde morava e onde trabalhava, ano a ano, na janela relevante
- Terra: própria, arrendada, em comodato, parceria, assentamento, posse? Quantos hectares? Quantos módulos fiscais?
- Quem trabalhava junto: quem é o grupo familiar
- O que produzia, para quem vendia, com que documento
- **Alguém do grupo tinha renda urbana?** Quanto? Era indispensável para o sustento? (Tema 532/STJ)
- Contratou empregado? Por quanto tempo no ano? (limite de 120 pessoas/dia por ano civil)
- Sindicato rural, associação, colônia de pescadores, cooperativa: é filiada? desde quando?
- Fez pré-natal onde? Posto rural? Tem cartão da gestante com endereço rural?
- Filhos estudam em escola rural? Transporte escolar rural?
- Já recebeu Bolsa Família/Auxílio Brasil, PRONAF, Garantia-Safra, seguro-defeso?
- Tem CAF (antiga DAP)? CadÚnico com marcação rural? Está no CNIS como segurada especial (art. 38-A)?
- Se indígena: tem CEAR da FUNAI? (Súmula 657/STJ é relevante em caso de menor de 16 anos)

### Bloco 4 — Histórico administrativo
- Já requereu? Quantas vezes? DER de cada uma
- Motivo exato do indeferimento — **peça a carta, não aceite o resumo da cliente**
- Houve exigência não cumprida? Foi notificada? Por qual canal?
- Foi convocada para entrevista rural ou justificação administrativa? Compareceu? Com testemunhas?
- Já recorreu? Em que fase está?
- Solicite: **cópia integral do processo administrativo** — é onde estão as contradições que o INSS
  cria contra si mesmo

### Bloco 5 — Contexto trabalhista (dispara segunda frente)
- Foi dispensada durante a gravidez? Sabia da gravidez? O empregador sabia?
- Pediu demissão? Acordo? (afeta estabilidade e período de graça)
- A empresa pagou algum valor a título de licença-maternidade?
- Houve desconto de INSS sobre o salário-maternidade nos holerites? → repetição de indébito

### Bloco 6 — Testemunhas (obrigatório nos trilhos R e D)
- Nome completo, CPF, idade, endereço, telefone
- **Como conhece a cliente e desde quando** — proximidade fabricada derruba o depoimento
- O que exatamente pode afirmar: viu trabalhando? onde? em que época? com que frequência?
- A testemunha é parente? Tem interesse? Já depôs em outros processos previdenciários?
- Roteiro de qualificação em `assets/modelo-quesitos-testemunhas.md`

---

## 4. Regras de condução

- **Peça documentos em bloco único.** Lista numerada, com o nome do documento, quem emite e para que
  serve. Interrogatório fatiado desgasta a cliente e atrasa o caso.
- **Não pergunte o que o CNIS responde.** Se houver CNIS, extraia de lá e confirme só as divergências.
- **Registre a fonte de cada fato:** `[cliente]`, `[CNIS]`, `[documento]`, `[presumido]`. No parecer,
  fato `[presumido]` vira risco explícito. Isso protege o advogado.
- **Ofereça prosseguir com premissas.** Se faltar dado, liste, adote a premissa mais provável, marque
  como premissa e siga. Trave só quando o dado for determinante do trilho.
