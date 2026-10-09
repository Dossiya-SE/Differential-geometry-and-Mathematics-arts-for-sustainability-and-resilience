/** MSR-VIS-002: deterministic, dependency-free scientific vector source. */
import {readFileSync,writeFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
function f(n){return Number(n.toFixed(3)).toString()}

function esc(t){return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}

function svg(id,title,desc,w,h,body){return `<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-labelledby="title description" data-figure-id="${id}">\n  <title id="title">${esc(title)}</title>\n  <desc id="description">${esc(desc)}</desc>\n  <rect x="0" y="0" width="${w}" height="${h}" fill="#FFFFFF"/>\n${body}\n</svg>\n`}

function renderViability(){
 const cx=420,cy=377,k=190,a=[.8,.45],b=[1.4,.35];
 const mark=(pos,name,color,dy)=>`  <circle data-point="${name}" cx="${f(cx+pos[0]*k)}" cy="${f(cy-pos[1]*k)}" r="11" fill="#FFFFFF" stroke="${color}" stroke-width="4"/>\n  <text x="${f(cx+pos[0]*k+17)}" y="${f(cy-pos[1]*k+dy)}" font-size="20" font-weight="700" fill="#17202A">${name}</text>`;
 const body=`  <text x="55" y="57" font-family="system-ui" font-size="30" font-weight="700" fill="#17202A">Invariance is a mathematical property</text>
  <text x="55" y="91" font-family="system-ui" font-size="19" fill="#5D6D7E">Autonomous, dimensionless example · initial state at τ = 0</text>
  <line x1="${cx-265}" y1="${cy}" x2="${cx+315}" y2="${cy}" stroke="#899BA9" stroke-width="2"/>
  <line x1="${cx}" y1="${cy+250}" x2="${cx}" y2="${cy-240}" stroke="#899BA9" stroke-width="2"/>
  <text x="${cx+323}" y="${cy+7}" font-family="system-ui" font-size="18" fill="#17202A">x₁</text>
  <text x="${cx+10}" y="${cy-244}" font-family="system-ui" font-size="18" fill="#17202A">x₂</text>
  <circle data-boundary="unit-disk" cx="${cx}" cy="${cy}" r="${k}" fill="none" stroke="#00BFFF" stroke-width="5"/>
  <text x="215" y="589" font-family="system-ui" font-size="19" fill="#0072B2">∂K: ‖x‖ = 1</text>
${mark(a,"A","#00BFFF",-16)}
${mark(b,"B","#17202A",-17)}
  <line x1="798" y1="133" x2="798" y2="631" stroke="#C5D2DC" stroke-width="2"/>
  <text x="823" y="167" font-family="system-ui" font-size="24" font-weight="650" fill="#17202A">Exact mathematical fixture</text>
  <text x="823" y="212" font-family="system-ui" font-size="20" fill="#17202A">dx/dτ = −x</text>
  <text x="823" y="250" font-family="system-ui" font-size="20" fill="#17202A">x(τ) = exp(−τ)x₀</text>
  <text x="823" y="300" font-family="system-ui" font-size="20" fill="#17202A">K = {x : ‖x‖ ≤ 1}</text>
  <text x="823" y="350" font-family="system-ui" font-size="18" fill="#17202A">A(0) = (0.80, 0.45)</text>
  <text x="823" y="379" font-family="system-ui" font-size="18" fill="#17202A">Starts in K: stays in K</text>
  <text x="823" y="435" font-family="system-ui" font-size="18" fill="#17202A">B(0) = (1.40, 0.35)</text>
  <text x="823" y="464" font-family="system-ui" font-size="18" fill="#17202A">Starts outside K: not viable at τ = 0</text>
  <text x="823" y="529" font-family="system-ui" font-size="17" fill="#5D6D7E">Proposed explanatory mathematics</text>
  <text x="823" y="562" font-family="system-ui" font-size="17" fill="#5D6D7E">No measured system or physical recovery</text>
  <text x="55" y="690" font-family="system-ui" font-size="17" fill="#5D6D7E">MSR-FIG-0004 · The disk is invariant for x′ = −x; the initial boundary is not a physical service threshold.</text>`;
 return svg("MSR-FIG-0004","Invariant unit disk and two initial states","A white coordinate plane with a blue unit circle, a labeled point A inside it and a point B outside it, alongside equations for the dimensionless flow x prime equals minus x. B is outside at time zero and therefore not viable at that initial instant.",1220,720,body)
}

function renderDiagram(){
 const names=["Theory","Model","Computation","Visualization","Interpretation"];
 const subs=["Definitions","Assumptions","Algorithms","Encodings","Conclusions"];
 const xs=[38,300,562,824,1086];
 const blocks=names.map((n,i)=>`  <rect data-node="${esc(n)}" x="${xs[i]}" y="207" width="210" height="126" rx="5" fill="#FFFFFF" stroke="${i===3?"#00BFFF":"#87CEFA"}" stroke-width="4"/>\n  <text x="${xs[i]+105}" y="263" text-anchor="middle" font-family="system-ui" font-size="${n==="Interpretation"?21:24}" font-weight="650" fill="#17202A">${n}</text>\n  <text x="${xs[i]+105}" y="300" text-anchor="middle" font-family="system-ui" font-size="18" fill="#5D6D7E">${subs[i]}</text>`).join("\n");
 const arr=xs.slice(0,4).map((x,i)=>`  <line data-edge="${names[i]}-to-${names[i+1]}" x1="${x+211}" y1="270" x2="${xs[i+1]-7}" y2="270" stroke="#0072B2" stroke-width="4" marker-end="url(#direction)"/>`).join("\n");
 const body=`  <defs><marker id="direction" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M 0 1 L 11 6 L 0 11" fill="none" stroke="#0072B2" stroke-width="2.7"/></marker></defs>
  <text x="45" y="72" font-family="system-ui" font-size="31" font-weight="700" fill="#17202A">From mathematical theory to justified interpretation</text>
  <text x="45" y="113" font-family="system-ui" font-size="19" fill="#5D6D7E">Five distinct stages · arrows mean methodological transfer, not validation</text>
${blocks}
${arr}
  <text x="45" y="401" font-family="system-ui" font-size="19" fill="#17202A">Gate: mathematical correctness, implementation verification and empirical validity are separate.</text>
  <text x="45" y="448" font-family="system-ui" font-size="17" fill="#5D6D7E">MSR-FIG-0005 · Proposed explanatory process diagram · no domain or causal effect selected.</text>`;
 return svg("MSR-FIG-0005","Five-stage mathematical visualization pipeline","Five labeled white rectangular stages in a row: Theory, Model, Computation, Visualization and Interpretation. Four large blue arrows indicate methodological transitions only, not inherited validity.",1336,480,body)
}

function renderMindmap(){
 const rootX=650,rootY=135,rootW=390;
 const cols=[215,680,1145], branches=["Foundations","Methods","Research interfaces"];
 const leaves=[["Geometry","Partial differential equations","Dynamical systems"],["Optimization","Uncertainty","Scientific computation"],["Viability","Networks","Visualization"]];
 const body=[];
 body.push(`  <text x="70" y="62" font-family="system-ui" font-size="31" font-weight="700" fill="#17202A">A nonexhaustive mathematics study taxonomy</text>`);
 body.push(`  <text x="70" y="99" font-family="system-ui" font-size="19" fill="#5D6D7E">Lines encode parent–child grouping, never causal or operational dependencies</text>`);
 body.push(`  <rect data-node="root" x="${rootX}" y="${rootY}" width="${rootW}" height="88" rx="5" fill="#FFFFFF" stroke="#00BFFF" stroke-width="4"/>`);
 body.push(`  <text x="${rootX+rootW/2}" y="168" text-anchor="middle" font-family="system-ui" font-size="22" font-weight="650" fill="#17202A">Mathematics for</text>`);
 body.push(`  <text x="${rootX+rootW/2}" y="197" text-anchor="middle" font-family="system-ui" font-size="22" font-weight="650" fill="#17202A">Sustainability and Resilience</text>`);
 for(let k=0;k<3;k++){
  const x=cols[k],w=328;
  body.push(`  <path data-relation="root-to-${k}" d="M 845 223 V 265 H ${x+164} V 289" fill="none" stroke="#87CEFA" stroke-width="3"/>`);
  body.push(`  <rect data-node="branch-${k}" x="${x}" y="289" width="${w}" height="67" rx="4" fill="#FFFFFF" stroke="#00BFFF" stroke-width="3"/>`);
  body.push(`  <text x="${x+w/2}" y="331" text-anchor="middle" font-family="system-ui" font-size="23" font-weight="650" fill="#17202A">${branches[k]}</text>`);
  for(let j=0;j<3;j++){
    const y=420+j*96;
    body.push(`  <path data-relation="branch-${k}-to-${j}" d="M ${x+164} 356 V 387 H ${x-18} V ${y+34} H ${x}" fill="none" stroke="#87CEFA" stroke-width="2.5"/>`);
    body.push(`  <rect data-node="leaf-${k}-${j}" x="${x}" y="${y}" width="${w}" height="68" rx="4" fill="#FFFFFF" stroke="#C5D2DC" stroke-width="2"/>`);
    body.push(`  <text x="${x+w/2}" y="${y+41}" text-anchor="middle" font-family="system-ui" font-size="${leaves[k][j].length>23?18:21}" font-weight="550" fill="#17202A">${leaves[k][j]}</text>`);
  }
 }
 body.push(`  <text x="70" y="780" font-family="system-ui" font-size="18" fill="#5D6D7E">MSR-FIG-0006 · Concept hierarchy only · 1 root / 3 branches / 9 leaves · proposed taxonomy.</text>`);
 return svg("MSR-FIG-0006","Mathematics taxonomy for sustainability and resilience","One central root concept connects without arrows to three groups Foundations, Methods and Research interfaces. Each group has three named child concepts, nine leaves total. Connecting lines encode membership and are not causal arrows.",1688,815,body.join("\n"))
}

function renderChart(){
 const x0=145,y0=603,dx=812,dy=446,ra=Math.hypot(.8,.45),rb=Math.hypot(1.4,.35);
 const X=t=>x0+dx*t/3,Y=r=>y0-dy*r/1.6;
 const path=r=>Array.from({length:181},(_,i)=>{let t=3*i/180;return(i?"L ":"M ")+f(X(t))+" "+f(Y(r*Math.exp(-t)))}).join(" ");
 const xticks=Array.from({length:7},(_,i)=>{let t=i*.5;return `  <line x1="${f(X(t))}" y1="${y0}" x2="${f(X(t))}" y2="${y0+8}" stroke="#17202A" stroke-width="2"/>\n  <text x="${f(X(t))}" y="${y0+32}" text-anchor="middle" font-family="system-ui" font-size="18" fill="#17202A">${f(t)}</text>`}).join("\n");
 const yticks=Array.from({length:5},(_,i)=>{let r=i*.4;return `  <line x1="${x0-8}" y1="${f(Y(r))}" x2="${x0}" y2="${f(Y(r))}" stroke="#17202A" stroke-width="2"/>\n  <text x="${x0-17}" y="${f(Y(r)+7)}" text-anchor="end" font-family="system-ui" font-size="18" fill="#17202A">${r.toFixed(1)}</text>`}).join("\n");
 const cross=Math.log(rb),xc=X(cross);
 const body=`  <text x="60" y="62" font-family="system-ui" font-size="30" font-weight="700" fill="#17202A">Exact radial trajectories for x′ = −x</text>
  <text x="60" y="100" font-family="system-ui" font-size="19" fill="#5D6D7E">Analytical functions, not observations · same fixture as the viability animation</text>
  <line x1="${x0}" y1="${Y(1.6)}" x2="${x0}" y2="${y0}" stroke="#17202A" stroke-width="3"/>
  <line x1="${x0}" y1="${y0}" x2="${x0+dx}" y2="${y0}" stroke="#17202A" stroke-width="3"/>
${xticks}
${yticks}
  <text x="${f(x0+dx/2)}" y="689" text-anchor="middle" font-family="system-ui" font-size="21" fill="#17202A">Dimensionless time τ</text>
  <text x="47" y="372" transform="rotate(-90 47 372)" text-anchor="middle" font-family="system-ui" font-size="21" fill="#17202A">Radial norm ‖x(τ)‖ (dimensionless)</text>
  <line data-curve="threshold" x1="${x0}" y1="${f(Y(1))}" x2="${x0+dx}" y2="${f(Y(1))}" stroke="#697785" stroke-width="2.5" stroke-dasharray="12 7"/>
  <path data-curve="A" d="${path(ra)}" fill="none" stroke="#00BFFF" stroke-width="4"/>
  <path data-curve="B" d="${path(rb)}" fill="none" stroke="#0072B2" stroke-width="4" stroke-dasharray="14 6"/>
  <circle data-event="B-crosses-threshold" cx="${f(xc)}" cy="${f(Y(1))}" r="7" fill="#FFFFFF" stroke="#0072B2" stroke-width="3"/>
  <text x="${f(xc+15)}" y="${f(Y(1)-15)}" font-family="system-ui" font-size="17" fill="#17202A">B enters K</text>
  <line x1="1014" y1="229" x2="1090" y2="229" stroke="#00BFFF" stroke-width="4"/>
  <text x="1104" y="237" font-family="system-ui" font-size="19" fill="#17202A">A: starts inside</text>
  <line x1="1014" y1="278" x2="1090" y2="278" stroke="#0072B2" stroke-width="4" stroke-dasharray="14 6"/>
  <text x="1104" y="286" font-family="system-ui" font-size="19" fill="#17202A">B: starts outside</text>
  <line x1="1014" y1="327" x2="1090" y2="327" stroke="#697785" stroke-width="3" stroke-dasharray="12 7"/>
  <text x="1104" y="335" font-family="system-ui" font-size="19" fill="#17202A">r = 1: boundary</text>
  <text x="1014" y="396" font-family="system-ui" font-size="18" fill="#17202A">A₀ = (0.80, 0.45)</text>
  <text x="1014" y="429" font-family="system-ui" font-size="18" fill="#17202A">B₀ = (1.40, 0.35)</text>
  <text x="1014" y="469" font-family="system-ui" font-size="18" fill="#17202A">τ enter = ln(‖B₀‖)</text>
  <text x="1014" y="503" font-family="system-ui" font-size="18" fill="#17202A">≈ ${f(cross)}</text>
  <text x="60" y="739" font-family="system-ui" font-size="18" fill="#5D6D7E">MSR-FIG-0007 · B is not viable at τ = 0 despite later entry. No physical recovery data.</text>`;
 return svg("MSR-FIG-0007","Analytic radial trajectories under x prime equals minus x","A quantitative chart with labeled dimensionless time 0 to 3 and radial norm 0 to 1.6. Two decreasing exponential trajectories start respectively inside and outside r=1. A dashed reference line marks r=1, and a marker identifies when the outside-start trajectory enters the disk; no measured data are shown.",1400,770,body)
}

function renderProjection(){
 const R=175,cx=455,cy=410,s2=Math.SQRT1_2,s6=1/Math.sqrt(6);
 const point=(p)=>[cx+R*s2*(p[0]-p[1]),cy-R*(-s6*(p[0]+p[1])+2*s6*p[2])];
 const P=[Math.sqrt(3)/2,0,-.5],N=[0,0,1],Q=[1/Math.sqrt(3),0,0]; const n=point(N),p=point(P),q=point(Q);
 const polys=[[-1.1,-1.1,0],[1.1,-1.1,0],[1.1,1.1,0],[-1.1,1.1,0]].map(point).map(v=>v.map(f).join(",")).join(" ");
 const eq=Array.from({length:181},(_,i)=>{const theta=2*Math.PI*i/180;let xy=point([Math.cos(theta),Math.sin(theta),0]);return(i?"L ":"M ")+xy.map(f).join(" ")}).join(" ");
 const body=`  <text x="58" y="65" font-family="system-ui" font-size="31" font-weight="700" fill="#17202A">Stereographic projection from S² to a plane</text>
  <text x="58" y="103" font-family="system-ui" font-size="19" fill="#5D6D7E">Orthographic drawing of a 3D construction · displayed lengths are not intrinsic distances</text>
  <polygon data-object="equatorial-plane" points="${polys}" fill="#FFFFFF" stroke="#9CAAB7" stroke-width="2.5" stroke-dasharray="11 6"/>
  <path data-object="equator" d="${eq}" fill="none" stroke="#87CEFA" stroke-width="2.5"/>
  <circle data-object="unit-sphere" cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#17202A" stroke-width="3.5"/>
  <line data-object="projection-line" x1="${f(n[0])}" y1="${f(n[1])}" x2="${f(p[0])}" y2="${f(p[1])}" stroke="#00BFFF" stroke-width="4"/>
  <circle data-point="N" cx="${f(n[0])}" cy="${f(n[1])}" r="9" fill="#FFFFFF" stroke="#17202A" stroke-width="3"/>
  <circle data-point="Q" cx="${f(q[0])}" cy="${f(q[1])}" r="10" fill="#FFFFFF" stroke="#00BFFF" stroke-width="4"/>
  <circle data-point="P" cx="${f(p[0])}" cy="${f(p[1])}" r="10" fill="#FFFFFF" stroke="#0072B2" stroke-width="4"/>
  <text x="${f(n[0]-26)}" y="${f(n[1]-15)}" font-family="system-ui" font-size="21" font-weight="650" fill="#17202A">N</text>
  <text x="${f(q[0]+15)}" y="${f(q[1]-8)}" font-family="system-ui" font-size="21" font-weight="650" fill="#17202A">Q</text>
  <text x="${f(p[0]+16)}" y="${f(p[1]+12)}" font-family="system-ui" font-size="21" font-weight="650" fill="#17202A">P</text>
  <text x="217" y="625" font-family="system-ui" font-size="19" fill="#17202A">plane z = 0 (schematic orthographic view)</text>
  <line x1="735" y1="158" x2="735" y2="633" stroke="#C5D2DC" stroke-width="2"/>
  <text x="765" y="195" font-family="system-ui" font-size="24" font-weight="650" fill="#17202A">Definition and correspondence</text>
  <text x="765" y="246" font-family="system-ui" font-size="21" fill="#17202A">S² = {p ∈ ℝ³ : ‖p‖ = 1}</text>
  <text x="765" y="293" font-family="system-ui" font-size="21" fill="#17202A">N = (0, 0, 1)</text>
  <text x="765" y="341" font-family="system-ui" font-size="20" fill="#17202A">P = (√3/2, 0, −1/2)</text>
  <text x="765" y="388" font-family="system-ui" font-size="20" fill="#17202A">Q = (1/√3, 0, 0)</text>
  <text x="765" y="452" font-family="system-ui" font-size="20" fill="#17202A">π(x, y, z) = (x/(1−z), y/(1−z))</text>
  <text x="765" y="490" font-family="system-ui" font-size="19" fill="#5D6D7E">Domain: S² without the north pole N</text>
  <text x="765" y="524" font-family="system-ui" font-size="19" fill="#5D6D7E">Codomain: ℝ² (equatorial plane)</text>
  <text x="765" y="579" font-family="system-ui" font-size="18" fill="#5D6D7E">N, Q, P lie on one Euclidean line.</text>
  <text x="58" y="696" font-family="system-ui" font-size="17" fill="#5D6D7E">MSR-FIG-0008 · Mathematically defined projection; no physical-system interpretation.</text>`;
 return svg("MSR-FIG-0008","Stereographic projection of a sphere onto an equatorial plane","An orthographic schematic of a unit sphere, equatorial plane, the north pole N, sphere point P, and its planar image Q. N, Q and P are collinear. The map is undefined at N and does not preserve intrinsic distances.",1310,720,body)
}

export const outputs = Object.freeze({
  'art/animations/viability_lab/static.svg':renderViability,
  'art/diagrams/model_to_visualization.svg':renderDiagram,
  'art/mindmaps/mathematics_taxonomy.svg':renderMindmap,
  'art/charts/analytic_radius.svg':renderChart,
  'art/mathematical_figures/stereographic_projection.svg':renderProjection,
});
export function renderAll(){return Object.fromEntries(Object.entries(outputs).map(([path,renderer])=>[path,renderer()]));}
if(process.argv[1] && fileURLToPath(import.meta.url)===process.argv[1]){
  const mode=process.argv[2];
  if(!['--check','--write'].includes(mode))throw Error('Choose --check or --write');
  const root=new URL('../../',import.meta.url);
  for(const [name,contents] of Object.entries(renderAll())){
    const target=new URL(name,root);
    if(mode==='--check'){
      if(readFileSync(target,'utf8')!==contents)throw Error('Outdated generated vector source: '+name);
      process.stdout.write('PASS '+name+'\n');
    }else writeFileSync(target,contents,'utf8');
  }
}
