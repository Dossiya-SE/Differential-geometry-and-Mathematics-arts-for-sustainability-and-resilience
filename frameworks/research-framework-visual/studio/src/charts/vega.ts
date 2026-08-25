import { compile, type TopLevelSpec } from 'vega-lite';
import type { ScientificChartSemantic } from '../ir/v1';

function vegaType(type: ScientificChartSemantic['data']['fields'][number]['type']): 'quantitative' | 'ordinal' | 'nominal' | 'temporal' {
  return type;
}

export function scientificChartToVegaLite(chart: ScientificChartSemantic): TopLevelSpec {
  const fields = new Map(chart.data.fields.map((field) => [field.id, field]));
  const xField = fields.get(chart.encoding.x.field);
  const yField = fields.get(chart.encoding.y.field);
  if (!xField || !yField) throw new Error('Chart encoding references undeclared x/y fields.');

  const spec: TopLevelSpec = {
    $schema: 'https://vega.github.io/schema/vega-lite/v6.json',
    data: { name: chart.data.name },
    mark: { type: chart.mark },
    encoding: {
      x: {
        field: xField.id,
        type: vegaType(xField.type),
        title: xField.unit ? `${xField.id} [${xField.unit.symbol}]` : xField.id,
      },
      y: {
        field: yField.id,
        type: vegaType(yField.type),
        title: yField.unit ? `${yField.id} [${yField.unit.symbol}]` : yField.id,
      },
    },
  };

  return spec;
}

export function compileScientificChart(chart: ScientificChartSemantic) {
  return compile(scientificChartToVegaLite(chart));
}
