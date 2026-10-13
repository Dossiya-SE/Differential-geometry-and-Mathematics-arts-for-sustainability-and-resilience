import { useEffect, useRef } from 'react';
import * as THREE from 'three';
import type { ParametricSurfaceIR } from '../visual-ir';
import { buildSurfaceGeometry } from '../renderers/threeSurface';

export function LiveCanvas({ ir }: { ir: ParametricSurfaceIR }) {
  const host = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = host.current;
    if (!el) return;
    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#061018');
    const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
    camera.position.set(...ir.camera.position);
    camera.lookAt(0, 0, 0);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    el.appendChild(renderer.domElement);
    const geometry = buildSurfaceGeometry(ir);
    const material = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.46, metalness: 0.1, side: THREE.DoubleSide, wireframe: ir.visual.showMesh });
    const mesh = new THREE.Mesh(geometry, material);
    mesh.rotation.x = 0.55;
    mesh.rotation.z = 0.2;
    scene.add(mesh);
    scene.add(new THREE.AmbientLight(0xffffff, 1.4));
    const key = new THREE.DirectionalLight(0xffffff, 3.2); key.position.set(4, 5, 7); scene.add(key);
    const rim = new THREE.DirectionalLight(0x38bdf8, 2.0); rim.position.set(-5, -1, 3); scene.add(rim);
    let raf = 0;
    const resize = () => { const width = Math.max(320, el.clientWidth); const height = Math.max(320, el.clientHeight); renderer.setSize(width, height, false); camera.aspect = width / height; camera.updateProjectionMatrix(); };
    const frame = () => { mesh.rotation.y += 0.0025; renderer.render(scene, camera); raf = requestAnimationFrame(frame); };
    resize();
    const observer = new ResizeObserver(resize); observer.observe(el); frame();
    return () => { cancelAnimationFrame(raf); observer.disconnect(); geometry.dispose(); material.dispose(); renderer.dispose(); renderer.domElement.remove(); };
  }, [ir]);
  return <div className="canvas-host" ref={host} aria-label="Interactive WebGL mathematical surface" />;
}
