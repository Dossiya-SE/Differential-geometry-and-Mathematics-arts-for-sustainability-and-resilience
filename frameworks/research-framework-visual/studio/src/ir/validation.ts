import type {
  ComputationalGraphSemantic,
  GateStatus,
  MVSProjectV1,
  ScientificChartSemantic,
  ValidationCheckV1,
} from './v1';

function unitSignature(unit: { symbol: string; dimension?: string } | undefined): string {
  if (!unit) return 'unitless';
  return unit.dimension ?? unit.symbol;
}

function aggregateStatus(checks: ValidationCheckV1[]): GateStatus {
  if (checks.some((check) => check.status === 'FAIL')) return 'FAIL';
  if (checks.some((check) => check.status === 'WARN')) return 'WARN';
  if (checks.some((check) => check.status === 'NOT_RUN')) return 'NOT_RUN';
  return 'PASS';
}

function validateGraph(graph: ComputationalGraphSemantic): ValidationCheckV1[] {
  const checks: ValidationCheckV1[] = [];
  const nodes = new Map(graph.nodes.map((node) => [node.id, node]));
  const ids = graph.nodes.map((node) => node.id);
  const duplicateNodeIds = ids.filter((id, index) => ids.indexOf(id) !== index);

  checks.push({
    id: `${graph.id}.node_ids`,
    domain: 'TOPOLOGY',
    status: duplicateNodeIds.length ? 'FAIL' : 'PASS',
    detail: duplicateNodeIds.length ? `Duplicate node ids: ${[...new Set(duplicateNodeIds)].join(', ')}` : 'Node ids are unique.',
  });

  for (const edge of graph.edges) {
    const source = nodes.get(edge.from.nodeId);
    const target = nodes.get(edge.to.nodeId);
    if (!source || !target) {
      checks.push({
        id: `${graph.id}.${edge.id}.references`,
        domain: 'TOPOLOGY',
        status: 'FAIL',
        detail: 'Edge references a missing source or target node.',
      });
      continue;
    }

    const sourcePort = source.ports.find((port) => port.id === edge.from.portId);
    const targetPort = target.ports.find((port) => port.id === edge.to.portId);
    if (!sourcePort || !targetPort) {
      checks.push({
        id: `${graph.id}.${edge.id}.ports`,
        domain: 'TOPOLOGY',
        status: 'FAIL',
        detail: 'Edge references a missing source or target port.',
      });
      continue;
    }

    const directionValid = sourcePort.direction === 'output' && targetPort.direction === 'input';
    const typeValid = sourcePort.valueKind === targetPort.valueKind;
    const unitValid = unitSignature(sourcePort.unit) === unitSignature(targetPort.unit);

    checks.push({
      id: `${graph.id}.${edge.id}.typing`,
      domain: typeValid && unitValid ? 'TOPOLOGY' : 'DIMENSION',
      status: directionValid && typeValid && unitValid ? 'PASS' : 'FAIL',
      detail: `direction=${directionValid}; type=${sourcePort.valueKind}->${targetPort.valueKind}; unit=${unitSignature(sourcePort.unit)}->${unitSignature(targetPort.unit)}`,
    });
  }

  return checks;
}

function validateChart(chart: ScientificChartSemantic): ValidationCheckV1[] {
  const fields = new Map(chart.data.fields.map((field) => [field.id, field]));
  const referenced = [chart.encoding.x.field, chart.encoding.y.field, chart.encoding.color?.field, chart.uncertainty?.field].filter(Boolean) as string[];
  const missing = referenced.filter((field) => !fields.has(field));

  return [{
    id: `${chart.id}.fields`,
    domain: 'DATA',
    status: missing.length ? 'FAIL' : 'PASS',
    detail: missing.length ? `Missing chart fields: ${missing.join(', ')}` : 'All visual encodings reference declared data fields.',
  }];
}

export function validateMVSProject(project: MVSProjectV1): ValidationCheckV1[] {
  const checks: ValidationCheckV1[] = [];
  const semanticIds = project.semantics.objects.map((object) => object.id);
  const duplicates = semanticIds.filter((id, index) => semanticIds.indexOf(id) !== index);

  checks.push({
    id: 'schema.project',
    domain: 'SCHEMA',
    status: project.schema === 'mvs.visual-ir/1.0' && project.presentation.schema === 'mvs.presentation-ir/1.0' ? 'PASS' : 'FAIL',
    detail: 'Semantic and presentation IR schema identifiers are explicit.',
  });

  checks.push({
    id: 'schema.semantic_ids',
    domain: 'SCHEMA',
    status: duplicates.length ? 'FAIL' : 'PASS',
    detail: duplicates.length ? `Duplicate semantic ids: ${[...new Set(duplicates)].join(', ')}` : 'Semantic object ids are unique.',
  });

  for (const object of project.semantics.objects) {
    if (object.kind === 'computational_graph') checks.push(...validateGraph(object));
    if (object.kind === 'scientific_chart') checks.push(...validateChart(object));
    if (object.kind === 'parametric_surface') {
      const { sampleU, sampleV, tolerance } = object.numericPolicy;
      const domainValid = Object.values(object.domain.bounds ?? {}).every(([min, max]) => Number.isFinite(min) && Number.isFinite(max) && min < max);
      checks.push({
        id: `${object.id}.domain`,
        domain: 'MATH',
        status: domainValid ? 'PASS' : 'FAIL',
        detail: domainValid ? 'All declared parameter domains are finite and ordered.' : 'Invalid parameter domain detected.',
      });
      checks.push({
        id: `${object.id}.numeric_policy`,
        domain: 'NUMERICAL',
        status: sampleU >= 8 && sampleV >= 8 && Number.isFinite(tolerance) && tolerance > 0 ? 'PASS' : 'FAIL',
        detail: `float64 samples=${sampleU}x${sampleV}; tolerance=${tolerance}`,
      });
      checks.push({
        id: `${object.id}.epistemic`,
        domain: 'PROVENANCE',
        status: object.epistemicStatus === 'ILLUSTRATIVE' ? 'WARN' : 'PASS',
        detail: `Object epistemic status is ${object.epistemicStatus}.`,
      });
    }
  }

  for (const item of project.presentation.objects) {
    checks.push({
      id: `presentation.${item.id}.semantic_ref`,
      domain: 'VISUAL_ENCODING',
      status: semanticIds.includes(item.semanticRef) ? 'PASS' : 'FAIL',
      detail: semanticIds.includes(item.semanticRef) ? 'Presentation object resolves to semantic source.' : `Unknown semanticRef ${item.semanticRef}.`,
    });
  }

  checks.push({
    id: 'reproduction.fail_closed',
    domain: 'REPRODUCTION',
    status: project.validationPolicy.failClosed === true ? 'PASS' : 'FAIL',
    detail: 'Project requires fail-closed validation.',
  });

  return checks;
}

export function summarizeValidation(checks: ValidationCheckV1[]): { status: GateStatus; byDomain: Record<string, GateStatus> } {
  const byDomain: Record<string, GateStatus> = {};
  for (const check of checks) {
    const current = byDomain[check.domain];
    if (!current) {
      byDomain[check.domain] = check.status;
      continue;
    }
    byDomain[check.domain] = aggregateStatus([
      { id: 'current', domain: check.domain, status: current, detail: '' },
      check,
    ]);
  }
  return { status: aggregateStatus(checks), byDomain };
}
