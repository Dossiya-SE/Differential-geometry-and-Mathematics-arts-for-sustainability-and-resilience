from __future__ import annotations
from pathlib import Path
import json
from .hashing import sha256_file

ALLOWED = {"USER_SPECIFIED","COMPUTED","OBSERVED","PUBLISHED","CALIBRATED","DERIVED","ASSUMED","SYNTHETIC","ILLUSTRATIVE","TO_BE_VALIDATED"}
REQUIRED_IDS = ["stage.real_problem","stage.evidence","stage.gap_architecture","stage.research_question","stage.system_assumptions","stage.mathematical_formulation","stage.computation","stage.verification","stage.calibration","stage.validation","stage.sensitivity","stage.uncertainty","stage.comparison","stage.results","stage.industrial_implication","stage.bounded_conclusion","central.model_manifold","central.controlled_trajectory","uncertainty.tube.visual","conclusion.admissible_region.visual"]
REQUIRED_EQ = ["EQ-MODEL-001","EQ-CONSTRAINT-001","EQ-VERIFY-001","EQ-CAL-001","EQ-VAL-001","EQ-SENS-001","EQ-UQ-001","EQ-CONCLUSION-001"]


def scientific_gate(request, framework_spec, data):
    checks={}
    checks['stage_count']=len(framework_spec['stages'])==request['qa']['required_stage_count']
    checks['unique_stage_ids']=len({s['object_id'] for s in framework_spec['stages']})==len(framework_spec['stages'])
    checks['epistemic_statuses']=all(o.get('status') in ALLOWED for o in data['objects'])
    checks['observed_has_source']=all((o.get('status')!='OBSERVED') or bool(o.get('source')) for o in data['objects'])
    return checks


def mathematical_gate(equations_text):
    return {'required_equation_ids': all(eq in equations_text for eq in REQUIRED_EQ)}


def visual_gate(svg_text, request):
    return {'stable_object_ids': all(f'id="{oid}"' in svg_text for oid in REQUIRED_IDS),'canvas_width': f'width="{request["canvas"]["width"]}"' in svg_text,'canvas_height': f'height="{request["canvas"]["height"]}"' in svg_text,'no_raster_image_elements': '<image ' not in svg_text}


def artifact_gate(outdir, required):
    outdir=Path(outdir); return {name:(outdir/name).exists() and (outdir/name).stat().st_size>0 for name in required}


def all_pass(mapping):
    return all(mapping.values())


def write_manifest(outdir, input_files, output_files, metadata):
    outdir=Path(outdir)
    manifest={'metadata':metadata,'inputs':{},'outputs':{}}
    for label,path in input_files.items(): manifest['inputs'][label]={'path':str(path),'sha256':sha256_file(path)}
    for label,path in output_files.items(): manifest['outputs'][label]={'path':Path(path).name,'sha256':sha256_file(path),'bytes':Path(path).stat().st_size}
    p=outdir/'manifest.json'; p.write_text(json.dumps(manifest,indent=2,sort_keys=True),encoding='utf-8'); return p
