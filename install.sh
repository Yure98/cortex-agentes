#!/usr/bin/env bash
# Cortex — Mac/Linux. O instalador preserva backup e reverte em caso de falha.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
command -v python3 >/dev/null || { echo 'Instale Python 3.10 ou superior.' >&2; exit 1; }
exec python3 "$ROOT/scripts/install.py" "$@"
