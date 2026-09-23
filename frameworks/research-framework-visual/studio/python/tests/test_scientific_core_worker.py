import hashlib
import json
import math
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKER = ROOT / "scientific_core_worker.py"
REQUIREMENTS = ROOT / "scientific-core-requirements.txt"
MANIFEST = ROOT.parent / "engine-packs" / "scientific-core" / "manifest.json"


def call(operation, arguments, request_id="test"):
    request = {
        "protocol": "mvs.engine/1.0",
        "requestId": request_id,
        "operation": operation,
        "arguments": arguments,
    }
    completed = subprocess.run(
        [sys.executable, str(WORKER)],
        input=json.dumps(request),
        text=True,
        capture_output=True,
        check=False,
        timeout=30,
    )
    if not completed.stdout:
        raise AssertionError(f"worker emitted no protocol output; stderr={completed.stderr}")
    return completed.returncode, json.loads(completed.stdout)


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


class ScientificCoreWorkerTests(unittest.TestCase):
    def test_manifest_content_hashes(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["payloadSha256"], sha256(WORKER))
        self.assertEqual(manifest["lockSha256"], sha256(REQUIREMENTS))

    def test_capabilities_and_dependency_identity(self):
        code, response = call("system.capabilities", {})
        self.assertEqual(code, 0)
        self.assertTrue(response["ok"])
        dependencies = response["result"]["dependencies"]
        expected = {
            "numpy": "2.3.5",
            "scipy": "1.18.0",
            "sympy": "1.14.0",
            "geomstats": "2.8.0",
            "networkx": "3.6.1",
            "ortools": "9.15.6755",
        }
        self.assertEqual(dependencies, expected)
        self.assertEqual(
            response["result"]["security"],
            {"network": False, "filesystem": False, "shell": False, "arbitraryPython": False},
        )

    def test_symbolic_simplification_is_bounded_and_correct(self):
        code, response = call("symbolic.simplify", {"expression": "(x + x) / 2", "symbols": ["x"]})
        self.assertEqual(code, 0)
        self.assertEqual(response["result"]["simplified"], "x")

        bad_code, bad = call(
            "symbolic.simplify",
            {"expression": "__import__('os').system('echo unsafe')", "symbols": []},
            request_id="reject-unsafe",
        )
        self.assertNotEqual(bad_code, 0)
        self.assertFalse(bad["ok"])

    def test_geomstats_sphere_geodesic_preserves_manifold(self):
        code, response = call(
            "geometry.sphere_geodesic",
            {"start": [1.0, 0.0, 0.0], "end": [0.0, 1.0, 0.0], "samples": 17},
        )
        self.assertEqual(code, 0, response)
        result = response["result"]
        self.assertAlmostEqual(result["geodesicDistance"], math.pi / 2, places=7)
        self.assertLess(result["maxUnitSphereResidual"], 1e-7)
        self.assertEqual(result["sampleCount"], 17)
        self.assertEqual(len(result["samples"]), 17)
        for point in result["samples"]:
            self.assertAlmostEqual(sum(x * x for x in point), 1.0, places=7)

    def test_networkx_shortest_path(self):
        code, response = call(
            "graph.shortest_path",
            {
                "nodes": ["A", "B", "C", "D"],
                "edges": [
                    {"source": "A", "target": "B", "weight": 1},
                    {"source": "B", "target": "D", "weight": 2},
                    {"source": "A", "target": "C", "weight": 4},
                    {"source": "C", "target": "D", "weight": 1},
                ],
                "source": "A",
                "target": "D",
                "directed": False,
            },
        )
        self.assertEqual(code, 0)
        self.assertEqual(response["result"]["path"], ["A", "B", "D"])
        self.assertEqual(response["result"]["distance"], 3.0)

    def test_ortools_min_cost_flow_proves_optimum(self):
        code, response = call(
            "optimization.min_cost_flow",
            {
                "nodes": [
                    {"id": "source", "supply": 5},
                    {"id": "middle", "supply": 0},
                    {"id": "sink", "supply": -5},
                ],
                "edges": [
                    {"id": "e1", "source": "source", "target": "middle", "capacity": 5, "unitCost": 2},
                    {"id": "e2", "source": "middle", "target": "sink", "capacity": 5, "unitCost": 3},
                    {"id": "e3", "source": "source", "target": "sink", "capacity": 5, "unitCost": 10},
                ],
            },
        )
        self.assertEqual(code, 0, response)
        result = response["result"]
        self.assertTrue(result["verifiedOptimal"])
        self.assertEqual(result["solverStatus"], "OPTIMAL")
        self.assertEqual(result["optimalCost"], 25)
        flows = {edge["id"]: edge["flow"] for edge in result["flows"]}
        self.assertEqual(flows, {"e1": 5, "e2": 5, "e3": 0})

    def test_protocol_output_is_deterministic(self):
        arguments = {
            "nodes": ["A", "B", "C"],
            "edges": [
                {"source": "A", "target": "B", "weight": 1},
                {"source": "B", "target": "C", "weight": 2},
            ],
            "source": "A",
            "target": "C",
        }
        code_a, a = call("graph.shortest_path", arguments, "determinism")
        code_b, b = call("graph.shortest_path", arguments, "determinism")
        self.assertEqual(code_a, 0)
        self.assertEqual(code_b, 0)
        self.assertEqual(a, b)

    def test_fail_closed_on_unknown_fields_and_operations(self):
        code, response = call("system.capabilities", {"unexpected": True})
        self.assertNotEqual(code, 0)
        self.assertFalse(response["ok"])

        code, response = call("unsafe.shell", {})
        self.assertNotEqual(code, 0)
        self.assertFalse(response["ok"])


if __name__ == "__main__":
    unittest.main()
