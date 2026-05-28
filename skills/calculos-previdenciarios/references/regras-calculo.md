# Regras e Fórmulas de Cálculo Previdenciário

## Valores de Referência 2026

| Item | Valor |
|------|-------|
| Salário Mínimo | R$ 1.518,00 |
| Teto do INSS | R$ 8.157,41 |
| Limite BPC/LOAS (1/4 SM per capita) | R$ 379,50 |
| Data-marco da Reforma | 13/11/2019 |
| Pontos 2026 — Mulher | 93 pontos |
| Pontos 2026 — Homem | 103 pontos |
| Idade progressiva 2026 — Mulher | 59 anos e 6 meses |
| Idade progressiva 2026 — Homem | 64 anos e 6 meses |

> **IMPORTANTE:** Sempre confirme esses valores com o usuário. Podem ter sido atualizados
> após a criação desta skill. Para o teto do INSS e salário mínimo do ano corrente,
> a skill pode consultar o site da Previdência ou do IBGE via navegador quando autorizada.

---

## Fator Previdenciário

**Fórmula:**
```
Fp = (Tc × a / Es) × [1 + (Id + Tc × a) / 100]
```

Onde:
- **Tc** = tempo de contribuição em anos
- **a** = 0,31 (coeficiente fixo)
- **Es** = expectativa de sobrevida na data de requerimento (tabela IBGE)
- **Id** = idade do segurado na data de requerimento

**Fonte oficial do Es:** IBGE — Tábua Completa de Mortalidade, publicada anualmente em
dezembro com os dados do ano anterior.

URL para consulta:
`https://www.ibge.gov.br/estatisticas/sociais/populacao/9126-tabuas-completas-de-mortalidade.html`

> A skill pode consultar essa página automaticamente via navegador quando o usuário autorizar
> (Bloco 6, pergunta 21 do interrogatório).

O Fator Previdenciário é usado APENAS nas seguintes situações:
- Aposentadoria por Tempo de Contribuição com Direito Adquirido (pré-reforma)
- Pedágio 50% (regra de transição)

---

## 5.1 — Direito Adquirido (antes de 13/11/2019)

### a) Aposentadoria por Tempo de Contribuição (ATC)

**Requisito:**
- Mulher: 30 anos de contribuição (sem idade mínima)
- Homem: 35 anos de contribuição (sem idade mínima)

**Cálculo da RMI:**
```
RMI = Média dos 80% MAIORES salários de contribuição desde jul/1994 × Fator Previdenciário
```

### b) Aposentadoria por Idade (regra antiga)

**Requisito:**
- Mulher: 60 anos + 15 anos de contribuição (carência)
- Homem: 65 anos + 15 anos de contribuição (carência)

**Cálculo da RMI:**
```
RMI = Média dos 80% maiores × (70% + 1% por ano completo de contribuição)
```

Limite máximo do coeficiente: 100% (com 30 anos de contribuição para mulher / 35 para homem)

### c) Aposentadoria Especial (regra antiga)

**Requisito:**
- 15, 20 ou 25 anos de atividade especial (conforme grau de risco)
- Sem idade mínima

**Cálculo da RMI:**
```
RMI = Média dos 80% maiores salários de contribuição
```
(Sem aplicação de Fator Previdenciário)

---

## 5.2 — Regras de Transição (EC 103/2019)

### a) Regra de Pontos

**Requisito 2026:**
- Mulher: 93 pontos + mínimo 30 anos de contribuição
- Homem: 103 pontos + mínimo 35 anos de contribuição

**Progressão anual:** +1 ponto por ano
- Limite final: 100 pontos (mulher) / 105 pontos (homem)

**Cálculo dos pontos:** Idade (em anos) + Tempo de contribuição (em anos)

**Cálculo da RMI:**
```
RMI = Média de 100% dos salários × (60% + 2% por ano excedente a 15 anos [mulher] ou 20 anos [homem])
```

Exemplo: Mulher com 30 anos de contribuição → 60% + 2% × 15 = 60% + 30% = 90%

### b) Idade Mínima Progressiva

**Requisito 2026:**
- Mulher: 59 anos e 6 meses + 30 anos de contribuição
- Homem: 64 anos e 6 meses + 35 anos de contribuição

**Progressão anual:** +6 meses por ano
- Limite final: 62 anos (mulher) / 65 anos (homem)

**Cálculo da RMI:** Igual à Regra de Pontos (60% + 2% por ano excedente)

### c) Pedágio 50%

