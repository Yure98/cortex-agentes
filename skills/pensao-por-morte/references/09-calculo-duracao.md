# 09. Cálculo, duração, DIB e acumulação

Use `scripts/calculadora_pensao.py` para todos os números. Confira sempre o regime pela data do
óbito (`references/01-mapa-normativo.md`).

## 1. Base de cálculo

**Óbito a partir de 13/11/2019 (EC 103/2019, art. 23):**

1. Apure a base:
   - se o falecido já era aposentado, a base é o valor da aposentadoria que recebia;
   - se não era aposentado, a base é o valor da aposentadoria por incapacidade permanente a que
     teria direito na data do óbito, calculada sobre 100% da média de todos os salários de
     contribuição desde julho de 1994, com o coeficiente aplicável (60% mais 2 pontos percentuais
     por ano de contribuição que exceder 20 anos para homem e 15 anos para mulher, com a regra
     integral de 100% da média quando a incapacidade decorre de acidente do trabalho, doença
     profissional ou do trabalho).
2. Aplique a fórmula das cotas: 50% de cota familiar mais 10 pontos percentuais por dependente,
   até 100%.
3. Divida o resultado em cotas iguais entre os dependentes habilitados.
4. Piso: o valor não pode ser inferior a um salário mínimo quando substituir a renda do
   dependente. Teto: limite máximo do RGPS do ano.
5. Exceção do art. 23, §2º: havendo dependente inválido ou com deficiência intelectual, mental ou
   grave, o valor equivale a 100% da aposentadoria até o limite do RGPS, com a regra específica
   para a parcela excedente no RPPS.

**Óbito anterior a 13/11/2019:** 100% do valor da aposentadoria que recebia ou daquela a que teria
direito, sem a fórmula das cotas.

Referências de valores de 2026 (confirmar antes de usar): salário mínimo R$ 1.621,00 e teto do
RGPS R$ 8.475,55.

### Exemplo
Base de R$ 4.000,00, viúva e dois filhos menores:
50% + 10% + 10% + 10% = 80% de R$ 4.000,00 = R$ 3.200,00, divididos em três cotas de
R$ 1.066,67. Quando o primeiro filho completa 21 anos, o total cai para 70% (R$ 2.800,00) e a cota
do filho **não** reverte aos demais.

## 2. Duração do benefício

### Filhos e irmãos
Até 21 anos, salvo invalidez ou deficiência preexistente, hipótese em que dura enquanto a condição
persistir. Emancipação cessa a cota. Curso universitário não prorroga.

### Pais
Enquanto durar a dependência comprovada.

### Cônjuge ou companheiro
Duas checagens antes da tabela:

1. O falecido tinha ao menos 18 contribuições mensais (ou 18 meses de atividade rural)?
2. O casamento ou a união estável tinha ao menos 2 anos na data do óbito?

Faltando qualquer um: **4 meses**, salvo se o óbito decorreu de acidente de qualquer natureza ou
de doença profissional ou do trabalho, hipótese em que se aplica a tabela normalmente.

Atendidos os dois, aplica-se a tabela pela idade do dependente na data do óbito:

**Óbito de 18/06/2015 a 31/12/2020**

| Idade na data do óbito | Duração |
|---|---|
| menos de 21 | 3 anos |
| 21 a 26 | 6 anos |
| 27 a 29 | 10 anos |
| 30 a 40 | 15 anos |
| 41 a 43 | 20 anos |
| 44 ou mais | vitalícia |

**Óbito a partir de 01/01/2021 (Portaria SEPRT/ME 424/2020)**

| Idade na data do óbito | Duração |
|---|---|
| menos de 22 | 3 anos |
| 22 a 27 | 6 anos |
| 28 a 30 | 10 anos |
| 31 a 41 | 15 anos |
| 42 a 44 | 20 anos |
| 45 ou mais | vitalícia |

