# 🧠 Cortex — Agentes de IA para Advocacia Previdenciária

Transforme o **Claude** numa equipe previdenciária completa. Quatro agentes especializados
que redigem petições, analisam CNIS, decidem a melhor aposentadoria e geram recursos ao INSS —
tudo com jurisprudência real e sem invenção.

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
/cnis        /peticionar        /decisor        /recurso
```

Pronto. Os agentes estão instalados e prontos para usar. ✅

---

## 🤖 Os 4 agentes

| Agente | Comando | O que faz |
|--------|---------|-----------|
| **Estagiário 2.0** | `/peticionar` | Redige petições completas com jurisprudência real dos 5 tribunais (STF, STJ, TNU, TRF5, TRF4), no estilo do escritório. |
| **Analista de CNIS** | `/cnis` | Analisa o CNIS, calcula tempo de contribuição, simula todos os benefícios e monta planejamento previdenciário (8 fases). |
| **Decisor de Aposentadoria** | `/decisor` | Compara cenários e recomenda a melhor opção com modelagem financeira (ponto de equilíbrio, VPL, antecipar × esperar). |
| **Recurso INSS** | `/recurso` | Gera recurso administrativo ao CRPS fundamentado a partir da carta de indeferimento. |

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
