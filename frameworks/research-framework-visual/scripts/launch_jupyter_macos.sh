#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="${VENV_PATH:-$ROOT/.venv}"
PYTHON="$VENV/bin/python"

if [[ ! -x "$PYTHON" ]]; then
  echo "Missing venv interpreter: $PYTHON" >&2
  echo "Run scripts/bootstrap_macos.sh first." >&2
  exit 2
fi

cd "$ROOT"
"$PYTHON" -m framework doctor --strict --notebook

# Invoke Notebook through the exact venv interpreter. This prevents a shell
# alias/hash or an active Conda base environment from selecting another
# Jupyter installation.
exec "$PYTHON" -m notebook
