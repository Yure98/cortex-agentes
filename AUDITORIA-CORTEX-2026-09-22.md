# Auditoria crítica do Cortex — 22/09/2026

**Objeto:** pacote conversacional de nove skills; não foi auditado o repositório do SaaS. **Base examinada:** `Yure98/cortex-agentes`, commit `f4f349cd2c962691af42b64f8c2aea29a2ab09dc`, de 24/08/2026. Os caminhos e números de linha abaixo se referem a esse commit. Consulta externa realizada em 22/09/2026.

**Método e limites.** Leitura integral dos 172 arquivos versionados: seis na raiz, 11 comandos e 155 arquivos nas nove pastas de skills. Inclui os seis agentes do Estagiário, todos os scripts, referências e assets, os 39 documentos numerados da biblioteca PCD, seu índice e o manual PDF de três páginas. Na biblioteca extraída de PDFs, linhas literalmente repetidas foram deduplicadas apenas na visualização de leitura, sem remover conteúdo distinto nem alterar os originais. Não houve avaliação por amostragem de arquivos. Executei os cinco scripts Python, com casos sintéticos de controle e de fronteira, detalhados adiante. Não executei sessões reais no Claude Code/Cowork nem os instaladores contra uma instalação de advogado.

O caminho Windows `D:\Yure\cortex-agentes` não está montado neste ambiente; foi examinada uma cópia do GitHub. Os 44 PDFs de origem mencionados pela biblioteca, em `Downloads/pcd`, e a configuração particular `~/.peticionar/clientes/{slug}/config.json` não estão no repositório. A planilha externa vinculada no documento PCD 11 não pôde ser recuperada. Portanto, li integralmente os materiais distribuídos, mas **não certifico fidelidade aos PDFs ausentes, dados da planilha externa ou funcionamento da configuração particular**.

**Classificação:** P0 = pode alterar direito, valor, prazo, competência ou liberar peça bloqueada; P1 = compromete confiabilidade/uso; P2 = manutenção. “Confirmado” distingue constatação no código ou fonte recuperada; “não confirmado” não deve virar regra de produção. Ausência de mudança localizada significa resultado da pesquisa, não garantia de inexistência de ato posterior. Fontes comerciais descrevem funcionalidades anunciadas, não qualidade comprovada.

## 1. Resumo executivo

- **P0 — Corrigir o núcleo de cálculo antes de ampliar automação.** Há RMI PCD contraditória, idade progressiva com tempo mínimo errado, valores de 2025 rotulados como 2026 e erros executáveis em maternidade e pensão. Exemplos: remuneração de R$ 12.000 vira R$ 8.475,55 no script maternal; óbito de 2018 recebe prazo de 30 dias no script de pensão (§§ 2.2, 2.3, 2.6, 2.8).
- **P0 — O guardrail “nunca inventar” precisa alcançar a própria biblioteca.** Súmulas reais aparecem com conteúdo de outras teses; modelos têm números de artigos incompatíveis com o argumento. Buscar um precedente verdadeiro não resolve citar a tese errada (§§ 2.1, 2.5, 2.8, 2.9).
- **P0 — Fechar a passagem após revisão bloqueada.** O coordenador do Estagiário manda prosseguir após o segundo ciclo, embora o revisor mande bloquear. O limite de tentativas deve produzir pendências, jamais aprovação implícita (§ 2.1).
- **P0 — Separar acidente comum de acidente do trabalho antes de escolher prova e juízo.** A skill de auxílio-acidente direciona genericamente à Justiça Federal e dá peso excessivo ao nexo ocupacional. A seção de IR também conflita com orientação da Receita (§ 2.7).
- **P0 — Tornar dados ausentes realmente desconhecidos.** A pensão considera filtros não informados como atendidos; ambos os scores aceitam retirar item essencial e alcançar 100/100. Pontuação alta não substitui requisito legal nem justifica tutela (§ 2.8 e testes).
- **P1 — Há conhecimento recente valioso a preservar.** Tema 1.421/STJ, Tema 1.360/STJ, Súmula 63/TNU atualizada, Lei 15.415/2026 e Portaria Conjunta 15/2026 já foram incorporados em partes do pacote. Não recomendo reinvenção da voz ou remoção desses controles (§§ 2.6–2.8).
- **P1 — A vigilância normativa ainda não fecha o ciclo.** A IN 212/2026 consta do catálogo oficial após o corte de 30/07/2026; a Portaria Conjunta 66/2026 acrescenta tema relevante à pensão. Detalhes ainda não recuperados em fonte primária estão separados para validação, não apresentados como código pronto (§ 3.1).
- **P1 — Modernizar com estado do caso, fontes verificáveis e cálculos testados.** O diferencial competitivo não exige mais agentes: exige não perder fatos entre etapas, vincular cada afirmação ao documento e usar motores com versão normativa. O mercado já anuncia CNIS → cálculo → petição integrado (§§ 3.4–3.6).
- **Entrega desta rodada:** somente este relatório. Nenhuma skill, comando, instalador ou regra jurídica foi modificada. Quick wins estão especificados; mudanças estruturais aguardam revisão do titular (§ 4).

## 2. Achados por skill

### 2.1 `estagiario-peticoes`

**O que está bom.** A separação Coordenador → Pesquisador → Analista → Redator → Revisor → Diagramador → Drive divide responsabilidades reais. O pesquisador deve conferir decisões, o analista filtra aderência e o revisor compara a peça com o briefing. A saída com campos a preencher e a indicação de falha de pesquisa por tribunal são melhores que completar lacunas. Manter os seis papéis; isso não obriga executar seis processos em toda demanda.

**Atualização/correção jurídica.**

| Evidência atual | Verificação e fonte | Reescrita necessária |
|---|---|---|
| `agents/analista.md`, exemplo “Súmula 54”, linhas 72–81, atribui argumento sobre prova rural/CTPS e descarte de tese. | A Súmula 54/TNU trata do período de aferição da atividade rural para aposentadoria por idade; publicação em 07/05/2012. Erro de atribuição, não novidade de 2026. [S1] | Substituir exemplo jurídico por dado validado ou exemplo explicitamente fictício sem número de precedente. Não deixar o exemplo funcionar como fonte. |
| Hierarquia do analista prioriza TNU acima de STF/STJ; redator, linha 111, introduz automaticamente “jurisprudência ... pacífica”. | O CPC, art. 927, distingue espécies de precedentes e deveres de observância; não autoriza uma ordem global por utilidade local. Lei 13.105, de 16/03/2015. [S2] | Separar força vinculante, competência, aderência fática, atualidade e orientação local. Só qualificar como pacífica quando sustentado pela pesquisa. |
| Tipologia inclui “Recurso Ordinário (JEF → Turma Recursal)”. | O recurso contra sentença no sistema dos juizados é usualmente denominado inominado; conferir arts. 41–42 da Lei 9.099/1995, aplicáveis pelo art. 1º da Lei 10.259/2001. [S3] | Distinguir recurso inominado judicial de recurso ordinário ao CRPS. |

Não localizei atualização superveniente que imponha mudar os seis papéis. As atualizações materiais do benefício devem ser herdadas de fontes verificadas da skill especializada, e não de memória do redator. Para peças com atrasados, a EC 136, de 09/09/2025, impede repetir indistintamente a fórmula antiga da EC 113 até o pagamento: há disciplina própria dos requisitórios federais. [S4]

**Raciocínio e alucinação estrutural — P0.** `SKILL.md:135`: “Se APROVADO ou 2º ciclo encerrado: prossiga.” `agents/revisor.md:97`: reprovação no segundo ciclo deve virar `BLOQUEADO`. A segunda frase perde efeito diante da primeira. Solução proposta: apenas `APROVADO` libera diagramação de peça final; bloqueio entrega parecer de pendências, mantendo eventual minuta identificada como incompleta. Ressalvas cosméticas não podem conter falta de prova essencial, citação não localizada ou prazo desconhecido.

O briefing resumido a poucos fatos e a devolução do pesquisador sem campos obrigatórios para URL, data de consulta e localização da tese criam perda de contexto. Exigir “ao menos um precedente por argumento” também pressiona a preencher espaço quando a busca falha. A saída legítima é “não localizado”, com consultas realizadas; nem toda proposição legal exige precedente adicional.

**Compatibilidade.** Os arquivos em `skills/estagiario-peticoes/agents/` são instruções para agentes, não cadastro automático em `.claude/agents/`. Isso pode funcionar se o coordenador ler o arquivo e passar seu conteúdo ao agente genérico. Falta explicitar esse contrato. A documentação atual do Claude Code permite subagentes aninhados, com limite configurável; versões anteriores tiveram padrões diferentes. Portanto, **não é correto afirmar que o pesquisador jamais pode delegar**. É necessário declarar versão/configuração compatível e fallback sequencial. [T1]

**Experiência do advogado.** O pedido do tipo de peça e o aproveitamento de modelos do escritório são úteis. Contudo, `/setup-cliente` não existe no pacote; configuração particular, ferramenta Drive e identificação do escritório não têm percurso completo de instalação. Atribuições prévias a Sergipe/OAB-SE podem contaminar peça de outro escritório. Inferir tipo de peça, tribunal e fase dos autos já anexados, confirmando somente conflitos. Mostrar “Vou conferir fatos, pesquisar fundamentos e entregar minuta com pendências”; manter nomes dos agentes e arquivos no registro técnico. A saída HTML exige escape de dados, validação de caminhos e identificação clara do que realmente foi exportado.

### 2.2 `calculos-previdenciarios`

**O que está bom.** `SKILL.md` exige inventário de vínculos, tratamento de concomitância, memória de cálculo e distinção entre contribuição e carência. A restrição da conversão especial após a reforma e os parâmetros de pontos 93/103 e idade progressiva 59,5/64,5 para 2026 estão coerentes com a progressão da EC 103. [S5] São boas bases para um motor; não são um motor implementado.

**Divergências confirmadas — P0.** O arquivo de fórmulas em `references/` deve ser corrigido junto do `SKILL.md`, nunca isoladamente.

