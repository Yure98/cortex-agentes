# 09. Cálculo do valor, DIB e tributação

> Parâmetros de 2026 usados neste arquivo: salário mínimo R$ 1.621,00 (Decreto 12.797/2025) e
> teto do RGPS R$ 8.475,55 (Portaria Interministerial MPS/MF nº 13, de 09/01/2026). Reconfirme os
> valores em janeiro de cada ano antes de usar em peça ou em simulação para cliente.

---

## 1. O percentual: 50% do salário de benefício

O auxílio-acidente corresponde a 50% do salário de benefício que deu origem ao próprio
auxílio-acidente. Não há coeficiente progressivo, não há redutor por idade, não há distinção por
sexo. É um percentual fixo.

**Não confundir com o coeficiente da aposentadoria por incapacidade permanente pós-EC 103/2019**
(60% da média, mais 2% por ano de contribuição que exceder 20 anos para homem ou 15 para
mulher). Esse coeficiente é de outro benefício. O auxílio-acidente segue sua regra própria e
independente, sempre 50% do salário de benefício.

**Piso e teto:** o auxílio-acidente não tem piso de um salário mínimo garantido, ao contrário de
muitos outros benefícios do RGPS. O valor pode, em tese, resultar inferior a um salário mínimo,
porque incide sobre 50% da base, não sobre 100%. Está sujeito ao teto do RGPS.

---

## 2. Como apurar o salário de benefício

### Quando o auxílio-acidente é precedido de auxílio-doença pelo mesmo fato gerador

Situação mais comum. O INSS reaproveita o salário de benefício já apurado para o auxílio-doença
anterior, sem novo cálculo do zero. A RMI do auxílio-acidente é 50% desse mesmo salário de
benefício.

### Quando não há auxílio-doença anterior

Calcula-se o salário de benefício pela média aritmética simples dos salários de contribuição do
período básico de cálculo, conforme a metodologia vigente para os benefícios por incapacidade,
que hoje considera todo o período contributivo desde julho de 1994, salvo regras de transição
aplicáveis a casos antigos.

### No caso rural, segurado especial sem contribuição facultativa complementar

O salário de benefício tende a corresponder ao piso, um salário mínimo, salvo se houver
contribuição facultativa sobre a produção que eleve a base de cálculo.

---

## 3. DIB, a data de início do benefício

| Situação | DIB |
|---|---|
| Precedido de auxílio-doença pelo mesmo fato gerador | Dia seguinte à cessação do auxílio-doença (art. 86, §2º; Tema 862/STJ) |
| Sem auxílio-doença anterior, requerimento tempestivo | Data do requerimento administrativo, após a consolidação da lesão |
| Reconhecimento judicial de nexo e sequela, sem prévio requerimento administrativo compatível | Data da citação ou da constatação pericial judicial da consolidação, conforme o caso, com discussão possível sobre retroação. Analise caso a caso com o advogado |

**Regra prática:** nunca afirme uma DIB sem antes confirmar se existiu auxílio-doença anterior
pelo mesmo fato gerador. Isso muda completamente o cálculo de retroativos.

---

## 4. Estimativa de retroativos (artefato)

```
SIMULACAO FINANCEIRA
Data do evento: ..../..../....
Data da consolidacao: ..../..../....  (fundamento: laudo, alta do auxilio-doenca em ..../..../....)
DIB projetada: ..../..../....  (fundamento: art. 86, par. 2, Tema 862/STJ, ou requerimento em ..../..../....)
Salario de beneficio: R$ ...........
RMI estimada (50%): R$ ...........
Competencias vencidas ate hoje: ... meses
Retroativo bruto estimado: R$ ...........
Prescricao quinquenal atinge: [nada | competencias anteriores a ..../..../....]
Observacao: valores estimados, sujeitos a confirmacao do salario de beneficio pelo INSS,
correcao monetaria e juros.
```

Confira com `python scripts/calculadora_auxilio_acidente.py rmi --base <valor>`.

---

## 5. Prescrição e decadência

**Prescrição:** aplica-se a prescrição quinquenal do art. 103, parágrafo único, da Lei
8.213/91, às parcelas vencidas antes do quinquênio contado da DER ou do ajuizamento, conforme o
Tema 862/STJ. Ressalva para menores, incapazes e ausentes, art. 79.

**Decadência:** o prazo decenal do art. 103, caput, aplica-se apenas à revisão de ato de
concessão já efetivado. Não há decadência para requerer o benefício pela primeira vez, nem para
indeferimento, cancelamento ou cessação, à luz da ADI 6096/STF e da Súmula 81/TNU, aplicáveis a
todo o sistema de benefícios por incapacidade.

---

## 6. Encerramento do benefício

O auxílio-acidente cessa:

- pela concessão de qualquer aposentadoria ao beneficiário, a partir de 11/11/1997 (art. 86,
  §2º; ver `references/10-cumulacao-e-vedacoes.md`);
- pelo óbito do beneficiário;
- não cessa pela simples continuidade do trabalho, nem pela melhora não caracterizada
  formalmente. Se o INSS suspeitar de melhora do quadro, deve instaurar procedimento de revisão
  com nova perícia, não simplesmente cessar administrativamente sem contraditório.

---

## 7. Décimo terceiro salário

O auxílio-acidente gera direito a décimo terceiro (gratificação natalina), calculado à razão de
um doze avos por competência recebida no ano-base, seguindo a sistemática comum dos benefícios
previdenciários de pagamento continuado.

---

## 8. Imposto de renda: atenção à isenção que NÃO se aplica aqui

A isenção de imposto de renda por moléstia grave, prevista na Lei 7.713/88, alcança
rendimentos de **aposentadoria, pensão ou reforma**. O auxílio-acidente não está nessa lista.
Ainda que o segurado seja portador de doença grave listada na lei, a isenção específica dessa
lei não se estende ao auxílio-acidente, por se tratar de benefício de natureza distinta,
indenizatória, e não de aposentadoria, pensão ou reforma.

**Não prometa ao cliente uma isenção que ele não tem direito de pedir sobre este benefício
específico.** Se ele for portador de moléstia grave e tiver também uma aposentadoria, a isenção
pode incidir sobre a aposentadoria, não sobre o auxílio-acidente pago paralelamente.

O décimo terceiro do auxílio-acidente está sujeito à retenção de imposto de renda na fonte,
conforme a faixa de tributação do beneficiário, como ocorre com a generalidade dos rendimentos
tributáveis pagos pelo INSS.
