# Modelos de Decisão Previdenciária — Referência Técnica

Fórmulas e modelos usados pelo Decisor de Melhor Aposentadoria. Todos os valores monetários
de referência (salário mínimo, teto) devem ser **confirmados com o usuário** no momento da
análise — podem ter mudado.

---

## 1. Requisitos das regras (resumo de decisão)

> Para os requisitos completos e fórmulas de RMI, ver a skill `calculos-previdenciarios`
> (references/regras-calculo.md). Aqui foca-se no que importa para DECIDIR.

| Regra | Idade mín. | Tempo contrib. | Fator? | Característica de decisão |
|-------|-----------|----------------|--------|---------------------------|
| Dir. Adquirido ATC (até 13/11/2019) | — | 30F / 35H | Sim (opcional) | Pode ser o maior valor se média alta |
| Dir. Adquirido Idade | 60F / 65H | 15 anos | Não | Antecipa para quem tem idade |
| Pontos | progressiva | 30F / 35H | Não | Equilíbrio valor × tempo |
| Idade progressiva | 59,5F / 64,5H (2026) | 15F / 20H | Não | Boa para quem tem idade e menos tempo |
| Pedágio 50% | — | faltava ≤2 anos em 2019 | **Sim** | Antecipa, mas fator pode reduzir |
| Pedágio 100% | 57F / 60H | dobro do que faltava | Não | Valor cheio (100% da média), sem fator |
| Idade definitiva | 62F / 65H | 15F / 20H | Não | Última opção, mais lenta |
| Especial | 55/58/60 | 15/20/25 anos | Não | Antecipa muito se exposição comprovada |
| PcD (LC 142/2013) | varia pelo grau | varia | Não | Antecipa para deficiência comprovada |

**Regra de bolso para decisão:**
- **Pedágio 100%** costuma dar o MAIOR valor (100% da média, sem fator) — mas é o mais lento.
- **Pedágio 50%** e **Dir. Adquirido ATC** aplicam fator → podem reduzir bastante se o cliente for jovem.
- **Pontos** tende a ser o melhor equilíbrio para quem tem muito tempo de contribuição.

---

## 2. Projeção de recebimento (linha do tempo)

Para cada cenário:

```
Recebimento_anual = RMI × 13          (12 meses + 13º)
Recebimento_acumulado(t) = Σ [RMI_ajustada(ano) × 13]  de início até t
RMI_ajustada(ano n) = RMI × (1 + reajuste)^n
```

- **reajuste**: usar INPC projetado. Default sugerido: 4%/ano. SEMPRE declarar a premissa.
- Benefícios no piso (1 salário mínimo) reajustam pelo SM, geralmente acima do INPC — sinalizar.

---

## 3. Ponto de Equilíbrio (Break-even) — antecipar × esperar

O modelo central da decisão. Compara um cenário que **paga menos, mas antes** (A) contra um
que **paga mais, mas depois** (B).

```
Dados:
  RMI_A, início_A   (antecipa)
  RMI_B, início_B   (espera);  início_B > início_A
  defasagem = meses entre início_A e início_B

Passo 1 — Vantagem inicial de A:
  A_acumulado_ate_B = RMI_A × defasagem   (o que A já embolsou enquanto B esperava)
  (incluir 13º proporcional se a defasagem cruzar dezembro)

Passo 2 — Vantagem mensal de B depois que começa:
  delta_mensal = RMI_B − RMI_A

Passo 3 — Tempo para B "alcançar" A:
  meses_equilibrio = A_acumulado_ate_B / delta_mensal
  data_equilibrio  = início_B + meses_equilibrio
  idade_equilibrio = idade do cliente em data_equilibrio

DECISÃO:
  Se expectativa de vida (IBGE) > idade_equilibrio → ESPERAR (B) compensa
  Se < idade_equilibrio, ou saúde frágil/urgência → ANTECIPAR (A) compensa
```

**Exemplo numérico (ilustrativo):**
```
A: R$ 2.000/mês a partir de hoje
B: R$ 2.600/mês a partir de 24 meses depois
A_acumulado_ate_B = 2.000 × 24 = R$ 48.000
delta_mensal = 2.600 − 2.000 = R$ 600
meses_equilibrio = 48.000 / 600 = 80 meses ≈ 6 anos e 8 meses
→ Se o cliente tem 60 anos hoje, o equilíbrio é aos ~68,7 anos.
→ Expectativa de sobrevida IBGE para 62 anos (início de B) costuma passar de 20 anos →
   ESPERAR tende a compensar, salvo urgência ou saúde frágil.
```

---

## 4. Valor Presente Líquido (VPL / NPV)

Para decidir "maximizar o total recebido na vida" considerando o valor do dinheiro no tempo.

```
VPL = Σ [ Fluxo_mensal_t / (1 + i)^t ]   para t = 1 até T

onde:
  Fluxo_mensal_t = RMI_ajustada no mês t (0 antes do início do benefício)
  i = taxa de desconto mensal (default sugerido: 0,5%/mês ≈ 6,17%/ano) — CONFIRMAR
  T = meses até a expectativa de vida (IBGE) a partir de hoje
```

- O cenário com **maior VPL** é o financeiramente ótimo para "maximizar o total".
- Mostrar VPL de cada cenário lado a lado.
- A taxa de desconto muda o resultado: taxa alta favorece antecipar; taxa baixa favorece esperar.
- SEMPRE declarar a taxa usada e oferecer recalcular com outra.

---

## 5. Custo de continuar contribuindo

Quando esperar exige mais aportes (CLT, contribuinte individual, facultativo).

```
Custo_total_esperar = (contribuição_mensal × meses_espera)      [dinheiro que sai]
                    + (RMI_menor × meses_espera)                 [benefício não recebido]

Ganho_total_esperar = (RMI_maior − RMI_menor) × meses_recebimento_esperado

DECISÃO: esperar só vale se  Ganho_total_esperar > Custo_total_esperar
```

`meses_recebimento_esperado` = (expectativa de vida IBGE − idade no início do benefício) × 12.

---

## 6. Tabela de sensibilidade (apresentar sempre)

Mostrar como a recomendação muda conforme a variável-chave:

| Se... | Então a melhor decisão é... |
|-------|------------------------------|
| Cliente com saúde frágil / doença | Antecipar (menor expectativa → break-even não compensa) |
| Cliente jovem e saudável | Esperar/maximizar (longa expectativa) |
| Urgência financeira | Antecipar |
| Taxa de desconto alta (dinheiro "caro" hoje) | Antecipar |
| Diferença de RMI pequena entre cenários | Antecipar (não vale esperar por pouco) |
| Diferença de RMI grande | Esperar tende a compensar |
| Fator previdenciário reduz muito (cliente jovem) | Fugir das regras com fator |

---

## 7. Premissas-padrão (declarar sempre, deixar o usuário ajustar)

| Premissa | Default sugerido | Observação |
|----------|------------------|------------|
| Reajuste anual do benefício | 4%/ano (INPC projetado) | Piso reajusta pelo SM |
| Taxa de desconto (VPL) | 0,5%/mês (~6,17%/ano) | Sensível — oferecer alternativas |
| Expectativa de vida | Tábua IBGE mais recente | Consultar por idade/sexo; nunca presumir saúde |
| 13º salário | Incluído (×13/ano) | |
| Inflação para corrigir contribuições | INPC | Ver skill de cálculos |

> Nenhuma premissa é "verdade" — todas devem aparecer no relatório e poder ser trocadas
> pelo advogado. A força do Decisor é a transparência da conta.
