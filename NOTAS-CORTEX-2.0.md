# Cortex 2.1.1 — Yure Digital

Pacote proprietário de IA previdenciária para Claude Code: **dez especialistas e o coordenador `/prev`**.

## Instalação e atualização

Baixe `Cortex-2.1.1.zip`, extraia a pasta inteira e abra `INSTALAR-CORTEX-WINDOWS.cmd` no Windows. Mac/Linux: `bash install.sh`. O mesmo instalador serve para primeira instalação e atualização.

- Verifica Python 3.10+ e orienta sobre pré-requisitos.
- Identifica pastas e comandos oficiais existentes no destino e substitui integralmente pelo Cortex 2.1.
- Preserva backup e restaura a instalação anterior se houver falha durante substituição.
- Não remove skills de terceiros. Personalizações dentro das pastas Cortex ficam no backup.
- Inclui a licença Yure Digital em cada skill instalada.
- Ao concluir, abra nova sessão no Claude Code e use `/prev` seguido do caso.

Destino padrão: `.claude` do usuário atual. Para instalações por projeto ou outro caminho, use `--dest`. Não procura nem apaga cópias em perfis de outros usuários ou pastas renomeadas. Não há atualização remota contínua: execute a nova versão do pacote para atualizar.

## Melhorias

Dossiê com proveniência e continuidade entre skills, verificação de fontes, bloqueios de revisão, entrevista progressiva, cálculos com validação de entradas e parâmetros temporais, entrevista PCD neutra e rotas especializadas. O coordenador escolhe e executa a sequência necessária sem exigir conhecimento dos comandos individuais.

## Nova especialista em benefícios por incapacidade

`/incapacidade` (alias `/auxiliodoenca`) trata auxílio por incapacidade temporária e aposentadoria por incapacidade permanente no RGPS: triagem por atividade e DII, qualidade/carência, nexo, perícia, reabilitação, Atestmed, cessação, precedentes oficiais, contestação e conexões com o auxílio-acidente e as demais skills. Pesquisa jurídica revisada em 24/09/2026, inclusive alteração de gestação de alto risco em julho e prorrogação excepcional do Atestmed em setembro de 2026, cujo inteiro teor oficial deve ser conferido para casos futuros. Script de simulação condicionado a médias já auditadas, sem apurar CNIS nem RMI final. A instalação preserva backup e atualiza também o coordenador `/prev`. Correção 2.1.1: o limite legal documental geral é 30 dias e os 90 dias decorrem de ato excepcional com vigência definida; dispensa de reavaliação alcança determinadas hipóteses de auxílio temporário, com exigência de infectologista na perícia de segurado com Aids, conforme Lei 15.157/2025.

## Propriedade e limites

**Cortex 2.0 é propriedade intelectual da Yure Digital. Uso exclusivo de clientes autorizados. Compartilhamento, redistribuição e revenda sem autorização prévia e expressa são proibidos.** Materiais de terceiros preservam seus direitos. Consulte LICENSE.

A licença não é um bloqueio técnico de cópia. Conteúdo público permanece acessível. Não há garantia de infalibilidade jurídica ou de anonimização integral do acervo histórico. Itens normativos não confirmados permanecem sinalizados. Integrações com Cowork, Drive e NotebookLM, bem como a interface Windows, ainda exigem validação em ambiente real; os testes automatizados exercitam o motor de instalação e as regressões em Linux.

## Correção 2.0.1

Tratamento de arquivos somente leitura do Git na instalação anterior (WinError 5), sem alterar permissões ACL ou forçar liberação de arquivos em uso. O instalador informa o backup antes de substituir, restaura somente destinos afetados e explica quando a recuperação não pôde terminar. Abertura dentro do ZIP agora mostra instruções de extração. Feche Claude e editores durante a atualização; backups de tentativas anteriores são preservados.
