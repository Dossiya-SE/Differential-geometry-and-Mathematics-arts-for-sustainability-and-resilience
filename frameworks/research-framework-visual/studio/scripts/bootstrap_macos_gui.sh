#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

fail() {
  printf 'ERROR: %s\n' "$1" >&2
  exit 1
}

command -v node >/dev/null 2>&1 || fail "Node.js is required. Install Node 22 LTS or newer."
command -v npm >/dev/null 2>&1 || fail "npm is required."
command -v rustc >/dev/null 2>&1 || fail "Rust is required. Install it from https://rustup.rs and reopen Terminal."
command -v cargo >/dev/null 2>&1 || fail "Cargo is required."
xcode-select -p >/dev/null 2>&1 || fail "Xcode Command Line Tools are required. Run: xcode-select --install"

NODE_MAJOR="$(node -p 'Number(process.versions.node.split(`.`)[0])')"
if (( NODE_MAJOR < 22 )); then
  fail "Node 22 or newer is required; detected $(node --version)."
fi

printf 'Node: %s\n' "$(node --version)"
printf 'npm: %s\n' "$(npm --version)"
printf 'Rust: %s\n' "$(rustc --version)"
printf 'Cargo: %s\n' "$(cargo --version)"
printf 'Xcode tools: %s\n' "$(xcode-select -p)"

npm install --no-audit --no-fund
npm run check
npm run desktop:check

cat <<'EOF'

PASS — desktop GUI prerequisites and source checks completed.

Development native GUI:
  npm run gui

Build installable macOS application:
  npm run gui:build -- --bundles dmg

The .dmg will be written under:
  src-tauri/target/release/bundle/dmg/
EOF
