import Ajv2020 from 'ajv/dist/2020';
import { describe, expect, it } from 'vitest';
import enginePackSchema from '../schemas/engine-pack-v1.schema.json';
import manifest from '../engine-packs/scientific-core/manifest.json';

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
});
