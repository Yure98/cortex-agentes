#!/usr/bin/env bash
# Cortex — Instalador (Mac / Linux)
# Uso: clone o repo e rode  ->  bash install.sh
set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE="$HOME/.claude"
SKILLS="$CLAUDE/skills"
CMDS="$CLAUDE/commands"

echo ""
echo "=================================================="
echo "  CORTEX - Agentes de IA para Advocacia"
echo "  Instalando no Claude Code..."
echo "=================================================="
echo ""

mkdir -p "$SKILLS" "$CMDS"

# Skills
for dir in "$ROOT"/skills/*/; do
  name="$(basename "$dir")"
  rm -rf "$SKILLS/$name"
  cp -r "$dir" "$SKILLS/$name"
  echo "  [skill]   $name"
done

# Comandos
for f in "$ROOT"/commands/*.md; do
  cp -f "$f" "$CMDS/"
  echo "  [comando] /$(basename "$f" .md)"
done

echo ""
echo "Instalacao concluida!"
echo "Reinicie o Claude Code e teste:  /cnis  /peticionar  /decisor  /recurso"
echo ""
