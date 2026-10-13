import type { ParametricSurfaceIR } from './visual-ir';

export function generateCode(ir: ParametricSurfaceIR) {
  const R = ir.parameters.values.R;
  const r = ir.parameters.values.r;
  return {
    python: `import numpy as np\n\ndef X(u, v, R=${R}, r=${r}):\n    return np.array([(R+r*np.cos(v))*np.cos(u),(R+r*np.cos(v))*np.sin(u),r*np.sin(v)])\n\ndef K(v, R=${R}, r=${r}):\n    return np.cos(v)/(r*(R+r*np.cos(v)))\n`,
    typescript: `export function X(u: number, v: number, R=${R}, r=${r}) {\n  return [(R+r*Math.cos(v))*Math.cos(u),(R+r*Math.cos(v))*Math.sin(u),r*Math.sin(v)];\n}\n`,
    glsl: `vec3 X(float u, float v) {\n  float R=${R.toFixed(3)}; float r=${r.toFixed(3)};\n  return vec3((R+r*cos(v))*cos(u),(R+r*cos(v))*sin(u),r*sin(v));\n}\n`,
    latex: ir.equations.latex
  };
}
