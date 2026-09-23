# 🧠 Cortex — Agentes de IA para Advocacia Previdenciária

Transforme o **Claude** numa equipe previdenciária completa. Agentes especializados
que redigem petições, analisam CNIS, decidem a melhor aposentadoria, geram recursos ao INSS
e cuidam de salário-maternidade e da aposentadoria da pessoa com deficiência, tudo com
jurisprudência real e sem invenção.

Funciona no **Claude Code** e no **Claude Cowork**.

---

## ⚡ Instalação rápida

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
/cnis   /peticionar   /decisor   /recurso   /raio-x   /pcd   /maternidade   /pensaopormorte   /auxilioacidente
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
  desenvolvido por <strong>Vértika</strong>
</p>

## Atualização estrutural de 23/09/2026

Requer Claude Code instalado e Python 3.10 ou superior disponível no terminal. As integrações opcionais com Drive/NotebookLM dependem de configuração própria; sua ausência permite entrega local. Não se declara compatibilidade testada com Cowork nem com uma versão específica do Claude Code.

Após clonar, execute `bash install.sh` no Mac/Linux ou `powershell -ExecutionPolicy Bypass -File install.ps1` no Windows. O instalador guarda a versão anterior e personalizações em um backup, exibe o caminho e o comando de restauração. Não mistura automaticamente personalizações com a nova versão. Skills de terceiros permanecem intactas. Para testar em outra pasta: `python3 scripts/install.py --dest /caminho/de/teste`.

Comece com `/raiox` para triagem, `/cnis` para apuração, `/decisor` para comparar cenários, `/pcd` para LC 142, `/maternidade`, `/auxilioacidente`, `/pensaopormorte`, `/recurso` ou `/peticionar`. Aliases antigos com acento continuam funcionando; todos encaminham para a mesma skill. Anexe o documento e diga o objetivo; não precisa preencher uma entrevista inteira antes do primeiro diagnóstico.

As nove skills compartilham dossiê versionado, registro de fontes e quatro portões de revisão. Dados ausentes continuam pendentes. Scripts não substituem enquadramento jurídico e podem recusar casos históricos ou incompletos. Uma revisão bloqueada entrega pendências, nunca uma peça marcada como concluída.

Para manutenção: editar o núcleo em `core/`, executar `python3 scripts/sync_core.py` e `python3 -m unittest discover -s tests -v`. As cópias `.cortex` tornam cada skill autocontida; `python3 scripts/sync_core.py --check` detecta divergências. Dossiês reais ficam em diretório privado fora deste repositório.

## Uma porta de entrada: `/prev`

Depois de instalar esta versão, use `/prev` seguido do relato e do objetivo. O coordenador seleciona e executa a especialista adequada na mesma conversa; se precisar de mais de uma, organiza a sequência e reaproveita o dossiê. Os comandos individuais continuam disponíveis. O pacote passa a ter dez skills: um coordenador e nove especialistas.

Exemplos:

- `/prev Minha cliente teve a aposentadoria PCD negada. Quero preparar recurso. Seguem decisão e CNIS.`
- `/prev Compare se compensa aposentar agora ou esperar dois anos. Tenho estas simulações...`
- `/prev Dê uma olhada rápida neste CNIS e aponte as pendências.`

Só `/prev`, sem texto, abre espaço para contar o caso. O coordenador não presume benefício ou fatos e não exige que você saiba qual agente escolher. Requer instalação completa das especialistas; não depende de subagentes para funcionar.
