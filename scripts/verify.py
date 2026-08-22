"""Portable evidence-to-publication verification for the MSR research platform."""

from __future__ import annotations

import argparse
import compileall
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "README.md",
    "CITATION.cff",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "LICENSES/README.md",
    "pyproject.toml",
    "_quarto.yml",
    "docs/REPOSITORY_ARCHITECTURE.md",
    "docs/RESEARCH_INTEGRITY.md",
    "literature_review/application_selection/DECISION_STATUS.yaml",
    "literature_review/protocol/CHAIN_ARCHITECTURE.yaml",
    "mathematics/model_contracts/MSR-MOD-0001.json",
    "experiments/registry/MSR-EXP-0001.json",
    "schemas/model-contract.schema.json",
    "schemas/experiment.schema.json",
    "art/VISUAL_ENCODING_STANDARD.md",
    "art/design_tokens.json",
    "figures/generated/MSR-FIG-0001_sphere-geodesic.svg",
    "figures/generated/MSR-FIG-0001.provenance.json",
    "MANIFEST.sha256",
)

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


class VerificationError(RuntimeError):
    """Raised when a repository quality gate fails."""


def _run(command: list[str], *, env: dict[str, str] | None = None) -> None:
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def check_required_paths() -> None:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).is_file()]
    if missing:
        raise VerificationError(f"missing required files: {', '.join(missing)}")


def check_python() -> None:
    if not compileall.compile_dir(ROOT / "src", quiet=1):
        raise VerificationError("Python package compilation failed")
    if not compileall.compile_dir(ROOT / "scripts", quiet=1):
        raise VerificationError("Python script compilation failed")

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    suite = ROOT / "tests"
    _run([sys.executable, "-m", "unittest", "discover", "-s", str(suite), "-v"], env=env)
    _run([sys.executable, "scripts/run_reference_experiment.py", "--check"], env=env)


def _load_json(path: Path) -> dict[str, Any]:
    value: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise VerificationError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def _fallback_record_check(record: dict[str, Any], schema: dict[str, Any], path: Path) -> None:
    required = schema.get("required", [])
    if not isinstance(required, list):
        raise VerificationError("schema required field must be an array")
    missing = [str(key) for key in required if key not in record]
    if missing:
        raise VerificationError(f"{path.relative_to(ROOT)} missing keys: {', '.join(missing)}")


def check_schemas(*, strict_tools: bool) -> None:
    pairs = (
        (
            ROOT / "schemas/model-contract.schema.json",
            ROOT / "mathematics/model_contracts/MSR-MOD-0001.json",
        ),
        (
            ROOT / "schemas/experiment.schema.json",
            ROOT / "experiments/registry/MSR-EXP-0001.json",
        ),
    )

    jsonschema_available = importlib.util.find_spec("jsonschema") is not None
    if strict_tools and not jsonschema_available:
        raise VerificationError("strict verification requires jsonschema")

    for schema_path, record_path in pairs:
        schema = _load_json(schema_path)
        record = _load_json(record_path)
        if jsonschema_available:
            from jsonschema import Draft202012Validator  # type: ignore[import-untyped]

            validator = Draft202012Validator(schema)
            errors = sorted(validator.iter_errors(record), key=lambda error: list(error.path))
            if errors:
                messages = "; ".join(error.message for error in errors)
                raise VerificationError(f"{record_path.relative_to(ROOT)}: {messages}")
        else:
            _fallback_record_check(record, schema, record_path)


def check_research_boundaries() -> None:
    decision = (ROOT / "literature_review/application_selection/DECISION_STATUS.yaml").read_text(
        encoding="utf-8"
    )
    required_not_selected = (
        "application_domain",
        "system_boundary",
        "hazard_or_stressor",
        "sustainability_outcome",
        "resilience_outcome",
        "geography",
        "demonstrator",
    )
    for key in required_not_selected:
        if not re.search(rf"^\s*{re.escape(key)}:\s*[\"']?NOT_SELECTED[\"']?\s*$", decision, re.M):
            raise VerificationError(f"decision boundary failed for {key}")

    architecture = (ROOT / "literature_review/protocol/CHAIN_ARCHITECTURE.yaml").read_text(
        encoding="utf-8"
    )
    identifiers = re.findall(r'^\s*-\s+id:\s*["\']?(C[0-9]{2})', architecture, re.M)
    expected = [f"C{index:02d}" for index in range(1, 11)]
    if identifiers != expected:
        raise VerificationError(
            f"chain identifiers must be exactly {expected}; found {identifiers}"
        )
    if 'application_decision: "NOT_SELECTED"' not in architecture:
        raise VerificationError(
            "chain architecture must preserve application_decision=NOT_SELECTED"
        )

    forbidden = ("power-water-transportation", "p-w-t-sw", "urban flooding")
    for path in (ROOT / "src").rglob("*.py"):
        lowered = path.read_text(encoding="utf-8").lower()
        if any(term in lowered for term in forbidden):
            raise VerificationError(f"domain-specific core term found in {path.relative_to(ROOT)}")


