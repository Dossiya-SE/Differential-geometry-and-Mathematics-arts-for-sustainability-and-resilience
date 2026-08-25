import Ajv2020 from 'ajv/dist/2020';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import enginePackSchema from '../schemas/engine-pack-v1.schema.json';
import manifest from '../engine-packs/scientific-core/manifest.json';

function sha256(path: URL): string {
  const bytes = readFileSync(path);
  return `sha256:${createHash('sha256').update(bytes).digest('hex')}`;
}

describe('MVS Scientific Core engine-pack governance', () => {
  it('validates the manifest and preserves the fail-closed permission boundary', () => {
    const ajv = new Ajv2020({ allErrors: true, strict: true });
    const validate = ajv.compile(enginePackSchema);
    expect(validate(manifest), JSON.stringify(validate.errors)).toBe(true);
    expect(manifest.capabilities.network).toEqual([]);
    expect(manifest.capabilities.processSpawn).toEqual([]);
    expect(manifest.capabilities.filesystem.read).toEqual([]);
    expect(manifest.capabilities.filesystem.write).toEqual([]);
  });

  it('content-addresses both the governed worker and its dependency lock', () => {
    expect(sha256(new URL('../python/scientific_core_worker.py', import.meta.url))).toBe(manifest.payloadSha256);
    expect(sha256(new URL('../python/scientific-core-requirements.txt', import.meta.url))).toBe(manifest.lockSha256);
  });
});
