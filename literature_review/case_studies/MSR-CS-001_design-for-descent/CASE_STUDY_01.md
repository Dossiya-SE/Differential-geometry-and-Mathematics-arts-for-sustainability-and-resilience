---
title: "Design Grammars for Sustainable Resilience: A Critical Transfer Review of Design for Descent"
review_id: "MSR-CS-001"
review_author: "Dossiya Dakou"
version: "0.3.0"
date: "2026-08-22"
status: "Main paper reviewed; artifact inventory and reproduction open"
evidence_cutoff: "2026-08-22"
primary_source_status: "OBSERVED - complete 11-page main paper; supplement not found after documented search"\nreproduction_status: "NOT_STARTED"
---

# Design Grammars for Sustainable Resilience

## A critical transfer review of *Design for Descent: What Makes a Shape Grammar Easy to Optimize?*

### Abstract

This case study critically examines Kodnongbua et al.'s *Design for Descent* as the first paper in the literature review for **Mathematics Exploration for Sustainable Resilience: Differential Geometry and Mathematical Art for Sustainability and Resilience**. The source introduces Stochastic Rewrite Descent (SRD), a mixed discrete-continuous optimization method for shape grammars, and identifies reversibility, jump continuity, local geometric control, and repairability as properties that make grammar-defined design spaces more amenable to gradient-based optimization. Full-text extraction, equation verification, table inspection, and visual review show strong direct contributions to procedural geometry, inverse design, topology optimization, and mathematical art. The paper does not directly implement differential geometry, sustainability assessment, climate hazards, infrastructure resilience, critical-service continuity, equity, or uncertainty quantification. It is therefore classified as a transferable mathematical method, geometric-design study, and visualization study (`M + G + V`), not a direct sustainable-resilience application. Building on its reviewed formalism, this review proposes only a domain-neutral research abstraction: discrete configurations connected by rewrite maps, with continuous state strata carrying justified dynamics, admissibility constraints, and possibly intrinsic metrics. It does not select an application system or demonstrator. The extension is explicitly labeled `PROPOSED`. The central finding is that sustainable-resilience optimization requires not only a capable optimizer but also a representation designed for feasible intervention, correction, adaptation, and verification.

**Keywords:** shape grammar; mixed discrete-continuous optimization; stochastic rewrite descent; procedural geometry; mathematical art; sustainable resilience; viability; hybrid systems; topology optimization; differential geometry

## 1. Introduction

Sustainable-resilience models must do more than describe degradation and recovery. They must represent discrete structural changes, continuous physical evolution, intervention choices, constraints, uncertainty, and critical-service outcomes in a form that permits analysis and optimization. This creates a representation problem: even a mathematically valid system description may be poorly suited to inverse design or recovery optimization.

Kodnongbua et al. (2025) address an analogous problem in computational design. Rather than accepting a fixed shape grammar and constructing an increasingly complicated search procedure, they ask how the grammar itself should be designed so that descent-style optimization becomes effective. Their answer provides a transferable principle for sustainable resilience: **optimization performance depends jointly on the objective, algorithm, and geometry and structure of the representation being searched**.

This review has three objectives:

1. establish exactly what the paper demonstrates;
2. determine which parts are directly or indirectly relevant to differential geometry, mathematical art, sustainability, and resilience;
3. formulate a defensible sustainable-resilience extension without attributing that extension to the source authors.

## 2. Review questions

**RQ1.** What mathematical and computational problem does the source solve?

**RQ2.** What evidence supports the four proposed grammar-design properties?

**RQ3.** Does the paper directly use differential geometry or quantify sustainability and resilience?

**RQ4.** What domain-neutral mathematical elements may be transferable to sustainable-resilience problems, and what evidence is required before choosing an application domain?

**RQ5.** How can its procedural forms support mathematical art without becoming misleading scientific evidence?

## 3. Method

### 3.1 Source and review unit

The unit of analysis is one focal publication:

> Kodnongbua, M., Zhang, Z. J., Sharp, N., and Schulz, A. (2025). *Design for Descent: What Makes a Shape Grammar Easy to Optimize?* SIGGRAPH Asia 2025 Conference Papers. https://doi.org/10.1145/3757377.3764004

The supplied main paper contains 11 pages. All pages were text-extracted. Pages containing the graphical abstract, design principles, experimental applications, topology-optimization sequence, and ablation figures were visually inspected. The source PDF checksum and inspection record are reported in `VALIDATION_LOG.md`; artifact identities and lifecycle states are recorded in `SOURCE_MANIFEST.yaml`.

### 3.2 Evidence discipline