| Arquivo diz hoje | Regra confrontada, fonte e data | Alteração necessária |
|---|---|---|
| Referência: SM R$ 1.518 e teto R$ 8.157,41; `SKILL.md:294` chama R$ 1.518 de SM 2026 e R$ 379,50 de ¼. | Tabela oficial de contribuição de 2026: R$ 1.621 e R$ 8.475,55. [S6] | Tabela por competência; para 2026, ¼ = R$ 405,25. Não transformar esse limite em análise completa de BPC. |
| `SKILL.md:207`: rural anterior a 11/1991 conta como carência e tempo indiscriminadamente. | Lei 8.213/1991, art. 55, §2º, distingue carência; há tratamento específico da aposentadoria híbrida no Tema 1.007/STJ. [S7, S8] | Separar tempo rural, carência contributiva e hipótese híbrida; não transportar exceção para todas as aposentadorias. |
| Referência PCD aplica `70% + 1%` a toda aposentadoria PCD. | LC 142, de 08/05/2013, art. 8º: coeficientes distintos para tempo e idade. [S9] | Tempo: 100%; idade: 70% + 1 ponto por grupo de 12 contribuições, limitado. Separar discussão da média da do coeficiente. |
| Referência de aposentadoria especial de transição manda usar média integral sem coeficiente; incapacidade permanente usa excedente de 20 anos sem diferenciar sexo. | EC 103, de 12/11/2019, art. 26 e parágrafos. [S5] | Aplicar coeficiente e exceções de sexo/atividade corretamente; não confundir média de todos os salários com RMI de 100% da média. |
| Pedágio de 50% admite quem faltava “até 2 anos”; referência classifica carência masculina como 240 contribuições. | EC 103, arts. 17 e 19; tabela oficial separa carência e tempo. [S5, S10] | Testar limite estrito de mais de 28/33 anos em 13/11/2019; separar 20 anos de contribuição da carência de 180. |
| Referência pré-reforma diz coeficiente máximo com 30 anos para mulher/35 para homem; uso de fator limitado a apenas duas modalidades. | Lei 8.213, art. 50, e LC 142, art. 9º, I. [S7, S9] | Corrigir grupos de contribuições do coeficiente e permitir fator favorável nas hipóteses legais, inclusive PCD. |

**Robustez.** Não há `scripts/` nesta skill. Correção dos salários “até hoje”, escolha facultativa de corrigir ou não e uso de “tábua interna” não entregue inviabilizam um cálculo judicial auditável. DER/DIB, competência dos índices, versão da tábua de mortalidade e regra de descarte devem ser entradas identificadas. Não se deve apresentar dois métodos, um sem correção, como equivalentes jurídicos. O art. 26 da EC 103 sustenta a necessidade de cálculo versionado; tabela IBGE e índices aplicáveis ainda precisam ser anexados/validados antes de implementação.

O fator previdenciário escrito é reconhecível, mas faltam ajustes legais e dados documentados para afirmar que a execução está certa. A recomendação é extrair cronologia contributiva para estrutura validada, calcular com script, devolver memória e rejeitar resultado quando faltar parâmetro. Determinismo sem testes apenas repete um erro com precisão.

**Consistência e UX.** Há 21 perguntas antes da produção principal, muitas já respondidas pelo CNIS ou irrelevantes ao benefício. A primeira entrega deve ser tabela extraída e lista de lacunas, seguida de até três perguntas que alterem resultado. `PREC-FBR` aparece como problema de mínimo, embora a referência oficial o associe à validação do facultativo de baixa renda. [S11] A `description` ampla, com “INSS”, “aposentadoria” e anexação de PDF, compete com quase todo o pacote. Remeter análise preliminar ao Raio-X e decisão econômica ao Decisor. Não encontrei nova lei de 2026 que substitua em bloco as transições da EC 103; os defeitos aqui são principalmente aplicação errada e parâmetros desatualizados, além da IN 212 pendente de conferência (§ 3.1).

**Jurisprudência recente que falta ao módulo.** O Tema 1.307/STJ, julgado em 07/05/2026 e publicado em 20/05/2026, admite especialidade por penosidade de motoristas/cobradores nas condições da tese, mediante perícia individualizada. Acrescentar caminho de investigação de prova, nunca conversão automática pela profissão. [S37] O Tema 1.300/STF, decidido em dezembro de 2025 e divulgado pelo MPS em 30/03/2026, confirma a constitucionalidade do cálculo de incapacidade permanente pós-reforma: não oferecer integralidade por doença grave como regra geral. [S38] O Tema 384/TNU, julgado em 06/08/2026, afeta efeitos financeiros de complementações de alíquotas reduzidas; incorporar condições de instrução e colaboração administrativa, sem confundir complementação com indenização de período não recolhido. [S39]

### 2.3 `decisor-aposentadoria`

**O que está bom.** Separar “posso me aposentar?” de “qual opção compensa?” é um diferencial. Comparação de recebimentos adiados, investimento contributivo, VPL e prazo de recuperação torna explícito o custo de esperar. O modelo não deve ser descartado: deve receber cenários juridicamente elegíveis e valores calculados por motor validado.

**P0 — Premissas legais na tabela.** `references/modelos-decisao.md:19` atribui à idade progressiva 15 anos para mulher/20 para homem. O art. 16 da EC 103 exige 30/35 nessa transição; trata-se de erro existente, não alteração de 2026. Na linha 20 repete-se o limite inclusivo do pedágio de 50%. [S5] A linha PCD associa idade ao grau e nega fator: na modalidade por idade, 55/60 independem do grau, e fator favorável é admitido. [S9] Reescrever a tabela com modalidade, data, requisitos e dependência do cálculo; não “corrigir” apenas o texto da recomendação final.

**P1 — Modelo econômico incompleto.** O ponto de equilíbrio precisa tratar diferença de RMI nula ou negativa: nesse caso não há payback finito pelo ganho mensal proposto. Incluir 13º de modo consistente nos dois cenários, despesas contributivas marginais efetivas, horizonte em meses e sensibilidade da taxa. Se a pessoa continuará empregada em ambos, não imputar toda contribuição futura só à espera. A equivalência de 0,5% ao mês com cerca de 6% ao ano é aproximação: efetivamente corresponde a aproximadamente 6,17% compostos. Declarar taxa real/nominal e forma de atualização.

Condição de saúde não autoriza converter expectativa individual de vida em certeza. Apresentar horizontes alternativos escolhidos com o advogado; não diagnóstico. Sem scripts, as fórmulas podem ser úteis como especificação, mas não garantem simulação reproduzível. Exigir validação de elegibilidade mesmo quando o usuário colar resultado de outra skill: dado colado não prova cálculo validado.

**Atualidade, consistência e experiência.** Os valores progressivos de idade de 2026 estão corretos; não localizei regra posterior que substitua a estrutura de comparação. Falta data de revisão normativa e origem da RMI. O encaminhamento a partir de cálculos é sensato; a abertura deve aproveitar os cenários existentes e pedir apenas objetivos, necessidade de renda e horizonte. Score probatório completo seria redundante aqui; melhor um bloqueio “cenário sem elegibilidade/RMI validada não recebe recomendação conclusiva”. Sua descrição é mais orientada a decisão que a palavra solta “aposentadoria”; o conflito principal vem da amplitude de Cálculos.

### 2.4 `raio-x-cnis`

**O que está bom.** O escopo de triagem, o aviso de valores aproximados e a ordem de marcar indicador desconhecido como “a verificar” (`SKILL.md:53–54`) são adequados. Não é necessário impor todos os portões de peticionamento a uma leitura inicial de CNIS.

**Atualização e correções.** `references/indicadores-cnis.md:42` chama 15 anos/20 anos de carência. Separar contagem de competências e tempo mínimo; a tabela do INSS distingue 180 contribuições dos requisitos temporais. [S10] No glossário, não agrupar `IREC` e `IREC-INDPEND` como “indício de irregularidade”, nem tratar códigos genéricos como significado oficial universal. Para `PEXT` e `PREC-FBR`, há definições administrativas específicas em documentação reproduzida pelo TCU. [S11] Reescrever a partir da legenda do próprio extrato e de tabela oficial versionada, preservando “não reconhecido → conferir”. A expansão exata de todos os demais códigos, incluindo `PADV`, permanece pendente de validação da versão de extrato; não proponho substituição por palpite.

A IN 212/2026 é relevante para a revisão do tratamento de CNIS, conforme pesquisa descrita no § 3.1; não foi possível confirmar integralmente seu impacto em fonte primária recuperada. Não localizei nova súmula específica que exija alterar o propósito desta triagem.

**Atualização de alto impacto na triagem de especialidade.** `references/indicadores-cnis.md:51` inclui “vigilante” entre grandes oportunidades de conversão sem ressalva. O STF decidiu o Tema 1.209, com acórdão de mérito publicado em 04/03/2026, afastando especialidade baseada na atividade de vigilante/perigo, com ou sem arma. [S40] Reescrever para não prometer enquadramento por profissão; distinguir eventual exposição a outro agente, período e situação processual, verificando embargos/modulação no caso. A pesquisa encontrou também Tema 1.307/STJ para motoristas (§ 2.2), hipótese de investigação técnica, não presunção ocupacional.

**Raciocínio/UX.** `SKILL.md:49–51` manda somar períodos e estimar contribuições sem script. Anos aproximados de vínculo não equivalem a carência: concomitância, recolhimento em atraso, pendência e competência inferior ao mínimo precisam de estados próprios. Exigir documento/página/linha para cada vínculo e separar “extraído”, “ilegível”, “inferido” e “validado”. Em PDF escaneado, solicitar imagem melhor somente das páginas afetadas. O semáforo vermelho “inviável” deve significar inviável com os dados disponíveis, sem excluir outras hipóteses de benefício. Perguntar nascimento/sexo/data de corte somente quando ausentes ou conflitantes; entregar primeiro mapa legível do extrato. A data de corte do caso mencionada na linha 42 não é data de atualização normativa da skill.

### 2.5 `recurso-inss`

**O que está bom.** Começar pela decisão/indeferimento e construir resposta por motivo concreto evita recurso genérico. A orientação de usar `[VERIFICAR enunciado CRPS aplicável]` em vez de inventar (`references/motivos-indeferimento.md:181`) deve ser preservada. Prazo, fundamento da negativa e documento faltante são os três dados iniciais certos.

**P0 — Referências incorretas.** No mesmo arquivo, linhas 62–63 e 103: Súmula 77/TNU não diz que incapacidade total/permanente é dispensável; 78 não trata genericamente de reabilitação; 68 não é tese de ruído/EPI. Correspondem, respectivamente, à análise de condições pessoais na ausência de incapacidade, HIV e laudo não contemporâneo. Publicações: 06/09/2013, 17/09/2014 e 24/09/2012. [S1] Reescrever as três linhas após vincular tese correta ao motivo de indeferimento; não basta trocar número de súmula automaticamente.

`references/motivos-indeferimento.md:170` ordena “CRPS > TNU > STJ > STF”. Substituir por matriz de vinculação e aplicabilidade; a utilidade administrativa do CRPS não o coloca acima de controle constitucional. [S2] A referência ao art. 690 da IN 128 para reafirmação da DER (linha 159) exige conferência: não foi confirmada nesta auditoria e não deve permanecer como citação pronta.

**Atualização confirmada.** A generalização da recuperação de carência pela metade (linha 39), se aplicada à maternidade, conflita com o cumprimento das ADIs 2.110/2.111 pela IN 188, de 08/07/2025. [S12] Deve haver exceção expressa e remissão ao fluxo maternal. O regimento atual localizado é a Portaria MPS 125, de 26/01/2026, com alteração pela Portaria 235, de 03/02/2026; o portal disponibiliza compilação. [S13] O recurso genérico precisa ler a versão vigente, identificar órgão competente e hipóteses de cabimento/alçada, em vez de pressupor uma sequência recursal universal. IN 203/208 e exigências posteriores também afetam a decisão entre recorrer e renovar requerimento (§ 3.1).

