/** Dimensionless autonomous teaching flow: x'(τ)=-x; x(0)=x0. */
export const INSIDE_START=Object.freeze([0.8,0.45]);
export const OUTSIDE_START=Object.freeze([1.4,0.35]);
export const T_MAX=3;
function vector(x){
  if(!Array.isArray(x)||x.length!==2||!x.every(v=>typeof v==='number'&&Number.isFinite(v)))throw new RangeError('expected finite 2D state');
}
function time(τ){if(typeof τ!=='number'||!Number.isFinite(τ)||τ<0)throw new RangeError('dimensionless time must be finite and nonnegative');}
export function trajectory(x0,τ){vector(x0);time(τ);const factor=Math.exp(-τ);return [x0[0]*factor,x0[1]*factor];}
export function norm(x){vector(x);return Math.hypot(...x);}
export function isViableAtStart(x0){return norm(x0)<=1;}
export function boundaryCrossingTime(x0){const r=norm(x0);return r>1?Math.log(r):null;}
export function squaredNormDerivative(x){return -2*norm(x)**2;}
