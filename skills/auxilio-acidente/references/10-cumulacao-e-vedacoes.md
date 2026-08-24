# 10. Cumulação e vedações: o que pode e o que não pode juntar

O auxílio-acidente tem regras de cumulação particulares, diferentes de outros benefícios do
RGPS. Erro aqui gera dois problemas opostos: promessa de acúmulo que não existe, e perda de
acúmulo que o cliente já teria direito de manter.

---

## 1. Cumulação com remuneração do trabalho

Isto é a regra, não a exceção. O auxílio-acidente tem natureza indenizatória e é compatível com
o exercício de atividade remunerada, seja a mesma função de antes, seja outra. Diferente do
auxílio-doença, que pressupõe afastamento, o auxílio-acidente é pago junto com o salário do
segurado que continua trabalhando.

---

## 2. Cumulação com aposentadoria: a regra da Súmula 507/STJ

**Regra geral, a partir de 11/11/1997 (Lei 9.528/97):** é vedada a cumulação de auxílio-acidente
com qualquer aposentadoria concedida a partir dessa data. O auxílio-acidente é extinto no dia
anterior ao início da aposentadoria (art. 86, §2º, redação da Lei 9.528/97).

**A EC 103/2019, no art. 26, §3º, II, reafirma essa vedação em nível constitucional**, para as
aposentadorias concedidas a partir de sua vigência. Não muda o regime, apenas confirma o que a
Lei 9.528/97 já determinava.

**Exceção pela Súmula 507/STJ:** a acumulação de auxílio-acidente com aposentadoria pressupõe
que **as duas condições sejam anteriores a 11/11/1997**:

1. a lesão incapacitante que gerou o direito ao auxílio-acidente, apurada pela data da
   consolidação, ou, nos casos de doença profissional ou do trabalho, pelo critério do art. 23
   da Lei 8.213/91; **e**
2. a concessão da própria aposentadoria.

Se qualquer uma das duas datas for posterior a 11/11/1997, a cumulação não é possível, mesmo que
a outra data seja anterior. As duas condições são cumulativas.

**Como aplicar o teste:**

```
python scripts/calculadora_auxilio_acidente.py cumulacao --lesao <data> --aposentadoria <data>
```

O script aplica automaticamente o corte de 11/11/1997 nas duas datas e informa se a cumulação é
possível.

---

## 3. Cumulação com auxílio-doença: depende do fato gerador

**Mesmo fato gerador:** é indevida a cumulação simultânea de auxílio-acidente e auxílio-doença
quando ambos decorrem exatamente da mesma lesão. A lógica é sequencial: primeiro o
auxílio-doença, durante o período de incapacidade temporária; depois, se e quando a lesão
consolidar com sequela residual, o auxílio-acidente assume, com DIB no dia seguinte à cessação
do auxílio-doença.

**Fatos geradores diferentes:** se o segurado já é titular de auxílio-acidente por uma sequela
antiga e sofre um novo evento incapacitante, independente do primeiro, é possível o recebimento
concomitante do novo auxílio-doença com o auxílio-acidente já concedido. São lesões distintas,
tratadas de forma autônoma.

**Como identificar isso na prática:** pergunte, sempre, se o novo afastamento tem relação com a
mesma parte do corpo e o mesmo evento do auxílio-acidente já recebido, ou se é um problema de
saúde totalmente independente.

---

## 4. Fim da conversão automática em aposentadoria por invalidez

Até a Lei 9.528/97, o auxílio-acidente podia ser convertido em aposentadoria por invalidez de
forma facilitada, quando o quadro evoluísse para incapacidade total. **Isso não existe mais.**

Hoje, se a sequela evolui para incapacidade total e permanente para qualquer atividade, o
caminho é um requerimento novo e autônomo de aposentadoria por incapacidade permanente
(antiga aposentadoria por invalidez), com perícia própria, analisando os requisitos específicos
desse benefício, carência, qualidade de segurado, incapacidade total e permanente para toda e
qualquer atividade. O auxílio-acidente anterior não se transforma automaticamente; ele é
extinto quando a nova aposentadoria é concedida, seguindo a regra geral de vedação de cumulação.

---

## 5. Cumulação com BPC/LOAS

O BPC é assistencial, não previdenciário, e tem renda per capita como requisito de elegibilidade.
Não há vedação legal específica de cumulação com auxílio-acidente no mesmo texto do art. 86, mas
o próprio requisito de renda per capita do BPC tende a ser afetado pela existência de qualquer
renda familiar, incluindo o auxílio-acidente. Avalie caso a caso a viabilidade de manter os
dois, considerando o critério de renda do BPC vigente.

---

## 6. Pensão de RPPS ou militar

Não há vedação específica de cumulação do auxílio-acidente do RGPS com pensão de regime próprio
estatutário ou militar, por serem regimes distintos, mas confirme eventual regra própria do
regime de origem do outro benefício antes de afirmar a compatibilidade.

---

## 7. Tabela-resumo de cumulação

| Combinação | Pode acumular? | Condição |
|---|---|---|
| Auxílio-acidente + salário do trabalho | Sim | Sempre, é a regra do benefício |
| Auxílio-acidente + auxílio-doença, mesma lesão | Não | São sequenciais, não simultâneos |
| Auxílio-acidente + auxílio-doença, lesão diferente | Sim | Fatos geradores autônomos |
| Auxílio-acidente + aposentadoria concedida após 11/11/1997 | Não | Extinção do auxílio-acidente na data de início da aposentadoria |
| Auxílio-acidente + aposentadoria, ambas anteriores a 11/11/1997 | Sim | Súmula 507/STJ |
| Auxílio-acidente + BPC/LOAS | Avaliar | Critério de renda per capita do BPC pode ser afetado |
| Conversão automática em aposentadoria por invalidez | Não existe mais | Extinta pela Lei 9.528/97. Requerimento novo e autônomo |
