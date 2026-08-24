# 06. Índice de Prontidão Probatória (IPP): pontuação de lacunas

O IPP transforma a entrevista em um número defensável. Ele responde a uma pergunta prática:
protocolo hoje, aguardo a consolidação, ou diligencio antes?

Escala de 0 a 100, dividida em 5 blocos. Cada item tem pontuação cheia, parcial ou zero. Toda
pontuação parcial obriga a skill a registrar o motivo e a forma de suprir.

Cálculo automático: `python scripts/score_prontidao.py caso.json`.

---

## Bloco A: qualidade de segurado e enquadramento do beneficiário (20 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| A1. Categoria do segurado dentro do rol do art. 18, §1º, na data do evento (8) | 8: empregado, avulso, doméstico ou especial confirmado por documento | 4: categoria alegada, sem confirmação documental | 0: fora do rol, sem exceção aplicável |
| A2. Qualidade de segurado documentada na data do evento (7) | 7: CNIS, CTPS ou cadastro rural conferido | 3: indício, sem confirmação | 0: sem prova |
| A3. Se fora do rol hoje: teste do período de graça de vínculo anterior (3) | 3: acidente dentro do período de graça, documentado | 1: alegado, sem datas confirmadas | 0: não se aplica ou não sustenta |
| A4. Coerência entre CNIS e categoria alegada (2) | 2: sem divergência | 1: divergência menor explicável | 0: divergência relevante não explicada |

---

## Bloco B: nexo técnico e fato gerador (25 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| B1. CAT emitida e coerente com o relato (8) | 8: CAT emitida, descrição compatível | 4: CAT emitida com divergência menor, ou emitida por via alternativa (sindicato, médico) | 0: sem CAT e sem via alternativa documentada |
| B2. Nexo técnico demonstrado por outros meios, se não há CAT (7) | 7: NTEP, PPP ou laudo técnico relacionando atividade e lesão | 3: indício de nexo sem documento técnico | 0: nexo apenas alegado |
| B3. Classificação da categoria do fato gerador definida (5) | 5: acidente típico, trajeto, doença profissional ou doença do trabalho, corretamente enquadrado | 2: enquadramento incerto | 0: não analisado |
| B4. Testemunhas do evento ou da atividade, quando aplicável (5) | 5: duas ou mais testemunhas idôneas identificadas | 2: uma testemunha, ou testemunhas com vínculo de interesse | 0: nenhuma |

---

## Bloco C: sequela, prova médica e redução da capacidade (30 pontos)

Este é o bloco mais pesado, porque é o núcleo do próprio benefício.

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| C1. Lesão consolidada, com data definida (10) | 10: laudo ou relatório médico confirma consolidação e data | 5: alegação de consolidação sem documento formal | 0: ainda em tratamento ou sem informação |
| C2. Laudos, exames de imagem e prontuários reunidos (8) | 8: conjunto robusto, cobrindo diagnóstico e evolução | 4: documentos parciais ou antigos | 0: nenhum documento médico |
| C3. Descrição funcional da redução de capacidade (7) | 7: relato específico do que mudou na atividade habitual, com exemplos concretos | 3: relato genérico ("ficou mais difícil") | 0: sem descrição funcional |
| C4. Redução compatível com o Anexo III do Decreto 3.048/99 ou fundamentável fora dele (5) | 5: sequela listada no Anexo III, ou fundamentação clara de que a lista é exemplificativa | 2: sequela atípica sem fundamentação | 0: dúvida real sobre existência de redução funcional |

---

## Bloco D: prova documental complementar (15 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| D1. Histórico de auxílio-doença, se houver, com datas de início e cessação (6) | 6: datas confirmadas por extrato do CNIS ou carta do INSS | 3: alegado sem confirmação | 0: não investigado |
| D2. PPP, PCMSO, PGR ou laudos ambientais da empresa, quando aplicável a doença ocupacional (5) | 5: documento obtido | 2: solicitado, aguardando | 0: não solicitado |
| D3. Prova complementar rural, quando aplicável (autodeclaração, CAF, cadastro art. 38-A) (4) | 4: documento em mãos | 2: em processo de obtenção | 0: ausente, sem justificativa |

