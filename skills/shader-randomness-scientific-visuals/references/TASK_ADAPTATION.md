# Task-aware visual adaptation contracts

Read `SKILL.md` and `CHAPTER_10_LESSONS.md` first. Classification and scientific purpose always precede style, effects, or shader implementation.

## Animation

**Question:** What mathematically meaningful quantity changes? Supply map `F(x,t,theta)`, parameter ranges, a declared meaning for time, and a paused state. Chapter 10's moving rows are a *display-time teaching fixture only*. Genuine resilience animations require `x'(t)=f(x,u,w)` or another explicit, validated governing model and defined physical time/units. Verify initial/end states, any conserved quantities, time-step dependence and reduced-motion fallback. Do not interpolate discrete failures as though intermediate states were physically realizable.

## Diagram

**Question:** Which nodes and edges have a semantic relationship? Author a typed node/edge table before layout. A seed may break ties in non-semantic placement; it may not create, delete, or orient causal edges. Distinguish association, physical dependency, hypothesis, information transfer and process flow with labels and the repository's evidence-line convention. Test edge inventory against the source. Produce a static SVG with large arrows only for declared directed relations.

## Mind map

**Question:** What is the parent-child hierarchy? Author a controlled concept taxonomy; any deterministic random jitter may be used *only* to resolve equal-rank label collisions. Mind maps encode conceptual membership, not empirical dependence or causality. Verify every concept appears once, each node has one declared parent (except root), and text remains readable at export scale. Prefer no arrows: use connective lines.

## Chart

**Question:** What observations, estimands, units and uncertainty are being compared? Use measured data or an explicitly synthetic/theoretical dataset. L2 may produce a theoretical curve under an ideal uniform input; the sine demonstration L1 and tile L5 must never be promoted to observations. State sample size, seed for simulated samples, binning and axis labels. Test aggregation, transformations and confidence intervals independently; avoid random decorative marks and misleading axes.

## Mathematical figure

**Question:** What set, mapping, geometry or theorem is depicted? Provide a numbered equation, declared domain/codomain, fixed parameters, coordinate labels, and singularities/discretization bounds. L3–L5 are appropriate for mathematical tilings; L7 for a *labelled synthetic interpolated field*. Require deterministic paths and a vector SVG fallback. Visual complexity must not obscure the mathematical statement.

## Sustainability and resilience application

A spatially plausible-looking random heat map is **not** an observed heat exposure surface. A row animation is **not** traffic recovery. A Truchet layout is **not** an infrastructure network. Before any research transfer, require:
1. explicit infrastructure/physical domain selection through the repository protocol;
2. mechanism and units connecting the random variable or field to system states;
3. distributional or covariance assumptions, calibrated with traceable evidence;
4. propagation of uncertainties through the *actual* governing model;
5. sensitivity and out-of-distribution tests;
6. validation bounded to a stated purpose, time and geography.

The domain-neutral core remains `NOT_SELECTED`. A teaching sample may use synthetic values only if visibly labeled **illustrative synthetic mathematics — no empirical claims**.

## Deliverable format for every task

Specify: title/message, artifact class and scientific question; exact math and source authority; input data/provenance and evidence status; coordinate/time/scale semantics; generator and fixed seeds; visual encoding and static alternative; numerical/unit/accessibility tests; known limits and promotion gate. Do not use vague terms such as "high-rigor" in place of actual checks.

## Publishing thresholds

- **PROPOSED:** definitions and generation exist, limitations documented.
- **REFERENCE_VERIFIED:** declared reference tests and reproducibility pass; does not mean application validation.
- **MATHEMATICAL-ART REVIEWED:** independent source/projection/renderer/accessibility review with documented device evidence.
- **APPLICATION VALIDATED:** separately justified evidence-based external evaluation for the exact use and domain; never inferred from earlier states.
