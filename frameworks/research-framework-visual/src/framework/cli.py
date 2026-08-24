from __future__ import annotations
import argparse, json
from .controller import render_release, reproduce_bundle, audit_release


def main():
    p=argparse.ArgumentParser(description='Governed research framework renderer')
    sub=p.add_subparsers(dest='command',required=True)
    r=sub.add_parser('render'); r.add_argument('--request',default='render_requests/Research_Framework_V4.yaml'); r.add_argument('--outdir',default='exports')
    b=sub.add_parser('build'); b.add_argument('--outdir',default='exports')
    rp=sub.add_parser('reproduce'); rp.add_argument('--bundle',default='exports/SOURCE_BUNDLE.zip')
    a=sub.add_parser('audit'); a.add_argument('--outdir',default='exports')
    args=p.parse_args()
    if args.command=='render': result=render_release(args.request,args.outdir)
    elif args.command=='build': result=render_release('render_requests/Research_Framework_V4.yaml',args.outdir)
    elif args.command=='reproduce': result=reproduce_bundle(args.bundle)
    else: result=audit_release(args.outdir)
    print(json.dumps(result,indent=2,sort_keys=True))
    if isinstance(result,dict) and result.get('final_status')=='RENDER_FAIL': raise SystemExit(2)
    if args.command=='reproduce' and not result.get('pass'): raise SystemExit(3)

if __name__=='__main__': main()
