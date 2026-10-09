import type { ParametricSurfaceIR } from '../visual-ir';

export const torusIR: ParametricSurfaceIR = {
  schemaVersion: '0.1.0',
  id: 'surface.torus.001',
  type: 'parametric_surface',
  name: 'Curvature-coded torus',
  epistemicStatus: 'ILLUSTRATIVE',
  parameters: {
    u: { min: 0, max: 2 * Math.PI },
    v: { min: 0, max: 2 * Math.PI },
    values: { R: 2.0, r: 0.72 }
  },
  equations: {
    x: '(R + r*cos(v))*cos(u)',
    y: '(R + r*cos(v))*sin(u)',
    z: 'r*sin(v)',
    latex: String.raw`\mathbf X(u,v)=\big((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v\big)`
  },
  geometry: { resolutionU: 128, resolutionV: 72 },
  visual: { colorField: 'gaussian_curvature', showMesh: false },
  camera: { projection: 'perspective', position: [4.8, 3.5, 4.2] },
  provenance: { engine: 'typescript', renderer: 'threejs-webgl', deterministicSeed: 20260825 }
};