Cônjuge inválido ou com deficiência: a pensão dura enquanto persistir a condição, respeitados os
prazos mínimos da tabela. Cessada a invalidez, completa-se o prazo mínimo correspondente à faixa
etária.

**Tema 377/TNU:** o prazo de 4 meses conta invariavelmente da data do óbito. Em habilitação
tardia, o dependente só recebe as parcelas entre a DER e o termo final dos 4 meses contados do
falecimento. Requerimento após esse período não gera direito a parcelas.

## 3. DIB (art. 74)

| Situação | DIB |
|---|---|
| Requerimento em até 90 dias do óbito | Data do óbito |
| Requerimento por filho menor de 16 anos em até 180 dias | Data do óbito |
| Requerimento após esses prazos | Data do requerimento (DER) |
| Óbito presumido por ausência ou catástrofe | Data da decisão judicial |

Para óbitos anteriores a 18/01/2019, o prazo era de 30 dias.

**Tema 1.421/STJ (2026):** não retroage à data do óbito o início dos efeitos financeiros da pensão
por morte ou do auxílio-reclusão requerido por filho menor de 16 anos após 180 dias do evento,
quando ocorrido na vigência da MP 871/2019, convertida na Lei 13.846/2019. Antes dessa alteração,
prevalecia a retroação em favor de incapazes.

Prescrição: parcelas anteriores aos 5 anos do requerimento estão prescritas (art. 103, parágrafo
único, e Súmula 85/STJ), salvo em favor de pensionista menor, incapaz ou ausente (art. 79).

## 4. Acumulação (art. 24 da EC 103/2019)

Para fatos geradores a partir de 13/11/2019, é vedada a acumulação de mais de uma pensão do mesmo
regime, salvo as hipóteses do §1º. Nas hipóteses permitidas, paga-se integralmente o benefício
mais vantajoso e aplica-se ao outro o redutor por faixas:

| Faixa do segundo benefício | Percentual aproveitado |
|---|---|
| Até 1 salário mínimo | 100% |
| Parcela entre 1 e 2 salários mínimos | 60% |
| Parcela entre 2 e 3 salários mínimos | 40% |
| Parcela entre 3 e 4 salários mínimos | 20% |
| Parcela acima de 4 salários mínimos | 10% |

Hipóteses admitidas: pensão de cônjuge ou companheiro de um regime com pensão de outro regime ou
com pensão militar; pensão de cônjuge ou companheiro com aposentadoria do RGPS ou de RPPS ou com
proventos militares; pensão militar com aposentadoria.

Observações práticas:
- Sempre simule as duas ordens possíveis para identificar qual benefício deve ser mantido
  integral. O script faz a comparação.
- BPC não acumula com pensão por morte. O cliente precisará optar, e a opção deve considerar
  valor, duração e reversibilidade.
- A constitucionalidade do art. 24 é discutida no STF. Registre a ressalva quando o valor perdido
  for expressivo, e avalie a conveniência de ressalvar o pedido na inicial.

## 5. Revisões frequentes de pensão já concedida

1. Aplicação indevida das cotas da EC 103/2019 a óbito anterior a 13/11/2019.
2. Ausência de reconhecimento de dependente inválido ou com deficiência, que levaria a 100%.
3. Base de cálculo errada por não computar vínculos ausentes no CNIS ou tempo especial.
4. Morte por acidente de trabalho não reconhecida, o que muda o coeficiente da aposentadoria ficta
   e afasta os filtros de duração.
5. Não reversão de cotas em óbitos anteriores à EC 103/2019, quando a regra era a reversão.
6. Cessação indevida de cota de filho inválido sem perícia.
7. Atrasados pagos a menor, sem juros e correção corretos (observar EC 113/2021 e a taxa Selic para
   débitos da Fazenda Pública).

Prazo: decadência de 10 anos para revisão do ato de concessão (art. 103) e prescrição quinquenal
das parcelas.
