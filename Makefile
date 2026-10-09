PYTHON ?= python3
PYTHONPATH := src

.PHONY: help verify verify-ci test webtest visualsuite lint typecheck experiment docs clean

help:
	@echo "MSR research-platform commands"
	@echo "  make verify      Run the portable evidence-to-publication checks"
	@echo "  make verify-ci   Run installed development tools plus portable checks"
	@echo "  make test        Run the complete Python test suite"
	@echo "  make webtest     Run dependency-free Node.js mathematical browser-kernel tests"
	@echo "  make visualsuite  Verify five deterministic SVG visual types"
	@echo "  make experiment  Reproduce the reference geometry experiment"
	@echo "  make docs        Render the Quarto site or validate with Pandoc"

verify:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/verify.py

verify-ci: lint typecheck test webtest
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/verify.py --strict-tools

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m pytest -q

webtest:
	node --test art/shaders/inversion_lab/probe.test.mjs skills/shader-randomness-scientific-visuals/examples/random_fields.test.mjs art/visual_suite/render.test.mjs art/animations/viability_lab/model.test.mjs
	node skills/shader-randomness-scientific-visuals/examples/render_static.mjs --check
	node art/visual_suite/render.mjs --check

visualsuite:
	node art/visual_suite/render.mjs --check

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
