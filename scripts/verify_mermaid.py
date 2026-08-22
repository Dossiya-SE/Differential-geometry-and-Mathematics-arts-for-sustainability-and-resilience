"""Validate Mermaid sources, embedded diagrams, and renderability."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIFECYCLE_DOC = ROOT / "docs/SCIENTIFIC_RESEARCH_LIFECYCLE.md"
LIFECYCLE_SOURCE = ROOT / "docs/diagrams/MSR_RA_002_SCIENTIFIC_RESEARCH_LIFECYCLE.mmd"
MERMAID_FENCE = re.compile(r"```mermaid[^\n]*\n(.*?)```", re.DOTALL)
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


class MermaidVerificationError(RuntimeError):
    """Raised when Mermaid source integrity or rendering fails."""


def _ignored(path: Path) -> bool:
    return any(part in IGNORED_PARTS or part.endswith(".egg-info") for part in path.parts)


def _markdown_blocks() -> list[tuple[str, str]]:
    diagrams: list[tuple[str, str]] = []
    sources = sorted(list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.qmd")))
    for source in sources:
        relative = source.relative_to(ROOT)
        if _ignored(relative):
            continue
        text = source.read_text(encoding="utf-8")
        for index, block in enumerate(MERMAID_FENCE.findall(text), start=1):
            diagrams.append((f"{relative.as_posix()}#mermaid-{index}", block.strip() + "\n"))
    return diagrams


def _standalone_sources() -> list[tuple[str, str]]:
    diagrams: list[tuple[str, str]] = []
    for source in sorted(ROOT.rglob("*.mmd")):
        relative = source.relative_to(ROOT)
        if _ignored(relative):
            continue
        diagrams.append((relative.as_posix(), source.read_text(encoding="utf-8").strip() + "\n"))
    return diagrams


def check_lifecycle_source_sync() -> None:
    if not LIFECYCLE_DOC.is_file():
        raise MermaidVerificationError(f"missing lifecycle document: {LIFECYCLE_DOC.relative_to(ROOT)}")
    if not LIFECYCLE_SOURCE.is_file():
        raise MermaidVerificationError(
            f"missing lifecycle Mermaid source: {LIFECYCLE_SOURCE.relative_to(ROOT)}"
        )

    authoritative = LIFECYCLE_SOURCE.read_text(encoding="utf-8").strip()
    embedded = [block.strip() for block in MERMAID_FENCE.findall(LIFECYCLE_DOC.read_text(encoding="utf-8"))]
    if authoritative not in embedded:
        raise MermaidVerificationError(
            "the authoritative MSR-RA-002 .mmd source and embedded lifecycle diagram have drifted"
        )

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if not MERMAID_FENCE.search(readme):
        raise MermaidVerificationError("README.md must retain the executive Mermaid architecture")


def _render_one(mmdc: str, label: str, source: str, workdir: Path, index: int) -> None:
    input_path = workdir / f"diagram-{index:03d}.mmd"
    output_path = workdir / f"diagram-{index:03d}.svg"
    input_path.write_text(source, encoding="utf-8")

    completed = subprocess.run(
        [mmdc, "-i", str(input_path), "-o", str(output_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        details = (completed.stderr or completed.stdout).strip()
        raise MermaidVerificationError(f"Mermaid render failed for {label}: {details}")
    if not output_path.is_file() or output_path.stat().st_size < 100:
        raise MermaidVerificationError(f"Mermaid render produced no usable SVG for {label}")
    rendered = output_path.read_text(encoding="utf-8")
    if "<svg" not in rendered or "</svg>" not in rendered:
        raise MermaidVerificationError(f"Mermaid render is not a complete SVG for {label}")


def check_renderability(*, require_cli: bool) -> int:
    mmdc = shutil.which("mmdc")
    if mmdc is None:
        if require_cli:
            raise MermaidVerificationError("mmdc is required; install @mermaid-js/mermaid-cli")
        print("SKIP  Mermaid rendering (mmdc not installed); source-integrity checks still passed")
        return 0

    diagrams = _standalone_sources() + _markdown_blocks()
    if not diagrams:
        raise MermaidVerificationError("no Mermaid diagrams were discovered")

    with tempfile.TemporaryDirectory(prefix="msr-mermaid-") as temporary:
        workdir = Path(temporary)
        for index, (label, source) in enumerate(diagrams, start=1):
            _render_one(mmdc, label, source, workdir, index)

    return len(diagrams)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-cli",
        action="store_true",
        help="fail when the Mermaid CLI is unavailable instead of performing source-only checks",
    )
    args = parser.parse_args()

    try:
        check_lifecycle_source_sync()
        print("PASS  MSR-RA-002 Mermaid source and embedded diagram are synchronized")
        rendered = check_renderability(require_cli=args.require_cli)
        if rendered:
            print(f"PASS  rendered {rendered} Mermaid diagram source(s) to valid SVG")
    except (MermaidVerificationError, OSError) as error:
        print(f"FAIL  {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
