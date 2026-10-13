from __future__ import annotations
from pathlib import Path
import json, shutil, tempfile, zipfile, subprocess, sys, os
import cairosvg
from PIL import Image

from .spec import load_yaml, load_json
from .svg_composer import compose_svg
from .pptx_export import export_pptx
from .hashing import sha256_file
from .qa import scientific_gate, mathematical_gate, visual_gate, artifact_gate, all_pass, write_manifest


def _resolve(base, p): return (Path(base)/p).resolve()


def load_context(request_path):
    request_path=Path(request_path).resolve(); root=request_path.parent.parent
    request=load_yaml(request_path)
    fs=load_yaml(_resolve(root,request['sources']['framework_spec']))
    vg=load_yaml(_resolve(root,request['sources']['visual_grammar']))
    eq_path=_resolve(root,request['sources']['equations']); eq=eq_path.read_text(encoding='utf-8')
    data_path=_resolve(root,request['sources']['research_data']); data=load_json(data_path)
    return root,request,fs,vg,eq,data,eq_path,data_path


def render_core(request_path, outdir):
    root,request,fs,vg,eq,data,eq_path,data_path=load_context(request_path)
    outdir=Path(outdir).resolve(); outdir.mkdir(parents=True,exist_ok=True)
    svg=compose_svg(request,fs,vg,data)
    svg_path=outdir/'poster_EDITABLE.svg'; svg_path.write_text(svg,encoding='utf-8')
    png_path=outdir/'poster.png'; pdf_path=outdir/'poster.pdf'; pptx_path=outdir/'poster_EDITABLE.pptx'
    cairosvg.svg2png(bytestring=svg.encode('utf-8'),write_to=str(png_path),output_width=request['canvas']['width']*2,output_height=request['canvas']['height']*2)
    cairosvg.svg2pdf(bytestring=svg.encode('utf-8'),write_to=str(pdf_path))
    export_pptx(request,fs,pptx_path)
    shutil.copy2(request_path,outdir/'render_request.yaml'); shutil.copy2(eq_path,outdir/'equations.tex'); shutil.copy2(data_path,outdir/'research_data.json')
    return {'root':root,'request':request,'framework_spec':fs,'visual_grammar':vg,'equations':eq,'data':data,'svg':svg,'paths':{'svg':svg_path,'png':png_path,'pdf':pdf_path,'pptx':pptx_path,'request':outdir/'render_request.yaml','equations':outdir/'equations.tex','data':outdir/'research_data.json'}}


def _bundle_sources(context, request_path, bundle_path, expected):
    root=context['root']; bundle_path=Path(bundle_path)
    members=[Path(request_path).resolve(), root/'spec'/'framework.yaml',root/'spec'/'visual_grammar.yaml',root/'equations'/'equations.tex',root/'data'/'research_data.json',root/'pyproject.toml']
    members += sorted((root/'src'/'framework').glob('*.py'))
    with zipfile.ZipFile(bundle_path,'w',zipfile.ZIP_DEFLATED) as z:
        for p in members: z.write(p,p.relative_to(root))
        z.writestr('expected_release.json',json.dumps(expected,indent=2,sort_keys=True))
        z.writestr('REPRODUCE.txt','Install dependencies from pyproject.toml, then run: framework reproduce --bundle SOURCE_BUNDLE.zip\nThe accepted SVG/PNG/PDF are not used as reproduction inputs.\n')


def reproduce_bundle(bundle_path, workdir=None):
    bundle_path=Path(bundle_path).resolve(); workdir=Path(workdir or tempfile.mkdtemp(prefix='framework-reproduce-')).resolve(); workdir.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(bundle_path) as z: z.extractall(workdir)
    expected=json.loads((workdir/'expected_release.json').read_text())
    env=os.environ.copy(); env['PYTHONPATH']=str(workdir/'src')
    cmd=[sys.executable,'-c',"from framework.controller import render_core; render_core('render_requests/Research_Framework_V4.yaml','reproduced')"]
    proc=subprocess.run(cmd,cwd=workdir,env=env,capture_output=True,text=True)
    result={'subprocess_returncode':proc.returncode,'stderr':proc.stderr[-2000:]}
    if proc.returncode!=0: result.update({'svg_hash_match':False,'png_dimensions_match':False,'pass':False}); return result
    svg=workdir/'reproduced'/'poster_EDITABLE.svg'; png=workdir/'reproduced'/'poster.png'
    result['svg_hash_match']=sha256_file(svg)==expected['svg_sha256']
    result['png_dimensions_match']=list(Image.open(png).size)==expected['png_dimensions']
    result['pass']=result['svg_hash_match'] and result['png_dimensions_match']
    return result