**Robustez, consistência e UX.** Falta portão equivalente ao revisor do Estagiário para tempestividade, ataque a cada fundamento e prova relacionada. Deve ser checklist curto, não IPC de 100 pontos. Se já há a carta, extrair data de ciência e fundamento antes de perguntar novamente; distinguir data impressa da ciência efetiva. Prometer Word/PDF exige ferramenta de exportação disponível; sem ela, entregar texto editável identificado. Não há script nesta skill. Abertura e descrição sobrepõem-se a recursos específicos de maternidade/pensão/auxílio; a especialidade deve conservar contexto e chamar o módulo recursal, não reiniciar a entrevista.

**Atualização recursal específica.** Tema 1.157/STJ, divulgado oficialmente em 31/07/2026, admite revisão administrativa de benefício por incapacidade concedido judicialmente, com devido processo, perícia, notificação e defesa. [S41] O módulo deve perguntar origem judicial e procedimento de revisão, sem sustentar impossibilidade absoluta de cessação administrativa. Tema 1.124/STJ, julgado em 08/10/2025, também exige distinguir instrução administrativa, colaboração do INSS e prova apresentada em juízo ao tratar de interesse de agir e efeitos financeiros. [S42] Esses controles devem alcançar o Estagiário e as fases judiciais dos benefícios.

### 2.6 `cortex-maternidade`

**O que está bom e atualizado.** O corte de 30/07/2026 é explícito. Classificação U/R/H/D, entrevista guiada, distinção entre norma e tese, referências permitidas e varredura de passivo são ativos. A Lei 15.415, de 25/05/2026, publicada em 26/05, de fato acrescentou o art. 73-A: prazo de decisão e concessão provisória nos pagamentos diretos do INSS. [S14] A Lei 15.222, de 29/09/2025, também consta corretamente como base da extensão hospitalar. [S15] Não remover essas novidades sob suposição de que sejam inexistentes.

**Divergências jurídicas e implementacionais.**

| Arquivo/conduta atual | Confronto | Reescrita necessária |
|---|---|---|
| `scripts/diagnostico.py:234–300` calcula remuneração integral, depois aplica teto RGPS a todas as categorias. | Empregada/avulsa têm disciplina específica, inclusive limite constitucional próprio, não teto contributivo ordinário. [S16] | Teto por categoria e regime; teste de R$ 12.000 deve preservar R$ 12.000 no exemplo. |
| Whitelist/mapa usa art. 73, II, para hipóteses de CI/adoção; referência 09 e script não têm o mesmo divisor. | Art. 73, II, refere-se à segurada especial; III disciplina as demais categorias ali abrangidas, com divisor 12 e janela máxima de 15 meses. [S7] | Corrigir inciso e unificar cálculo; adoção não define sozinha categoria de renda. |
| `calcular_periodo_graca`, linhas 160–194, comentário fala segundo mês, código escolhe o seguinte. | Contradição interna reproduzida: última competência 01/2025 gera limite 15/02/2026. Regra de perda está no art. 15, §4º, e no regulamento. [S7, S17] | Usar competência, prazo legal de recolhimento e dia de perda; distinguir último dia protegido do dia da perda. Validar calendário bancário. |
| Mesmo cálculo prorroga facultativa por desemprego e considera contribuições totais como prova de sequência sem perda. | A extensão por desemprego não é extensão genérica dos seis meses do facultativo; o histórico sem perda é dado separado. [S17] | Categoria/períodos e prova como entradas; ausência não vira `False` nem zero factual. |
| `calcular_prescricao` usa `5*365+1` e declara “todas as parcelas”. | Prescrição de prestações não pode ser decidida só pela data do parto; suspensão também precisa de cronologia válida. [S7; S1, Súmula 74] | Calendário civil por parcela, ciência, suspensão e situações pessoais; resultado incompleto quando faltarem datas. |
| `calcular_duracao` explica desconto pré-parto, mas calcula alta + 120; RMI mantém total de 120 dias. | Lei 15.222/2025 exige considerar recebimento anterior e extensão por internação relacionada ao parto. [S15] | Adicionar início de pagamento, altas da mãe/bebê, nexo e dias anteriores; uma mesma duração deve alimentar valor e DCB. |

**P0 — Dados e decisões.** `Caso.de_dict` assume contribuinte individual, utiliza parâmetros de 2026 mesmo em fato antigo e converte a string `"false"` em verdadeiro. A lista de salários não contém competências: o programa não verifica janela de 15 meses. O art. 73-A usa o relógio do sistema e não afasta a sugestão de implementação quando já há decisão; precisa de data de referência e estado processual. A frase de confiança absoluta no script deve ser substituída por “cálculo reproduzível, sujeito às entradas e regras validadas”.

**Rural e pós-ADI.** A eliminação de carência está confirmada no INSS. [S12] Não se deve, porém, apagar toda referência a janela probatória rural como se fosse necessariamente carência: a Resolução CRPS 13/2026/Enunciado 19, reproduzida em fonte secundária, distingue atividade dentro da janela de exercício contínuo durante ela. O texto oficial dessa resolução não foi recuperado; a interpretação específica permanece **não confirmada para alteração**. Revisar referências 03/11 para evitar que “12 meses” ou “10 meses” virem exigência de duração mínima reintroduzida por linguagem ambígua. Afirmação categórica de que boia-fria nunca pode receber tratamento probatório rural também exige revisão individual da tese.

**Consistência/UX.** A abertura obrigatória urbano/rural pode repetir fato já informado; o fluxo de nove fases não deve obrigar recurso se o pedido ainda nem foi feito. Entregar diagnóstico e próxima providência conforme a fase. Corrigir remissão a `checklist-documental-urbano` para o asset existente `assets/checklists-documentais.md` e o nome de pasta `salario-maternidade` no README local. “Fase 3”, whitelist e caminhos devem ficar internos. “Litispendência” com recurso administrativo na referência 11 precisa ser distinguida de renúncia/desistência administrativa por ação de mesmo objeto; não são o mesmo instituto. A regra de atualização monetária genérica também precisa do recorte da EC 136/2025. [S4]

**Novidade após o corte:** a IN 212/2026 é confirmada como alteração da IN 128; efeitos específicos ainda pendentes (§ 3.1). Não encontrei revogação posterior confirmada do art. 73-A ou da extensão hospitalar.

### 2.7 `auxilio-acidente`

**O que está bom e atualizado.** O pacote distingue sequela de incapacidade total, dá relevância ao trabalho habitual, não torna CAT requisito absoluto e inclui objeções do INSS e benefícios conexos. A Portaria Conjunta MPS/INSS 15, de 23/03/2026, publicada em 24/03, realmente trata de análise documental do auxílio-acidente; não deve ser confundida com a Portaria 13 do Atestmed. Existência e objeto confirmados pelo CJF. [S18] A transcrição integral recuperada em fonte secundária descreve etapa documental anterior à eventual perícia, não substituição indistinta desta. [S19]

**P0 — Competência, escopo e tributação.**

| Evidência | Confronto e fonte | Reescrita |
|---|---|---|
| `references/13-fase-judicial.md:7–8`: ação tramita na Justiça Federal/JEF conforme valor. | A competência depende da natureza da lide; concessão fundada em acidente do trabalho exige ramo estadual, observada a delimitação jurisprudencial. CF, art. 109, I; STJ confirma distinções, inclusive em 2026. [S20] | Primeiro identificar acidente comum/ocupacional e objeto; só depois competência e rito. Espelhar em modelos e description. |
| Abertura e score concentram CAT/NTEP/nexo ocupacional, descrição destaca B94. | O benefício também abrange acidente de qualquer natureza; a página do INSS não o limita a trabalho. [S21] | Criar percurso B36/acidente comum; ausência de CAT não pode reduzir prontidão como se fosse prova necessária nessa hipótese. |
| `references/09-calculo-e-valor.md:115–129` nega isenção e trata recebimentos como tributáveis. | Manual da Receita inclui auxílio-acidente entre rendimentos isentos/não tributáveis. [S22] | Corrigir orientação, separar isenção própria do benefício da isenção de aposentadoria por moléstia grave. |
| EC 103, art. 26, §3º, II, é citado como vedação de acumulação. | Esse dispositivo trata de cálculo de incapacidade permanente de origem laboral. [S5] | Remeter vedação/exceção à base efetivamente aplicável; não manter remissão apenas porque a conclusão geral parece correta. |

**Jurisprudência e atualização.** Súmula 88/TNU está corretamente ligada à redução leve; a 89 exige que exista redução/maior esforço. [S1] A data de julgamento do Tema 416 que aparece em referência deve ser corrigida: STJ registra 25/08/2010, publicação em 08/09/2010, não 2018. [S23] A tese de contribuinte individual em período de graça já é rotulada emergente: preservar o rótulo e exigir acórdão completo; não localizei confirmação primária suficiente da decisão de TRF4 de julho de 2026 mencionada. A IN 212 demanda conferência adicional sobre o art. 354 (§ 3.1).

Há conflito de datas nas próprias fontes oficiais sobre empregado doméstico: página de serviço informa 01/06/2015, texto indexado da IN menciona 02/06/2015. [S21, S17] Não substituir por outubro de 2015; a divergência de um dia exige cotejo da vigência da LC 150. Também revisar referências rurais antigas a embarcação de seis toneladas; não publicar número substituto sem validar regra e período.

**Scripts.** O cálculo simples de 50% está correto para a entrada contemporânea válida testada: SB R$ 3.000 → R$ 1.500, sem piso artificial. O programa, porém, aceita SB negativo e retorna R$ -50. Não valida finitude, data-base ou série histórica. `prazos` soma dias, mas não é calendário completo de recurso com expediente/suspensões. O score usa metade do peso para todo “parcial”, não necessariamente os pontos intermediários da rubrica, e aceita `na` sem justificativa nem restrição de requisito essencial. Não confundir pontuação documental com probabilidade de êxito.

**Experiência e consistência.** A entrevista condicionada à categoria é útil; a pergunta sobre natureza do acidente deve preceder CAT/NTEP. Inferir vínculo, função e datas do documento já enviado e perguntar somente lacunas. “Red team” pode aparecer ao advogado como “objeções prováveis do INSS”; o conceito jurídico permanece. Os aliases com acento devem continuar funcionando, com uma única fonte canônica (§ 3.3).

### 2.8 `pensao-por-morte`

**O que está bom e atualizado.** O óbito como eixo temporal, entrevistas urbana/rural, classes de dependentes, dossiê de prova, objeções e conexos formam o conjunto mais completo de operação. Distingue corretamente ausência de carência dos 18 recolhimentos relacionados à duração. O Tema 1.421/STJ, julgado em 10/06/2026, está incorporado e foi confirmado no STJ; a habilidade também já registra a atualização da Súmula 63/TNU e o Tema 1.360/STJ, julgado em 11/03/2026. [S24, S1, S25] A Lei 15.108/2025 aparece na referência jurisprudencial: não é correto apontá-la como inteiramente ausente.

