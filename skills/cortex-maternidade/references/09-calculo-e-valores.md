# 09 — Cálculo, Valores e Consectários

## 1. Parâmetros 2026 `[VOLÁTIL — conferir em janeiro]`

| Parâmetro | Valor |
|---|---|
| Salário mínimo | R$ 1.621,00 (Decreto 12.797/2025) |
| Teto do RGPS | R$ 8.475,55 (Portaria Interministerial MPS/MF nº 13, de 09/01/2026) |
| Alçada do JEF | 60 SM = R$ 97.260,00 |

Piso constitucional: nenhum benefício substitutivo do salário pode ser inferior ao mínimo
(CF art. 201, § 2º; art. 73 da Lei 8.213/91) — **mesmo que o cálculo resulte em valor menor**.

---

## 2. RMI por categoria

| Categoria | Base legal | Regra |
|---|---|---|
| Empregada | art. 72 | Remuneração integral. Se variável, média aritmética simples dos **6 últimos** salários |
| Empregada rural registrada | art. 72 | Idem |
| Trabalhadora avulsa | art. 72 | Última remuneração; se variável, média dos 6 últimos |
| Empregada doméstica | art. 73, I | Último salário de contribuição; se variável, média dos 6 últimos |
| Contribuinte individual | art. 73, III | **1/12 da soma dos 12 últimos salários de contribuição**, apurados em período **não superior a 15 meses** |
| Facultativa | art. 73, III | Idem |
| **Desempregada em período de graça** | art. 73, III + **Tema 202/TNU** | Idem — **mesmo que a última vinculação tenha sido como empregada** |
| MEI | — | 1 salário mínimo na base MEI; complemento de alíquota sobre a mesma base não aumenta a renda |
| Segurada especial | art. 39, parágrafo único | 1 salário mínimo; se recolheu facultativamente, art. 73, III |
| Adotante | art. 71-A | Conforme a categoria (art. 72 ou art. 73), pago sempre pelo INSS |
| Cônjuge sobrevivente (art. 71-B) | art. 71-B, § 2º | Remuneração integral se empregado/avulso; se desempregado, 1/12 dos 12 últimos, em até 15 meses |

**Regra dos 15 meses:** procura-se **para trás** o período necessário para reunir 12 salários de
contribuição, sem ultrapassar 15 meses. Mesmo com menos de 12 competências no intervalo, o divisor legal é 12 — respeitado o piso.

---

## 3. Duração e valor total

| Fato gerador | Dias |
|---|---|
| Parto (com vida ou natimorto) | 120 |
| Aborto não criminoso | 14 |
| Adoção / guarda para fins de adoção | 120 |
| Internação > 2 semanas com nexo ao parto | Período da internação + 120 dias após a alta, descontado o repouso pré-parto já fruído (art. 71, § 3º) |

Valor total aproximado = RMI × 4 (para 120 dias). Para o aborto, proporcional a 14 dias.

13º proporcional: o salário-maternidade integra a base de cálculo do 13º na relação de emprego. Nos
benefícios pagos pelo INSS, confira o tratamento do abono anual no caso concreto `[VOLÁTIL]`.

---

## 4. Atrasados

**Termo inicial (DIB):**
- Parto: data do parto (ou até 28 dias antes, se houve afastamento anterior).
- Adoção/guarda: data da decisão ou do termo.
- Requerimento posterior: DIB no fato gerador, limitada pela prescrição.

**Prescrição:** quinquenal, **de parcelas** (art. 103, parágrafo único). Como o benefício dura 120
dias, na prática o corte funciona quase como tudo ou nada: se o fato gerador tem mais de 5 anos e não
houve requerimento que suspendesse o prazo, todas as parcelas prescreveram.

