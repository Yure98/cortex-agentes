# 05. Índice de Prontidão do Caso (IPC): pontuação de lacunas

O IPC transforma a entrevista em um número defensável. Ele responde a uma pergunta prática:
**protocolo hoje ou diligencio antes?**

Escala de 0 a 100, dividida em 5 blocos. Cada item tem pontuação cheia, parcial ou zero. Toda
pontuação parcial obriga a skill a registrar o motivo e a forma de suprir.

Cálculo automático: `python3 scripts/score_prontidao.py caso.json`.

---

## Bloco A: Evento morte e legitimação (15 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| A1. Certidão de óbito em mãos (5) | 5: certidão registrada | 2: declaração de óbito ou boletim, certidão em trâmite | 0: nada |
| A2. Causa da morte documentada (4) | 4: certidão com causa, laudo IML, CAT ou BO quando acidental | 2: causa informada sem documento | 0: desconhecida |
| A3. Legitimidade do requerente definida (3) | 3: relação documentada e classe correta | 1: relação alegada sem documento | 0: indefinida |
| A4. Mapeamento de outros habilitados (3) | 3: mapeamento feito com consulta a certidões e CNIS | 1: mapeamento apenas pela palavra do cliente | 0: não feito |

Alerta: quando a morte pode ser acidental e não há documento, a perda potencial é grande, porque
a morte acidental afasta os filtros de duração.

---

## Bloco B: Qualidade de segurado do falecido (25 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| B1. CNIS completo e atualizado do falecido (6) | 6: CNIS extraído e conferido | 3: CNIS parcial ou antigo | 0: sem CNIS |
| B2. Vínculo ou contribuição vigente na data do óbito (8) | 8: contribuição no mês do óbito ou benefício ativo | 4: dentro do período de graça sem prorrogação comprovada | 0: fora do período de graça |
| B3. Prorrogação do período de graça documentada, se necessária (5) | 5: prova de desemprego involuntário ou de mais de 120 contribuições | 2: alegação com indício | 0: necessária e ausente |
| B4. Vínculos não constantes do CNIS mapeados (3) | 3: mapeados com prova | 1: mapeados sem prova | 0: não investigados |
| B5. Direito adquirido a aposentadoria em vida, se aplicável (3) | 3: apurado e documentado | 1: apurado sem cálculo | 0: não apurado quando havia perda de qualidade |

No caso rural, substitua B2 e B3 por:
- B2r. Prova de exercício de atividade rural na data do óbito (8).
- B3r. Ausência de descaracterização por vínculo urbano acima de 120 dias no ano civil (5).

---

## Bloco C: Qualidade de dependente (25 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| C1. Documento formal da relação (8) | 8: certidão de casamento, nascimento, tutela ou guarda | 4: declaração particular, escritura de união estável recente | 0: apenas alegação |
| C2. Início de prova material contemporânea, quando exigido (8) | 8: dois ou mais documentos dentro dos 24 meses anteriores | 4: um documento no período | 0: nenhum documento no período |
| C3. Prova de dependência econômica, quando exigida (5) | 5: prova documental robusta | 2: prova indireta | 0: ausente |
| C4. Invalidez ou deficiência documentada, quando alegada (4) | 4: laudo e histórico anteriores ao óbito e aos 21 anos | 2: laudo atual sem histórico | 0: alegada sem documento |

Se a relação for casamento vigente e sem separação de fato, C2 recebe pontuação cheia por
presunção, salvo se o INSS já tiver questionado.

---

## Bloco D: Prova material e coerência temporal (20 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| D1. Linha do tempo probatória sem vazios relevantes (7) | 7: documentos cobrem o período crítico | 3: vazios pontuais | 0: vazios estruturais |
| D2. Coerência entre bases oficiais, CNIS, CadÚnico, INCRA, endereço, sindicato (5) | 5: coerentes | 2: divergência menor explicável | 0: divergência relevante não explicada |
| D3. Testemunhas identificadas e sem interesse direto (4) | 4: três ou mais idôneas | 2: uma ou duas, ou parentes | 0: nenhuma |
| D4. Documentos em nome de terceiro do grupo familiar aproveitáveis (4) | 4: identificados e vinculados | 2: identificados sem vínculo demonstrado | 0: não pesquisados |

No caso urbano, D1 e D4 pesam menos e podem ser marcados como "não aplicável", com redistribuição
proporcional dos pontos para os blocos B e C (o script faz isso automaticamente).

---

## Bloco E: Cálculo, DIB, acumulação e riscos (15 pontos)

| Item | Cheio | Parcial | Zero |
|---|---|---|---|
| E1. Base de cálculo apurada (4) | 4: valor do benefício ou média de salários apurada | 2: estimativa | 0: sem informação |
| E2. DIB definida corretamente conforme prazo de requerimento (4) | 4: dentro de 90 ou 180 dias, ou DIB na DER assumida conscientemente | 2: prazo perdido sem análise de impacto | 0: não analisada |
| E3. Acumulação e opção mais vantajosa analisadas (3) | 3: simulada com redutores | 1: mencionada | 0: ignorada |
| E4. Riscos e bloqueios fatais checados (4) | 4: checklist da seção 8 do SKILL.md rodado | 2: parcialmente | 0: não rodado |

---

## Faixas e decisão

