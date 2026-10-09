/**
 * MSR-MOD-0002 — dimensionless browser reference for a two-dimensional
 * pointwise inversion inspector. Python remains the mathematical authority.
 * No GPU precision or physical-system conclusions are inferred here.
 */
export function invertPoint2(point, radius) {
  if (!Array.isArray(point) || point.length !== 2 ||
      !point.every(Number.isFinite) || !Number.isFinite(radius) || radius <= 0) {
    throw new RangeError('Expected a finite 2D point and a positive finite radius');
  }
  const squared = point[0] * point[0] + point[1] * point[1];
  if (!Number.isFinite(squared) || squared === 0) {
    throw new RangeError('Inversion is singular or outside representable range');
  }
  const scale = (radius / Math.sqrt(squared)) ** 2;
  const result = [scale * point[0], scale * point[1]];
  if (!Number.isFinite(scale) || scale === 0 ||
      !result.every(Number.isFinite) || (result[0] === 0 && result[1] === 0)) {
    throw new RangeError('Inverted coordinate cannot be represented reliably');
  }
  return result;
}

/** Both errors are absolute residuals, not empirical model validation. */
export function inspectProbe(point, radius) {
  const image = invertPoint2(point, radius);
  const recovered = invertPoint2(image, radius);
  return {
    image,
    roundTripError: Math.hypot(recovered[0] - point[0], recovered[1] - point[1]),
    radialError: Math.abs(Math.hypot(...point) * Math.hypot(...image) - radius * radius)
  };
}
