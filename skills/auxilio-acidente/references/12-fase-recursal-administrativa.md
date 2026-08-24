# 12. Fase recursal administrativa: recurso ao CRPS

---

## 1. Estrutura do CRPS

O Conselho de Recursos da Previdência Social julga recursos em duas instâncias:

1. **Junta de Recursos (JR)**, primeira instância recursal.
2. **Câmara de Julgamento (CaJ)**, segunda instância, se a Junta mantiver a decisão
   desfavorável.

O julgamento tramita pelo sistema e-Recursos.

---

## 2. Prazos

- 30 dias, contados da ciência da decisão do INSS, para o recurso ordinário à Junta de
  Recursos, com base no art. 305, §1º, do Decreto 3.048/99.
- 30 dias, contados da ciência da decisão da Junta de Recursos, para o recurso especial à
  Câmara de Julgamento, quando cabível.
- Sempre confira a data exata de ciência informada nos autos digitais e calcule o prazo com
  precisão antes de qualquer recomendação. Use
  `python scripts/calculadora_auxilio_acidente.py prazos --ciencia <data>`.

**Fundamento legal do cabimento do recurso:** art. 126 da Lei 8.213/91.

---

## 3. O que fundamentar no recurso, conforme o motivo da negativa

| Motivo alegado pelo INSS | Fundamentação de ataque |
|---|---|
| Ausência de nexo técnico | NTEP, PPP, laudos técnicos, jurisprudência sobre dispensabilidade da CAT. Ver `references/04-nexo-tecnico-e-fato-gerador.md` |
| Ausência de redução de capacidade, ou "grau mínimo" | Tema 416/STJ e Súmula 88/TNU. Se for caso de disacusia, também a Súmula 44/STJ |
| Lesão não consolidada | Reforçar relatório médico atualizado, ou reconhecer a prematuridade e reorientar para outro benefício, se for o caso |
| Categoria fora do rol do art. 18, §1º | Testar a exceção do período de graça de vínculo anterior. Ver `references/05-beneficiarios-e-qualidade-segurado.md`, com a ressalva de que é tese não pacificada |
| Indeferimento na análise documental prévia por documentação insuficiente | Juntar, com o recurso, exatamente o documento apontado como ausente, com pedido de reconsideração fundamentado |
| Vedação de cumulação com aposentadoria | Testar a Súmula 507/STJ, verificando as duas datas relevantes |

---

## 4. Requisitos formais do recurso

- Qualificação completa do recorrente.
- Número do benefício ou do protocolo.
- Síntese objetiva dos fatos e do fundamento da negativa.
- Fundamentação jurídica específica, ponto a ponto, sem citação decorativa de precedente.
- Pedido claro: reforma da decisão e concessão do benefício, com a DIB pretendida.
- Documentos novos, se houver, organizados e identificados.

Modelo em `assets/modelo-recurso-ordinario-crps.md` e `assets/modelo-recurso-especial-crps.md`.

---

## 5. Cumprimento de decisão favorável do CRPS

Decisões do CRPS favoráveis ao segurado devem ser cumpridas pelo INSS dentro do prazo
regulamentar após disponibilização no sistema de recursos, ressalvadas determinações judiciais
ou impedimentos devidamente justificados. Acompanhe o cumprimento e, se houver demora
injustificada, avalie medida judicial de cumprimento.

---

## 6. Quando pular direto para a via judicial

Avalie a via judicial em vez do recurso ao CRPS quando:

- houver urgência incompatível com o tempo médio de julgamento do CRPS, especialmente se a
  sequela ou a situação financeira do cliente exigir resposta rápida;
- o motivo da negativa for essencialmente probatório, dependente de perícia judicial mais
  robusta do que a via administrativa costuma proporcionar;
- já houver entendimento consolidado, na jurisdição do cliente, favorável à tese, tornando a via
  judicial mais previsível que o CRPS.

Em regra, e sempre que não houver dispensa expressa aplicável, exige-se o prévio requerimento
administrativo como condição de interesse de agir, conforme o Tema 350/STF. O recurso ao CRPS
não é, em si, requisito obrigatório antes da via judicial, uma vez já indeferido o requerimento
administrativo inicial.

Ver `references/13-fase-judicial.md`.
