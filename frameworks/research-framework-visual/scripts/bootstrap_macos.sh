#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This bootstrap is intended for macOS." >&2
  exit 2
fi

BOOTSTRAP_PYTHON="${PYTHON_BOOTSTRAP:-python3}"
VENV="${VENV_PATH:-$ROOT/.venv}"

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required to provision native Cairo on macOS." >&2
  echo "Install Homebrew, then rerun this bootstrap." >&2
  exit 3
fi

brew list cairo >/dev/null 2>&1 || brew install cairo
brew list libffi >/dev/null 2>&1 || brew install libffi

CAIRO_PREFIX="$(brew --prefix cairo)"
LIBFFI_PREFIX="$(brew --prefix libffi)"
export DYLD_FALLBACK_LIBRARY_PATH="$CAIRO_PREFIX/lib:${DYLD_FALLBACK_LIBRARY_PATH:-/opt/homebrew/lib}"
export PKG_CONFIG_PATH="$CAIRO_PREFIX/lib/pkgconfig:$LIBFFI_PREFIX/lib/pkgconfig:${PKG_CONFIG_PATH:-}"
export LDFLAGS="-L$CAIRO_PREFIX/lib -L$LIBFFI_PREFIX/lib ${LDFLAGS:-}"
export CPPFLAGS="-I$CAIRO_PREFIX/include -I$LIBFFI_PREFIX/include ${CPPFLAGS:-}"

"$BOOTSTRAP_PYTHON" -m venv "$VENV"
VENV_PYTHON="$VENV/bin/python"

"$VENV_PYTHON" -m pip install --upgrade pip
"$VENV_PYTHON" -m pip install -e '.[dev,notebook]'
"$VENV_PYTHON" -m ipykernel install --user \
  --name research-framework-visual \
  --display-name 'Python (Research Framework Visual)'

if ! "$VENV_PYTHON" -m framework doctor --strict --notebook; then
  cat >&2 <<EOF
Environment validation failed.

Native Cairo prefix:
  $CAIRO_PREFIX

Exact Python:
  $VENV_PYTHON

Rerun the diagnostic with the same native-library path:
  DYLD_FALLBACK_LIBRARY_PATH="$CAIRO_PREFIX/lib:/opt/homebrew/lib" \\
  $VENV_PYTHON -m framework doctor --strict --notebook

Do not fall back to /opt/anaconda3/bin/jupyter when this venv is intended.
EOF
  exit 4
fi

cat <<EOF
macOS environment is ready.

Exact interpreter:
  $VENV_PYTHON

Native Cairo:
  $CAIRO_PREFIX

Render:
  DYLD_FALLBACK_LIBRARY_PATH="$CAIRO_PREFIX/lib:/opt/homebrew/lib" \\
  $VENV_PYTHON -m framework render --request render_requests/Research_Framework_V4.yaml

Launch Jupyter without Conda/base leakage:
  bash $ROOT/scripts/launch_jupyter_macos.sh
EOF
