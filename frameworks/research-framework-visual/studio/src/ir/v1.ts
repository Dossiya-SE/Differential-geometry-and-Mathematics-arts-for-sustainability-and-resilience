export type EpistemicStatus =
  | 'USER_SPECIFIED'
  | 'COMPUTED'
  | 'OBSERVED'
  | 'PUBLISHED'
  | 'CALIBRATED'
  | 'DERIVED'
  | 'ASSUMED'
  | 'SYNTHETIC'
  | 'ILLUSTRATIVE'
  | 'TO_BE_VALIDATED';

export type GateStatus = 'PASS' | 'WARN' | 'FAIL' | 'NOT_RUN';
export type ValidationDomain =
  | 'SCHEMA'
  | 'MATH'
  | 'DIMENSION'
  | 'NUMERICAL'
  | 'TOPOLOGY'
  | 'DATA'
  | 'VISUAL_ENCODING'
  | 'RENDER'
  | 'PROVENANCE'
  | 'REPRODUCTION';

export type ValueKind =
  | 'scalar'
  | 'vector'
  | 'matrix'
  | 'boolean'
  | 'string'
  | 'dataset'
  | 'surface'
  | 'scalar_field'
  | 'vector_field'
  | 'camera';

export interface UnitRef {
  symbol: string;
  dimension?: string;
}

export interface DomainRef {
  id: string;
  variables: string[];
  bounds?: Record<string, [number, number]>;
}

export interface MathExpression {
  id: string;
  source: string;
  language: 'infix' | 'sympy' | 'latex';
  variables: string[];
  exact: boolean;
  unit?: UnitRef;
}

export interface GraphPort {
  id: string;
  direction: 'input' | 'output';
  valueKind: ValueKind;
  unit?: UnitRef;
  domainRef?: string;
  required?: boolean;
}

export interface ComputationalNode {
  id: string;
  kind: string;
  label: string;
  ports: GraphPort[];
  expressionRef?: string;
  assumptions?: string[];
}

export interface ComputationalEdge {
  id: string;
  from: { nodeId: string; portId: string };
  to: { nodeId: string; portId: string };
}

export interface ComputationalGraphSemantic {
  id: string;
  kind: 'computational_graph';
  epistemicStatus: EpistemicStatus;
  nodes: ComputationalNode[];
  edges: ComputationalEdge[];
}

export interface ParametricSurfaceSemantic {
  id: string;
  kind: 'parametric_surface';
  name: string;
  epistemicStatus: EpistemicStatus;
  domain: DomainRef;
  parameters: Record<string, number>;
  assumptions: string[];
  mapping: {
    x: MathExpression;
    y: MathExpression;
    z: MathExpression;
  };
  derived: MathExpression[];
  coordinateFrame: {
    id: string;
    handedness: 'right' | 'left';
    unit: UnitRef;
  };
  numericPolicy: {
    scalarType: 'float64';
    tolerance: number;
    sampleU: number;
    sampleV: number;
  };
}

export interface ChartField {
  id: string;
  type: 'quantitative' | 'ordinal' | 'nominal' | 'temporal';
  unit?: UnitRef;
}

export interface ScientificChartSemantic {
  id: string;
  kind: 'scientific_chart';
  epistemicStatus: EpistemicStatus;
  data: {
    name: string;
    fields: ChartField[];
  };
  mark: 'line' | 'point' | 'bar' | 'area';
  encoding: {
    x: { field: string };
    y: { field: string };
    color?: { field: string };
  };
  uncertainty?: {
    field: string;
    meaning: 'standard_error' | 'standard_deviation' | 'confidence_interval';
  };
}

export type SemanticObject =
  | ParametricSurfaceSemantic
  | ComputationalGraphSemantic
  | ScientificChartSemantic;

export interface PresentationObject {
  id: string;
  semanticRef: string;
  visible: boolean;
  layer: 'precision-2d' | 'dense-2d' | 'interactive-3d' | 'overlay';
  encoding?: Record<string, string | number | boolean>;
}

export interface PresentationIRV1 {
  schema: 'mvs.presentation-ir/1.0';
  objects: PresentationObject[];
  renderPolicy: {
    preview2d: 'svg';
    preview3d: 'threejs';
    scientific3d: 'vtk';
    publication: 'svg' | 'pdf';
    gpuPreference: 'webgpu-with-webgl2-fallback';
  };
}

export interface MVSProjectV1 {
  schema: 'mvs.visual-ir/1.0';
  id: string;
  title: string;
  semantics: {
    expressions: MathExpression[];
    objects: SemanticObject[];
  };
  presentation: PresentationIRV1;
  validationPolicy: {
    failClosed: true;
    requiredDomains: ValidationDomain[];
  };
}

export interface ValidationCheckV1 {
  id: string;
  domain: ValidationDomain;
  status: GateStatus;
  detail: string;
}

export interface EnginePackManifestV1 {
  schema: 'mvs.engine-pack/1';
  id: string;
  version: string;
  platform: string;
  adapterProtocol: string;
  entrypoint: string;
  runtime: { kind: string; version: string };
  capabilities: {
    filesystem: { read: string[]; write: string[] };
    network: string[];
    processSpawn: string[];
  };
  payloadSha256: string;
  lockSha256: string;
}

export interface RenderRecordV1 {
  schema: 'mvs.render-record/1';
  projectHash: string;
  visualIrHash: string;
  engine: {
    pack: string;
    version: string;
    runtime: string;
    architecture: string;
    lockHash: string;
  };
  execution: {
    seed: number;
    network: boolean;
    freshWorker: boolean;
  };
  outputs: Array<{ uri: string; mime: string; sha256: string }>;
}
