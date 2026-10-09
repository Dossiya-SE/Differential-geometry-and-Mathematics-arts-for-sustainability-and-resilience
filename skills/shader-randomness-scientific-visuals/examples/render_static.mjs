/** Deterministic static diagonal-tile SVG for the Chapter 10 learning fixture. */
import {tileOrientation} from './random_fields.mjs';
import {readFileSync, writeFileSync} from 'node:fs';

export function renderStaticSvg() {
  const paths = [];
  const cells = [];
  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      const x = 150 + 51 * col;
      const y = 126 + 51 * row;
      const d = tileOrientation(col, row)
        ? `M ${x} ${y + 51} L ${x + 51} ${y}`
        : `M ${x} ${y} L ${x + 51} ${y + 51}`;
      cells.push(`  <rect x="${x}" y="${y}" width="51" height="51" fill="none" stroke="#D1DCE4" stroke-width="1"/>`);
      paths.push(`  <path d="${d}" fill="none" stroke="#00BFFF" stroke-width="3.4"/>`);
    }
  }
  return [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 710 625" role="img" data-figure-id="MSR-FIG-0003">',
    '  <title>Deterministic Truchet-style tile orientation, 8 by 8 grid</title>',
    '  <desc>On a white background, sixty-four outlined square cells contain one of two blue diagonal line orientations. Each orientation is selected by a fixed-seed integer hash; there is no physical network or measured quantity represented.</desc>',
    '  <text x="50" y="52" font-size="25" font-family="Arial,sans-serif" fill="#17202A" font-weight="600">Cell orientation from a fixed seed</text>',
    '  <text x="50" y="81" font-size="18" font-family="Arial,sans-serif" fill="#516270">Synthetic mathematical art — not spatial data</text>',
    '  <text x="150" y="113" font-size="17" font-family="Arial,sans-serif" fill="#17202A">Column →</text>',
    '  <text x="63" y="146" font-size="17" font-family="Arial,sans-serif" fill="#17202A">Row ↓</text>',
    ...cells,
    ...paths,
    '  <text x="50" y="574" font-size="17" font-family="Arial,sans-serif" fill="#17202A">seed = 20261009  |  hash: deterministic uint32 mix  |  orientation: two diagonal glyphs</text>',
    '  <text x="50" y="601" font-size="17" font-family="Arial,sans-serif" fill="#516270">MSR-FIG-0003 · domain-neutral proposed educational fixture</text>',
    '</svg>',
    ''
  ].join('\n');
}

if (process.argv[1] && import.meta.url === new URL(`file://${process.argv[1]}`).href) {
  const output = new URL('../../../art/shaders/randomness_lab/static.svg', import.meta.url);
  if (process.argv.includes('--check')) {
    if (readFileSync(output, 'utf8') !== renderStaticSvg()) {
      throw new Error('Static SVG differs from generated reference; re-render before commit');
    }
    process.stdout.write('PASS static randomness SVG source equivalence\n');
  } else if (process.argv.includes('--write')) {
    writeFileSync(output, renderStaticSvg(), 'utf8');
  } else {
    throw new Error('Choose --check or --write');
  }
}