Claims are labeled `OBSERVED`, `INFERRED`, `EXTERNAL`, `PROPOSED`, `NOT_OBSERVED`, or `NOT_VERIFIED` according to the repository evidence protocol. `PROPOSED` statements are project constructs and are not evidence from Kodnongbua et al. These claim statuses are distinct from artifact-lifecycle and execution statuses defined in `protocol/PRIMARY_EVIDENCE_BUNDLE.md` at the literature-review root.

### 3.3 Classification rule

The paper is evaluated against five study classes: direct application (`D`), transferable method (`M`), geometric design (`G`), visualization and mathematical art (`V`), and contextual (`C`). Classes are assigned from explicit full-text evidence, not keywords or popularity.\n\n### 3.4 Artifact and reproduction boundary\n\nThe complete 11-page main paper has been reviewed. The official implementation repository has been identified and inspected only at the level of provenance, pinned revision, top-level structure, and selected environment metadata. The referenced supplement was not located in a documented search. The environment has not been built, the code has not been executed, and no numerical result has been reproduced. Accordingly, this document is a `MAIN_PAPER_REVIEWED` critical review, not a reproduction report.

## 4. Verified source contribution

### 4.1 Parametric grammar

`OBSERVED` - Section 3.1 defines a parametric shape grammar as

$$
G=(V,\Sigma,R,\omega),
$$

where $V$ is a finite set of geometric primitives, $\Sigma$ is the formal parameter set, $R$ is a finite set of rewrite rules, and $\omega$ is the initial shape or axiom.

Each design contains a discrete structure $s$ and a continuous parameter vector $p\in\mathbb{R}^{d(s)}$. The full design space is

```math
\mathcal X
=
\bigsqcup_{s\in S}
\{s\}\times\mathbb{R}^{d(s)}.
```

Because the dimension $d(s)$ can change after a rewrite, this is a transdimensional disjoint union of continuous parameter spaces. The source informally discusses the changing geometry of this space, but does not equip it with a Riemannian metric or prove that the union is a smooth manifold.

### 4.2 Objective

`OBSERVED` - The source formulates

```math
(s^*,p^*)
=
\arg\min_{\substack{s\in S\\p\in\mathbb{R}^{d(s)}}}
\left[f\!\left(I(s,p)\right)+g(s,p)\right],
```

where $I$ is a differentiable rendering or representation map, $f$ is a differentiable objective, and $g$ may be a non-differentiable objective such as structural simplicity.

### 4.3 Stochastic Rewrite Descent

`OBSERVED` - SRD alternates continuous parameter updates within the current structure and discrete rewrites between structures. A continuous step has the form

$$
p\leftarrow p-\eta\nabla_p f\!\left(I(s,p)\right).
$$

For sampled rewrites $\rho$, the algorithm estimates an improvement after a local continuous optimization step:

