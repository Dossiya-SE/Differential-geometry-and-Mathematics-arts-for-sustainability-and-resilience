import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {renderAll,outputs} from './render.mjs';
import {INSIDE_START,OUTSIDE_START,norm,boundaryCrossingTime} from '../animations/viability_lab/model.mjs';

const root=new URL('../../',import.meta.url);
test('all five mathematical/semantic artifacts are byte-exactly reproducible',()=>{
  assert.equal(Object.keys(outputs).length,5);
  const generated=renderAll();
  for(const [path,svg] of Object.entries(generated)){
    assert.equal(readFileSync(new URL(path,root),'utf8'),svg,path);
    assert.ok(svg.startsWith('<?xml version="1.0"'));
    assert.match(svg,/<title id="title">/);
    assert.match(svg,/<desc id="description">/);
    assert.ok(!svg.includes('#E69F00')&&!svg.includes('linearGradient'));
  }
});
test('diagram contains exactly five stages and four typed arrows',()=>{
  const svg=renderAll()['art/diagrams/model_to_visualization.svg'];
  assert.equal((svg.match(/data-node=/g)||[]).length,5);
  assert.equal((svg.match(/data-edge=/g)||[]).length,4);
  for(const stage of ['Theory','Model','Computation','Visualization','Interpretation'])
    assert.ok(svg.includes('data-node="'+stage+'"'));
});
test('mind map is nine unambiguous children under three branches and one root',()=>{
  const svg=renderAll()['art/mindmaps/mathematics_taxonomy.svg'];
  assert.equal((svg.match(/data-node="root"/g)||[]).length,1);
  assert.equal((svg.match(/data-node="branch-/g)||[]).length,3);
  assert.equal((svg.match(/data-node="leaf-/g)||[]).length,9);
  assert.equal((svg.match(/data-relation=/g)||[]).length,12);
  assert.equal((svg.match(/marker-end=/g)||[]).length,0);
});
test('analytic chart curve endpoints agree with the numerical flow',()=>{
  const figure=renderAll()['art/charts/analytic_radius.svg'];
  const samples=label=>{
    const m=figure.match(new RegExp('data-curve="'+label+'" d="([^"]+)"'));
    assert.ok(m,'missing curve '+label);
    return [...m[1].matchAll(/[ML] ([0-9.]+) ([0-9.]+)/g)].map(z=>[Number(z[1]),Number(z[2])]);
  };
  const A=samples('A'),B=samples('B');
  assert.equal(A.length,181);assert.equal(B.length,181);
  const chartY=r=>603-446*r/1.6;
  for(const [label,series,start] of [['A',A,INSIDE_START],['B',B,OUTSIDE_START]]){
    assert.ok(Math.abs(series[0][1]-chartY(norm(start)))<0.001,label);
    assert.ok(Math.abs(series.at(-1)[1]-chartY(norm(start)*Math.exp(-3)))<0.001,label);
    for(let i=1;i<series.length;i++)assert.ok(series[i][1]>=series[i-1][1],label+' nonincreasing radial norm');
  }
  assert.match(figure,/data-curve="threshold"/);
  const cross=boundaryCrossingTime(OUTSIDE_START);
  assert.ok(cross!==null);
  const m=figure.match(/data-event="B-crosses-threshold" cx="([^"]+)" cy="([^"]+)"/);
  assert.ok(m);
  assert.ok(Math.abs(Number(m[1])-(145+812*cross/3))<.001);
  assert.ok(Math.abs(Number(m[2])-chartY(1))<.001);
});
test('stereographic projection points are collinear in the declared orthographic camera',()=>{
  const figure=renderAll()['art/mathematical_figures/stereographic_projection.svg'];
  const getPoint=name=>{
    const match=figure.match(new RegExp('data-point="'+name+'" cx="([^"]+)" cy="([^"]+)"'));
    assert.ok(match);return [Number(match[1]),Number(match[2])];
  };
  const [nx,ny]=getPoint('N'),[px,py]=getPoint('P'),[qx,qy]=getPoint('Q');
  const determinant=(qx-nx)*(py-ny)-(qy-ny)*(px-nx);
  assert.ok(Math.abs(determinant)<0.5,'projection line must pass through all three plotted points');
  assert.match(figure,/Domain: S² without the north pole N/);
});
