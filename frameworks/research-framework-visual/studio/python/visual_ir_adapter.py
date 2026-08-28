"""Python adapter for the shared Visual IR torus object."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class TorusParameters:
    R: float = 2.0
    r: float = 0.72
    def validate(self) -> None:
        if not (self.R > self.r > 0):
            raise ValueError("Regular torus requires R > r > 0")

def surface(u: np.ndarray, v: np.ndarray, p: TorusParameters) -> np.ndarray:
    p.validate()
    x = (p.R + p.r * np.cos(v)) * np.cos(u)
    y = (p.R + p.r * np.cos(v)) * np.sin(u)
    z = p.r * np.sin(v)
    return np.stack([x, y, z], axis=-1)

def gaussian_curvature(v: np.ndarray, p: TorusParameters) -> np.ndarray:
    p.validate()
    return np.cos(v) / (p.r * (p.R + p.r * np.cos(v)))