**Suspensão:** Súmula 74/TNU + Decreto 20.910/1932, arts. 4º e 5º. Roteiro de cálculo:
```
1. Fato gerador ................................... F
2. Requerimento administrativo .................... R   → prazo SUSPENSO
3. Ciência da decisão administrativa .............. C   → prazo VOLTA A CORRER pelo saldo
4. Ajuizamento .................................... A
Consumido = (R − F) + (A − C).  Se > 5 anos → prescrito.
```
Use `scripts/diagnostico.py` — a conta é simples e o erro é comum.

---

## 5. Correção e juros

| Período | Regra |
|---|---|
| Até 08/12/2021 | Correção pelo INPC (Tema 905/STJ, art. 41-A da Lei 8.213/91); juros conforme o entendimento aplicável (Tema 810/STF) |
| A partir de **09/12/2021** | **EC 113/2021, art. 3º**: incidência, **uma única vez**, até o efetivo pagamento, da **Selic acumulada mensalmente**, englobando correção monetária e juros |

Não cumule Selic com INPC ou com juros autônomos no mesmo período. É erro frequente em planilhas e
gera impugnação certa pelo INSS, com atraso na RPV.

---

## 6. Honorários

**No JEF:** sem honorários em primeiro grau. Na Turma Recursal, o recorrente vencido paga.

**Na Vara Federal:** art. 85, § 3º, do CPC — percentual escalonado sobre o proveito econômico.
**Base de cálculo:** **Súmula 111/STJ** — parcelas vencidas **até a sentença**.

Como o salário-maternidade é benefício de duração fechada, quase sempre toda a condenação já está
vencida na sentença. Efeito prático: a Súmula 111 costuma **não** reduzir a base aqui, ao contrário do
que acontece em benefícios continuados. Vale conferir, e vale argumentar.

**Contratuais:** peticione o destaque antes da expedição da RPV (art. 22, § 4º, do Estatuto da OAB).

---

## 7. Pagamento

| Situação | Quem paga |
|---|---|
| Empregada CLT — parto | Empresa, com compensação (art. 72, § 1º) |
| Empregada CLT — adoção | **INSS** (art. 71-A, § 1º) |
| Empregada CLT dispensada na gravidez | **INSS** (Enunciado CRPS nº 6) |
| Doméstica, avulsa, MEI, CI, facultativa, especial, desempregada | **INSS** (art. 73) |

Prazos: concessão em até **30 dias** (art. 73-A, para os pagos pelo INSS); primeiro pagamento em até
45 dias da entrega dos documentos (art. 41-A, § 5º).

---

## 8. Empresa Cidadã e frentes tributárias

- **Lei 11.770/2008:** prorrogação de 60 dias (120 → 180). O acréscimo é **remuneração paga pela
  empresa**, com incentivo fiscal, **não** salário-maternidade do INSS.
- **Tema 72/STF:** inconstitucional a contribuição previdenciária **patronal** sobre o salário-maternidade
  → compensação/restituição para empresas clientes do escritório.
- **Tema 1.274/STF:** validade da contribuição **da segurada** sobre o salário-maternidade — pendente.
  Há decisões aplicando o Tema 72 por analogia para afastar a cota da empregada e determinar a
  repetição de indébito. `[TESE EM CONSTRUÇÃO]`
- **Tema 1.290/STJ:** valores pagos a gestantes afastadas na pandemia (Lei 14.151/2021) têm natureza de
  remuneração do empregador, **não** de salário-maternidade, para fins de compensação; legitimidade
  passiva da Fazenda Nacional. Fecha uma porta que muitos escritórios ainda tentam abrir.

---

## 9. Checagem final do cálculo

- [ ] Categoria correta identificada
- [ ] RMI conforme a categoria (atenção ao Tema 202/TNU para desempregada)
- [ ] Piso do salário mínimo respeitado
- [ ] Teto respeitado
- [ ] Duração correta para o fato gerador
- [ ] Regra da Lei 15.222/2025 aplicada, se houve internação
- [ ] DIB correta
- [ ] Prescrição calculada com a suspensão
- [ ] Selic única a partir de 09/12/2021, sem cumulação
- [ ] Honorários sobre a base certa
