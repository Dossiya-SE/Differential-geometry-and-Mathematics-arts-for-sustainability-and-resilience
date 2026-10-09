import {INSIDE_START,OUTSIDE_START,T_MAX,trajectory,norm} from './model.mjs';
const byId=id=>document.getElementById(id);
const slider=byId('time'),play=byId('play'),reset=byId('reset');
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
let frame=null,last=null;
function stop(){if(frame!==null)cancelAnimationFrame(frame);frame=null;last=null;play.textContent='Play';}
function update(){
  const t=Number(slider.value),toScreen=x=>[420+190*x[0],377-190*x[1]];
  for(const [id,initial] of [['A',INSIDE_START],['B',OUTSIDE_START]]){
    const state=trajectory(initial,t),[cx,cy]=toScreen(state);
    const point=byId('point'+id),label=byId('label'+id);
    point.setAttribute('cx',cx.toFixed(3));point.setAttribute('cy',cy.toFixed(3));
    label.setAttribute('x',(cx+17).toFixed(3));label.setAttribute('y',(cy-17).toFixed(3));
    byId('r'+id).textContent='‖'+id+'(τ)‖ = '+norm(state).toFixed(4);
  }
  byId('timeLabel').textContent=t.toFixed(2);
  byId('status').textContent='τ='+t.toFixed(2)+'. Both trajectories follow exp(−τ); B was outside K at τ=0 even if it has entered now.';
}
function tick(stamp){
  if(last!==null)slider.value=String(Math.min(T_MAX,Number(slider.value)+(stamp-last)*.0005));
  last=stamp;update();
  if(Number(slider.value)>=T_MAX){stop();return;}
  frame=requestAnimationFrame(tick);
}
function refreshMotion(){
  if(reduced.matches)stop();
  play.disabled=reduced.matches;
  play.title=reduced.matches?'Animation disabled by reduced-motion preference':'Play dimensionless parameter';
}
slider.disabled=false;reset.disabled=false;
byId('reference').classList.add('hidden');
byId('interactive').classList.remove('hidden');
slider.addEventListener('input',()=>{stop();update();});
play.addEventListener('click',()=>{
  if(reduced.matches)return;
  if(frame!==null){stop();return;}
  if(Number(slider.value)>=T_MAX)slider.value='0';
  play.textContent='Pause';last=null;frame=requestAnimationFrame(tick);
});
reset.addEventListener('click',()=>{stop();slider.value='0';update();});
reduced.addEventListener('change',refreshMotion);
document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});
refreshMotion();update();
