import test from 'node:test';
import assert from 'node:assert/strict';
import {INSIDE_START,OUTSIDE_START,trajectory,norm,isViableAtStart,boundaryCrossingTime,squaredNormDerivative} from './model.mjs';
test('exact initial state, semigroup and derivative law',()=>{
  for(const x0 of [INSIDE_START,OUTSIDE_START,[-1,0],[0,1]]){
    assert.deepEqual(trajectory(x0,0),x0);
    for(let k=0;k<=50;k++){
      const s=k/17,t=k/31;
      const a=trajectory(trajectory(x0,s),t),b=trajectory(x0,s+t);
      a.forEach((v,i)=>assert.ok(Math.abs(v-b[i])<3e-15));
    }
    const eps=1e-6;
    const finiteDiff=(norm(trajectory(x0,eps))**2-norm(trajectory(x0,0))**2)/eps;
    assert.ok(Math.abs(finiteDiff-squaredNormDerivative(x0))<1e-5);
  }
});
test('unit disk invariance and admission at initial instant',()=>{
  assert.equal(isViableAtStart(INSIDE_START),true);
  assert.equal(isViableAtStart(OUTSIDE_START),false);
  assert.equal(isViableAtStart([1,0]),true);
  for(let i=0;i<=300;i++){
    const theta=2*Math.PI*(i/301),r=(i%23)/22;
    const x0=[r*Math.cos(theta),r*Math.sin(theta)];
    assert.equal(isViableAtStart(x0),true);
    assert.ok(norm(trajectory(x0,i/100))<=1+1e-14);
  }
});
test('outside point enters disk but is not viable from outside initial state',()=>{
  const cross=boundaryCrossingTime(OUTSIDE_START);
  assert.ok(cross!==null && cross>0 && cross<1);
  assert.ok(Math.abs(norm(trajectory(OUTSIDE_START,cross))-1)<1e-14);
  assert.ok(norm(trajectory(OUTSIDE_START,cross+0.1))<1);
  assert.equal(isViableAtStart(OUTSIDE_START),false);
  assert.equal(boundaryCrossingTime(INSIDE_START),null);
});
test('invalid inputs are rejected instead of silently rendered',()=>{
  for(const x of [[],[1],[NaN,0],[Infinity,1],[0,0,0]])assert.throws(()=>trajectory(x,1),RangeError);
  for(const τ of [-0.01,NaN,Infinity])assert.throws(()=>trajectory([1,0],τ),RangeError);
});