**P0 — Divergências.**

| Arquivo diz hoje | Confronto/fonte | Alteração |
|---|---|---|
| `scripts/calculadora_pensao.py:199–201`: todo óbito antes da MP 871 usa 30 dias. | Lei 13.183, de 04/11/2015, já havia fixado 90 dias. [S26] | Tabela histórica por vigência; óbito em 01/01/2018 e DER em 01/03/2018 deve retroagir ao óbito no caso adulto testado. |
| `references/06-qualidade-segurado.md` inclui auxílio-acidente na manutenção ilimitada. | Art. 15, I, tem exceção ao auxílio-acidente desde a Lei 13.846/2019. [S7] | Retirar generalização e tratar regra temporal do caso. |
| Referência de dependentes e score C4 exigem invalidez anterior aos 21 anos. | STJ distingue invalidez anterior ao óbito de anterioridade à maioridade. Fonte oficial de 16/03/2023 reafirma isso. [S27] | Não eliminar filho maior inválido apenas porque invalidez surgiu após 21 anos; avaliar dependência e controvérsia específica. |
| Script e referências invocam art. 79 como dispositivo vigente para prescrição. | Art. 79 foi revogado pela Lei 13.846/2019. [S7] | Reconstruir fundamento atual e temporal, sem concluir que a revogação elimina toda proteção civil do incapaz. |
| Referência rural atribui boia-fria à Súmula 73/TNU e documentos familiares à 30; 34 é parafraseada de forma ampla. | Os números não correspondem às proposições apresentadas na lista oficial. [S1] | Conferir cada tese/número e eliminar citação incorreta de modelos. |
| `references/10-fase-administrativa.md` usa art. 41-A, §5º, como prazo de decisão de 30 dias. | Não confundir primeiro pagamento com prazo de conclusão decisória; cotejar Lei 8.213 e Lei 9.784, art. 49. [S7, S28] | Identificar evento inicial, tipo de prazo e hipótese, sem um relógio universal. |

**Scripts — alucinação por default.** `cmd_duracao:159–160` usa `is None or ...`: sem contribuições ou tempo de união, imprime **ATENDIDO**. Isso viola diretamente a regra “não inventar”. Ausência deve bloquear conclusão ou gerar cenários condicionais. O mesmo comando limita todo dia de término a 28; para óbito em 31/01/2026 e duração de dez anos, retorna 28/01/2036. Quatro meses são aproximados por 120 dias. Usar aritmética civil de meses/anos e tratar 29/02 especificamente.

`cmd_rmi` assume regime novo se faltar óbito, aceita zero dependentes/base negativa, aplica piso ao valor atual mas não à projeção de cessação de cotas e não sabe se o dependente inválido permanece. No teste, pensão de R$ 1.621 com dois dependentes vira projeção de R$ 972,60 com um, sem reaplicar a regra de piso usada pelo próprio programa. A acumulação por faixas, por outro lado, funcionou no controle R$ 6.000 + R$ 4.000 → R$ 8.896,80, SM R$ 1.621; falta validar se a combinação é juridicamente acumulável e o regime temporal. [S5]

O mapa histórico generaliza “100%” e vitaliciedade para todo passado anterior às mudanças recentes. Casos antigos precisam de faixas próprias, inclusive tratamento da MP 664/2014, sem presumir que um único corte em junho de 2015 resolve o período. A conclusão exata de cada hipótese histórica fica condicionada à legislação vigente no óbito.

**Score.** O script tem cinco bloqueios, enquanto a rubrica documental contém outras condições impeditivas. A certidão de óbito (`A1`) pode ser marcada `na`; com os demais itens cheios e sem objeto `bloqueios`, o programa retorna 100 e recomenda protocolar/judicializar com tutela. Também divergem os pesos parciais e o destino da redistribuição de itens rurais não aplicáveis. Corrigir contrato, pesos e bloqueios juntos. Urgência processual pode justificar providência conservatória mesmo com documentação incompleta; o score não deve consumir prazo nem ordenar tutela automaticamente.

**Novidade localizada.** Portaria Conjunta PRES/INSS/SRGPS/MPS 66, de 14/07/2026, consta do catálogo oficial para avaliação da deficiência em pensão/auxílio-reclusão, mas não foi localizada no conteúdo da skill. [S29] Acrescentar verificação do instrumento aplicável; detalhes operacionais aguardam íntegra oficial. Tema 1.341/STJ: a página consultada identifica controvérsia do filho maior inválido com renda própria, sem tese final recuperada nesta auditoria. Manter acompanhamento; não converter afetação em tese julgada. [S30]

**UX e consistência.** O questionário condicionado e o painel são úteis. Devem aproveitar certidão, CNIS e informação de dependentes já recebidos. Perguntar data da ciência antes de entrevista longa em recurso. Abertura não deve forçar toda operação de 100 pontos para uma dúvida pontual. A referência a SPVAT em conexos pede revisão de vigência antes de sugerir benefício; não foi validada nesta rodada para uso positivo. Aplicar também recorte da EC 136 nos atrasados. [S4]

### 2.9 `aposentadoria-pcd`

**O que está bom.** A distinção deficiência/incapacidade, centralidade da DID, análise por atividade do IF-BrA, provas de barreiras e impugnação específica do laudo são adequadas. A biblioteca cobre administrativo, judicial, quesitos, réplica, revisão e complementação MEI; não é só uma descrição de agente. O fluxo pode produzir peça ou diagnóstico sem obrigar responder todas as 205 perguntas. Preservar essa flexibilidade.

**P0 — RMI contraditória.** `SKILL.md:49` afirma “100% da média” sem distinguir as modalidades. A LC 142/2013, art. 8º, diferencia tempo de contribuição e idade; quinze grupos anuais na modalidade por idade resultam em 85% do salário de benefício, antes de limites e fator favorável. [S9] A skill de Cálculos erra no sentido inverso (§ 2.2). Criar especificação única para coeficiente; o debate sobre média pós-EC 103 deve ser tratado separadamente e validado, não resolvido por copiar a fórmula de uma skill para outra.

**P0 — Entrevista orientada ao resultado.** `references/biblioteca/06-roteiro-perguntas-visao-monocular.md:10` declara objetivo de reduzir pontuação de 7.950 para até 7.584. `references/roteiros-atendimento.md:67` orienta “evitando 100 em excesso”; há respostas sugeridas e faixas-alvo. O problema não é defender repercussões funcionais reais: é selecionar o grau antes de apurar os fatos. Reescrever para pergunta aberta → resposta literal → exemplo cotidiano → documento → pontuação tecnicamente justificada, aceitando 100 quando os fatos o sustentam. Modelos de respostas devem ser exemplos didáticos, nunca respostas imputadas ao cliente. Isso fortalece o guardrail do produto, sem eliminar atuação advocatícia.

**P0/P1 — IF-BrA e biblioteca.**

- A metodologia deve explicitar as duas avaliações e a soma, sem comparar a soma de apenas 41 respostas com faixas calculadas para a combinação. A fonte normativa do IF-BrA é a Portaria Interministerial de 27/01/2014; o Formulário 4 deve ser aplicado integralmente. A transcrição consultada distingue nota 75 em todas as atividades relevantes de nota 75 isolada. A metodologia resumida e o modelo 07 não estão suficientemente alinhados nesse ponto. Validar íntegra e implementar casos de fronteira antes de automatizar Fuzzy. [S31]
- `biblioteca/10-inicial-grau-moderado-visual.md:37,87` usa 6.450 pontos em peça de grau moderado, mas a própria tabela de `roteiros-atendimento.md:5` coloca 6.355–7.584 no leve. Contradição interna confirmada. Não alterar a pontuação do caso para encaixar no título: verificar laudos e corrigir classificação ou exemplo.
- `biblioteca/25-replica-unico-ponto-didef.md` associa artigos 396 e 391 do CPC a fundamentos processuais que não correspondem ao conteúdo desses dispositivos. Conferir, conforme a finalidade, arts. 350–351; jamais trocar automaticamente sem ler a peça. [S2]
- `biblioteca/27-revisao-judicial-sem-pericia.md` reproduz redação ampla de decadência para indeferimento/cessação e contém referência a “LC 143”. A ADI 6.096, julgada em sessão encerrada em 09/10/2020, impede usar aquela ampliação como regra atual. [S32] Corrigir a referência legal e o recorte da pretensão.
- `biblioteca/30-tese-tempo-pcd-mais-tempo-especial.md` contém “1,32%” onde descreve fator de conversão: distinguir multiplicador de percentual e conferir tabela/período. A aplicação conjunta no mesmo período tem limite no art. 10 da LC 142. [S9]
- Modelos 34/37 usam Tema 378/TNU. A tese localizada trata de BPC e visão monocular, não transforma diretamente todo pedido da LC 142 em hipótese idêntica. Identificar analogia e fundamento próprio, em vez de anunciar vinculação fora do objeto. [S33]

**Atualização normativa.** Não localizei substituição confirmada da LC 142 ou novo coeficiente de 2026. Portaria 66/2026 tem objeto de dependentes em pensão/auxílio-reclusão; não deve ser importada automaticamente como alteração da aposentadoria PCD. [S29] Resolução CNJ 673/2026 foi localizada em publicação oficial, mas seu alcance específico precisa ser conferido antes de aplicar o instrumento judicial à LC 142. [S18]

**Controvérsia confirmada, não tese resolvida.** O Tema 389/TNU foi afetado em 12/02/2026 e consta “Em Julgamento”, sem tese preenchida na ficha consultada: discute precisamente média da PCD após a EC 103. [S43] Acrescentar esse estado ao cálculo e separar cenário administrativo de tese judicial, preservando a correção certa do coeficiente. O modelo `biblioteca/31-complementacao-mei.md` deve ser confrontado com o Tema 384/TNU, julgado em 06/08/2026: adiar complementação sem considerar exigência regular e encerramento administrativo pode alterar efeitos financeiros. [S39] Os modelos 09 e 27 já mencionam Tema 1.124/STJ, mas a frase de afastamento automático deve ser substituída pela análise das hipóteses da tese e dos documentos efetivamente apresentados. [S42]

**Consistência/UX.** Há vários aliases anunciados no README/manual sem correspondência demonstrada em arquivos de comando; escrever `/pcd` dentro da descrição não registra um comando. [T2] As 205 perguntas são banco de aprofundamento, não onboarding. Usar inicialmente benefício pretendido, histórico funcional/DID, prova disponível e fase do caso. Não mostrar nome de arquivo ao advogado como se fosse ato processual. O documento 04 tem bytes inválidos em UTF-8, sobretudo em símbolos; precisa normalização preservando texto. Há dados individualizantes, NB e históricos de casos na biblioteca: produzir versões neutras e confirmar autorização/proveniência dos materiais antes de redistribuir. Isso é constatação documental; não é conclusão de infração ou de falta de autorização.

## 3. Achados transversais

