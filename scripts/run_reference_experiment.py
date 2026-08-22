"""Execute the registered two-sphere round-trip verification experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import numpy.typing as npt

from msr.geometry.sphere import distance, normalize, round_trip_residual

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "experiments/registry/MSR-EXP-0001.json"


def _load_record() -> dict[str, Any]:
    value: Any = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("experiment registry must contain a JSON object")
    return value


def _point(rng: np.random.Generator) -> npt.NDArray[np.float64]:
    return normalize(rng.normal(size=3))


def execute() -> dict[str, int | float | str]:
    """Run the deterministic registered sample and return its measured summary."""
    record = _load_record()
    execution = record["execution"]
    parameters = record["parameters"]
    seed = int(execution["random_seed"])
    sample_size = int(parameters["sample_size"])
    cut_margin = float(parameters["cut_locus_margin_radians"])
    threshold = float(record["acceptance_rule"]["threshold"])

    rng = np.random.default_rng(seed)
    residuals: list[float] = []
    minimum_cut_margin = float("inf")

    while len(residuals) < sample_size:
        base = _point(rng)
        target = _point(rng)
        angle = distance(base, target)
        margin = float(np.pi - angle)
        if margin <= cut_margin:
            continue
        residuals.append(round_trip_residual(base, target))
        minimum_cut_margin = min(minimum_cut_margin, margin)

    maximum = max(residuals)
    return {
        "experiment_id": str(record["experiment_id"]),
        "model_id": str(record["model_id"]),
        "sample_size": sample_size,
        "random_seed": seed,
        "maximum_round_trip_residual": maximum,
        "mean_round_trip_residual": float(np.mean(residuals)),
        "minimum_cut_locus_margin_radians": minimum_cut_margin,
        "acceptance_threshold": threshold,
        "status": "PASS" if maximum <= threshold else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="return a nonzero exit status when the registered acceptance rule fails",
    )
    args = parser.parse_args()
    result = execute()
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.check and result["status"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
