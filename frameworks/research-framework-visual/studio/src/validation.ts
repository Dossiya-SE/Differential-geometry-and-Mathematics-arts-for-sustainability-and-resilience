import type { ParametricSurfaceIR, ValidationCheck } from './visual-ir';
import { torusGaussianCurvature, validateTorus } from './math';

export function validateIR(ir: ParametricSurfaceIR): ValidationCheck[] {
  const structural = validateTorus(ir);
  let finite = true;
  let regularMetric = true;
  const R = ir.parameters.values.R;
  const r = ir.parameters.values.r;
  for (let i = 0; i <= 180; i += 1) {
    const v = ir.parameters.v.min + (i / 180) * (ir.parameters.v.max - ir.parameters.v.min);
    finite &&= Number.isFinite(torusGaussianCurvature(ir, v));
    const E = (R + r * Math.cos(v)) ** 2;
    const G = r ** 2;
    regularMetric &&= E * G > 1e-12;
  }
  return [
    { id: 'ir.structure', label: 'Visual IR structure', status: structural.length === 0 ? 'PASS' : 'FAIL', detail: structural.length === 0 ? 'Required torus invariants satisfied.' : structural.join(' ') },
    { id: 'math.finite', label: 'Finite curvature', status: finite ? 'PASS' : 'FAIL', detail: finite ? 'Gaussian curvature is finite on the sampled domain.' : 'Non-finite curvature detected.' },
    { id: 'geometry.metric', label: 'Metric regularity', status: regularMetric ? 'PASS' : 'FAIL', detail: regularMetric ? 'EG-F² > 0 across the sampled domain.' : 'Degenerate metric detected.' },
    { id: 'epistemic.status', label: 'Epistemic status', status: ir.epistemicStatus === 'ILLUSTRATIVE' ? 'WARN' : 'PASS', detail: `Object is classified as ${ir.epistemicStatus}.` },
    { id: 'reproducibility.seed', label: 'Deterministic seed', status: Number.isInteger(ir.provenance.deterministicSeed) ? 'PASS' : 'FAIL', detail: `seed=${ir.provenance.deterministicSeed}` }
  ];
}
