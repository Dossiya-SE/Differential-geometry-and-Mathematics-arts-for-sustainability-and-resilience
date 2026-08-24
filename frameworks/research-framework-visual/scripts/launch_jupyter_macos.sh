#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="${VENV_PATH:-$ROOT/.venv}"
PYTHON="$VENV/bin/python"

if [[ ! -x "$PYTHON" ]]; then
  echo "Missing venv interpreter: $PYTHON" >&2
  echo "Run: bash scripts/bootstrap_macos.sh" >&2
  exit 2
fi

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required to locate native Cairo." >&2
  exit 3
fi

CAIRO_PREFIX="$(brew --prefix cairo)"
LIBFFI_PREFIX="$(brew --prefix libffi)"
export DYLD_FALLBACK_LIBRARY_PATH="$CAIRO_PREFIX/lib:${DYLD_FALLBACK_LIBRARY_PATH:-/opt/homebrew/lib}"
export PKG_CONFIG_PATH="$CAIRO_PREFIX/lib/pkgconfig:$LIBFFI_PREFIX/lib/pkgconfig:${PKG_CONFIG_PATH:-}"

cd "$ROOT"
"$PYTHON" -m framework doctor --strict --notebook

# Invoke Notebook through the exact venv interpreter. This prevents a shell
# alias/hash or an active Conda base environment from selecting another
# Jupyter installation.
exec "$PYTHON" -m notebook