No caso urbano sem componente rural, D3 é marcado como "não aplicável" e seus pontos são
redistribuídos proporcionalmente entre D1 e D2 pelo script.

---

## Bloco E: cálculo, cumulação e riscos (10 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| E1. Base de cálculo apurada, salário de benefício estimado (4) | 4: valor apurado ou simulado com CNIS/HISCRE | 2: estimativa grosseira | 0: sem informação |
| E2. Situação de cumulação analisada, aposentadoria e outros benefícios (3) | 3: analisada com o teste da Súmula 507/STJ, se aplicável | 1: mencionada sem análise | 0: ignorada |
| E3. Riscos e bloqueios fatais checados (3) | 3: checklist da seção 8 do SKILL.md rodado | 1: parcialmente | 0: não rodado |

---

## Faixas e decisão

| IPP | Leitura | Conduta |
|---|---|---|
| 85 a 100 | Maduro | Protocolar. Se já indeferido, judicializar |
| 70 a 84 | Protocolável | Protocolar e suprir lacunas durante a análise documental prévia |
| 50 a 69 | Insuficiente | Diligenciar antes. A análise documental prévia da Portaria 15/2026 pode indeferir sem perícia se a instrução for fraca |
| 30 a 49 | Frágil | Reunir prova médica e de nexo. Avaliar se a lesão ainda não consolidou |
| 0 a 29 | Inviável hoje | Reavaliar a tese, pode ser cedo demais ou pode ser caso de auxílio-doença, e informar o cliente com clareza |

## Bloqueios fatais

Se qualquer um estiver presente, a recomendação vira "não protocolar" independentemente do
score. Use o código do veto no relatório.

| Código | Veto | Fundamento | Saída possível |
|---|---|---|---|
| V1 | Categoria fora do rol do art. 18, §1º, sem exceção aplicável | art. 18, §1º | Testar o período de graça de vínculo anterior. Se não sustentar, orientar o cliente sobre a impossibilidade |
| V2 | Ausência de qualidade de segurado, dentro de categoria elegível, na data do evento | art. 18, §1º c/c art. 15 | Reexaminar CNIS, prorrogação de período de graça |
| V3 | Lesão ainda não consolidada | art. 86, caput | Aguardar a consolidação. Avaliar se cabe pedido de auxílio-doença nesse ínterim |
| V4 | Ausência de qualquer redução de capacidade constatável | art. 86, caput; Tema 416/STJ | Reavaliar a tese, ou aguardar evolução do quadro |
| V5 | Nexo técnico inexistente ou fortemente contestável | arts. 19, 20 e 21 | Buscar prova alternativa de nexo, ou reconhecer a fragilidade da tese |

## Como reportar o IPP

Nunca entregue apenas o número. O formato correto é:

```
IPP 58/100 (faixa: instrucao insuficiente)
A 15/20  B 14/25  C 16/30  D 8/15  E 5/10

Lacunas prioritarias:
1. C1 (5/10) Consolidacao nao documentada formalmente.
   Fontes: relatorio do medico assistente afirmando estabilizacao do quadro, ou data de alta do INSS.
   Ganho potencial: +5 e destrava a viabilidade de protocolo.
2. B1 (4/8) CAT nao emitida, sem via alternativa ainda buscada.
   Fontes: emissao pelo proprio segurado no Meu INSS, ou pelo sindicato.
   Ganho potencial: +4.
3. C3 (3/7) Relato funcional generico.
   Fontes: nova entrevista focada em tarefas especificas do dia a dia de trabalho.
   Ganho potencial: +4.

Com as tres lacunas resolvidas: IPP projetado 71 (protocolavel).
```

Sempre projete o IPP pós-diligência. É o dado que permite ao advogado decidir se vale o esforço,
e é especialmente importante aqui porque a análise documental prévia da Portaria 15/2026 pune
com dureza a instrução malfeita.
