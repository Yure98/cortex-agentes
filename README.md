# 🧠 Cortex 2.2 — Yure Digital

Transforme o **Claude** numa equipe previdenciária completa. Agentes especializados
que redigem petições, analisam CNIS, decidem a melhor aposentadoria, geram recursos ao INSS
e cuidam de salário-maternidade, incapacidade, BPC/LOAS, aposentadoria especial, atividade rural e aposentadoria da pessoa com deficiência. As análises dependem de prova e fontes verificadas; dados ausentes permanecem `[CONFERIR]`.

Ambiente-alvo: **Claude Code**. Compatibilidade com Cowork ainda não validada.

---

## Instalar ou atualizar no computador do cliente

**Propriedade intelectual da Yure Digital. Compartilhamento, redistribuição ou revenda sem autorização prévia e expressa são proibidos.** Ver [LICENSE](LICENSE).

1. Baixe o ZIP desta versão pelo botão **Code → Download ZIP** e **extraia tudo** antes de executar.
2. No Windows, abra **INSTALAR-CORTEX-WINDOWS.cmd** com dois cliques. No Mac/Linux, execute `bash install.sh` na pasta extraída.
3. O instalador verifica Python 3.10+, identifica a instalação anterior no destino escolhido e instala ou substitui as **14 skills** (coordenador e 13 especialistas) e seus comandos pelos arquivos do Cortex 2.2. Não é preciso desinstalar a versão anterior nem copiar pastas manualmente.
4. Um backup preserva os arquivos substituídos, inclusive personalizações. Arquivos antigos dentro das pastas Cortex deixam de ficar ativos; skills de terceiros não são removidas.
5. Ao terminar, abra uma nova sessão do Claude Code e digite `/prev`, seguido do caso. Se faltarem pré-requisitos, o instalador informa o próximo passo; não instala Python ou Claude silenciosamente.

Destino padrão: pasta `.claude` do usuário que executa o instalador. Para outra conta ou instalação por projeto, execute no usuário correto ou informe `--dest CAMINHO_DA_PASTA_CLAUDE`. Cópias antigas em outros projetos, perfis ou pastas renomeadas não são apagadas por varredura indiscriminada. Execute a atualização em cada destino utilizado. Feche sessões do Claude que estejam usando as skills durante a atualização.

O pacote funciona como instalador e atualizador **ao ser executado**. Não há serviço oculto, atualização remota contínua ou bloqueio anticópia. A licença proíbe compartilhamento; o repositório público continua tecnicamente acessível.

## ⚡ Instalação pelo terminal

### 1. Baixe o repositório
```bash
git clone https://github.com/Yure98/cortex-agentes.git
cd cortex-agentes
```

### 2. Rode o instalador

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

**Mac / Linux:**
```bash
bash install.sh
```

### 3. Reinicie o Claude Code e teste
```
/prev   /bpc   /especial   /rural   /incapacidade   /auxiliodoenca   /cnis   /peticionar   /decisor   /recurso   /raio-x   /pcd   /maternidade   /pensaopormorte   /auxilioacidente
```

Pronto. Os agentes estão instalados e prontos para usar. ✅

---

## 🤖 Os agentes

| Agente | Comando | O que faz |
|--------|---------|-----------|
| **Estagiário 2.0** | `/peticionar` | Redige petições completas com jurisprudência real dos 5 tribunais (STF, STJ, TNU, TRF5, TRF4), no estilo do escritório. |
| **Analista de CNIS** | `/cnis` | Analisa o CNIS, calcula tempo de contribuição, simula todos os benefícios e monta planejamento previdenciário (8 fases). |
| **Decisor de Aposentadoria** | `/decisor` | Compara cenários e recomenda a melhor opção com modelagem financeira (ponto de equilíbrio, VPL, antecipar × esperar). |
| **Recurso INSS** | `/recurso` | Gera recurso administrativo ao CRPS fundamentado a partir da carta de indeferimento. |
| **Raio-X do CNIS** | `/raio-x` | Triagem rápida de CNIS: tempo aproximado, alertas, pendências, possíveis direitos e veredito. |
| **Aposentadoria PCD** | `/pcd` | Aposentadoria da pessoa com deficiência (LC 142/2013): atendimento, IF-BrA, grau, perícia e peças. |
| **Cortex Maternidade** | `/maternidade` | Salário-maternidade de ponta a ponta: triagem, prova, requerimento, recurso ao CRPS e petição no JEF. |
| **Pensão por Morte** | `/pensaopormorte` | Pensão por morte urbana e rural: entrevista, Índice de Prontidão, dependência, cálculo de cota e duração, DIB/DER, fase administrativa e recursal. |
| **Auxílio-Acidente** | `/auxilioacidente` | Auxílio-acidente urbano e rural: nexo técnico (CAT, NTEP, trajeto, doença ocupacional), Índice de Prontidão Probatória, análise documental prévia, cálculo (50% do SB), cumulação, fase administrativa e recursal. |
| **Benefícios por Incapacidade** | `/incapacidade` (`/auxiliodoenca`) | Auxílio por incapacidade temporária e aposentadoria por incapacidade permanente: triagem funcional, qualidade/carência, perícia, Atestmed, nexo, reabilitação, cessação, precedentes e simulação condicionada. |
| **BPC/LOAS** | `/bpc` | Benefício assistencial para pessoa idosa ou com deficiência: grupo e renda, CadÚnico, biometria, avaliação biopsicossocial, suspensão e revisão; cálculo aritmético condicionado a dados comprovados. |
| **Aposentadoria Especial** | `/especial` | PPP, LTCAT, agentes nocivos, EPI, períodos pré/pós-reforma e ADI 6309; verifica o conflito entre decisão do STF de 2026 e página ainda desatualizada do INSS. |
| **Segurado Especial/Rural** | `/rural` | Categoria, autodeclaração, documentos por período, aposentadoria rural e híbrida; articula maternidade, pensão e incapacidade. |

