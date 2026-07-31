# 02 — Trilho Urbano (U)

Aplica-se a empregada, empregada rural registrada, doméstica, avulsa, MEI, contribuinte individual,
facultativa e desempregada em período de graça.

## 1. Os quatro requisitos

Depois das ADIs 2.110/2.111, a estrutura ficou assim:

| # | Requisito | Situação |
|---|---|---|
| 1 | **Qualidade de segurada na data do fato gerador** | Único requisito realmente disputado hoje |
| 2 | **Fato gerador** | Documental, raramente controvertido |
| 3 | **Afastamento da atividade** (art. 71-C) | Verificar; costuma passar em branco |
| 4 | ~~Carência~~ | **Extinta** para todas as categorias |

Consequência estratégica: o litígio migrou inteiro para o requisito 1. Toda peça urbana deve ser
construída em torno da **qualidade de segurada**, não da carência. Petição que gasta cinco páginas
provando que a carência caiu e uma linha sobre a qualidade de segurada está mal calibrada.

---

## 2. Qualidade de segurada — como se prova e como se perde

### Período de graça (art. 15)
| Situação | Prazo de manutenção |
|---|---|
| Em gozo de benefício | Enquanto durar |
| Regra geral após cessar contribuições | **12 meses** |
| + Mais de 120 contribuições sem perda intercalada | **+12 meses** (24) |
| + Desemprego involuntário comprovado | **+12 meses** (36 no máximo) |
| Segurado facultativo | **6 meses** |
| Segregado/detido, serviço militar | Regras próprias |

Contagem: o prazo corre a partir do **fim do mês seguinte** ao término do período de graça, com a
extensão do art. 30, II, da Lei 8.212/91. Use `scripts/diagnostico.py` — errar isso por um mês perde
o caso e é o erro mais comum do trilho U.

### Prova do desemprego involuntário para prorrogar
Não se exige registro no Ministério do Trabalho (**Tema 19/TNU**). Servem:
- TRCT, aviso prévio, homologação
- Recibos de seguro-desemprego
- CNIS sem vínculo posterior
- Declaração + prova testemunhal, na via judicial

### Armadilha da facultativa `[ATUALIZAÇÃO 2026]`
**Resolução CRPS 13/2026** (novo inciso IV e § 2º do Enunciado 19): a facultativa precisa comprovar
o pagamento **e** demonstrar que a filiação ao RGPS estava **regularmente constituída antes do fato
gerador**. Filiação de facultativa só produz efeitos com a **primeira contribuição válida e paga no
prazo**. Primeira GPS recolhida depois do parto não gera direito retroativo.

Como enfrentar quando a cliente está nessa situação:
1. Verificar se havia filiação anterior como segurada obrigatória — nesse caso não se trata de nova
   filiação, e sim de manutenção; o argumento do CRPS não se aplica.
2. Verificar se o recolhimento, embora pago em atraso, refere-se a competência **anterior** ao fato
   gerador e dentro do prazo legal de recolhimento.
3. Se realmente for primeira contribuição pós-parto: o caso é 🔴. Diga isso.

### Recolhimento em atraso pelo contribuinte individual
Recolhimentos extemporâneos, mas referentes a competências anteriores ao parto, têm sido admitidos
na jurisprudência para fins de qualidade de segurada. Distinga sempre: **competência a que se refere**
× **data em que foi pago**. É a distinção que decide o caso.

---

## 3. Por categoria

### 3.1 Empregada (CLT) e empregada rural registrada
- Sem carência (art. 26, VI)
- **Quem paga:** a empresa, com compensação (art. 72, § 1º) — a cliente **não** vai encontrar parcelas
  no Meu INSS; procurar lá é procurar no lugar errado, e isso gera reclamação infundada
- RMI: remuneração integral; se variável, média aritmética simples dos 6 últimos salários
- Exceção: adoção → pago pelo INSS (art. 71-A, § 1º)
- Exceção: dispensa durante a gravidez → **Enunciado CRPS nº 6**, INSS paga
- Estabilidade da gestante: ADCT art. 10, II, "b" — frente trabalhista paralela
- Empresa Cidadã (Lei 11.770/2008): 60 dias adicionais pagos pela empresa, com incentivo fiscal.
  **Não** é salário-maternidade do INSS nesse acréscimo

### 3.2 Empregada doméstica
- Sem carência (LC 150/2015 + art. 26)
- **Quem paga: o INSS diretamente** (art. 73, I) — diferença central em relação à CLT comum
- RMI: último salário de contribuição; se variável, média dos 6 últimos
- Problema recorrente: empregador que não recolhe ou não registra no eSocial Doméstico. O vínculo
  existe independentemente do recolhimento; a obrigação de recolher é do empregador. Prova: CTPS,
  recibos, transferências, testemunhas, conversas

