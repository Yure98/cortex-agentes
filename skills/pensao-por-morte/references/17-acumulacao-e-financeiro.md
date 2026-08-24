# 17. Acumulação, tributação e simulação financeira

Complementa `references/09-calculo-duracao.md`. Aqui está a camada que o INSS mais erra e que o
cliente mais precisa entender antes de assinar contrato.

> Parâmetros de 2026: salário mínimo **R$ 1.621,00** (Decreto 12.797/2025) e teto do RGPS
> **R$ 8.475,55** (Portaria Interministerial MPS/MF nº 13, de 09/01/2026). Reconfirme em janeiro de
> cada ano antes de usar em peça ou em simulação para cliente. Ver
> `references/12-vigilancia-normativa.md`.

---

## 1. Acumulação de benefícios (art. 24 da EC 103)

Aplica-se a **fatos geradores a partir de 13/11/2019**. Antes disso, há direito adquirido a
acumular integralmente.

**Vedação absoluta**: mais de uma pensão por morte deixada por cônjuge ou companheiro no mesmo
regime.

**Permitido, com redutor**: pensão por morte de um regime com aposentadoria do RGPS ou de RPPS, ou
com proventos militares, e as demais combinações do §1º.

**Como funciona**: recebe-se integralmente o benefício **de maior valor** e, sobre cada um dos
demais, aplica-se o escalonamento abaixo, calculado **por faixa cumulativa** sobre o salário
mínimo.

| Faixa do benefício menor | Percentual mantido |
|---|---|
| Até 1 salário mínimo | 100% |
| Parte que excede 1 e vai até 2 SM | 60% |
| Parte que excede 2 e vai até 3 SM | 40% |
| Parte que excede 3 e vai até 4 SM | 20% |
| Parte que excede 4 SM | 10% |

### Exemplo trabalhado (2026)

Pensão de R$ 6.000,00 e aposentadoria de R$ 4.000,00.
Faixas: 1 SM = R$ 1.621,00; 2 SM = R$ 3.242,00; 3 SM = R$ 4.863,00.

Benefício maior: pensão de R$ 6.000,00, paga integralmente.
Benefício menor: aposentadoria de R$ 4.000,00.

| Faixa | Valor na faixa | % | Resultado |
|---|---|---|---|
| Até 1 SM | R$ 1.621,00 | 100% | R$ 1.621,00 |
| 1 a 2 SM | R$ 1.621,00 | 60% | R$ 972,60 |
| 2 a 3 SM | R$ 758,00 (o benefício para em 4.000) | 40% | R$ 303,20 |

Aposentadoria reduzida: **R$ 2.896,80**. Renda total: **R$ 8.896,80**.

Confira com `python scripts/calculadora_pensao.py acumulacao --beneficio-a 6000 --beneficio-b 4000
--salario-minimo 1621`.

### Erros do INSS que geram revisão

Cheque um a um em toda carta de concessão com acumulação:

1. Aplicar o redutor sobre o benefício de **maior** valor.
2. Usar o salário mínimo de ano anterior nas faixas.
3. Somar percentuais em vez de aplicar por faixa cumulativa.
4. Aplicar redutor a **BPC** (assistencial, fora da regra do art. 24) ou a auxílio-acidente.
5. Aplicar redutor entre **cotas da mesma pensão**, o que não é acumulação.
6. Aplicar o art. 24 a óbito anterior a 13/11/2019.

Cada um destes é pedido de revisão administrativa com retroativo de até 5 anos.

**BPC/LOAS**: não acumula com pensão por morte. Se a pensão for de valor superior, oriente a
opção. Se inferior, avalie manter o BPC. Simule sempre e entregue por escrito.

---

## 2. Abono anual, imposto de renda e descontos

- **Abono anual (13º)**: devido proporcionalmente ao período de recebimento no ano.
- **Imposto de renda**: a pensão é rendimento tributável. Isenção integral para portador de
  moléstia grave listada na Lei 7.713/88, e o dependente pensionista pode ser isento se ele próprio
  for portador. Parcela isenta adicional para maiores de 65 anos. Verifique restituição retroativa
  dos últimos 5 anos quando a isenção for reconhecida tardiamente.
- **Descontos admitidos**: pensão alimentícia fixada judicialmente e valores devidos à Previdência.
  No mais, o benefício é impenhorável (art. 114).

---

## 3. Curva decrescente de cotas: o que o cliente precisa entender antes de assinar

Nos óbitos posteriores a 13/11/2019 as cotas individuais **não revertem** (art. 23, §1º, da EC
103). Quando um filho completa 21 anos, o valor total da família cai 10 pontos percentuais.

Simule a curva e entregue por escrito. Exemplo com base de R$ 2.960,00 e três dependentes:

| Momento | Dependentes | Percentual | Valor |
|---|---|---|---|
| Hoje | 3 | 80% | R$ 2.368,00 |
| Filho mais velho faz 21 | 2 | 70% | R$ 2.072,00 |
| Segundo filho faz 21 | 1 | 60% | R$ 1.776,00 |

Exceção: preserva-se o valor de 100% quando o número de dependentes remanescentes for igual ou
superior a 5. E havendo dependente inválido ou com deficiência intelectual, mental ou grave, o
valor é 100% da base independentemente do número de dependentes (art. 23, §2º, da EC 103).

---

## 4. Artefato: simulação financeira

```
SIMULAÇÃO FINANCEIRA
Data do óbito: ..../..../....
DIB projetada: ..../..../....  (fundamento: art. 74, ...)
RMI estimada: R$ ...........  (base: R$ ... × cotas ...%)
Competências vencidas até hoje: ... meses
Abonos anuais no período: ...
Retroativo bruto estimado: R$ ...........
Prescrição quinquenal atinge: [nada | competências anteriores a ..../..../....]
Acúmulo com benefício atual: [não se aplica | redutor art. 24 EC 103 → renda total R$ ...]
Duração projetada: [4 meses | ... anos | vitalícia] · Fundamento: art. 77, §2º, V, ...
Curva de cotas: hoje ...% → em .../.... cai para ...% (filho completa 21)
Observação: valores estimados, sujeitos a conferência do CNIS, correção monetária e juros.
```

---

## 5. Artefato obrigatório: duas datas de DER

Nunca recomende uma data de protocolo sem mostrar o custo da alternativa. Este bloco entra em todo
parecer de viabilidade.

```
Cenário A · protocolar em [hoje]
  DIB: ...           Retroativo: R$ ...
  Risco de indeferimento: [alto | médio | baixo] · IPC atual: ...
Cenário B · protocolar em [após fechar lacunas, em ... dias]
  DIB: ...           Retroativo: R$ ...  (diferença: R$ ...)
  Risco de indeferimento: [ ... ] · IPC projetado: ...
Recomendação e justificativa: ...
```

**Regra de decisão**: o indeferimento é recorrível, a DIB perdida não volta. Quando o óbito ocorreu
há menos de 90 dias (ou 180 para filho menor de 16), a perda da retroatividade costuma custar mais
que o risco de indeferimento. Simule os dois cenários em números antes de recomendar.