### 3.1 Vigilância normativa: confirmar a fonte não é apenas encontrar o número

| Assunto | Estado constatado em 22/09/2026 | Impacto no pacote |
|---|---|---|
| IN PRES/INSS 212, de 06/08/2026 | Catálogo oficial confirma alteração da IN 128; página oficial de 2022 identifica publicação em 11/08/2026, DOU extra, pp. 8–9. A íntegra oficial não foi recuperada pelas rotas tentadas. [S34] | Não aparece nos arquivos auditados. Prioridade alta de conferência para todas as skills que aplicam a IN 128. Não elevar automaticamente a data de corte. |
| Possíveis efeitos da IN 212 | Fonte secundária de 21/08/2026 aponta arts. 184, 216, 223, 354, 369-A, 566, 574 e 600, entre outros. **Detalhes ainda não confirmados em íntegra primária nesta auditoria.** [S35] | Conferir graça, contribuições reduzidas/CNIS, rol de sequelas, filho póstumo e exigências. Só então alterar fluxos, calculadoras e modelos. Não apresentar como “novos direitos” todas as mudanças redacionais. |
| IN 203, de 22/04/2026, e IN 208, de 19/05/2026 | Existência confirmada no catálogo; reprodução da IN 208 recuperada contém art. 576-A e exceções para revisão e benefícios por incapacidade. [S34, S36] | Maternidade/pensão já consideram restrição a novo requerimento; Recurso deve comparar recurso, revisão e novo pedido. Conferir as exceções na consolidação oficial antes de implementar regra comum. |
| Regimento CRPS | Portaria 125/2026 e alteração 235/2026 constam do portal oficial. [S13] | Usar compilação datada e verificar rito/cabimento; a citação genérica “regimento vigente” não entrega rastreabilidade. |
| Portaria Conjunta 66, de 14/07/2026 | Objeto confirmado em catálogo oficial: instrumento para deficiência em pensão/auxílio-reclusão. [S29] | Lacuna específica de pensão. Não confundir com mudança de aposentadoria PCD. |
| EC 136, de 09/09/2025 | Altera atualização dos requisitórios federais, com IPCA/juros e limite relacionado à Selic. [S4] | Separar conhecimento/liquidação/requisitório; revisar modelos de pedidos que estendem Selic indiscriminadamente até pagamento. |
| Valores de 2026 | SM R$ 1.621 e teto R$ 8.475,55 confirmados. [S6] | Cálculos está atrasado; scripts especializados têm valores atuais, mas falta seleção histórica por data. |
| Jurisprudência recente já incorporada | Tema 1.421 e 1.360/STJ; atualização da Súmula 63/TNU. [S24, S25, S1] | Preservar; acrescentar URL oficial, datas e alcance. Não reclassificar como “pendente” tese já julgada. |
| Jurisprudência adicional relevante | Temas 1.307/STJ, 1.209/STF e 384/TNU em 2026; 389/TNU ainda em julgamento. [S37, S39, S40, S43] | Atualizar especialidade, complementação e estado da controvérsia sobre média PCD; propagar aos cenários do Decisor sem torná-lo fonte jurídica autônoma. |

**Modelo proposto de registro de fonte:** identificador, órgão, espécie, número, dispositivo/tese, URL oficial, data do ato, publicação, início/fim de vigência, status processual, alcance, data de consulta e responsável pela validação. A versão do benefício é determinada pelo fato relevante (óbito, DER/DIB, competência etc.), não só pela data em que a skill foi escrita. `[CONFERIR]` deve bloquear a conclusão que depende daquela informação, sem bloquear tarefas independentes como organizar provas.

Uma lista de fontes permitidas protege contra referências inventadas, mas fica perigosa se perpetua erro da própria lista. Verificar separadamente: **existência da fonte → correspondência da proposição → vigência → aplicação ao caso**. Se os quatro itens não estiverem completos, não chamar a citação de validada.

### 3.2 Matriz de consistência

Todos os nove `name` correspondem às respectivas pastas. A divergência principal não é o nome, mas a licença, extensão das descriptions e presença de mecanismos de controle.

| Skill | `license` | Corte normativo explícito | Painel/controle existente | Avaliação da diferença |
|---|---|---|---|---|
| Estagiário | Proprietário — Cortex / Vértika | Não | Briefing, revisão, campos pendentes | Bom controle editorial; corrigir bloqueio e fonte por afirmação. |
| Cálculos | Mesmo texto | Não | Tabelas, memória e conferências | Precisa portão de entradas e motor; IPC documental completo é dispensável. |
| Decisor | Mesmo texto | Não | Cenários, comparação econômica | Exigir cenário validado; não duplicar entrevista probatória. |
| Recurso | Mesmo texto | Não | Motivo do indeferimento, tese e prova | Falta revisão final de prazo/cabimento e cobertura de fundamentos. |
| Raio-X | Mesmo texto | Não; corte do caso é outra coisa | Semáforo de triagem | Escopo enxuto é deliberadamente útil. Evitar “inviável” definitivo. |
| Maternidade | Ausente | 30/07/2026 | Diagnóstico, semáforo, checklist, passivo | Equivalente funcional a vários portões; não precisa copiar score de pensão. |
| Auxílio-acidente | Uso interno. Programa Cortex. | Agosto/2026 | Prontidão 0–100, painel, objeções e conexos | Mais completo, porém rubricagem e código divergem. |
| Pensão | Uso interno. Programa Cortex. | Agosto/2026 | IPC 0–100, painel, objeções e conexos | Completo; dados ausentes/bloqueios precisam correção. |
| PCD | Proprietário — Cortex / Vértika | Não; data do manual não basta | DID, IF-BrA, roteiro, revisão por atividade | IF-BrA não é score de prontidão. Acrescentar mapa de prova, não um segundo diagnóstico oficial. |

Padronizar licença exige decisão do titular: não presumir licença aberta nem simplesmente substituir as duas formulações. Padronização editorial segura: “Painel do caso”, “Lacunas de prova”, “Objeções prováveis do INSS” e “Hipóteses conexas”. Preservar termos jurídicos de domínio e diferenciar IF-BrA de índice interno de prontidão. Não há justificativa para varredura exaustiva de conexos antes de uma pergunta pontual; há justificativa antes de fechar estratégia ou peça.

### 3.3 Ativação, comandos e instalação

**Sobreposição real.** A premissa de que as três skills têm exatamente o mesmo gatilho “aposentadoria” não se confirma literalmente. Cálculos é excessivamente ampla; Decisor enumera escolha/espera/VPL; PCD privilegia deficiência/IF-BrA, embora também seja muito longa. A documentação atual informa uso das descriptions na seleção e limites de tamanho/orçamento. Logo, há risco plausível de ativação ambígua, **não medição de erro em execução real**. [T2]

Descriptions propostas, sujeitas à avaliação de roteamento antes de substituir:

| Skill | Texto proposto |
|---|---|
| Raio-X | “Triagem inicial de CNIS: extrai vínculos, remunerações, indicadores e lacunas, com localização no documento. Use para primeira leitura ou diagnóstico de pendências; para RMI e simulação completa, encaminhe a Cálculos.” |
| Cálculos | “Calcula tempo, carência, elegibilidade e RMI com memória verificável a partir de CNIS e dados do caso. Use quando houver pedido de cálculo ou simulação de regras. Para escolher entre cenários calculados, use Decisor; para avaliação funcional/IF-BrA, use PCD.” |
| Decisor | “Compara aposentar agora ou esperar usando cenários de elegibilidade e RMI previamente validados; apresenta VPL, recebimentos adiados e sensibilidade. Use para escolha de regra, DER ou estratégia contributiva.” |
| PCD | “Atuação na aposentadoria da pessoa com deficiência pela LC 142: DID, prova funcional, IF-BrA, perícia e peças. Use quando deficiência e aposentadoria/avaliação funcional estiverem no objeto; dúvida sobre pensão de dependente com deficiência segue Pensão.” |

Nas skills de benefício, retirar a obrigação de executar operação completa “mesmo que a pergunta pareça simples”; manter ativação temática, com profundidade proporcional ao pedido. Em recurso de benefício específico, a skill especializada conserva o dossiê e utiliza o módulo comum de recurso. Em pedido de peça, Estagiário recebe esse dossiê; não inicia caso novo.

**Aliases.** Existem arquivos duplicados com/sem acento em `commands/`, além de cópias dentro de auxílio/pensão. Recomendo **um corpo canônico e aliases finos compatíveis**, com tabela de geração, mantendo `/auxílio-acidente`, `/auxilioacidente`, `/pensãopormorte` e `/pensaopormorte`. Não apagar comandos usados por escritórios. Validar no sistema de arquivos do Windows/macOS/Linux e no Claude alvo. Apenas anunciar aliases no front-matter não os cria. [T2]

**Instaladores.** `install.sh:23–24` remove a pasta anterior antes de copiar; `install.ps1:23–24` faz o equivalente. Uma falha intermediária pode deixar instalação incompleta e atualizações descartam personalizações locais. `commands` também é sobrescrito. Mudança estrutural: validar pacote em pasta temporária, registrar versão/manifesto, fazer backup apenas do escopo Cortex, trocar com rollback e oferecer desinstalação pelo manifesto. Não apagar diretórios gerais de skills/comandos do usuário.

**README.** Há instrução de clone e instalação por plataforma, o que é positivo. Falta percurso para quem nunca usou terminal: pré-requisitos de Git, Claude Code e Python, onde executar, resultado esperado, primeiro comando e solução para erro. O script maternal usa anotações `date | None`, exigindo Python 3.10+ na forma distribuída. O pacote afirma compatibilidade com Code e Cowork, mas não inclui matriz de ferramentas/versões nem teste dessa equivalência. Documentar ambientes efetivamente testados, ferramentas opcionais e fallback quando busca, Agent, exportação ou Drive estiverem indisponíveis. Não prometer envio de arquivo que não ocorreu.

### 3.4 Modernização de agentes e redução de alucinação

As propostas abaixo são recomendações de engenharia derivadas desta auditoria; não alegações de que uma arquitetura elimina erro jurídico.