**Elegibilidade:** Somente para segurados que, em 13/11/2019, faltavam até 2 anos para
completar o tempo de contribuição necessário (30 anos mulher / 35 anos homem).

**Requisito:**
- Tempo faltante em 13/11/2019 + 50% desse tempo faltante
- Exemplo: Faltavam 2 anos → deve cumprir mais 1 ano de pedágio = 3 anos adicionais
- Sem idade mínima

**Cálculo da RMI:**
```
RMI = Média de 100% dos salários × Fator Previdenciário
```
> Esta é a ÚNICA regra de transição que aplica o Fator Previdenciário.

### d) Pedágio 100%

**Requisito:**
- Idade mínima: 57 anos (mulher) / 60 anos (homem)
- Tempo mínimo: 30 anos (mulher) / 35 anos (homem)
- + dobro do tempo que faltava em 13/11/2019

**Cálculo da RMI:**
```
RMI = Média de 100% dos salários × 100%
```
(Sem Fator Previdenciário — coeficiente fixo de 100%)

### e) Aposentadoria Especial — Transição por Pontos

| Tempo especial | Pontos exigidos | Tempo efetivo mínimo |
|---------------|-----------------|---------------------|
| 25 anos | 86 pontos | 25 anos efetivos |
| 20 anos | 76 pontos | 20 anos efetivos |
| 15 anos | 66 pontos | 15 anos efetivos |

**Cálculo da RMI:** Média de 100% dos salários (sem fator previdenciário)

---

## 5.3 — Regra Definitiva (pós EC 103/2019)

### a) Aposentadoria por Idade

**Requisito:**
- Mulher: 62 anos + 15 anos de contribuição (carência)
- Homem: 65 anos + 20 anos de contribuição (carência)

**Cálculo da RMI:**
```
RMI = Média de 100% dos salários × (60% + 2% por ano excedente a 15F / 20H)
```

### b) Aposentadoria Especial (definitiva)

| Tempo especial | Idade mínima |
|---------------|--------------|
| 25 anos | 60 anos de idade |
| 20 anos | 58 anos de idade |
| 15 anos | 55 anos de idade |

---

## 5.4 — Aposentadoria da Pessoa com Deficiência (LC 142/2013)

### Por Tempo de Contribuição

| Grau de deficiência | Tempo exigido — Homem | Tempo exigido — Mulher |
|--------------------|----------------------|------------------------|
| Grave | 25 anos | 20 anos |
| Moderada | 29 anos | 24 anos |
| Leve | 33 anos | 28 anos |

### Por Idade

- Homem: 60 anos + 15 anos de contribuição
- Mulher: 55 anos + 15 anos de contribuição

**Cálculo da RMI (ambas as modalidades):**
```
RMI = Média dos 80% maiores × (70% + 1% por ano de contribuição)
```
Sem Fator Previdenciário.

---

## 5.5 — Pensão por Morte

**Cálculo:**
```
Cota familiar = 50% + 10% por dependente (máximo 100%)
```

**Base de cálculo:**
- Se falecido era aposentado: usa o valor do benefício que recebia
- Se falecido não era aposentado: calcular a aposentadoria por incapacidade permanente
  hipotética (usando as regras abaixo)

**Duração para cônjuge/companheiro:**
- Varia conforme tempo de casamento/união e idade do sobrevivente
- Verificar legislação vigente (alterações recentes podem impactar)

---

## 5.6 — Auxílio por Incapacidade

### Temporário (antigo Auxílio-Doença)

**Carência:** 12 meses
- Exceções: acidente de qualquer natureza ou doença grave listada (sem carência)

**Cálculo:**
```
Benefício = Média de 100% dos salários × 91%
```
Limitado à média dos últimos 12 salários de contribuição.

### Permanente (Aposentadoria por Incapacidade — antigo Aposentadoria por Invalidez)

**Cálculo — Doença Comum:**
```
RMI = Média de 100% × (60% + 2% por ano excedente a 20 anos de contribuição)
Mínimo garantido: 1 salário mínimo
```

**Cálculo — Acidente de trabalho ou doença ocupacional:**
```
RMI = Média de 100% × 100%
```

**Acréscimo de 25%:** Se o segurado necessitar de assistência permanente de terceiros.

---

## 5.7 — BPC/LOAS

**Requisitos:**
- Idoso: 65 anos ou mais
- Pessoa com Deficiência: deficiência de longo prazo (impedimentos por 2+ anos)
- Renda per capita familiar: máximo 1/4 do salário mínimo (R$ 379,50 em 2026)

