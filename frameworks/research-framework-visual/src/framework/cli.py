from __future__ import annotations

import argparse
import json

from .environment import doctor


def main():
    p = argparse.ArgumentParser(description="Governed research framework renderer")
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("render")
    r.add_argument("--request", default="render_requests/Research_Framework_V4.yaml")
    r.add_argument("--outdir", default="exports")

    b = sub.add_parser("build")
    b.add_argument("--outdir", default="exports")

    rp = sub.add_parser("reproduce")
    rp.add_argument("--bundle", default="exports/SOURCE_BUNDLE.zip")

    a = sub.add_parser("audit")
    a.add_argument("--outdir", default="exports")

    d = sub.add_parser("doctor", help="Audit interpreter isolation and rendering dependencies")
    d.add_argument("--strict", action="store_true", help="Exit non-zero when a required check fails")
    d.add_argument("--notebook", action="store_true", help="Also validate Jupyter, NumPy, Matplotlib and bundled fonts")

    args = p.parse_args()

    if args.command == "doctor":
        result = doctor(require_notebook=args.notebook)
    else:
        # Import rendering dependencies lazily so `framework doctor` can
        # diagnose a missing native Cairo runtime instead of crashing while
        # importing the controller.
        from .controller import audit_release, render_release, reproduce_bundle

        if args.command == "render":
            result = render_release(args.request, args.outdir)
        elif args.command == "build":
            result = render_release("render_requests/Research_Framework_V4.yaml", args.outdir)
        elif args.command == "reproduce":
            result = reproduce_bundle(args.bundle)
        else:
            result = audit_release(args.outdir)

    print(json.dumps(result, indent=2, sort_keys=True))

    if isinstance(result, dict) and result.get("final_status") == "RENDER_FAIL":
        raise SystemExit(2)
    if args.command == "reproduce" and not result.get("pass"):
        raise SystemExit(3)
    if args.command == "doctor" and args.strict and not result.get("pass"):
        raise SystemExit(4)


if __name__ == "__main__":
    main()