def _bibliography_keys() -> set[str]:
    keys: set[str] = set()
    for path in (ROOT / "literature_review").rglob("*.bib"):
        text = path.read_text(encoding="utf-8")
        keys.update(re.findall(r"^@[A-Za-z]+\{([^,]+),", text, re.M))
    return keys


def check_citations() -> None:
    available = _bibliography_keys()
    model = _load_json(ROOT / "mathematics/model_contracts/MSR-MOD-0001.json")
    evidence = model.get("evidence")
    if not isinstance(evidence, dict):
        raise VerificationError("model evidence object is missing")
    requested = evidence.get("citation_keys")
    if not isinstance(requested, list):
        raise VerificationError("model citation_keys must be an array")
    missing = sorted(str(key) for key in requested if str(key) not in available)
    if missing:
        raise VerificationError(f"model citation keys missing from bibliography: {missing}")


def check_internal_links() -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    failures: list[str] = []
    for path in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.qmd")):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        for raw_target in link_pattern.findall(path.read_text(encoding="utf-8")):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                failures.append(f"{path.relative_to(ROOT)} -> {target}")
    if failures:
        raise VerificationError("broken internal links: " + "; ".join(sorted(failures)))


def check_figure_provenance() -> None:
    provenance = _load_json(ROOT / "figures/generated/MSR-FIG-0001.provenance.json")
    required = {
        "figure_id",
        "model_id",
        "experiment_id",
        "artifact_class",
        "mathematical_validity",
        "communication_impact",
        "alt_text",
        "source",
    }
    missing = sorted(required - provenance.keys())
    if missing:
        raise VerificationError(f"figure provenance missing keys: {missing}")
    if provenance["communication_impact"] != "NOT_EVALUATED":
        raise VerificationError("foundation figure must not claim evaluated communication impact")
    svg = (ROOT / "figures/generated/MSR-FIG-0001_sphere-geodesic.svg").read_text(encoding="utf-8")
    for token in ("<title", "<desc", 'data-figure-id="MSR-FIG-0001"'):
        if token not in svg:
            raise VerificationError(f"SVG accessibility/provenance token missing: {token}")

    _run([sys.executable, "scripts/generate_reference_figure.py", "--check"])


def _manifest_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.name == "MANIFEST.sha256":
            continue
        if any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts):
            continue
        files.append(path)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def check_manifest() -> None:
    manifest_path = ROOT / "MANIFEST.sha256"
    recorded: dict[str, str] = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, relative = line.split("  ", 1)
        recorded[relative] = digest

    current_paths = {path.relative_to(ROOT).as_posix(): path for path in _manifest_files()}
    if set(recorded) != set(current_paths):
        missing = sorted(set(current_paths) - set(recorded))
        extra = sorted(set(recorded) - set(current_paths))
        raise VerificationError(f"manifest file set mismatch; missing={missing}, extra={extra}")

    mismatches = []
    for relative, path in current_paths.items():
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != recorded[relative]:
            mismatches.append(relative)
    if mismatches:
        raise VerificationError(f"manifest checksum mismatch: {sorted(mismatches)}")


def check_document_sources(*, strict_tools: bool) -> None:
    quarto = shutil.which("quarto")
    pandoc = shutil.which("pandoc")
    if strict_tools and quarto is None:
        raise VerificationError("strict verification requires Quarto")

    with tempfile.TemporaryDirectory(prefix="msr-docs-") as output_dir:
        if quarto is not None:
            _run([quarto, "render", "--output-dir", output_dir])
        elif pandoc is not None:
            for source in sorted((ROOT / "docs").glob("*.qmd")):
                output = Path(output_dir) / f"{source.stem}.html"
                _run([pandoc, str(source), "--standalone", "--output", str(output)])
        else:
            raise VerificationError("Quarto or Pandoc is required to validate documentation")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict-tools",
        action="store_true",
        help="require the complete controlled CI toolchain rather than portable fallbacks",
    )
    args = parser.parse_args()

    checks = (
        ("required repository objects", check_required_paths),
        ("Python package, tests, and reference experiment", check_python),
        ("model and experiment schemas", lambda: check_schemas(strict_tools=args.strict_tools)),
        ("application and chain boundaries", check_research_boundaries),
        ("bibliography crosswalk", check_citations),
        ("internal documentation links", check_internal_links),
        ("figure provenance and accessibility", check_figure_provenance),
        ("repository checksum manifest", check_manifest),
        (
            "publication source rendering",
            lambda: check_document_sources(strict_tools=args.strict_tools),
        ),
    )

    try:
        for label, check in checks:
            check()
            print(f"PASS  {label}")
    except (
        VerificationError,
        OSError,
        subprocess.CalledProcessError,
        json.JSONDecodeError,
    ) as error:
        print(f"FAIL  {error}", file=sys.stderr)
        return 1

    print("PASS  MSR portable verification completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
