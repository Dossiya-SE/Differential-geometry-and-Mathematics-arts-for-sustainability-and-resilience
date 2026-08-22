PYTHON ?= python3
PYTHONPATH := src

.PHONY: help verify verify-ci test lint typecheck experiment docs clean

help:
	@echo "MSR research-platform commands"
	@echo "  make verify      Run the portable evidence-to-publication checks"
	@echo "  make verify-ci   Run installed development tools plus portable checks"
	@echo "  make test        Run the complete Python test suite"
	@echo "  make experiment  Reproduce the reference geometry experiment"
	@echo "  make docs        Render the Quarto site or validate with Pandoc"

verify:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/verify.py

verify-ci: lint typecheck test
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/verify.py --strict-tools

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check src tests scripts
	$(PYTHON) -m ruff format --check src tests scripts

typecheck:
	MYPYPATH=$(PYTHONPATH) $(PYTHON) -m mypy src scripts

experiment:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/run_reference_experiment.py --check

docs:
	@if command -v quarto >/dev/null 2>&1; then quarto render; \
	elif command -v pandoc >/dev/null 2>&1; then pandoc docs/index.qmd --standalone --output /tmp/msr-docs.html; \
	else echo "Neither Quarto nor Pandoc is available" >&2; exit 1; fi

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache .quarto _site htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