Cada agente também ativa **automaticamente** por contexto — basta mencionar o tema
(ex: "analisa esse CNIS", "preciso recorrer desse indeferimento").

---

## 📖 Bônus: Bíblia de Prompts

O arquivo [`BIBLIA-DE-PROMPTS-PREVIDENCIARIO.md`](BIBLIA-DE-PROMPTS-PREVIDENCIARIO.md) traz
25+ prompts prontos para tarefas do dia a dia (análise de documentos, atendimento ao cliente,
quesitos de perícia, conteúdo para Instagram e mais). Copie, cole no Claude e use.

---

## 🔗 Como os agentes se conectam

```
  /cnis  →  /decisor  →  /recurso (administrativo)  ou  /peticionar (judicial)
```

Fluxo típico: analisa o CNIS → decide a melhor aposentadoria → recorre no INSS ou ajuíza a ação.

---

## 🗂️ O que o instalador faz

Copia para a sua pasta do Claude:
- `skills/*` → `~/.claude/skills/`
- `commands/*` → `~/.claude/commands/`

Nada além disso. Para desinstalar, basta apagar essas pastas.

---

## ⚠️ Aviso importante

Os agentes são **ferramentas de apoio** ao advogado. Toda saída (petição, cálculo, recurso,
parecer) é uma **minuta** para revisão e assinatura do profissional. Sempre confira
jurisprudência, dispositivos legais e cálculos antes de protocolar. Não substitui o
advogado nem software de cálculo homologado.

---

<p align="center">
  <strong>Cortex</strong> · IA aplicada à advocacia previdenciária<br>
  propriedade intelectual da <strong>Yure Digital</strong>
</p>

## Atualização estrutural de 23/09/2026

Requer Claude Code instalado e Python 3.10 ou superior disponível no terminal. As integrações opcionais com Drive/NotebookLM dependem de configuração própria; sua ausência permite entrega local. Não se declara compatibilidade testada com Cowork nem com uma versão específica do Claude Code.

Após clonar, execute `bash install.sh` no Mac/Linux ou `powershell -ExecutionPolicy Bypass -File install.ps1` no Windows. O instalador guarda a versão anterior e personalizações em um backup, exibe o caminho e o comando de restauração. Não mistura automaticamente personalizações com a nova versão. Skills de terceiros permanecem intactas. Para testar em outra pasta: `python3 scripts/install.py --dest /caminho/de/teste`.

Comece com `/prev` seguido do caso, ou `/bpc`, `/especial`, `/rural`, `/raiox` para triagem, `/cnis` para apuração, `/decisor` para comparar cenários, `/pcd` para LC 142, `/maternidade`, `/incapacidade` (também `/auxiliodoenca`), `/auxilioacidente`, `/pensaopormorte`, `/recurso` ou `/peticionar`. Aliases antigos com acento continuam funcionando; todos encaminham para a mesma skill. Anexe o documento e diga o objetivo; não precisa preencher uma entrevista inteira antes do primeiro diagnóstico.

As skills compartilham dossiê versionado, registro de fontes e quatro portões de revisão. Dados ausentes continuam pendentes. Scripts não substituem enquadramento jurídico e podem recusar casos históricos ou incompletos. Uma revisão bloqueada entrega pendências, nunca uma peça marcada como concluída.

Para manutenção: editar o núcleo em `core/`, executar `python3 scripts/sync_core.py` e `python3 -m unittest discover -s tests -v`. As cópias `.cortex` tornam cada skill autocontida; `python3 scripts/sync_core.py --check` detecta divergências. Dossiês reais ficam em diretório privado fora deste repositório.

## Uma porta de entrada: `/prev`

Depois de instalar esta versão, use `/prev` seguido do relato e do objetivo. O coordenador seleciona e executa a especialista adequada na mesma conversa; se precisar de mais de uma, organiza a sequência e reaproveita o dossiê. Os comandos individuais continuam disponíveis. O pacote tem **14 skills: um coordenador e 13 especialistas**. Para BPC/LOAS vai a `bpc-loas`; exposição nociva/PPP a `aposentadoria-especial`; prova rural e pescador a `segurado-especial-rural`; incapacidade laboral a `beneficios-incapacidade`; sequela consolidada com redução vai a `auxilio-acidente`.

Exemplos:

- `/prev Minha cliente teve a aposentadoria PCD negada. Quero preparar recurso. Seguem decisão e CNIS.`
- `/prev Compare se compensa aposentar agora ou esperar dois anos. Tenho estas simulações...`
- `/prev Dê uma olhada rápida neste CNIS e aponte as pendências.`

Só `/prev`, sem texto, abre espaço para contar o caso. O coordenador não presume benefício ou fatos e não exige que você saiba qual agente escolher. Requer instalação completa das especialistas; não depende de subagentes para funcionar.
