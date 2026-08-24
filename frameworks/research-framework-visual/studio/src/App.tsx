import { useMemo, useState } from 'react';
import 'katex/dist/katex.min.css';
import './styles.css';
import { torusIR } from './examples/torus';
import type { ParametricSurfaceIR } from './visual-ir';
import { validateIR } from './validation';
import { generateCode } from './codegen';
import { LiveCanvas } from './components/LiveCanvas';

type CodeTab = 'python' | 'typescript' | 'glsl' | 'latex';

function isDesktopRuntime(): boolean {
  if (typeof window === 'undefined') return false;
  return '__TAURI_INTERNALS__' in (window as Window & { __TAURI_INTERNALS__?: unknown });
}

export default function App() {
  const [ir, setIr] = useState<ParametricSurfaceIR>(torusIR);
  const [tab, setTab] = useState<CodeTab>('python');
  const checks = useMemo(() => validateIR(ir), [ir]);
  const code = useMemo(() => generateCode(ir), [ir]);
  const desktop = isDesktopRuntime();

  const updateParameter = (name: 'R' | 'r', value: number) =>
    setIr((current) => ({
      ...current,
      parameters: {
        ...current.parameters,
        values: { ...current.parameters.values, [name]: value }
      }
    }));

  return (
    <main className="studio-shell">
      <header className="topbar">
        <div>
          <span className="eyebrow">MSR Visual Engineering</span>
          <h1>Mathematical Visual Design Studio</h1>
        </div>
        <span className="engine-badge">
          {desktop ? 'Native Desktop GUI · Tauri 2' : 'Web Preview'} · Visual IR 0.1
        </span>
      </header>

      <section className="workspace">
        <aside className="project-panel panel">
          <h2>Project</h2>
          <div className="tree-item active">◉ {ir.name}</div>
          {['Equations', 'Geometry', 'Fields', 'Camera', 'Lighting', 'Labels', 'Animation'].map((item) => (
            <div className="tree-item child" key={item}>└ {item}</div>
          ))}

          <h3>Pipeline</h3>
          <div className="node-stack">
            {['Domain', 'Equation', 'Surface', 'Curvature', 'Color Map', 'Camera', 'Renderer'].map((node, index) => (
              <div className="node" key={node}>
                <span>{index + 1}</span>{node}
              </div>
            ))}
          </div>
        </aside>

        <section className="canvas-panel panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">Live Canvas</span>
              <h2>WebGL differential-geometry preview</h2>
            </div>
            <span className="status-chip">{ir.epistemicStatus}</span>
          </div>
          <LiveCanvas ir={ir} />
          <div className="equation-box">{ir.equations.latex}</div>
        </section>

        <aside className="parameter-panel panel">
          <h2>Parameters</h2>

          <label>
            Major radius R
            <input
              type="range"
              min="0.9"
              max="3.5"
              step="0.01"
              value={ir.parameters.values.R}
              onChange={(e) => updateParameter('R', Number(e.target.value))}
            />
            <output>{ir.parameters.values.R.toFixed(2)}</output>
          </label>

          <label>
            Minor radius r
            <input
              type="range"
              min="0.15"
              max="1.5"
              step="0.01"
              value={ir.parameters.values.r}
              onChange={(e) => updateParameter('r', Number(e.target.value))}
            />
            <output>{ir.parameters.values.r.toFixed(2)}</output>
          </label>

          <div className="metric-card"><span>Color field</span><strong>K — Gaussian curvature</strong></div>
          <div className="metric-card"><span>Mesh</span><strong>{ir.geometry.resolutionU} × {ir.geometry.resolutionV}</strong></div>
          <div className="metric-card"><span>Renderer</span><strong>Three.js / WebGL</strong></div>
          <div className="metric-card"><span>GUI shell</span><strong>{desktop ? 'Tauri native window' : 'Browser'}</strong></div>
          <div className="metric-card"><span>Canonical object</span><code>{ir.id}</code></div>
        </aside>
      </section>

      <section className="code-panel panel">
        <div className="code-tabs">
          {(Object.keys(code) as CodeTab[]).map((name) => (
            <button key={name} className={tab === name ? 'active' : ''} onClick={() => setTab(name)}>
              {name}
            </button>
          ))}
        </div>
        <pre><code>{code[tab]}</code></pre>
      </section>

      <footer className="validation-panel panel">
        <div className="validation-grid">
          {checks.map((check) => (
            <div
              className={`validation-item ${check.status.toLowerCase()}`}
              key={check.id}
              title={check.detail}
            >
              <span className="status-dot" />
              <span>{check.label}</span>
              <strong>{check.status}</strong>
            </div>
          ))}
        </div>
      </footer>
    </main>
  );
}