| Prática com fonte técnica | Aplicação concreta ao Cortex | Critério de aceite |
|---|---|---|
| Contexto selecionado, leitura sob demanda e notas persistentes; Anthropic, 29/09/2025. [T3] | Índice de referências por problema e dossiê persistido a cada etapa. A leitura integral foi necessária à auditoria; não deve ser exigida do modelo em todo atendimento. | Reabrir conversa com dossiê e reproduzir fatos, lacunas e etapa sem reinventar dados. |
| Estado recuperável em tarefas longas; Anthropic, 26/11/2025 e arquitetura de 08/04/2026. [T4, T5] | Registro separado de fatos, evidências, hipóteses, cálculos e decisões. Cada agente recebe a mesma versão do caso e produz alterações identificadas. | Contradição não sobrescreve fato; atualização exige origem e registra versão anterior. |
| Avaliações de agentes com verificadores e leitura de trajetórias; Anthropic, 09/01/2026. [T6] | Casos de regressão jurídica, testes de cálculo e conjuntos “deve ativar/não deve ativar”. | Repetir casos sintéticos; nenhum dado ausente vira fato e nenhum P0 volta após mudança. |
| Ferramentas calculam e retornam resultados rastreáveis; padrão já oferecido por API/MCP no mercado. [M3] | Interface única para motores locais ou serviço autorizado, sem obrigar fornecedor externo. | Entrada/saída com regra, data, arredondamento, erro e memória; não mandar CNIS a terceiro só porque há conector. |
| RAG não garante ausência de alucinação; estudo empírico Stanford/RegLab sobre ferramentas jurídicas. [T7] | Verificador de citações independente da redação: existência, conteúdo, status e aplicação. | Citação não localizada é marcada e excluída de afirmação conclusiva; medir cobertura e erros, sem promessa “zero alucinação”. |

**Contrato mínimo de caso, proposto:**

```json
{
  "versao": 1,
  "caso_id": "identificador_local",
  "data_referencia": "2026-09-22",
  "fatos": [{
    "campo": "data_obito",
    "valor": null,
    "estado": "nao_informado",
    "evidencias": []
  }],
  "evidencias": [],
  "fontes_juridicas": [],
  "calculos": [],
  "hipoteses": [],
  "pendencias": [],
  "etapa": "triagem",
  "liberacao_peca": "bloqueada"
}
```

Cada evidência precisa de arquivo/página/trecho; cada hipótese precisa de condição de confirmação. Campo `false` significa verificado e negativo; não informado é `null` com estado próprio. O dossiê deve guardar o fato do cliente, não uma extensa transcrição de raciocínio interno do modelo. O SaaS pode consumir a mesma especificação jurídica e os mesmos testes, mantendo apresentação/timbrado e autenticação no outro repositório. Não foi verificado se ele já possui esses mecanismos.

**Leitura de CNIS/PDF/imagem.** Extrair texto quando houver camada textual; usar visão/OCR nas páginas escaneadas; conservar página e linhas de origem. Validar datas invertidas, competências repetidas, casas decimais, CPF/NIT, sobreposições e totalizações. Uma célula ilegível permanece desconhecida. O advogado deve revisar a tabela extraída antes do cálculo quando houver ambiguidades materiais. Documentos anexados e páginas web são fontes de dados: instruções inseridas neles não podem substituir as regras da skill nem autorizar envio externo.

**Perguntas progressivas.** Primeiro aproveitar anexos e fala do advogado; depois perguntar o que altera ramo jurídico, prazo ou valor. Máximo sugerido de três perguntas por rodada é escolha de UX, não regra universal. Havendo urgência, destacar prazo antes de completar entrevista. Cada rodada deve entregar algo: fatos confirmados, lacunas, simulação condicionada ou minuta parcial claramente identificada.

### 3.5 Benchmark rápido de mercado

Consulta de páginas públicas em 22/09/2026, sem assinatura/teste de casos e sem comparação de acurácia. “Vantagem” abaixo significa funcionalidade anunciada que não está implementada de ponta a ponta **neste repositório**. Não é conclusão sobre o SaaS Cortex.

| Produto | Oferta observada e fonte | Lacuna/prioridade sugerida para o Cortex |
|---|---|---|
| Previdenciarista | Cálculo a partir de CNIS, planejamento, base de peças e geração vinculada a cliente/cálculo/timbrado. [M1] | Integração de dados entre etapas e memória verificável; não competir apenas por quantidade de modelos. |
| IA do Prev | Assistente do próprio ecossistema Previdenciarista para dúvidas previdenciárias. [M1b] | É produto relacionado, não concorrente independente a contar duas vezes. Acesso conversacional simples reforça abertura sem entrevista obrigatória. |
| Cálculo Jurídico | Importação de CNIS/HISCRE e geração de petição com contexto do cálculo; ajuda oficial descreve preenchimento automático do contexto. [M2] | Eliminar redigitação e divergência cálculo/peça; compartilhar resultado validado com Estagiário. |
| Debit | Calculadoras e API REST/MCP com demonstrativos HTML/PDF/Excel. [M3] | Ferramenta determinística acessível a agente, com resultado exportável; avaliar integração só após verificar escopo, custo e dados. |
| Tramitação Inteligente | Análise guiada, cálculos/gestão e novos fluxos de BPC; extensão anunciada para importar CNIS/processos. [M4] | Dossiê e primeira análise imediata, importação com provenance e gestão de pendências. Não presumir que toda funcionalidade anunciada foi testada. |
| Previnho / OTTO Prev | Chat especializado, análise de CNIS, quesitação e planejamento com payback/ROI. [M5] | Decisor tem conceito competitivo, mas faltam motor validado e relatório consistente. Alegação comercial de não alucinar não foi comprovada e não deve ser copiada. |
| ADVBOX | PREV-7 produz peças previdenciárias dentro da plataforma de gestão; guias mostram uso especializado. [M6] | Continuidade entre documentos, tarefa e revisão. Não confirma superioridade jurídica do texto gerado. |
| AdvTechPro.ai | Site oficial apresenta IA para documentos jurídicos; conteúdo integral recuperável foi limitado. [M7] | Não confirmado motor previdenciário/CNIS específico nem diferencial técnico superior ao Cortex. Não preencher lacuna com marketing de terceiros. |
| Jus IA / Jusbrasil | Exibe fontes e anuncia verificação de referências e consulta à base jurídica; materiais públicos de 2026 detalham conferência. [M8] | Fonte acessível por afirmação, estado de validação e documento original são padrão de UX a perseguir. Não é entrante necessariamente nova nem prova de ausência de erro. |

Não localizei estudo público comparável, em casos brasileiros previdenciários idênticos, que permita ordenar esses produtos por taxa de acerto. O estudo estrangeiro [T7] não estima a taxa de erro do Cortex nem de concorrentes brasileiros. A prioridade sugerida decorre de recursos observáveis e dos defeitos locais reproduzidos, não de ranking inventado.

### 3.6 Execução dos cinco scripts: resultados reproduzíveis

Execução em Python 3.12, sem dependências externas, entradas sintéticas. Os três calculadores e os dois scores foram importados/executados. Isso testa os casos abaixo, não certifica toda a legislação nem a integração com Claude.

| Caso/entrada | Resultado observado | Resultado/conduta esperada |
|---|---|---|
| Maternidade: empregada, parto 01/08/2026, remuneração 12.000 | RMI 8.475,55 | 12.000 no cenário, sem aplicar teto RGPS ordinário. [S16] |
| Maternidade: última competência 01/2025, empregada, fato 01/03/2026 | Limite 15/02/2026; qualidade negada | Implementar extensão legal corretamente; algoritmo está um mês aquém até do próprio comentário. [S17] |
| Maternidade: facultativa + desemprego verdadeiro | 18 meses | Não prorrogar automaticamente a proteção de facultativa como se obrigatória. |
| Maternidade: JSON `desemprego_involuntario: "false"` | Acrescenta 12 meses | Rejeitar tipo string; não converter para verdadeiro. |
| Pensão: óbito 01/01/2018, DER 01/03/2018, idade 40 | DIB na DER, prazo 30 | DIB no óbito pelo prazo de 90 aplicável. [S26] |
| Pensão: óbito 31/01/2026, idade 30; contribuições/união omitidas | Filtros atendidos, dez anos, cessação 28/01/2036 | Requisitos desconhecidos; se comprovados, preservar dia 31 no aniversário. |
| Pensão: base 1.621, dois dependentes | Total 1.621; projeção para um = 972,60 | Reaplicar regras de piso e dependentes em cada cenário. |
| Pensão: base -100, zero dependentes | Pensão 1.621 | Erro de entrada; não gerar benefício. |
| Pensão: acumulação 6.000 + 4.000, SM 1.621 | 8.896,80 | Controle aritmético correto para faixas utilizadas. |
| Auxílio: SB 3.000 | 1.500 | Controle correto do cálculo simples contemporâneo. |
| Auxílio: SB -100 | -50 | Erro de entrada. |
| Ambos os scores: itens cheios, `A1=na`, objeto bloqueios ausente | 100/100 e recomendação favorável | Rejeitar não aplicabilidade não justificada de item essencial; exigir checagem dos bloqueios. |

Reprodução dos casos CLI a partir da raiz:

```bash
python3 skills/pensao-por-morte/scripts/calculadora_pensao.py dib --obito 2018-01-01 --der 2018-03-01 --idade-dependente 40
python3 skills/pensao-por-morte/scripts/calculadora_pensao.py duracao --obito 2026-01-31 --idade-dependente 30
python3 skills/pensao-por-morte/scripts/calculadora_pensao.py rmi --base 1621 --dependentes 2
python3 skills/pensao-por-morte/scripts/calculadora_pensao.py rmi --base -100 --dependentes 0
python3 skills/pensao-por-morte/scripts/calculadora_pensao.py acumulacao --beneficio-a 6000 --beneficio-b 4000
python3 skills/auxilio-acidente/scripts/calculadora_auxilio_acidente.py rmi --base 3000
python3 skills/auxilio-acidente/scripts/calculadora_auxilio_acidente.py rmi --base -100
```

Reprodução das funções importadas (não altera arquivos do projeto):

```python
import importlib.util
import sys

sys.dont_write_bytecode = True

def carregar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[nome] = modulo
    spec.loader.exec_module(modulo)
    return modulo

m = carregar('maternal', 'skills/cortex-maternidade/scripts/diagnostico.py')
c = m.Caso.de_dict({'fato_gerador': '2026-08-01',
                   'categoria': 'empregada', 'remuneracao_mensal': 12000})
print(m.calcular_rmi(c))
for skill in ('pensao-por-morte', 'auxilio-acidente'):
    s = carregar(skill.replace('-', '_'), f'skills/{skill}/scripts/score_prontidao.py')
    caso = s.template()
    caso['itens'] = {k: 'cheio' for k in caso['itens']}
    caso['itens']['A1'] = 'na'
    caso.pop('bloqueios', None)
    total, _, lacunas = s.pontuar(caso)
    print(skill, total, s.faixa(total), lacunas)
```

**Arredondamento.** Os scripts usam `float` e formatação/arredondamento final; não há convenção única de centavos ou arredondamento por parcela. Não observei erro de centavos nos controles positivos executados. Proponho `Decimal` e política explícita, com testes de meio centavo, sem afirmar que todo uso de `float` já causou dano. Para datas, as divergências foram reproduzidas e são prioridade superior.

## 4. Plano de ação priorizado

### 4.1 Quick wins — escopo pequeno, sem redesenhar o produto

Não implementados nesta entrega: o relatório foi produzido primeiro e permanece a única alteração. São tarefas que podem ser executadas diretamente na próxima rodada, respeitados os limites indicados.

