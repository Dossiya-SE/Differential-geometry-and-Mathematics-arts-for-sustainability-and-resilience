import Ajv2020 from 'ajv/dist/2020';
import { describe, expect, it } from 'vitest';
import visualSchema from '../schemas/visual-ir-v1.schema.json';
import presentationSchema from '../schemas/presentation-ir-v1.schema.json';
import enginePackSchema from '../schemas/engine-pack-v1.schema.json';
import renderRecordSchema from '../schemas/render-record-v1.schema.json';
import { canonicalJSONString } from '../src/ir/canonical';
import { goldenEnginePackV1, goldenProjectV1 } from '../src/ir/golden';
import { summarizeValidation, validateMVSProject } from '../src/ir/validation';
import type { ComputationalGraphSemantic, ScientificChartSemantic } from '../src/ir/v1';
import { layoutComputationalGraph } from '../src/layout/elk';
import { compileScientificChart } from '../src/charts/vega';

function schemaValidator() {
  const ajv = new Ajv2020({ allErrors: true, strict: true });
  ajv.addSchema(presentationSchema);
  return ajv;
}

describe('MVS Architecture Foundation v1', () => {
  it('validates the golden project against canonical JSON Schema', () => {
    const ajv = schemaValidator();
    const validate = ajv.compile(visualSchema);
    expect(validate(goldenProjectV1), JSON.stringify(validate.errors)).toBe(true);
  });

  it('validates the fail-closed engine-pack manifest', () => {
    const ajv = schemaValidator();
    const validate = ajv.compile(enginePackSchema);
    expect(validate(goldenEnginePackV1), JSON.stringify(validate.errors)).toBe(true);
    expect(goldenEnginePackV1.capabilities.network).toEqual([]);
    expect(goldenEnginePackV1.capabilities.processSpawn).toEqual([]);
  });

  it('validates immutable render-record structure', () => {
    const ajv = schemaValidator();
    const validate = ajv.compile(renderRecordSchema);
    const hash = `sha256:${'a'.repeat(64)}`;
    expect(validate({
      schema: 'mvs.render-record/1',
      projectHash: hash,
      visualIrHash: hash,
      engine: { pack: 'org.mvs.python.science', version: '1.0.0', runtime: 'CPython 3.13', architecture: 'aarch64-apple-darwin', lockHash: hash },
      execution: { seed: 20260825, network: false, freshWorker: true },
      outputs: [{ uri: 'artifact://figure.svg', mime: 'image/svg+xml', sha256: hash }],
    }), JSON.stringify(validate.errors)).toBe(true);
  });

  it('canonicalizes object-key order deterministically and rejects non-finite values', () => {
    expect(canonicalJSONString({ b: 2, a: { d: 4, c: 3 } })).toBe(canonicalJSONString({ a: { c: 3, d: 4 }, b: 2 }));
    expect(() => canonicalJSONString({ x: Number.NaN })).toThrow(/NaN|Infinity/);
  });

  it('passes the golden project without any hard scientific-contract failure', () => {
    const checks = validateMVSProject(goldenProjectV1);
    expect(checks.filter((check) => check.status === 'FAIL')).toHaveLength(0);
    expect(summarizeValidation(checks).status).toBe('WARN');
  });

  it('fails closed when a typed graph edge violates units', () => {
    const invalid = structuredClone(goldenProjectV1);
    const graph = invalid.semantics.objects.find((object): object is ComputationalGraphSemantic => object.kind === 'computational_graph');
    if (!graph) throw new Error('Golden graph is missing.');
    const curvature = graph.nodes.find((node) => node.id === 'node:curvature');
    if (!curvature) throw new Error('Curvature node is missing.');
    const input = curvature.ports.find((port) => port.id === 'surface');
    if (!input) throw new Error('Surface input port is missing.');
    input.unit = { symbol: 's', dimension: 'time' };
    expect(validateMVSProject(invalid).some((check) => check.status === 'FAIL' && check.domain === 'DIMENSION')).toBe(true);
  });

  it('uses ELK to produce finite deterministic-layout geometry for the typed pipeline', async () => {
    const graph = goldenProjectV1.semantics.objects.find((object): object is ComputationalGraphSemantic => object.kind === 'computational_graph');
    if (!graph) throw new Error('Golden graph is missing.');
    const layout = await layoutComputationalGraph(graph);
    expect(layout).toHaveLength(graph.nodes.length);
    expect(layout.every((node) => [node.x, node.y, node.width, node.height].every(Number.isFinite))).toBe(true);
  });

  it('compiles the scientific chart through the current Vega-Lite compiler', () => {
    const chart = goldenProjectV1.semantics.objects.find((object): object is ScientificChartSemantic => object.kind === 'scientific_chart');
    if (!chart) throw new Error('Golden chart is missing.');
    const compiled = compileScientificChart(chart);
    expect(compiled.spec).toBeTruthy();
    expect(compiled.spec.$schema).toContain('vega');
  });
});
