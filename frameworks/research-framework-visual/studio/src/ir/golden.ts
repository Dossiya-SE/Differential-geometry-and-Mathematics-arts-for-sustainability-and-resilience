import type { EnginePackManifestV1, MVSProjectV1 } from './v1';

const lengthUnit = { symbol: 'm', dimension: 'length' } as const;
const curvatureUnit = { symbol: '1/m^2', dimension: 'length^-2' } as const;

export const goldenProjectV1: MVSProjectV1 = {
  schema: 'mvs.visual-ir/1.0',
  id: 'project:golden-differential-geometry',
  title: 'Golden Differential Geometry Pipeline',
  semantics: {
    expressions: [
      { id: 'expr:x', source: '(R+r*cos(v))*cos(u)', language: 'infix', variables: ['u', 'v', 'R', 'r'], exact: true, unit: lengthUnit },
      { id: 'expr:y', source: '(R+r*cos(v))*sin(u)', language: 'infix', variables: ['u', 'v', 'R', 'r'], exact: true, unit: lengthUnit },
      { id: 'expr:z', source: 'r*sin(v)', language: 'infix', variables: ['v', 'r'], exact: true, unit: lengthUnit },
      { id: 'expr:K', source: 'cos(v)/(r*(R+r*cos(v)))', language: 'infix', variables: ['v', 'R', 'r'], exact: true, unit: curvatureUnit },
    ],
    objects: [
      {
        id: 'surface:torus-001',
        kind: 'parametric_surface',
        name: 'Torus',
        epistemicStatus: 'ILLUSTRATIVE',
        domain: { id: 'domain:uv', variables: ['u', 'v'], bounds: { u: [0, 2 * Math.PI], v: [0, 2 * Math.PI] } },
        parameters: { R: 2, r: 0.72 },
        assumptions: ['R > r', 'r > 0'],
        mapping: {
          x: { id: 'expr:x', source: '(R+r*cos(v))*cos(u)', language: 'infix', variables: ['u', 'v', 'R', 'r'], exact: true, unit: lengthUnit },
          y: { id: 'expr:y', source: '(R+r*cos(v))*sin(u)', language: 'infix', variables: ['u', 'v', 'R', 'r'], exact: true, unit: lengthUnit },
          z: { id: 'expr:z', source: 'r*sin(v)', language: 'infix', variables: ['v', 'r'], exact: true, unit: lengthUnit },
        },
        derived: [
          { id: 'expr:K', source: 'cos(v)/(r*(R+r*cos(v)))', language: 'infix', variables: ['v', 'R', 'r'], exact: true, unit: curvatureUnit },
        ],
        coordinateFrame: { id: 'frame:world', handedness: 'right', unit: lengthUnit },
        numericPolicy: { scalarType: 'float64', tolerance: 1e-10, sampleU: 128, sampleV: 64 },
      },
      {
        id: 'graph:curvature-pipeline',
        kind: 'computational_graph',
        epistemicStatus: 'DERIVED',
        nodes: [
          {
            id: 'node:surface',
            kind: 'surface-source',
            label: 'Parametric Surface',
            ports: [{ id: 'surface', direction: 'output', valueKind: 'surface', unit: lengthUnit, domainRef: 'domain:uv' }],
          },
          {
            id: 'node:curvature',
            kind: 'gaussian-curvature',
            label: 'Gaussian Curvature',
            assumptions: ['metric regular'],
            ports: [
              { id: 'surface', direction: 'input', valueKind: 'surface', unit: lengthUnit, domainRef: 'domain:uv', required: true },
              { id: 'K', direction: 'output', valueKind: 'scalar_field', unit: curvatureUnit, domainRef: 'domain:uv' },
            ],
          },
          {
            id: 'node:encoding',
            kind: 'visual-encoding',
            label: 'Curvature → Colour',
            ports: [{ id: 'field', direction: 'input', valueKind: 'scalar_field', unit: curvatureUnit, domainRef: 'domain:uv', required: true }],
          },
        ],
        edges: [
          { id: 'edge:surface-curvature', from: { nodeId: 'node:surface', portId: 'surface' }, to: { nodeId: 'node:curvature', portId: 'surface' } },
          { id: 'edge:curvature-encoding', from: { nodeId: 'node:curvature', portId: 'K' }, to: { nodeId: 'node:encoding', portId: 'field' } },
        ],
      },
      {
        id: 'chart:curvature-slice',
        kind: 'scientific_chart',
        epistemicStatus: 'DERIVED',
        data: {
          name: 'curvature-slice',
          fields: [
            { id: 'v', type: 'quantitative', unit: { symbol: 'rad', dimension: 'angle' } },
            { id: 'K', type: 'quantitative', unit: curvatureUnit },
            { id: 'K_se', type: 'quantitative', unit: curvatureUnit },
          ],
        },
        mark: 'line',
        encoding: { x: { field: 'v' }, y: { field: 'K' } },
        uncertainty: { field: 'K_se', meaning: 'standard_error' },
      },
    ],
  },
  presentation: {
    schema: 'mvs.presentation-ir/1.0',
    objects: [
      { id: 'view:torus', semanticRef: 'surface:torus-001', visible: true, layer: 'interactive-3d', encoding: { colorField: 'expr:K' } },
      { id: 'view:pipeline', semanticRef: 'graph:curvature-pipeline', visible: true, layer: 'precision-2d' },
      { id: 'view:chart', semanticRef: 'chart:curvature-slice', visible: true, layer: 'precision-2d' },
    ],
    renderPolicy: {
      preview2d: 'svg',
      preview3d: 'threejs',
      scientific3d: 'vtk',
      publication: 'svg',
      gpuPreference: 'webgpu-with-webgl2-fallback',
    },
  },
  validationPolicy: {
    failClosed: true,
    requiredDomains: ['SCHEMA', 'MATH', 'DIMENSION', 'NUMERICAL', 'TOPOLOGY', 'DATA', 'VISUAL_ENCODING', 'PROVENANCE', 'REPRODUCTION'],
  },
};

export const goldenEnginePackV1: EnginePackManifestV1 = {
  schema: 'mvs.engine-pack/1',
  id: 'org.mvs.python.science',
  version: '1.0.0',
  platform: 'aarch64-apple-darwin',
  adapterProtocol: '1.0',
  entrypoint: 'bin/python-worker',
  runtime: { kind: 'cpython', version: '3.13' },
  capabilities: {
    filesystem: { read: ['project:///**'], write: ['artifact:///**'] },
    network: [],
    processSpawn: [],
  },
  payloadSha256: 'sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
  lockSha256: 'sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
};
