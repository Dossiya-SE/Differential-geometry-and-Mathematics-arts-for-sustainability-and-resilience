#!/usr/bin/env python3
"""Governed MVS Scientific Core Engine.

JSON-in/JSON-out only. The worker exposes a bounded whitelist of mathematical
operations and intentionally exposes no shell, filesystem, network, eval, or
arbitrary Python execution.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.metadata
import json
import math
import sys
from typing import Any, Callable

PROTOCOL = "mvs.engine/1.0"
ENGINE_ID = "org.mvs.python.scientific-core"
ENGINE_VERSION = "0.1.0"
DEPENDENCIES = ("numpy", "scipy", "sympy", "geomstats", "networkx", "ortools")


class WorkerError(Exception):
    pass


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def hash_json(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode()).hexdigest()


def versions() -> dict[str, str | None]:
    result: dict[str, str | None] = {}
    for package in DEPENDENCIES:
        try:
            result[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            result[package] = None
    return result


def obj(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise WorkerError(f"{label} must be an object.")
    return value


def strict(value: dict[str, Any], allowed: set[str], required: set[str], label: str) -> None:
    extra = sorted(set(value) - allowed)
    missing = sorted(required - set(value))
    if extra:
        raise WorkerError(f"{label} contains unsupported fields: {', '.join(extra)}")
    if missing:
        raise WorkerError(f"{label} is missing required fields: {', '.join(missing)}")


def text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise WorkerError(f"{label} must be a non-empty string.")
    return value


def number(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise WorkerError(f"{label} must be numeric.")
    out = float(value)
    if not math.isfinite(out):
        raise WorkerError(f"{label} must be finite.")
    return out


def integer(value: Any, label: str, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise WorkerError(f"{label} must be an integer.")
    if minimum is not None and value < minimum:
        raise WorkerError(f"{label} must be >= {minimum}.")
    return value


def vector3(value: Any, label: str) -> list[float]:
    if not isinstance(value, list) or len(value) != 3:
        raise WorkerError(f"{label} must have exactly three coordinates.")
    return [number(x, f"{label}[{i}]") for i, x in enumerate(value)]


def safe_sympy(expression: str, names: list[str]):
    import sympy as sp

    symbols = {name: sp.Symbol(name) for name in names}
    functions = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt}
    tree = ast.parse(expression, mode="eval")

    def convert(node: ast.AST):
        if isinstance(node, ast.Expression):
            return convert(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
                raise WorkerError("Only numeric constants are allowed.")
            return sp.Integer(node.value) if isinstance(node.value, int) else sp.Float(node.value)
        if isinstance(node, ast.Name):
            if node.id not in symbols:
                raise WorkerError(f"Unknown symbol: {node.id}")
            return symbols[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            x = convert(node.operand)
            return x if isinstance(node.op, ast.UAdd) else -x
        if isinstance(node, ast.BinOp):
            a, b = convert(node.left), convert(node.right)
            if isinstance(node.op, ast.Add): return a + b
            if isinstance(node.op, ast.Sub): return a - b
            if isinstance(node.op, ast.Mult): return a * b
            if isinstance(node.op, ast.Div): return a / b
            if isinstance(node.op, ast.Pow): return a ** b
            raise WorkerError("Unsupported binary operator.")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in functions:
                raise WorkerError("Only approved symbolic functions are allowed.")
            if len(node.args) != 1 or node.keywords:
                raise WorkerError("Approved symbolic functions accept one positional argument.")
            return functions[node.func.id](convert(node.args[0]))
        raise WorkerError(f"Unsupported symbolic syntax: {type(node).__name__}")

    return convert(tree)


def capabilities(arguments: dict[str, Any]) -> dict[str, Any]:
    strict(arguments, set(), set(), "arguments")
    return {
        "engineId": ENGINE_ID,
        "engineVersion": ENGINE_VERSION,
        "operations": sorted(OPERATIONS),
        "dependencies": versions(),
        "security": {"network": False, "filesystem": False, "shell": False, "arbitraryPython": False},
    }


def symbolic_simplify(arguments: dict[str, Any]) -> dict[str, Any]:
    strict(arguments, {"expression", "symbols"}, {"expression", "symbols"}, "arguments")
    expression = text(arguments["expression"], "expression")
    names = arguments["symbols"]
    if not isinstance(names, list) or not all(isinstance(x, str) and x.isidentifier() for x in names):
        raise WorkerError("symbols must be an array of identifiers.")
    if len(names) != len(set(names)) or len(names) > 32 or len(expression) > 4096:
        raise WorkerError("Symbolic request violates bounded-input constraints.")
    import sympy as sp
    result = sp.simplify(safe_sympy(expression, names))
    return {"expression": expression, "symbols": names, "simplified": str(result), "srepr": sp.srepr(result)}


def sphere_geodesic(arguments: dict[str, Any]) -> dict[str, Any]:
    strict(arguments, {"start", "end", "samples", "tolerance"}, {"start", "end"}, "arguments")
    start, end = vector3(arguments["start"], "start"), vector3(arguments["end"], "end")
    samples = integer(arguments.get("samples", 33), "samples", 2)
    tolerance = number(arguments.get("tolerance", 1e-8), "tolerance")
    if samples > 4097 or not (0 < tolerance <= 1e-3):
        raise WorkerError("Invalid geodesic sampling/tolerance bounds.")

    norm = lambda v: math.sqrt(sum(x * x for x in v))
    if abs(norm(start) - 1) > tolerance or abs(norm(end) - 1) > tolerance:
        raise WorkerError("Endpoints must lie on the unit sphere; implicit normalization is forbidden.")
    if sum(a * b for a, b in zip(start, end)) < -1 + 100 * tolerance:
        raise WorkerError("Antipodal endpoints do not define a unique shortest geodesic.")

    import geomstats.backend as gs
    from geomstats.geometry.hypersphere import Hypersphere
    sphere = Hypersphere(dim=2)
    a, b = gs.array(start), gs.array(end)
    curve = sphere.metric.geodesic(initial_point=a, end_point=b)
    raw = curve(gs.linspace(0.0, 1.0, samples))
    points = [[float(x) for x in row] for row in raw]
    residual = max(abs(norm(p) - 1) for p in points)
    if residual > max(1e-7, 10 * tolerance):
        raise WorkerError(f"Unit-sphere invariant failed with residual {residual:.3e}.")
    return {
        "manifold": "S2",
        "start": start,
        "end": end,
        "samples": points,
        "sampleCount": samples,
        "geodesicDistance": float(sphere.metric.dist(a, b)),
        "maxUnitSphereResidual": residual,
    }


def shortest_path(arguments: dict[str, Any]) -> dict[str, Any]:
    strict(arguments, {"nodes", "edges", "source", "target", "directed"}, {"nodes", "edges", "source", "target"}, "arguments")
    nodes, edges = arguments["nodes"], arguments["edges"]
    if not isinstance(nodes, list) or not nodes or not all(isinstance(x, str) and x for x in nodes):
        raise WorkerError("nodes must be a non-empty array of node IDs.")
    if len(nodes) != len(set(nodes)) or not isinstance(edges, list):
        raise WorkerError("nodes must be unique and edges must be an array.")
    source, target = text(arguments["source"], "source"), text(arguments["target"], "target")
    if source not in nodes or target not in nodes:
        raise WorkerError("source and target must be registered nodes.")
    directed = arguments.get("directed", False)
    if not isinstance(directed, bool):
        raise WorkerError("directed must be boolean.")

    import networkx as nx
    graph = nx.DiGraph() if directed else nx.Graph()
    graph.add_nodes_from(nodes)
    for i, item in enumerate(edges):
        edge = obj(item, f"edges[{i}]")
        strict(edge, {"source", "target", "weight"}, {"source", "target", "weight"}, f"edges[{i}]")
        u, v = text(edge["source"], "edge source"), text(edge["target"], "edge target")
        if u not in graph or v not in graph:
            raise WorkerError(f"edges[{i}] references an unknown node.")
        weight = number(edge["weight"], "edge weight")
        if weight < 0:
            raise WorkerError("Dijkstra weights must be non-negative.")
        graph.add_edge(u, v, weight=weight)
    try:
        path = nx.shortest_path(graph, source, target, weight="weight", method="dijkstra")
        distance = float(nx.shortest_path_length(graph, source, target, weight="weight", method="dijkstra"))
    except nx.NetworkXNoPath as exc:
        raise WorkerError("No path exists between source and target.") from exc
    return {"directed": directed, "source": source, "target": target, "path": path, "distance": distance}


def min_cost_flow(arguments: dict[str, Any]) -> dict[str, Any]:
    strict(arguments, {"nodes", "edges"}, {"nodes", "edges"}, "arguments")
    nodes, edges = arguments["nodes"], arguments["edges"]
    if not isinstance(nodes, list) or not nodes or not isinstance(edges, list):
        raise WorkerError("nodes must be non-empty and edges must be an array.")

    ids, supplies = [], []
    for i, item in enumerate(nodes):
        node = obj(item, f"nodes[{i}]")
        strict(node, {"id", "supply"}, {"id", "supply"}, f"nodes[{i}]")
        node_id = text(node["id"], "node id")
        if node_id in ids:
            raise WorkerError(f"Duplicate node ID: {node_id}")
        ids.append(node_id)
        supplies.append(integer(node["supply"], "node supply"))
    if sum(supplies) != 0:
        raise WorkerError("Node supplies must sum to zero.")

    from ortools.graph.python import min_cost_flow as mcf
    solver = mcf.SimpleMinCostFlow()
    position = {node_id: i for i, node_id in enumerate(ids)}
    specs: list[dict[str, Any]] = []
    for i, item in enumerate(edges):
        edge = obj(item, f"edges[{i}]")
        strict(edge, {"id", "source", "target", "capacity", "unitCost"},
               {"id", "source", "target", "capacity", "unitCost"}, f"edges[{i}]")
        edge_id = text(edge["id"], "edge id")
        if any(x["id"] == edge_id for x in specs):
            raise WorkerError(f"Duplicate edge ID: {edge_id}")
        source, target = text(edge["source"], "edge source"), text(edge["target"], "edge target")
        if source not in position or target not in position:
            raise WorkerError(f"edges[{i}] references an unknown node.")
        capacity = integer(edge["capacity"], "capacity", 0)
        cost = integer(edge["unitCost"], "unitCost")
        solver.add_arc_with_capacity_and_unit_cost(position[source], position[target], capacity, cost)
        specs.append({"id": edge_id, "source": source, "target": target, "capacity": capacity, "unitCost": cost})
    for i, supply in enumerate(supplies):
        solver.set_node_supply(i, supply)

    status = solver.solve()
    status_name = {
        solver.OPTIMAL: "OPTIMAL", solver.FEASIBLE: "FEASIBLE", solver.INFEASIBLE: "INFEASIBLE",
        solver.UNBALANCED: "UNBALANCED", solver.BAD_RESULT: "BAD_RESULT", solver.BAD_COST_RANGE: "BAD_COST_RANGE",
    }.get(status, f"STATUS_{int(status)}")
    flows = []
    if status == solver.OPTIMAL:
        for arc, edge in enumerate(specs):
            flow = int(solver.flow(arc))
            flows.append({**edge, "flow": flow, "arcCost": flow * edge["unitCost"]})
    return {
        "solver": "OR-Tools SimpleMinCostFlow",
        "solverStatus": status_name,
        "verifiedOptimal": status == solver.OPTIMAL,
        "optimalCost": int(solver.optimal_cost()) if status == solver.OPTIMAL else None,
        "flows": flows,
    }


OPERATIONS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "system.capabilities": capabilities,
    "symbolic.simplify": symbolic_simplify,
    "geometry.sphere_geodesic": sphere_geodesic,
    "graph.shortest_path": shortest_path,
    "optimization.min_cost_flow": min_cost_flow,
}


def handle(value: Any) -> dict[str, Any]:
    request = obj(value, "request")
    strict(request, {"protocol", "requestId", "operation", "arguments"},
           {"protocol", "requestId", "operation", "arguments"}, "request")
    if request["protocol"] != PROTOCOL:
        raise WorkerError(f"Unsupported protocol: {request['protocol']!r}")
    request_id, operation = text(request["requestId"], "requestId"), text(request["operation"], "operation")
    arguments = obj(request["arguments"], "arguments")
    handler = OPERATIONS.get(operation)
    if handler is None:
        raise WorkerError(f"Unsupported operation: {operation}")
    result = handler(arguments)
    return {
        "protocol": PROTOCOL,
        "requestId": request_id,
        "operation": operation,
        "ok": True,
        "result": result,
        "provenance": {
            "engineId": ENGINE_ID,
            "engineVersion": ENGINE_VERSION,
            "protocol": PROTOCOL,
            "dependencies": versions(),
            "requestHash": hash_json(request),
            "resultHash": hash_json(result),
            "networkUsed": False,
        },
    }


def main() -> int:
    value: Any = None
    try:
        raw = sys.stdin.read()
        if len(raw.encode()) > 1_000_000:
            raise WorkerError("Request exceeds the 1 MB limit.")
        value = json.loads(raw)
        response, code = handle(value), 0
    except (WorkerError, json.JSONDecodeError, SyntaxError, ValueError) as exc:
        response, code = {
            "protocol": PROTOCOL,
            "requestId": value.get("requestId") if isinstance(value, dict) else None,
            "operation": value.get("operation") if isinstance(value, dict) else None,
            "ok": False,
            "error": {"type": type(exc).__name__, "message": str(exc)},
        }, 2
    except Exception as exc:
        response, code = {
            "protocol": PROTOCOL,
            "requestId": value.get("requestId") if isinstance(value, dict) else None,
            "operation": value.get("operation") if isinstance(value, dict) else None,
            "ok": False,
            "error": {"type": "WorkerError", "message": f"Engine execution failed: {type(exc).__name__}: {exc}"},
        }, 3
    sys.stdout.write(canonical_json(response) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