| Prioridade | Mudança concreta | Aceite objetivo |
|---|---|---|
| P0 | Corrigir valores de 2026 em `regras-calculo.md` e referências correspondentes, mantendo parâmetros históricos identificados. | Nenhum R$ 1.518/R$ 8.157,41 rotulado como vigente em 2026; referências de anos antigos preservadas. |
| P0 | Corrigir número/conteúdo de súmulas comprovadamente trocados, data do Tema 416, inciso do art. 73 e nome do recurso do JEF. | Cada alteração vem com fonte e recorte; não introduzir precedente substituto não pesquisado. |
| P1 | Corrigir caminhos quebrados da Maternidade e documentação de comando inexistente. | Todos os links locais resolvem; README não manda usar recurso não instalado. |
| P1 | Acrescentar pré-requisitos e primeiro uso ao README; distinguir corte normativo de data do caso. | Instrução executável para Windows e Unix, Python 3.10+, versão efetivamente testada do Claude identificada. Não inventar versão mínima de integração. |
| P1 | Remover frase de infalibilidade do script; trocar confiança absoluta por memória/verificação. | Guardrails mantidos e reforçados, sem mudar voz geral. |
| P2 | Normalizar UTF-8 do documento PCD 04, preservando conteúdo jurídico. | Decodificação estrita e diff limitado a caracteres danificados. |
| P2 | Corrigir remissões editoriais, sem alterar licença ou apagar aliases. | Ausência de alteração de fluxo, direitos de uso ou interface pública. |

### 4.2 Mudanças estruturais — apresentar implementação para aprovação antes de aplicar

| Ordem | Escopo | Motivo e critério de aceite |
|---|---|---|
| 1 — P0 | Contrato de entrada dos cinco scripts e bloqueio de revisão do Estagiário | Desconhecido não vira fato; valores inválidos rejeitados; `BLOQUEADO` nunca libera peça final. Todos os casos negativos do § 3.6 passam. |
| 2 — P0 | Núcleo normativo compartilhado: cálculo/decisor/PCD, histórico de pensão e maternidade | Uma regra por modalidade e vigência, com fonte, testes de fronteira e memória. Não promover automaticamente teses controvertidas à regra administrativa. |
| 3 — P0 | Auxílio: ramo comum/ocupacional, competência, prova e tributação | Caso comum não perde pontos por CAT ausente; ação ocupacional não recebe JEF por default; modelos seguem ramo validado. |
| 4 — P0 | PCD: entrevista neutra e IF-BrA/Fuzzy verificável | Nenhuma resposta pré-preenchida atribuída ao cliente; grau deriva de fatos; duas avaliações e critérios integrais documentados. |
| 5 — P1 | Dossiê único e passagem entre skills/agentes | Fatos, documentos, fontes e cálculos sobrevivem a retomada/compactação; conflitos ficam visíveis. Separar dado do cliente de conclusão do agente. |
| 6 — P1 | Registro de fontes e verificador de citações | Existência, proposição, vigência e aplicabilidade checadas; status pendente bloqueia apenas conclusões dependentes. |
| 7 — P1 | Rubricas e gates proporcionais ao produto | Auxílio/pensão usam pesos compatíveis com scripts e bloqueios completos; Raio-X/Decisor mantêm leveza com controles próprios. |
| 8 — P1 | Descriptions, roteamento, aliases canônicos e entrevista progressiva | Casos positivos/negativos de ativação; aliases antigos continuam; informação já extraída não é perguntada de novo. |
| 9 — P1 | Instalação transacional e matriz Code/Cowork | Instalação/reinstalação/falha/restauração verificadas em destino temporário; preserva outras skills e personalizações. |
| 10 — P1 | Higienização da biblioteca e possível compartilhamento com SaaS | Modelos neutros, origem/licença validada; motor compartilhado somente após análise do outro repositório. |

**Sequência de validação recomendada:** primeiro regressões determinísticas; depois casos jurídicos sintéticos revistos por advogado; por último sessões reais no Claude com anexos anonimizados. Exemplos obrigatórios: 33 anos exatos no pedágio, PCD idade versus tempo, óbito em 2018, facultativa sem informação de contribuição, acidente doméstico não ocupacional, referência judicial inexistente, CNIS ilegível e segundo ciclo de revisão bloqueado. Não basta avaliar se a resposta “parece boa”.

### 4.3 Pesquisa adicional necessária — não transformar em conteúdo confirmado

1. **Íntegra oficial da IN 212/2026:** conferir redação anterior/imediatamente posterior, vigência e efeitos em cada skill; prioritários arts. 184, 216, 223, 354, 369-A, 566, 574 e 600. Catálogo confirmado, efeitos detalhados ainda pendentes.
2. **Portaria 66/2026 e Resolução CRPS 13/2026:** recuperar íntegra oficial e anexos; validar instrumento de deficiência e redação do Enunciado 19, sobretudo facultativa, atividade rural e concomitância.
3. **Regimento CRPS compilado e IN 208:** conferir exceções, alçada, calendário, recurso especial e renovação de requerimento. Não codificar texto secundário sem cotejo oficial.
4. **PCD:** validar média pós-reforma por via administrativa/judicial, Fuzzy integral, tabelas de conversão e pertinência dos temas citados. Recuperar os 44 PDFs para conferir transcrição, tabelas e direitos de redistribuição. Ausência dos PDFs não impede corrigir contradições internas já demonstradas.
5. **Jurisprudência emergente:** acórdão do TRF4 sobre contribuinte individual/auxílio-acidente; status final do Tema 1.341/STJ; conferir temas rurais e eventuais modulações antes de alterar regras. Não se verificou exaustivamente o universo de decisões dos seis TRFs.
6. **Histórico temporal:** MP 664/2014, pensões antigas, parâmetros anuais, regras da MP 905 e data exata de proteção do doméstico na LC 150. Definir intervalos e casos de fronteira antes de motor histórico.
7. **CNIS:** legenda oficial por versão, inclusive `PADV`, `IREC` e códigos compostos; validar abaixo do mínimo por categoria e período. Não criar dicionário a partir de expansão linguística plausível da sigla.
8. **Conexos e dados:** vigência de SPVAT, parâmetros rurais de pesca e condição de garimpeiro; autorização para materiais/casos identificáveis. Esses itens não receberam validação suficiente para afirmar direito atual.
9. **Execução real:** testar Code/Cowork, exportação/timbrado/Drive, ativação natural e retomada de contexto. O comportamento efetivo do modelo não foi medido nesta auditoria estática e de scripts.

### 4.4 Estado da entrega

Somente `AUDITORIA-CORTEX-2026-09-22.md` foi criado. Os arquivos do produto permanecem no estado auditado. Os testes usaram dados sintéticos, não casos reais; caches gerados pela execução foram removidos. Nenhuma mudança estrutural foi aplicada. O próximo passo é revisar as decisões da seção 4.2 e resolver as fontes impeditivas da seção 4.3 antes de converter as recomendações em comportamento de produção.

## 5. Fontes consultadas

Links abaixo são parte do relatório e permitem conferência independente. Todos consultados em 22/09/2026. Data de consulta não substitui data de vigência. Fontes sem data editorial identificada são páginas correntes, não atos novos. A pesquisa tentou fontes oficiais primeiro; reprodução secundária está marcada expressamente.

### Normas, jurisprudência e orientações oficiais

