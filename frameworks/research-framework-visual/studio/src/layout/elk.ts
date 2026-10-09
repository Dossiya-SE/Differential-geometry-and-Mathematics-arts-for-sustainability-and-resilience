import ELK from 'elkjs/lib/elk.bundled.js';
import type { ComputationalGraphSemantic } from '../ir/v1';

export interface ResolvedNodeLayout {
  id: string;
  x: number;
  y: number;
  width: number;
  height: number;
}

const elk = new ELK();

export async function layoutComputationalGraph(graph: ComputationalGraphSemantic): Promise<ResolvedNodeLayout[]> {
  const result = await elk.layout({
    id: graph.id,
    layoutOptions: {
      'elk.algorithm': 'layered',
      'elk.direction': 'RIGHT',
      'elk.edgeRouting': 'ORTHOGONAL',
      'elk.layered.spacing.nodeNodeBetweenLayers': '80',
      'elk.spacing.nodeNode': '40',
    },
    children: graph.nodes.map((node) => ({ id: node.id, width: 220, height: 96 })),
    edges: graph.edges.map((edge) => ({
      id: edge.id,
      sources: [edge.from.nodeId],
      targets: [edge.to.nodeId],
    })),
  });

  const resolved = (result.children ?? []).map((node) => ({
    id: node.id,
    x: node.x ?? Number.NaN,
    y: node.y ?? Number.NaN,
    width: node.width ?? Number.NaN,
    height: node.height ?? Number.NaN,
  }));

  if (resolved.some((node) => ![node.x, node.y, node.width, node.height].every(Number.isFinite))) {
    throw new Error('ELK returned non-finite layout geometry.');
  }

  return resolved;
}
