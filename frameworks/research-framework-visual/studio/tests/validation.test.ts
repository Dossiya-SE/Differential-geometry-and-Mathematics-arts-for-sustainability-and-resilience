import { describe, expect, it } from 'vitest';
import { torusIR } from '../src/examples/torus';
import { validateIR } from '../src/validation';
import { torusGaussianCurvature } from '../src/math';

describe('Visual IR scientific validation', () => {
  it('passes regular torus mathematical gates', () => { expect(validateIR(torusIR).filter((c) => c.status === 'FAIL')).toHaveLength(0); });
  it('matches known torus Gaussian curvature signs', () => { expect(torusGaussianCurvature(torusIR, 0)).toBeGreaterThan(0); expect(torusGaussianCurvature(torusIR, Math.PI)).toBeLessThan(0); });
  it('fails a degenerate parameterization', () => { const bad = structuredClone(torusIR); bad.parameters.values.R = 0.5; bad.parameters.values.r = 0.8; expect(validateIR(bad).some((c) => c.status === 'FAIL')).toBe(true); });
});
