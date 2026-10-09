import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {biasQuantile, cellCoordinates, hashCell, rowShift, sineFragmentLesson,
        smoothValueField, tileOrientation} from './random_fields.mjs';
import {renderStaticSvg} from './render_static.mjs';

test('fractional sine is deterministic and range-bounded, not claimed random', () => {
  for (const x of [-5, -1, 0, 0.125, 1, 3.75]) {
    const a = sineFragmentLesson(x);
    assert.equal(a, sineFragmentLesson(x));
    assert.ok(a >= 0 && a < 1);
  }
  assert.throws(() => sineFragmentLesson(Infinity), RangeError);
});

test('power quantile is monotone and has expected endpoints', () => {
  for (const gamma of [0.5, 1, 2, 3.5]) {
    assert.equal(biasQuantile(0, gamma), 0);
    assert.equal(biasQuantile(1, gamma), 1);
    let prior = -1;
    for (let i = 0; i <= 100; i++) {
      const result = biasQuantile(i / 100, gamma);
      assert.ok(result >= prior);
      prior = result;
    }
  }
  assert.equal(biasQuantile(0.4, 1), 0.4);
  for (const bad of [[-0.1, 2], [1.1, 2], [0.5, 0], [NaN, 2]]) {
    assert.throws(() => biasQuantile(...bad), RangeError);
  }
});

test('integer hash is bounded, stable and sensitive to configured seed', () => {
  for (const i of [-100, -3, -1, 0, 1, 7, 120]) {
    for (const j of [-19, -1, 0, 1, 63]) {
      const h = hashCell(i, j, 20261009);
      assert.ok(h >= 0 && h < 1);
      assert.equal(h, hashCell(i, j, 20261009));
      assert.equal(h * 16777216, Math.floor(h * 16777216));
    }
  }
  assert.notEqual(hashCell(2, -3, 7), hashCell(2, -3, 8));
  assert.throws(() => hashCell(0.4, 1), RangeError);
  assert.throws(() => hashCell(2147483648, 0), RangeError);
  assert.throws(() => hashCell(0, 1, -1), RangeError);
});

test('cell indexing handles negative coordinates and deterministic tile glyphs', () => {
  const a = cellCoordinates(-0.1, 0.51, 4);
  assert.deepEqual(a, {column: -1, row: 2, u: 0.6, v: 0.040000000000000036});
  // The same integer cell always has the same orientation.
  assert.equal(tileOrientation(a.column, a.row), tileOrientation(-1, 2));
  assert.ok([0, 1].includes(tileOrientation(-1, 2)));
  assert.throws(() => cellCoordinates(1, 2, 0), RangeError);
});

test('row movement denotes synthetic display time, not system physics', () => {
  for (const row of [-3, -2, 0, 1, 2]) {
    assert.equal(rowShift(row, 0), 0);
    const s = rowShift(row, 1);
    assert.ok(Math.abs(s) >= 0.25 && Math.abs(s) <= 0.85);
    assert.ok(Math.abs(rowShift(row, 2) - 2 * s) < 1e-15);
  }
});

test('value interpolation reproduces lattice corners and remains continuous', () => {
  for (const i of [-5, -2, 0, 2, 7]) {
    for (const j of [-3, 0, 4]) {
      assert.equal(smoothValueField(i, j), hashCell(i, j));
      for (const x of [i - 1e-7, i + 1e-7]) {
        assert.ok(Math.abs(smoothValueField(x, j + 0.32)
                          - smoothValueField(i, j + 0.32)) < 1e-5);
      }
    }
  }
  for (let k = 0; k < 80; k++) {
    const v = smoothValueField(k / 11 - 3, k / 17 - 2);
    assert.ok(v >= 0 && v < 1);
  }
});

test('proposed static fallback is exactly reproducible', () => {
  const path = new URL('../../../art/shaders/randomness_lab/static.svg', import.meta.url);
  assert.equal(readFileSync(path, 'utf8'), renderStaticSvg());
  assert.ok(renderStaticSvg().includes('data-figure-id="MSR-FIG-0003"'));
  assert.ok(renderStaticSvg().includes('<desc>'));
});
