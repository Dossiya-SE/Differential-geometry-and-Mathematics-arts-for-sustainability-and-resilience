function normalize(value: unknown): unknown {
  if (value === null || typeof value === 'string' || typeof value === 'boolean') return value;

  if (typeof value === 'number') {
    if (!Number.isFinite(value)) throw new Error('Canonical Visual IR cannot contain NaN or Infinity.');
    return Object.is(value, -0) ? 0 : value;
  }

  if (Array.isArray(value)) return value.map(normalize);

  if (typeof value === 'object') {
    const record = value as Record<string, unknown>;
    const normalized: Record<string, unknown> = {};
    for (const key of Object.keys(record).sort()) {
      const entry = record[key];
      if (entry === undefined) continue;
      if (typeof entry === 'function' || typeof entry === 'symbol' || typeof entry === 'bigint') {
        throw new Error(`Unsupported canonical Visual IR value at key ${key}.`);
      }
      normalized[key] = normalize(entry);
    }
    return normalized;
  }

  throw new Error(`Unsupported canonical Visual IR type: ${typeof value}`);
}

export function canonicalizeVisualIR(value: unknown): unknown {
  return normalize(value);
}

export function canonicalJSONString(value: unknown): string {
  return JSON.stringify(canonicalizeVisualIR(value));
}