### 3.3 Trabalhadora avulsa
- Sem carência
- Pago pelo INSS
- RMI: última remuneração; se variável, média dos 6 últimos
- Prova: registros do sindicato ou do OGMO

### 3.4 MEI
- Sem carência (pós-ADI)
- Pago pelo INSS
- RMI: **1 salário mínimo**, salvo complementação para 20% (código de complementação), quando passa
  a seguir a média do art. 73, III
- Requisito real: DAS pagos suficientes para manter a qualidade de segurada
- Atenção: MEI com atividade rural pode, conforme o objeto, ser reenquadrada — ver art. 11, § 12

### 3.5 Contribuinte individual (autônoma)
- Sem carência (pós-ADI). **Este é o perfil típico da revisão pós-ADI 2.110**
- Pago pelo INSS
- RMI: 1/12 da soma dos 12 últimos salários de contribuição, em período não superior a 15 meses
- Plano simplificado (11% sobre o mínimo) → piso; plano normal (20%) → proporcional, até o teto
- Exige comprovação do exercício de atividade remunerada, além do recolhimento

### 3.6 Facultativa
- Sem carência, mas ver §2 acima — é onde o CRPS apertou em 2026
- Pago pelo INSS
- RMI: art. 73, III
- Período de graça reduzido: **6 meses**

### 3.7 Desempregada em período de graça
- **Tema 113/TNU**: devido mesmo em desemprego, pago diretamente pela Previdência
- **Tema 202/TNU**: mesmo que a última vinculação tenha sido como **empregada**, a RMI segue o
  art. 73, III (média), e **não** a remuneração integral do art. 72. Erro clássico: pedir remuneração
  integral e ter o pedido reduzido em sentença, com impacto em honorários
- Prova central: manutenção da qualidade de segurada na data do parto + desemprego involuntário

---

## 4. Dossiê documental — trilho U

Checklist operacional em `assets/checklist-documental-urbano.md`.

**Núcleo (todos):**
1. RG, CPF, comprovante de residência
2. Certidão de nascimento / óbito do natimorto / atestado médico / termo de guarda ou sentença
3. **CNIS completo e atualizado** — extrato de vínculos e contribuições
4. Carta de indeferimento e **processo administrativo integral**
5. Dados bancários em nome da segurada

**Por categoria:**
| Categoria | Adicionais |
|---|---|
| Empregada | CTPS (qualificação + contrato), holerites, atestado de afastamento, comunicação ao empregador |
| Doméstica | CTPS, eSocial Doméstico, recibos, comprovantes de pagamento |
| Avulsa | Declaração do sindicato/OGMO, registros de escala |
| MEI | CCMEI, DAS pagos, extrato do Simples |
| CI | GPS/DARF pagas, comprovação da atividade (contratos, notas, recibos, prints de plataforma) |
| Facultativa | GPS pagas, **prova da data de filiação**, extrato do CNIS com a inscrição |
| Desempregada | TRCT, aviso prévio, seguro-desemprego, CNIS demonstrando o período de graça |

---

## 5. Semáforo de viabilidade — trilho U

| Sinal | Critério |
|---|---|
| 🟢 **Verde** | Qualidade de segurada inequívoca no CNIS na data do fato gerador; fato gerador documentado; requisitos objetivos preenchidos |
| 🟡 **Amarelo** | Qualidade de segurada depende de contagem de período de graça, de recolhimento extemporâneo, de vínculo não registrado no CNIS, ou de prorrogação por desemprego |
| 🔴 **Vermelho** | Nenhuma filiação anterior ao fato gerador; primeira contribuição de facultativa posterior ao parto; período de graça inequivocamente vencido; prescrição consumada |

Um 🟡 não é "provavelmente ganha". É "existe trabalho probatório a fazer antes de prometer qualquer coisa".

---

## 6. Erros específicos do trilho U

1. Discutir carência em vez de qualidade de segurada.
2. Pedir remuneração integral para desempregada, contra o Tema 202/TNU.
3. Mandar a empregada CLT requerer no Meu INSS quando quem paga é a empresa — e depois narrar isso
   como "indeferimento".
4. Contar o período de graça sem a extensão do art. 30, II, da Lei 8.212/91.
5. Não distinguir competência de referência × data de pagamento no recolhimento em atraso.
6. Deixar de checar o desconto da cota da segurada sobre o benefício (repetição de indébito).
7. Ignorar a estabilidade gestante quando houve dispensa na gravidez — perde-se a segunda frente.
