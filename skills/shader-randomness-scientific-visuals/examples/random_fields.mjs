/**
 * Deterministic, domain-neutral mathematical examples inspired by the concepts
 * taught in The Book of Shaders, Chapter 10. Original implementation.
 * These are procedural graphics examples, not stochastic/physical models.
 */
const UINT_DENOMINATOR = 16777216;
const INT_MIN = -2147483648;
const INT_MAX = 2147483647;

function finiteNumber(value, name) {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    throw new RangeError(`${name} must be a finite number`);
  }
}
function signedCell(value, name) {
  if (!Number.isInteger(value) || value < INT_MIN || value > INT_MAX) {
    throw new RangeError(`${name} must be a signed 32-bit integer`);
  }
}
function checkedSeed(seed) {
  if (!Number.isSafeInteger(seed) || seed < 0 || seed > 0xffffffff) {
    throw new RangeError('seed must be a uint32 integer');
  }
}

/** Educational fractional-sine map; not a scientific random number generator. */
export function sineFragmentLesson(x) {
  finiteNumber(x, 'x');
  const y = Math.sin(7.41 * x + 0.31) * 437.71;
  return y - Math.floor(y);
}

/** Quantile mapping U -> U^gamma, conditional on a true uniform input U. */
export function biasQuantile(u, gamma) {
  finiteNumber(u, 'u');
  finiteNumber(gamma, 'gamma');
  if (u < 0 || u > 1 || gamma <= 0) {
    throw new RangeError('require 0 <= u <= 1 and gamma > 0');
  }
  return u ** gamma;
}

/**
 * Full uint32 arithmetic; return the 24 most significant hash bits divided
 * by 2^24 to avoid false claims of representing all 32 bits in GPU float32.
 * Hash collisions/dependence remain possible.
 */
export function hashCell(column, row, seed = 20261009) {
  signedCell(column, 'column');
  signedCell(row, 'row');
  checkedSeed(seed);
  let h = (Math.imul(column, 0x9e3779b1) ^ Math.imul(row, 0x85ebca77) ^ seed) >>> 0;
  h ^= h >>> 16;
  h = Math.imul(h, 0x7feb352d) >>> 0;
  h ^= h >>> 15;
  h = Math.imul(h, 0x846ca68b) >>> 0;
  h ^= h >>> 16;
  return (h >>> 8) / UINT_DENOMINATOR;
}

/** Integer lattice and local in-cell position, including negative positions. */
export function cellCoordinates(x, y, frequency) {
  finiteNumber(x, 'x');
  finiteNumber(y, 'y');
  finiteNumber(frequency, 'frequency');
  if (frequency <= 0) throw new RangeError('frequency must be positive');
  const sx = x * frequency;
  const sy = y * frequency;
  if (!Number.isFinite(sx) || !Number.isFinite(sy)) {
    throw new RangeError('scaled coordinates overflow');
  }
  const column = Math.floor(sx);
  const row = Math.floor(sy);
  signedCell(column, 'column');
  signedCell(row, 'row');
  return {column, row, u: sx - column, v: sy - row};
}

/** Two diagonal tile orientations; visual adjacency is not physical topology. */
export function tileOrientation(column, row, seed = 20261009) {
  return hashCell(column, row, seed) < 0.5 ? 0 : 1;
}

/** Signed row displacement as a function of *display* time only. */
export function rowShift(row, displayTime, seed = 20261009) {
  signedCell(row, 'row');
  finiteNumber(displayTime, 'displayTime');
  // Return canonical +0 for both positive and negative rows at reset.
  if (displayTime === 0) return 0;
  const speed = 0.25 + 0.6 * hashCell(row, 0, seed);
  const direction = row % 2 === 0 ? 1 : -1;
  const shift = direction * speed * displayTime;
  if (!Number.isFinite(shift)) throw new RangeError('display displacement overflow');
  return shift;
}

function easedFraction(u) {
  return u * u * (3 - 2 * u);
}

/**
 * Bilinear value interpolation with cubic smoothstep; continuous synthetic
 * coordinate field, with no specified empirical covariance.
 */
export function smoothValueField(x, y, seed = 20261009) {
  const {column, row, u, v} = cellCoordinates(x, y, 1);
  if (column === INT_MAX || row === INT_MAX) {
    throw new RangeError('neighbor cell beyond supported integer lattice');
  }
  const a = hashCell(column, row, seed);
  const b = hashCell(column + 1, row, seed);
  const c = hashCell(column, row + 1, seed);
  const d = hashCell(column + 1, row + 1, seed);
  const sx = easedFraction(u);
  const sy = easedFraction(v);
  return (1 - sy) * ((1 - sx) * a + sx * b) + sy * ((1 - sx) * c + sx * d);
}
