import type { ParametricSurfaceIR } from './visual-ir';

export function torusPoint(ir: ParametricSurfaceIR, u: number, v: number): [number, number, number] {
  const R = ir.parameters.values.R;
  const r = ir.parameters.values.r;
  return [(R + r * Math.cos(v)) * Math.cos(u), (R + r * Math.cos(v)) * Math.sin(u), r * Math.sin(v)];
}

export function torusGaussianCurvature(ir: ParametricSurfaceIR, v: number): number {
  const R = ir.parameters.values.R;
  const r = ir.parameters.values.r;
  return Math.cos(v) / (r * (R + r * Math.cos(v)));
}

export function validateTorus(ir: ParametricSurfaceIR): string[] {
  const errors: string[] = [];
  const R = ir.parameters.values.R;
  const r = ir.parameters.values.r;
  if (!(R > r && r > 0)) errors.push('Require R > r > 0 for a regular embedded torus.');
  if (ir.geometry.resolutionU < 8 || ir.geometry.resolutionV < 8) errors.push('Resolution is too low for stable visualization.');
  if (!(ir.parameters.u.max > ir.parameters.u.min)) errors.push('u domain is invalid.');
  if (!(ir.parameters.v.max > ir.parameters.v.min)) errors.push('v domain is invalid.');
  return errors;
}
