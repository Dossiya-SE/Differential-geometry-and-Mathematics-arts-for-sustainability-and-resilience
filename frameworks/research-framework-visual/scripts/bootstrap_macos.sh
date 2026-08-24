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

"$BOOTSTRAP_PYTHON" -m venv "$VENV"
VENV_PYTHON="$VENV/bin/python"

"$VENV_PYTHON" -m pip install --upgrade pip
"$VENV_PYTHON" -m pip install -e '.[dev,notebook]'
"$VENV_PYTHON" -m ipykernel install --user \
  --name research-framework-visual \
  --display-name 'Python (Research Framework Visual)'

if ! "$VENV_PYTHON" -m framework doctor --strict --notebook; then
  cat >&2 <<'EOF'
Environment validation failed.

If the failure mentions CairoSVG/native Cairo and Homebrew is available, install:
  brew install cairo libffi

Then rerun:
  .venv/bin/python -m framework doctor --strict --notebook

Do not fall back to /opt/anaconda3/bin/jupyter when this venv is intended.
EOF
  exit 3
fi

cat <<EOF
macOS environment is ready.

Exact interpreter:
  $VENV_PYTHON

Render:
  $VENV_PYTHON -m framework render --request render_requests/Research_Framework_V4.yaml

Launch Jupyter without Conda/base leakage:
  bash $ROOT/scripts/launch_jupyter_macos.sh
EOF
