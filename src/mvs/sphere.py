from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from .model import SceneObject, VisualIR

FloatArray = NDArray[np.float64]


def fibonacci_sphere(count: int) -> FloatArray:
    if count < 2:
        raise ValueError("count must be >= 2")

    indices = np.arange(count, dtype=np.float64)
    golden_angle = np.pi * (3.0 - np.sqrt(5.0))
    y = 1.0 - 2.0 * indices / (count - 1)
    radius = np.sqrt(np.maximum(0.0, 1.0 - y * y))
    theta = golden_angle * indices
    points = np.column_stack((np.cos(theta) * radius, y, np.sin(theta) * radius))
    return np.asarray(points, dtype=np.float64)


def tangent_vectors(points: FloatArray) -> FloatArray:
    if points.ndim != 2 or points.shape[1] != 3:
        raise ValueError("points must have shape (n, 3)")

    reference = np.array([0.0, 0.0, 1.0], dtype=np.float64)
    alternate = np.array([1.0, 0.0, 0.0], dtype=np.float64)
    vectors: list[FloatArray] = []

    for point in points:
        ref = alternate if abs(float(np.dot(point, reference))) > 0.95 else reference
        tangent = np.cross(point, ref)
        norm = float(np.linalg.norm(tangent))
        if norm <= np.finfo(np.float64).eps:
            raise ValueError("cannot construct a stable tangent vector")
        vectors.append(np.asarray(tangent / norm, dtype=np.float64))

    return np.asarray(vectors, dtype=np.float64)


def geodesic_distance(a: FloatArray, b: FloatArray) -> float:
    return float(np.arccos(np.clip(np.dot(a, b), -1.0, 1.0)))


def validate_scene(
    points: FloatArray,
    vectors: FloatArray,
    delta: float,
    tol: float = 1e-10,
) -> dict[str, bool]:
    if delta < 0.0 or delta > np.pi:
        raise ValueError("delta must satisfy 0 <= delta <= pi")
    if tol <= 0.0:
        raise ValueError("tol must be positive")
    if points.shape != vectors.shape or points.ndim != 2 or points.shape[1] != 3:
        raise ValueError("points and vectors must both have shape (n, 3)")

    unit_points = bool(np.allclose(np.linalg.norm(points, axis=1), 1.0, atol=tol))
    tangent = bool(np.all(np.abs(np.sum(points * vectors, axis=1)) <= tol))
    separation = all(
        geodesic_distance(points[i], points[j]) >= delta
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    return {"unit_sphere": unit_points, "tangent": tangent, "separation": separation}


def build_sphere_visual_ir(count: int = 12, delta: float = 0.3) -> VisualIR:
    points = fibonacci_sphere(count)
    vectors = tangent_vectors(points)
    validation = validate_scene(points, vectors, delta)
    if not all(validation.values()):
        raise ValueError(f"mathematical validation failed: {validation}")

    objects: list[SceneObject] = [
        SceneObject(
            visual_id="sphere:surface",
            semantic_id="S2",
            kind="sphere",
            geometry={"center": [0.0, 0.0, 0.0], "radius": 1.0},
            constraint_refs=("constraint:S2",),
        )
    ]
    for index, (point, vector) in enumerate(zip(points, vectors, strict=True)):
        objects.append(
            SceneObject(
                visual_id=f"point:{index}",
                semantic_id=f"S2.point.{index}",
                kind="point",
                geometry={"position": point.tolist()},
                constraint_refs=("constraint:S2", "constraint:separation"),
            )
        )
        objects.append(
            SceneObject(
                visual_id=f"tangent:{index}",
                semantic_id=f"TS2.vector.{index}",
                kind="tangent_vector",
                geometry={"origin": point.tolist(), "vector": vector.tolist()},
                constraint_refs=("constraint:tangent",),
            )
        )

    return VisualIR(
        version="0.1.1",
        scene_id="benchmark:S2-tangent-field",
        objects=tuple(objects),
        provenance={"generator": "mvs.sphere", "mathematical_authority": "VisualIR"},
    )