| IPC | Leitura | Conduta |
|---|---|---|
| 85 a 100 | Maduro | Protocolar. Se já indeferido, judicializar com tutela |
| 70 a 84 | Protocolável | Protocolar e suprir lacunas durante a análise |
| 50 a 69 | Insuficiente | Diligenciar antes. Protocolo prematuro trava 30 dias (art. 576-A da IN 128/2022) |
| 30 a 49 | Frágil | Reunir prova, considerar justificação administrativa, avaliar prova testemunhal judicial |
| 0 a 29 | Inviável hoje | Reavaliar tese, informar o cliente com clareza |

## Bloqueios fatais

Se qualquer um estiver presente, a recomendação vira "não protocolar" independentemente do score.
Use o código do veto no relatório, para que o advogado saiba exatamente o que precisa ser resolvido
antes de qualquer outra diligência.

| Código | Veto | Fundamento | Saída possível |
|---|---|---|---|
| **V1** | Ausência de prova do óbito | art. 74, caput | Registro tardio, ação de justificação de óbito, morte presumida (art. 78) |
| **V2** | Perda da qualidade de segurado sem tese de recuperação | art. 15 c/c art. 74 | Reexame do CNIS, vínculos não registrados, doença anterior, Súmula 416/STJ, art. 102, §2º |
| **V3** | Existência de dependente de classe superior, para pleito das classes 2 e 3 | art. 16, §1º | Só cabe demonstrando exclusão do de classe superior. Renúncia é irrelevante; indignidade e inexistência, não |
| **V4** | Vínculo dependente de prova material, óbito posterior a 18/01/2019, sem qualquer documento contemporâneo | art. 16, §5º; Tema 371/TNU | Buscar prova material antes do protocolo. Força maior ou caso fortuito é exceção estreita |
| **V5** | Condenação transitada em julgado por homicídio doloso contra o segurado | art. 16, §7º; art. 74, §1º | Nenhuma, salvo absolutamente incapaz ou inimputável |
| **V6** | Concubinato impeditivo | Temas 526 e 529/STF | Provar separação de fato anterior (art. 1.723, §1º, do CC) |
| **V7** | Fraude ou simulação de casamento ou união estável reconhecida | art. 74, §2º | Nenhuma |

## A regra do prazo sobrepõe a faixa

Quando o óbito ocorreu há menos de 90 dias (ou 180 dias para filho menor de 16), a perda da
retroatividade costuma custar mais do que o risco de indeferimento, **porque o indeferimento é
recorrível e a DIB perdida não volta**.

Nessa situação, um IPC na faixa "instrução insuficiente" pode ainda assim recomendar protocolo
imediato. A condição é obrigatória: simule os dois cenários em números (ver o artefato de duas
datas de DER em `references/17-acumulacao-e-financeiro.md`) e registre o trade-off por escrito com
o cliente antes de protocolar.

A regra do prazo **não** vence veto. Veto continua bloqueando protocolo em qualquer hipótese.

## Priorize o plano de fechamento por ganho sobre esforço

Ordene as tarefas pela razão ganho/esforço, não pela ordem lógica do processo.

| # | Lacuna | Ação | Onde | Esforço | Prazo | Ganho IPC |
|---|---|---|---|---|---|---|
| 1 | Sem IR do falecido | Extrair declarações dos últimos 5 anos | e-CAC com procuração do espólio, ou exibição judicial | Baixo | 3 dias | +8 |
| 2 | Sem prova de atividade rural em 2021 e 2022 | Bloco de notas e notas de entrada | Cooperativa, laticínio, atravessador, secretaria da fazenda estadual | Médio | 15 dias | +7 |
| 3 | Testemunhas frágeis | Substituir parentes por vizinho de muro e comerciante local | Visita ao local | Médio | 10 dias | +5 |

Regra prática: se três tarefas de esforço baixo somam mais de 15 pontos de IPC, **espere e execute**
antes de protocolar, salvo prazo de DIB correndo.

## Recalibração após eventos

Recalcule o IPC sempre que:

- Chegar exigência do INSS. A carta revela o que o analista considerou insuficiente. Recalibre os
  blocos C e D conforme o texto.
- Sair indeferimento. Leia a fundamentação e converta cada motivo em lacuna
  (`references/11-fase-recursal.md`).
- Surgir concorrente habilitado. Recalcule o bloco C e refaça o mapa de rateio.
- Mudar entendimento vinculante aplicável, como o Tema 1271/STF.

Antes de entregar qualquer parecer ou peça, rode `references/14-red-team-inss.md`.

## Como reportar o IPC

Nunca entregue apenas o número. O formato correto é:

```
IPC 62/100 (faixa: instrução insuficiente)
A 13/15  B 11/25  C 18/25  D 12/20  E 8/15

Lacunas prioritárias:
1. B3 (0/5) Prorrogação do período de graça: obter comprovação de desemprego involuntário.
   Fontes: rescisão, seguro-desemprego, CAGED, prova testemunhal admitida pelo Tema 1.360/STJ.
   Ganho potencial: +5 e destrava o requisito central.
2. C2 (4/8) Falta um segundo documento dos 24 meses anteriores ao óbito.
   Fontes: plano de saúde, conta conjunta, comprovante de endereço, prontuário hospitalar.
   Ganho potencial: +4.
3. E1 (2/4) Base de cálculo estimada. Obter HISCRE e simular RMI.
   Ganho potencial: +2 e define a viabilidade econômica.

Com as três lacunas resolvidas: IPC projetado 73 (protocolável).
```

Sempre projete o IPC pós-diligência. É o dado que permite ao advogado decidir se vale o esforço.
