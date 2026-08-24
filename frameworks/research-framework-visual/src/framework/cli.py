from __future__ import annotations

import argparse
import json
from .render import build


def main():
    parser = argparse.ArgumentParser(description="Research framework renderer")
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build", help="Build framework exports")
    build_parser.add_argument("--spec", default="spec/framework.yaml")
    build_parser.add_argument("--outdir", default="exports")
    args = parser.parse_args()
    if args.command == "build":
        print(json.dumps(build(spec_path=args.spec, outdir=args.outdir), indent=2))


if __name__ == "__main__":
    main()