$$
\Delta L_\rho
\approx
L(s,p)-L(s',\widehat p),
$$

where $(s',p')=\rho(s,p)$ and $\widehat p$ is locally updated under the rewritten structure. The implementation samples 64 valid rewrites per step and greedily selects a compatible improving subset.

### 4.4 Grammar-design properties

`OBSERVED` - Table 1 and Section 3.2 present four guidelines.

| Property | Source meaning | Formal boundary for this review |
|---|---|---|
| Reversibility | A rewrite $A\rightarrow B$ should have a complementary $B\rightarrow A$ rewrite | Not physical or thermodynamic reversibility |
| Jump continuity | A rewrite should cause negligible instantaneous change in the rendered shape | Not proof of global smooth-manifold continuity |
| Local geometric control | Local shape changes should be possible without changing distant regions | Not control-theoretic controllability |
| Repairability | Rewrites should return infeasible shapes to a feasible region | Not proof of dynamically feasible physical recovery |

The authors describe these as guidelines rather than universal requirements and note that they may conflict for some tasks.

## 5. Experimental evidence

### 5.1 Grammars and applications

`OBSERVED` - The experiments use Tree, Arc-Line, and Union-Rectangle grammars. Applications include target-image matching, changing-target morphing, text-conditioned shape generation through Score Distillation Sampling, and topology optimization of cantilever and MBB beams.

### 5.2 Image datasets

`OBSERVED` - The target-image experiment uses SketchGraphs-derived data divided into:

- 128 single-component shapes;
- 25 donut-topology shapes;
- 23 two-component shapes.

### 5.3 Ablation evidence

`OBSERVED` - The full Arc-Line grammar substantially outperforms the variant without `AddLoop` on targets requiring additional boundaries or components.

| Arc-Line configuration | One component PSNR | Donut PSNR | Two components PSNR |
|---|---:|---:|---:|
| Without `AddLoop` | 44.1 | 11.4 | 20.9 |
| Full grammar | **44.3** | **48.1** | **49.3** |

For the Tree grammar, the complete grammar improves PSNR relative to the basic constructive grammar:

| Tree configuration | One component PSNR | Donut PSNR | Two components PSNR |
|---|---:|---:|---:|
| Basic `AddLeaf` grammar | 15.4 | 9.7 | 10.3 |
| Full grammar | **22.0** | **21.7** | **22.6** |

These results support the narrower claim that rewrite capabilities materially influence optimization quality on the reported tasks. They do not validate sustainability or resilience outcomes.

### 5.4 Comparison with RJMCMC

`OBSERVED` - The paper reports the following comparison for a tree-generation task:

| Method or grammar | PSNR | Runtime (minutes) |
|---|---:|---:|
| RJMCMC | 15.3 | 219 |
| Tr-1 | 20.0 | 19 |
| Tr-5 | **31.3** | 99 |

The result supports the value of gradient information and richer rewrite structure for this experiment. It does not establish universal superiority over all mixed discrete-continuous optimizers.

### 5.5 Topology optimization

`OBSERVED` - The paper applies the Arc-Line grammar to cantilever and MBB beam examples using a signed-distance field and a level-set-inspired objective. The cantilever is described as close to published results. The MBB result is described as structurally sound but different from typical results because the design was not constrained to remain inside the initial region.

`NOT_OBSERVED` - The main paper does not report life-cycle carbon, embodied energy, resource depletion, cost, equity, service continuity, or field performance for these shapes. Therefore, reduced weight cannot be treated as a complete sustainability result.

## 6. Direct relevance assessment

| Project dimension | Full-text finding | Judgment |
|---|---|---|
| Differential geometry | No explicit Riemannian metric, geodesic, curvature, connection, tangent bundle, or intrinsic manifold analysis | Indirect only |
| Mathematical art | Procedural trees, text-conditioned forms, image matching, morphing, and visual grammar sequences | Strong direct relevance |
| Geometric design | Mixed discrete-continuous shape optimization and topology optimization | Strong direct relevance |
| Sustainability | No quantified environmental, economic, social, or integrated sustainability output | Weak transfer relevance |
| Resilience | No hazard, failure, service loss, recovery, viability, or resilience metric | Not directly demonstrated |
| Infrastructure | Structural beam examples, but no coupled infrastructure system | Limited |
| Optimization | Formal objective, algorithm, ablations, and a comparator | Strong direct relevance |
| Reproducibility | Code availability is stated; the code and supplemental material have not been executed or independently audited here | Partial |

The evidence-based classification is

$$
\boxed{\mathrm{M+G+V}},
$$

not `D`.

## 7. Provisional ten-chain mapping

| Project chain | Source coverage | Evidence status |
|---|---|---|
| C01: Forcing → Physical laws → States and flows → Dynamics | Shape states change during optimization, but no environmental forcing or coupled-system physical dynamics is modeled | OBSERVED_PARTIAL |
| C02: Structure → Interfaces → Coupling → Feedback and cascade propagation | Grammar structure, local geometric control, and rewrite transitions are implemented; infrastructure interfaces and cascades are not | OBSERVED_PARTIAL |
| C03: Sensing → Data → Identification → Estimation → Uncertainty → Prediction → Validation | Target data and inverse fitting are used, but sensing, identifiability, state estimation, uncertainty quantification, and external validation are absent | OBSERVED_PARTIAL |
| C04: Hazard or stressor → Exposure → Vulnerability → Failure or degradation → Service loss → Consequences | Not implemented | NOT_OBSERVED |
| C05: Constraints → Admissible states → Viability kernel → Reachability → Response and recovery → Resilience → Adaptation or transformation | Reversibility and repairability motivate a conceptual transfer, but no viability kernel, recovery trajectory, or resilience outcome is implemented | INFERRED |
| C06: Objectives and trade-offs → Decision → Intervention design → Control or optimization → Implementation → Monitoring → Learning | Formal objectives, mixed discrete-continuous optimization, ablations, and design examples are the paper's strongest contribution; deployment and adaptive monitoring are absent | OBSERVED_PARTIAL / STRONG |
| C07: Service capacity → Availability and continuity → Population access → Critical needs → Distributional effects → Equity and well-being | Not implemented | NOT_OBSERVED |
| C08: Resource extraction → Transformation → Stocks and flows → Emissions and waste → Life-cycle burdens → Circularity or regeneration → Sustainability | Structural weight appears as an optimization objective, but no resource-flow, life-cycle, emissions, circularity, or sustainability assessment is performed | OBSERVED_PARTIAL / SUSTAINABILITY_NOT_OBSERVED |
| C09: Ownership and institutions → Governance → Incentives and finance → Coordination → Operations and maintenance → Adoption and legitimacy | Not implemented | NOT_OBSERVED |
| C10: Mathematical encoding → Visual, sonic, or material form → Interpretation → Comprehension and participation → Decision influence → Evaluated impact | Mathematical encodings and visual form generation are direct; comprehension, participation, behavioral influence, and decision impact are not evaluated | OBSERVED_PARTIAL / STRONG |

The paper therefore contributes most strongly to C06 and the form-generation portion of C10, supplies transferable partial evidence for C01–C03, and motivates only an inferred connection to C05. It does not directly establish C04, C07, C08 sustainability outcomes, or C09. This mapping uses the [`MSR-CA-001` architecture](../../protocol/CHAIN_ARCHITECTURE.md) and does not convert method relevance into sustainable-resilience evidence.

## 8. Proposed domain-neutral sustainable-resilience extension

This section is `PROPOSED`. It is not part of Kodnongbua et al.'s contribution and does not select an application domain. Any named system must first pass the repository's application-domain exploration and selection protocol.

### 8.1 Stratified hybrid state space

Define

```math
\mathcal X_{\mathrm{SR}}
=
\bigsqcup_{\sigma\in\mathscr S}
\{\sigma\}\times\mathcal M_\sigma,
```

where $\sigma$ represents a discrete configuration, topology, regime, or operating mode and $\mathcal M_\sigma$ contains the continuous states admitted under that configuration. The physical meaning of $\sigma$, $\mathcal M_\sigma$, and their dimensions must be defined separately for every candidate application.

Candidate rewrite classes may include:

- addition, removal, activation, or isolation of a component;
- switching between operating regimes;
- reconfiguration of a network, boundary, material form, or control pathway;
- repair, replacement, substitution, or adaptive transformation;
- creation or removal of a feasible connection.

These classes are abstract. Their admissibility, directionality, cost, physical consequences, and reversibility must be established from domain evidence rather than assumed from the grammar analogy.

Continuous dynamics within one mode may be written as

$$
\dot Y=f_\sigma(Y,u,\eta,t),
$$

subject to the conservation laws, constitutive relations, capacities, operational rules, environmental limits, safety requirements, and distributional constraints justified for the selected domain.

### 8.2 Intrinsic metric within each stratum

Where scientifically justified for a candidate application, each continuous stratum may carry a metric

$$
g_{\sigma,Y}(v,w)=v^{\mathsf T}G_\sigma(Y)w.
$$

The metric must be dimensionally coherent or constructed from explicit nondimensionalization, covariance, energy, service sensitivity, or another defensible physical/statistical basis. It cannot be selected for visual convenience.

### 8.3 Sustainability-constrained admissible region

Define

```math
K_\sigma(t)
=
\left\{
Y\in\mathcal M_\sigma:
\begin{array}{l}
Q_{\mathrm{essential}}(Y,t)\ge Q_{\min},\\
C_{\mathrm{carbon}}(Y,t)\le B_{\mathrm{carbon}},\\
C_{\mathrm{resource}}(Y,t)\le B_{\mathrm{resource}},\\
I_{\mathrm{equity}}(Y,t)\le B_{\mathrm{equity}},\\
h_{\mathrm{safety}}(Y,t)\ge0
\end{array}
\right\}.
```

The design problem becomes multi-objective:

$$
\min
\left(
J_{\mathrm{unserved}},
J_{\mathrm{recovery}},
J_{\mathrm{carbon}},
J_{\mathrm{resource}},
J_{\mathrm{cost}},
J_{\mathrm{inequity}}
\right),
$$

subject to dynamics, admissibility, uncertainty, and non-anticipative control requirements.

### 8.4 Translation of the grammar principles

| Source principle | Proposed sustainable-resilience interpretation | Required safeguard |
|---|---|---|
| Reversibility | Complementary corrective, adaptive, or alternative transformations | Do not confuse with physical or thermodynamic reversibility |
| Jump continuity | Bounded instantaneous change in a defined performance variable after a rewrite | Verify the bound under the selected system dynamics |
| Local geometric control | Targeted change with spatially, functionally, or structurally limited intended effects | Quantify unintended nonlocal propagation |
| Repairability | An admissible operator returning soft violations to feasibility | Hard safety constraints must remain invariant |
| Redundancy | Multiple viable representations and recovery pathways | Account for cost, carbon, resources, and operational burden |

A performance-level jump condition can be written as

$$
\left\|
P(Y)-P\!\left(\rho(Y)\right)
\right\|_W
\le \varepsilon_P.
$$

This proposed inequality must be validated against physical dynamics and service data; it is not established by the source paper.

## 9. Mathematical-art exploration

`PROPOSED` - The paper's procedural geometry motivates a domain-neutral visual grammar for comparing candidate sustainable-resilience systems. Before application selection, the visual vocabulary should encode only formal constructs shared across candidates:

- separate visual strata: discrete configurations or regimes;
- position within a stratum: continuous state coordinates or a declared embedding;
- paths: observed, simulated, or proposed transitions;
- boundary contours: admissibility or viability constraints;
- distance, width, color, and opacity: defined variables with units or explicit normalization;
- rewrite glyphs: intervention, adaptation, repair, or structural change;
- uncertainty bands or ensembles: epistemic or aleatory uncertainty, kept distinct.

The visual is scientific only if each property is tied to a defined variable, unit, normalization rule, uncertainty statement, and data provenance. Otherwise, it remains interpretive mathematical art. Domain-specific colors, symbols, and narratives will be designed only after application selection.

## 10. Limitations and validity threats

### 10.1 Source limitations reported by the authors

- sensitivity to step size and gradient regularity;
- grammar-specific scaling factors and scheduling;
- approximately uniform rewrite-type sampling;
- incomplete theoretical foundations;
- limited grammar complexity and primarily two-dimensional demonstrations;
- future need for richer 3D grammars and automated grammar design.

### 10.2 Limitations of this review

- Only the 11-page main paper was supplied and reviewed.
- Algorithms 1 and 2, Appendix D, and the stated theoretical result in Appendix A are located in supplemental material that was not supplied.
- The linked code repository was stated by the paper but was not executed or audited for this review version.
- No independent reproduction of the numerical experiments was performed.
- The sustainable-resilience formulation is a proposed transfer, not an empirical result.
- No global absence claim is made from one paper.

## 11. Research propositions generated by the case study

The following are `PROPOSED` and require future testing.

**P1 - Representation proposition.** A hybrid sustainable-resilience grammar satisfying appropriately adapted reversibility, bounded jumps, local control, and safe repairability will yield better feasible-solution discovery than a representation lacking these properties.

**P2 - Service continuity proposition.** Explicit bounds on service changes across rewrites will reduce control-induced critical-service loss during recovery optimization.

**P3 - Viability proposition.** Projecting candidate interventions onto sustainability-constrained admissible sets will reduce infeasible recovery recommendations, provided hard constraints are maintained throughout the trajectory.

**P4 - Path-diversity proposition.** Redundant recovery representations will improve robustness to blocked or failed interventions, but only when their additional economic, environmental, and operational burdens are included.

**P5 - Geometry proposition.** A physically justified metric within each continuous state stratum will change the ranking of recovery or adaptation paths relative to unweighted Euclidean distance.

## 12. Conclusion

Kodnongbua et al. demonstrate that the design of a search representation can be as important as the optimization algorithm. Their evidence supports four useful grammar guidelines across image-fitting, generative, and structural examples. The paper is a strong source for procedural geometry, mathematical art, and mixed discrete-continuous inverse design. It does not directly establish differential-geometric, sustainability, or resilience claims.

Its legitimate contribution to this project is therefore methodological. It motivates exploration of hybrid grammar-geometric models in which discrete changes and continuous dynamics are considered together under application-specific physical, functional, environmental, resource, safety, and equity constraints. It does not determine which application should be chosen. That decision requires comparative evidence across candidate domains, after which the selected integration must be formally developed, numerically verified, and empirically validated.

## Data and artifact availability

- Primary paper DOI: https://doi.org/10.1145/3757377.3764004
- Source PDF redistribution: not included in this package.
- Source checksum and inspection record: [`VALIDATION_LOG.md`](VALIDATION_LOG.md)
- Machine-readable evidence record: [`EVIDENCE_RECORD.yaml`](EVIDENCE_RECORD.yaml)
- Claim-level matrix: [`EVIDENCE_MATRIX.csv`](EVIDENCE_MATRIX.csv)
- Bibliography: [`../../references/references.bib`](../../references/references.bib)

## References

Kodnongbua, M., Zhang, Z. J., Sharp, N., and Schulz, A. (2025). Design for Descent: What Makes a Shape Grammar Easy to Optimize? *SIGGRAPH Asia 2025 Conference Papers*, 1-11. https://doi.org/10.1145/3757377.3764004