**Valor:** 1 salário mínimo (R$ 1.518,00 em 2026)

**Observações:**
- Não exige nenhum período de contribuição
- Não gera pensão por morte para dependentes
- Não acumula com outros benefícios previdenciários (com exceções específicas)

---

## Fatores de Conversão — Tempo Especial em Comum

> Aplicável SOMENTE para períodos até 13/11/2019

| Tempo especial | Fator — Homem | Fator — Mulher |
|---------------|--------------|----------------|
| 25 anos | 1,4 | 1,2 |
| 20 anos | 1,75 | 1,5 |
| 15 anos | 2,33 | 2,0 |

**Exemplo:** 10 anos de atividade especial (25 anos) de um homem →
10 × 1,4 = 14 anos de tempo comum

---

## Cálculo da Média Salarial

**Regra geral:**
- Utiliza 100% dos salários de contribuição (desde 07/1994)
- Para direito adquirido (pré-reforma): média dos 80% MAIORES

**Correção monetária (INPC):**

Quando o usuário autorizar a correção monetária (Bloco 6, pergunta 20):

1. Identifique a competência (mês/ano) de cada salário de contribuição
2. Aplique o fator de correção INPC acumulado da competência até o mês de referência
3. Fórmula:
   ```
   SC_corrigido = SC_nominal × (INPC_referência / INPC_competência)
   ```
4. Fonte oficial dos índices INPC:
   - IBGE: `https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9258-indice-nacional-de-precos-ao-consumidor.html`
   - Banco Central (Calculadora do Cidadão): `https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormCorrecaoValores.do?method=exibirFormCorrecaoValores&aba=1`
5. Para automação, a tabela INSS atualizada de correção mensal também é publicada
   no Diário Oficial mensalmente

> A skill pode consultar essas fontes via navegador quando autorizada, OU usar uma tabela
> interna até a última atualização. Sempre informe ao usuário qual fonte foi utilizada.

**Teto:** Nenhum salário de contribuição pode superar o teto do INSS vigente em cada
competência. Salários acima do teto são limitados ao teto.

**Período de carência:**
- Regra geral: 180 contribuições (15 anos)
- Aposentadoria por Idade (definitiva — homem): 240 contribuições (20 anos)
- Auxílio por incapacidade: 12 contribuições

---

## Progressão dos Pontos (Regra de Pontos)

| Ano | Pontos — Mulher | Pontos — Homem |
|-----|----------------|----------------|
| 2019 | 86 | 96 |
| 2020 | 87 | 97 |
| 2021 | 88 | 98 |
| 2022 | 89 | 99 |
| 2023 | 90 | 100 |
| 2024 | 91 | 101 |
| 2025 | 92 | 102 |
| **2026** | **93** | **103** |
| 2027 | 94 | 104 |
| 2028 | 95 | 105 (limite homem) |
| 2029 | 96 | 105 |
| 2030 | 97 | 105 |
| 2031 | 98 | 105 |
| 2032 | 99 | 105 |
| 2033+ | 100 (limite mulher) | 105 |

> **Nota:** Confirme sempre a pontuação vigente no ano da consulta.

---

## Progressão da Idade Mínima (Idade Progressiva)

| Ano | Idade — Mulher | Idade — Homem |
|-----|---------------|---------------|
| 2019 | 56 anos | 61 anos |
| 2020 | 56,5 anos | 61,5 anos |
| 2021 | 57 anos | 62 anos |
| 2022 | 57,5 anos | 62,5 anos |
| 2023 | 58 anos | 63 anos |
| 2024 | 58,5 anos | 63,5 anos |
| 2025 | 59 anos | 64 anos |
| **2026** | **59,5 anos** | **64,5 anos** |
| 2027 | 60 anos | 65 anos (limite homem) |
| 2028 | 60,5 anos | 65 anos |
| 2029 | 61 anos | 65 anos |
| 2030 | 61,5 anos | 65 anos |
| 2031+ | 62 anos (limite mulher) | 65 anos |

---

## Período de Graça (Manutenção da Qualidade de Segurado)

Após cessar as contribuições, o segurado mantém a qualidade por:
- **12 meses:** regra geral
- **24 meses:** se já completou 120 contribuições (10 anos)
- **36 meses:** se o desemprego for comprovado com registro formal

Após o período de graça, perde a qualidade de segurado e perde a proteção previdenciária
(exceto BPC/LOAS, que independe de contribuição).
