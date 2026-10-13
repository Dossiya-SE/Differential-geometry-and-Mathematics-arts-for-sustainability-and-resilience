export type EpistemicStatus =
  | 'USER_SPECIFIED' | 'COMPUTED' | 'OBSERVED' | 'PUBLISHED' | 'CALIBRATED'
  | 'DERIVED' | 'ASSUMED' | 'SYNTHETIC' | 'ILLUSTRATIVE' | 'TO_BE_VALIDATED';

export type ColorField = 'z' | 'gaussian_curvature' | 'mean_curvature' | 'gradient_curvature';
export interface Range { min: number; max: number; }

export interface ParametricSurfaceIR {
  schemaVersion: '0.1.0';
  id: string;
  type: 'parametric_surface';
  name: string;
  epistemicStatus: EpistemicStatus;
  parameters: { u: Range; v: Range; values: Record<string, number>; };
  equations: { x: string; y: string; z: string; latex: string; };
  geometry: { resolutionU: number; resolutionV: number; };
  visual: { colorField: ColorField; showMesh: boolean; };
  camera: { projection: 'perspective' | 'orthographic'; position: [number, number, number]; };
  provenance: { engine: 'typescript'; renderer: 'threejs-webgl'; deterministicSeed: number; };
}

export interface ValidationCheck {
  id: string;
  label: string;
  status: 'PASS' | 'WARN' | 'FAIL';
  detail: string;
}
