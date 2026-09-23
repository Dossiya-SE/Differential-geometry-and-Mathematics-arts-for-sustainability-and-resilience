import * as THREE from 'three';
import type { ParametricSurfaceIR } from '../visual-ir';
import { torusGaussianCurvature, torusPoint } from '../math';

function curvatureColor(k: number, maxAbs: number): THREE.Color {
  const t = maxAbs === 0 ? 0.5 : 0.5 + 0.5 * Math.max(-1, Math.min(1, k / maxAbs));
  return new THREE.Color().setHSL(0.66 - 0.58 * t, 0.78, 0.56);
}

export function buildSurfaceGeometry(ir: ParametricSurfaceIR): THREE.BufferGeometry {
  const nu = ir.geometry.resolutionU;
  const nv = ir.geometry.resolutionV;
  const positions: number[] = [];
  const colors: number[] = [];
  const indices: number[] = [];
  const curvature: number[] = [];

  for (let j = 0; j <= nv; j += 1) {
    const v = ir.parameters.v.min + (j / nv) * (ir.parameters.v.max - ir.parameters.v.min);
    for (let i = 0; i <= nu; i += 1) {
      const u = ir.parameters.u.min + (i / nu) * (ir.parameters.u.max - ir.parameters.u.min);
      positions.push(...torusPoint(ir, u, v));
      curvature.push(torusGaussianCurvature(ir, v));
    }
  }
  const maxAbs = Math.max(...curvature.map((k) => Math.abs(k)), 1e-12);
  curvature.forEach((k) => { const c = curvatureColor(k, maxAbs); colors.push(c.r, c.g, c.b); });
  for (let j = 0; j < nv; j += 1) {
    for (let i = 0; i < nu; i += 1) {
      const a = j * (nu + 1) + i;
      const b = a + 1;
      const c = (j + 1) * (nu + 1) + i + 1;
      const d = (j + 1) * (nu + 1) + i;
      indices.push(a, b, d, b, c, d);
    }
  }
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
  geometry.setIndex(indices);
  geometry.computeVertexNormals();
  return geometry;
}
