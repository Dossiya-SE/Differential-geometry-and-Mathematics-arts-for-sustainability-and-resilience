import test from 'node:test';
import assert from 'node:assert/strict';
import { invertPoint2, inspectProbe } from './probe.mjs';

test('known 2D inversion and fixed-radius points', () => {
  assert.deepEqual(invertPoint2([2, 0], 1), [0.5, 0]);
  assert.deepEqual(invertPoint2([1, 0], 1), [1, 0]);
  assert.deepEqual(invertPoint2([0, 2], 2), [0, 2]);
});

test('invalid and singular inputs fail closed', () => {
  for (const [point, r] of [
    [[0, 0], 1], [[1, 0], 0], [[Infinity, 1], 1],
    [[1, Number.NaN], 1], [[1], 1], [[1, 1], Infinity],
    [[1e-300, 0], 1], [[1e300, 0], 1]
  ]) assert.throws(() => invertPoint2(point, r), RangeError);
});

test('radial product and involution across 240 deterministic parameter sets', () => {
  let seed = 20261009;
  const sample = () => { seed = (1664525 * seed + 1013904223) >>> 0; return seed / 2**32; };
  for (let i = 0; i < 240; i++) {
    const theta = 2 * Math.PI * sample();
    const distance = 0.3 + 2.2 * sample();
    const radius = 0.6 + 1.3 * sample();
    const point = [distance * Math.cos(theta), distance * Math.sin(theta)];
    const { roundTripError, radialError } = inspectProbe(point, radius);
    assert.ok(roundTripError < 1e-12, `round-trip residual ${roundTripError}`);
    assert.ok(radialError < 1e-12, `radial residual ${radialError}`);
  }
});
