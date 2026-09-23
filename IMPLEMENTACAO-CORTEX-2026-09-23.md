# Implementação estrutural Cortex — 23/09/2026

Autorização: implementação das melhorias estruturais nas nove skills, após a auditoria de 22/09/2026. O relatório de auditoria foi preservado como registro anterior à intervenção.

## Entregas

- **Nove skills:** protocolo comum, dossiê versionado, proveniência de fatos, registro de fontes, coleta em até três perguntas e quatro portões. Raio-X continua triagem; não se impôs score universal.
- **Núcleo autocontido:** fonte canônica em `core/`, distribuição determinística para `.cortex` em cada skill. Validador de dossiê e liberação final; coeficientes delimitados; comparação financeira com 13º uniforme, taxa real e custos incrementais; fronteira do pedágio de 50%; soma de dois formulários IF-BrA.
- **Estagiário:** revisão reprovada no segundo ciclo bloqueia finalização; passagem de dossiê completo; sem ranking fixo de tribunais, precedente fictício ou ementa obrigatória por argumento. Integrações opcionais têm alternativa local.
- **Cálculos/Decisor:** gatilhos separados; correção de requisitos, coeficientes e valores de 2026; atualização e parâmetros vinculados à data-base; comparação recusa cenários com elegibilidade desconhecida.
- **PCD:** entrevista neutra, sem respostas sugeridas ou meta de grau; distinção idade/tempo; dois formulários para soma; Fuzzy depende de instrumento completo. Biblioteca identificada como material histórico; NB/protocolos identificáveis e números de assinatura OAB substituídos por campos de conferência. Isso não equivale a anonimização completa do acervo/histórico.
- **Maternidade:** categoria, referência e parâmetros explícitos; rejeição de booleanos textuais; período de graça facultativo sem extensão por desemprego; correção do mês de vencimento; salários sem competências não geram RMI; remuneração integral sem teto RGPS automático; prescrição por evento não declara todas as parcelas prescritas; decisão comunicada impede presumir mora atual.
- **Pensão:** óbito obrigatório, parâmetros monetários explícitos, filtros de duração desconhecidos bloqueiam conta, quatro meses civis, datas anuais preservadas, DIB histórica de 2018 com 90 dias, prazo de 180 condicionado a filho, projeção com inválido bloqueada sem composição futura. Regimes anteriores a 18/06/2015 recusados pelo motor simplificado.
- **Auxílio-acidente:** ramo comum/ocupacional, CAT sem penalidade automática no ramo comum, competência estadual para ação acidentária ocupacional e correção de tratamento fiscal; valores não finitos rejeitados; sem prazo especial fictício de 30+30 dias.
- **Raio-X/Recurso:** revisão de indicadores, ausência de oportunidade automática para vigilante, súmulas TNU corrigidas, conferência de rito e prova antes de recurso final.
- **Scores:** bloqueios iniciam `null`; strings como `"false"` recusadas; `na` exige justificativa e não pode excluir requisito essencial; pesos do script são rubrica operacional canônica; score alto não autoriza protocolo ou tutela.
- **Comandos/instalação:** aliases antigos preservados e rotas PCD efetivamente instaladas; instalador único em Python, preparação e backup antes da substituição, restauração em falha; wrappers Bash/PowerShell; preservação de outras skills. Personalizações Cortex são guardadas no backup, sem tentativa de mesclagem automática.

## Validação executada

`python3 -m unittest discover -s tests -v`: **27 testes aprovados**, incluindo entradas negativas, fronteiras temporais, dossiê, coeficientes, IF-BrA, fluxo financeiro, ramo comum, instalação, reinstalação, restauração e falha simulada durante cópia.

Também executados: compilação Python, `bash -n install.sh`, `git diff --check`, conferência de nove front-matters, UTF-8 estrito do Markdown, paridade das cópias do núcleo, CLI de maternidade, pensão e auxílio-acidente.

Dois cenários independentes com leitura das skills revisadas: PCD com 15 anos apenas declarados e sem laudo não afirmou renda devida nem conduziu grau leve; Estagiário com segundo ciclo bloqueado recusou documento final e listou pendências. Essas simulações não substituem teste no produto Claude Code.

## Limites e pendências reais

1. **Não há motor completo de benefícios.** Apuração integral de CNIS, atualização por competência, tábuas IBGE, conversões PCD/especial, regras históricas e elegibilidade jurídica continuam exigindo dados e revisão. Os utilitários dizem seu alcance e recusam casos fora dele.
2. **Validador de fontes é estrutural.** Confere campos e estados; não prova que a URL existe ou que o texto sustenta a proposição. Consulta primária e revisão de aderência continuam obrigatórias no fluxo.
3. **Prescrição de maternidade e internação:** a estimativa auxilia triagem; não liquida cada parcela, condições pessoais, causas de suspensão nem toda extensão hospitalar. Não se certifica termo final sem conferir calendário fornecido.
4. **Fuzzy integral e novidades normativas:** IN 212/2026, Portaria 66/2026, Resolução CRPS 13/2026, média PCD pós-reforma e outros pontos da auditoria sem confirmação integral não viraram regras automáticas. Fontes e limites em `core/fontes-e-limites.md`.
5. **Biblioteca histórica:** marcação e substituição de identificadores óbvios não certificam anonimização, direitos de redistribuição ou correção de todas as transcrições. PDFs originais ausentes não foram reconstruídos; não houve reescrita do histórico Git. Não usar exemplos como prova ou jurisprudência verificada.
6. **Integrações:** não houve sessão real no Claude Code/Cowork, execução do wrapper PowerShell no Windows, exportação de timbrado, Drive/NotebookLM ou teste do SaaS, cujo repositório não integra este trabalho. Instalação e recuperação foram exercitadas em destinos temporários no Linux.
7. **Licença:** descrições de front-matter apontam para a licença proprietária existente; direitos do arquivo LICENSE não foram modificados.

## Operação e manutenção

Instalar com `bash install.sh` ou `powershell -ExecutionPolicy Bypass -File install.ps1`. O instalador imprime backup e comando de restauração. Não executar simultaneamente duas instalações no mesmo destino. O usuário mantém a decisão de protocolar/assinar; a automação entrega trabalho técnico revisável.

Editar `core/`, rodar `python3 scripts/sync_core.py` e regressões antes de publicar. Dados reais de casos permanecem fora do repositório. Alterações futuras de lei exigem fonte, recorte temporal e teste de fronteira correspondente.