- **[S1] CJF/TNU — lista oficial de súmulas**, com datas de publicação e alterações: <https://www.cjf.jus.br/phpdoc/virtus/listaSumulas.php>. Conferidas especialmente 30, 34, 54, 63, 68, 73, 74, 77, 78, 88 e 89. O texto integral, e não o resumo do buscador, foi usado para distinguir as teses.
- **[S2] Lei 13.105, de 16/03/2015 — CPC**, arts. 350, 351, 391, 396 e 927: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm>.
- **[S3] Leis 9.099, de 26/09/1995, e 10.259, de 12/07/2001**, recursos nos juizados: <https://www.planalto.gov.br/ccivil_03/leis/l9099.htm> e <https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10259.htm>.
- **[S4] EC 136, de 09/09/2025**, especialmente art. 3º, alteração da EC 113: <https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc136.htm>.
- **[S5] EC 103, de 12/11/2019**, arts. 16, 17, 19, 23, 24 e 26: <https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm>.
- **[S6] INSS — tabela de contribuição mensal, competência 2026:** <https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal>.
- **[S7] Lei 8.213, de 24/07/1991, texto compilado**, dispositivos indicados nos achados: <https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm>.
- **[S8] STJ — Tema 1.007**, aposentadoria híbrida e tempo rural remoto, ficha oficial: <https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1007&cod_tema_inicial=1007&novaConsulta=true&tipo_pesquisa=T>.
- **[S9] LC 142, de 08/05/2013**, arts. 3º, 8º, 9º e 10: <https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp142.htm>.
- **[S10] INSS — regras de aposentadorias**, tabela de tempo/carência: <https://www.gov.br/inss/pt-br/direitos-e-deveres/aposentadorias/regras-de-aposentadorias>.
- **[S11] TCU — documento oficial com indicadores do CNIS**, inclui `PEXT` e `PREC-FBR`: <https://pesquisa.apps.tcu.gov.br/redireciona/acordao-completo/ACORDAO-COMPLETO-2539216>. Usado como referência documental dos códigos, não prova de que todas as versões atuais do CNIS usam idêntica legenda.
- **[S12] INSS — salário-maternidade**, cumprimento das ADIs 2.110/2.111 pela IN 188, de 08/07/2025: <https://www.gov.br/inss/pt-br/direitos-e-deveres/salario-maternidade/salario-maternidade>.
- **[S13] MPS/CRPS — regimento e histórico oficial**, Portarias 125, de 26/01/2026, e 235, de 03/02/2026: <https://www.gov.br/previdencia/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/conselho-de-recursos-da-previdencia-social/regimento-interno> e <https://www.gov.br/previdencia/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/conselho-de-recursos-da-previdencia-social/regimento-interno-instrucao-normativa-portarias/historico-de-atualizacoes-regimento-interno>.
- **[S14] Lei 15.415, de 25/05/2026**, DOU 26/05/2026: <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15415.htm>.
- **[S15] Lei 15.222, de 29/09/2025**, DOU 30/09/2025: <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15222.htm>.
- **[S16] INSS — Portal IN, Portaria 991, renda do salário-maternidade**, limite próprio para empregada/avulsa: <https://portalin.inss.gov.br/portaria991>. Texto pertinente recuperado no índice de busca; página dinâmica tem limitação de extração direta. Corroboração institucional: notas do FRGPS/2024, <https://www.gov.br/inss/pt-br/centrais-de-conteudo/publicacoes/relatorios/2024/ne-frgps-2024-anual.pdf>.
- **[S17] Decreto 3.048, de 06/05/1999, compilado**, qualidade de segurado: <https://www.planalto.gov.br/ccivil_03/decreto/d3048.htm>; IN 128 consolidada, trechos indexados: <https://portalin.inss.gov.br/in/530>. Recuperação da consolidação integral limitada.
- **[S18] CJF — DOUInforme de 24/03/2026**, Portarias 13, 14 e 15 e Resolução CNJ 673: <https://www.cjf.jus.br/cjf/noticias/2026/marco-1/douinforme-24-03.2026>.
- **[S19] Reprodução secundária da Portaria Conjunta MPS/INSS 15, de 23/03/2026**, texto integral consultado, objeto corroborado por [S18]: <https://okai.com.br/ministerio-previdencia-social/documentos/2026-03-24/portaria-conjunta-mps-inss-n%C2%BA-15-de-23-de-marco-de-2026>.
- **[S20] CF/1988, art. 109, I:** <https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm>. STJ, competência estadual em ação acidentária, notícia de 07/11/2016: <https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias-antigas/2016/2016-11-07_09-44_Justica-estadual-julgara-acidente-de-trabalho-sofrido-por-mecanico-adolescente.aspx>. Delimitação em julgado publicado em 25/05/2026: <https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?dt_publicacao=25%2F05%2F2026&num_registro=202600587347>.
- **[S21] INSS — auxílio-acidente**, condições e categorias: <https://www.gov.br/inss/pt-br/direitos-e-deveres/beneficios-por-incapacidade/auxilio-acidente>.
- **[S22] Receita Federal — Manual do IR, outros rendimentos**, lista de rendimentos isentos: <https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/preenchimento/manual-mir/rendimentos/outros-rendimentos>.
- **[S23] STJ — repertório institucional de repetitivos previdenciários**, Tema 416, julgamento 25/08/2010 e DJe 08/09/2010: <https://www.stj.jus.br/publicacaoinstitucional/index.php/Repeorg/article/download/11135/11265>.
- **[S24] STJ — Tema 1.421**, notícia de 24/06/2026: <https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/24062026-Pensao-por-morte-e-auxilio-reclusao-a-menores-de-16-anos-nao-retroagem-se-pedido-e-posterior-ao-prazo-legal.aspx>; acórdão publicado em 17/06/2026: <https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?dt_publicacao=17%2F06%2F2026&num_registro=202504104930>.
- **[S25] STJ — Tema 1.360**, julgamento de 11/03/2026, Informativo 881, de 17/03/2026: <https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&livre=%270881%27.cod.>.
- **[S26] Lei 13.183, de 04/11/2015**, alteração do art. 74: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13183.htm>.
- **[S27] STJ — Pesquisa Pronta, notícia de 16/03/2023**, invalidez anterior ao óbito: <https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2023/16032023-Pensao-por-morte-para-dependente-invalido-e-legitimidade-para-execucao-de-honorarios-estao-na-nova-Pesquisa.aspx>.
- **[S28] Lei 9.784, de 29/01/1999**, art. 49: <https://www.planalto.gov.br/ccivil_03/leis/l9784.htm>.
- **[S29] INSS — catálogo de portarias conjuntas de 2026**, Portaria PRES/INSS/SRGPS/MPS 66, de 14/07/2026, registro de 15/07: <https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/portarias-conjuntas/2026>.
- **[S30] STJ — Tema 1.341**, ficha consultada: <https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?i=1&novaConsulta=true&p=true&pesquisa_livre=1341&quantidadeResultadosPorPagina=10>.
- **[S31] Portaria Interministerial AGU/MPS/MF/SEDH/MP 1, de 27/01/2014**, reprodução secundária integral: <https://www.legisweb.com.br/legislacao/?id=265085>. Aplicação descrita em acórdão oficial TRF3: <https://web.trf3.jus.br/acordaos/Acordao/BuscarDocumentoPje/366943647>. A automatização do anexo ainda depende de cotejo oficial integral.
- **[S32] STF — ADI 6.096**, notícia sobre julgamento encerrado em 09/10/2020: <https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=453347&ori=1>.
- **[S33] CJF/TNU — Tema 378**, objeto BPC/visão monocular: <https://cjf.jus.br/cjf/corregedoria-da-justica-federal/turma-nacional-de-uniformizacao/temas-representativos/tema-378>.
- **[S34] INSS — catálogos de instruções normativas**, atos de 2026 e histórico da IN 128: <https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/instrucao-normativa/2026> e <https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/instrucao-normativa/2022>.
- **[S35] Gustavo Lopes, 21/08/2026 — análise secundária da IN 212**, usada para localizar pontos de conferência, não como substituto da íntegra oficial: <https://gustavolopes.adv.br/in-212-2026-o-que-mudou-na-in-128/>.
- **[S36] IN 208, de 19/05/2026**, reprodução secundária, DOU 20/05: <https://www.legisweb.com.br/legislacao/?id=495991>.
- **[S37] STJ — Tema 1.307**, notícia de 03/06/2026: <https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/03062026-Motoristas-e-cobradores-STJ-permite-reconhecimento-de-aposentadoria-especial-por-trabalho-penoso.aspx>; datas de julgamento/publicação no repertório: <https://scon.stj.jus.br/SCON/repetitivos/toc.jsp?filtroPorNota=&l=100&livre=&ordenacao=MAT%2CTIT%2C%40NUM&tema1=1307&tema2=1307>.
- **[S38] MPS — Tema 1.300/STF**, divulgação em 30/03/2026 do julgamento de dezembro/2025: <https://www.gov.br/previdencia/pt-br/assuntos/rpps/julgamentos/re-1469150-tema-1300-rg-calculo-de-aposentadoria-por-incapacidade>. A página está na seção RPPS; o uso aqui é da tese reportada, sem importar indiferenciadamente requisitos do RPPS ao RGPS.
- **[S39] CJF/TNU — Tema 384**, julgamento em 06/08/2026, publicação em 19/08/2026, tabela oficial: <https://www.cjf.jus.br/cjf/corregedoria-da-justica-federal/turma-nacional-de-uniformizacao/temas-representativos/?b_size:int=40&b_start:int=360>.
- **[S40] STF — Tema 1.209**, ficha e andamento oficial, publicação do mérito em 04/03/2026: <https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1209> e <https://portal.stf.jus.br/processos/detalhe.asp?incidente=6344761>. Notícia de 24/02/2026: <https://noticias.stf.jus.br/postsnoticias/stf-afasta-aposentadoria-especial-para-vigilantes-por-exposicao-a-perigo/>. Conteúdo oficial pertinente recuperado por indexação; abertura direta teve restrições.
- **[S41] STJ — Tema 1.157**, notícia de 31/07/2026: <https://www.stj.jus.br/sites/portalp/paginas/comunicacao/noticias/2026/31072026-revisao-administrativa-pode-cancelar-beneficio-previdenciario-por-incapacidade-concedido-judicialmente.aspx>.
- **[S42] STJ — Tema 1.124**, julgamento em 08/10/2025, Informativo 866, de 14/10/2025: <https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&livre=%270866%27.cod.>.
- **[S43] CJF/TNU — Tema 389**, afetação em 12/02/2026, estado “Em Julgamento” consultado em 22/09/2026: <https://www.cjf.jus.br/cjf/corregedoria-da-justica-federal/turma-nacional-de-uniformizacao/temas-representativos/tema-389>.

### Engenharia de agentes e pesquisa

- **[T1] Anthropic — Claude Code, subagents**, documentação corrente, inclusive aninhamento/configuração: <https://code.claude.com/docs/en/sub-agents>.
- **[T2] Anthropic — Claude Code, skills**, front-matter, ativação, comandos e contexto: <https://code.claude.com/docs/en/skills>.
- **[T3] Anthropic, 29/09/2025 — Effective context engineering for AI agents:** <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>.
- **[T4] Anthropic, 26/11/2025 — Effective harnesses for long-running agents:** <https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>.
- **[T5] Anthropic, 08/04/2026 — Scaling Managed Agents:** <https://www.anthropic.com/engineering/managed-agents>. Inspiração de separação entre sessão/estado/execução; não recomendação de migração obrigatória à plataforma.
- **[T6] Anthropic, 09/01/2026 — Demystifying evals for AI agents:** <https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>.
- **[T7] Stanford/RegLab — Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools**, pesquisa de 2024, com publicação posterior: <https://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/>. Estudo de ferramentas/direito estrangeiros; sem extrapolação de taxas ao Brasil.

### Fontes comerciais — funcionalidades anunciadas

- **[M1] Previdenciarista:** <https://previdenciarista.com/assine/> e <https://previdenciarista.com/peticoes-produto/>.
- **[M1b] IA do Prev:** <https://lp.previdenciarista.com/assine/ia-do-prev>.
- **[M2] Cálculo Jurídico:** <https://calculojuridico.com.br/calculos-previdenciarios/> e ajuda sobre cálculo/contexto da petição: <https://ajuda.calculojuridico.com.br/pt-BR/articles/7832340-perguntas-frequentes-calculo-de-concessao-planejamento>.
- **[M3] Debit — API/MCP:** <https://www.debit.com.br/api> e <https://www.debit.com.br/>.
- **[M4] Tramitação Inteligente:** <https://planilha.tramitacaointeligente.com.br/blog/lancamento-analise-guiada-de-bpc-loas> e extensão publicada pelo fornecedor: <https://chromewebstore.google.com/publisher/tramitacao-inteligente-lt/u324f40a68d34a64670ba8af17cc127be>.
- **[M5] OTTO/Previnho:** <https://www.ottoprev.com/>.
- **[M6] ADVBOX — PREV-7 e guia de agentes:** <https://advbox.com.br/blog/agente-prev-7/> e <https://guia.advbox.com.br/agentes-de-ia/agentes-juridicos-ia>.
- **[M7] AdvTechPro.ai:** <https://advtechpro.ai/>. Recuperação limitada; não atribuídos recursos específicos não confirmados.
- **[M8] Jus IA/Jusbrasil:** <https://ia.jusbrasil.com.br/> e explicação de fontes: <https://ia.jusbrasil.com.br/jusia-academy/como-verificar-fontes-juridicas-no-jus-ia/5670818794>.

## 6. Registro de cobertura documental

Inventário do commit auditado, anterior à criação deste relatório. Contagem inclui referências, assets, comandos internos, scripts e arquivos auxiliares; não inclui caches de execução.

| Escopo | Arquivos lidos |
|---|---:|
| `commands` | 11 |
| `raiz` | 6 |
| `skills/aposentadoria-pcd` | 46 |
| `skills/auxilio-acidente` | 36 |
| `skills/calculos-previdenciarios` | 2 |
| `skills/cortex-maternidade` | 21 |
| `skills/decisor-aposentadoria` | 2 |
| `skills/estagiario-peticoes` | 7 |
| `skills/pensao-por-morte` | 37 |
| `skills/raio-x-cnis` | 2 |
| `skills/recurso-inss` | 2 |
| **Total** | **172** |

A biblioteca PCD foi lida do documento `01-if-bra-205-perguntas.md` ao `39-curso-pcd-pro-sintese.md`, incluindo `INDEX.md`, sem seleção de modelos. A Bíblia de Prompts da raiz também foi lida por referência cruzada. O manual PDF foi extraído e lido integralmente; não se fez certificação de diagramação.