def render_release(request_path='render_requests/Research_Framework_V4.yaml', outdir='exports'):
    request_path=Path(request_path).resolve(); outdir=Path(outdir).resolve()
    if outdir.exists():
        for p in outdir.iterdir():
            if p.is_file() or p.is_symlink(): p.unlink()
            elif p.is_dir(): shutil.rmtree(p)
    context=render_core(request_path,outdir)
    expected={'svg_sha256':sha256_file(context['paths']['svg']),'png_dimensions':list(Image.open(context['paths']['png']).size)}
    bundle=outdir/'SOURCE_BUNDLE.zip'; _bundle_sources(context,request_path,bundle,expected)
    reproduction=reproduce_bundle(bundle)
    scientific=scientific_gate(context['request'],context['framework_spec'],context['data'])
    mathematical=mathematical_gate(context['equations'])
    visual=visual_gate(context['svg'],context['request'])
    pre_required=[a for a in context['request']['required_artifacts'] if a not in {'manifest.json','qa_report.json'}]
    editability=artifact_gate(outdir,pre_required)
    provenance={'source_bundle_exists':bundle.exists(),'render_request_frozen':(outdir/'render_request.yaml').exists(),'equation_source_preserved':(outdir/'equations.tex').exists(),'research_data_preserved':(outdir/'research_data.json').exists()}
    gates={'scientific':all_pass(scientific),'mathematical':all_pass(mathematical),'visual':all_pass(visual),'editability':all_pass(editability),'provenance':all_pass(provenance),'reproduction':bool(reproduction.get('pass'))}
    final_status=context['request']['acceptance']['status_pass'] if all(gates.values()) else context['request']['acceptance']['status_fail']
    qa={'controller':context['request']['controller'],'final_status':final_status,'gates':gates,'details':{'scientific':scientific,'mathematical':mathematical,'visual':visual,'editability':editability,'provenance':provenance,'reproduction':reproduction},'notes':['All research mini-objects in the default V4 data file are ILLUSTRATIVE unless their epistemic status is explicitly changed with valid provenance.','poster_EDITABLE.svg is canonical; poster_EDITABLE.pptx is a convenience-editable derivative and does not redefine canonical geometry.']}
    qa_path=outdir/'qa_report.json'; qa_path.write_text(json.dumps(qa,indent=2,sort_keys=True),encoding='utf-8')
    input_files={'render_request':request_path,'framework_spec':context['root']/'spec'/'framework.yaml','visual_grammar':context['root']/'spec'/'visual_grammar.yaml','equations':context['root']/'equations'/'equations.tex','research_data':context['root']/'data'/'research_data.json'}
    output_files={'poster_EDITABLE.svg':context['paths']['svg'],'poster_EDITABLE.pptx':context['paths']['pptx'],'poster.png':context['paths']['png'],'poster.pdf':context['paths']['pdf'],'render_request.yaml':outdir/'render_request.yaml','equations.tex':outdir/'equations.tex','research_data.json':outdir/'research_data.json','qa_report.json':qa_path,'SOURCE_BUNDLE.zip':bundle}
    write_manifest(outdir,input_files,output_files,{'controller_id':context['request']['controller']['id'],'project_version':context['request']['project']['version'],'final_status':final_status})
    final_artifacts=artifact_gate(outdir,context['request']['required_artifacts'])
    if not all_pass(final_artifacts):
        qa['final_status']=context['request']['acceptance']['status_fail']; qa['gates']['editability']=False; qa['details']['final_artifacts']=final_artifacts; qa_path.write_text(json.dumps(qa,indent=2,sort_keys=True),encoding='utf-8')
    return json.loads(qa_path.read_text())


def audit_release(outdir='exports'):
    outdir=Path(outdir); return json.loads((outdir/'qa_report.json').read_text())
