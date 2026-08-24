# Research Framework Visual

Automated mathematical–computational framework renderer integrated into this repository.

## Purpose

This module provides a reproducible pipeline for:

- declarative research-framework specifications;
- mathematical/scientific panel generation;
- SVG, PNG, and PDF export;
- automated validation;
- GitHub Actions rendering;
- future visual-regression testing against approved baselines.

## Local use

```bash
cd frameworks/research-framework-visual
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
python -m framework build
```

Outputs are written to `exports/`.

## Scientific boundary

The current miniature plots are deterministic illustrative placeholders. They must be replaced with real evidence, computation, calibration, validation, sensitivity, uncertainty, and comparison outputs before they are presented as empirical research results.

## Automation

The repository workflow `.github/workflows/render-research-framework.yml` runs tests, builds the framework, validates the artifact contract, and uploads exports as a GitHub Actions artifact.
