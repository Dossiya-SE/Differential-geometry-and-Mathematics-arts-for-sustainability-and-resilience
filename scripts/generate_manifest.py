"""Generate or verify the repository SHA-256 integrity manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.sha256"
IGNORED_PARTS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".quarto",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "_site",
    "htmlcov",
    "node_modules",
}


def _ignored(path: Path) -> bool:
    return any(part in IGNORED_PARTS or part.endswith(".egg-info") for part in path.parts)


def render() -> str:
    lines: list[str] = []
    for path in sorted(ROOT.rglob("*"), key=lambda item: item.relative_to(ROOT).as_posix()):
        if not path.is_file() or path == MANIFEST:
            continue
        relative = path.relative_to(ROOT)
        if _ignored(relative):
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {relative.as_posix()}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()

    if args.write:
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"wrote {MANIFEST.relative_to(ROOT)} with {len(expected.splitlines())} entries")
        return 0
    if not MANIFEST.exists() or MANIFEST.read_text(encoding="utf-8") != expected:
        print("MANIFEST.sha256 is not synchronized with repository contents")
        return 1
    print(f"verified MANIFEST.sha256 with {len(expected.splitlines())} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
