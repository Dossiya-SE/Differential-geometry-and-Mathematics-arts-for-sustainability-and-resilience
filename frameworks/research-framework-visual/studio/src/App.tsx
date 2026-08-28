import { useMemo, useState } from 'react';
import 'katex/dist/katex.min.css';
import './styles.css';
import { torusIR } from './examples/torus';
import type { ParametricSurfaceIR } from './visual-ir';
import { validateIR } from './validation';
import { generateCode } from './codegen';
import { LiveCanvas } from './components/LiveCanvas';
import { RuntimeLab } from './components/RuntimeLab';

type CodeTab = 'python' | 'typescript' | 'glsl' | 'latex';
type WorkspaceMode = 'studio' | 'compute' | 'engines' | 'quality';

type Capability = {
  name: string;
  detail: string;
  state: 'BUILT-IN' | 'COMPUTE LAB' | 'ADAPTER';
};

const CAPABILITIES: Capability[] = [
  { name: 'Symbolic mathematics', detail: 'SymPy · exact differentiation · equations', state: 'COMPUTE LAB' },
  { name: 'Scientific numerics', detail: 'NumPy · SciPy · JAX', state: 'COMPUTE LAB' },
  { name: 'Differential geometry', detail: 'Visual IR · curvature · metric validation', state: 'BUILT-IN' },
  { name: 'Scientific 3D', detail: 'Three.js/WebGL · PyVista/VTK bridge', state: 'BUILT-IN' },
  { name: 'Mathematical animation', detail: 'Manim · FFmpeg', state: 'ADAPTER' },
  { name: 'Cinematic geometry', detail: 'Blender · Geometry Nodes', state: 'ADAPTER' },
  { name: 'Publication vectors', detail: 'SVG · LaTeX · Tectonic · Asymptote', state: 'ADAPTER' },
  { name: 'High-performance math', detail: 'Julia/Makie · Rust/WASM · WebGPU', state: 'ADAPTER' },
];

function isDesktopRuntime(): boolean {
  if (typeof window === 'undefined') return false;
  return '__TAURI_INTERNALS__' in (window as Window & { __TAURI_INTERNALS__?: unknown });
}

function ModeButton({
  active,
  glyph,
  label,
  onClick,
}: {
  active: boolean;
  glyph: string;
  label: string;
  onClick: () => void;
}) {
  return (
    <button className={`rail-button ${active ? 'active' : ''}`} onClick={onClick} title={label}>
      <span className="rail-glyph">{glyph}</span>
      <span>{label}</span>
    </button>
  );
}

function CapabilityDeck() {
  return (
    <div className="capability-deck">
      {CAPABILITIES.map((capability) => (
        <article className="capability-card" key={capability.name}>
          <div className="capability-topline">
            <strong>{capability.name}</strong>
            <span className={`capability-state ${capability.state.toLowerCase().replace(' ', '-')}`}>
              {capability.state}
            </span>
          </div>
          <p>{capability.detail}</p>
        </article>
      ))}
    </div>
  );
}

export default function App() {
  const [ir, setIr] = useState<ParametricSurfaceIR>(torusIR);
  const [tab, setTab] = useState<CodeTab>('python');
  const [mode, setMode] = useState<WorkspaceMode>('studio');
  const checks = useMemo(() => validateIR(ir), [ir]);
  const code = useMemo(() => generateCode(ir), [ir]);
  const desktop = isDesktopRuntime();
  const passCount = checks.filter((check) => check.status === 'PASS').length;
  const failCount = checks.filter((check) => check.status === 'FAIL').length;

  const updateParameter = (name: 'R' | 'r', value: number) =>
    setIr((current) => ({
      ...current,
      parameters: {
        ...current.parameters,
        values: { ...current.parameters.values, [name]: value },
      },
    }));

  return (
    <main className="pro-shell">
      <header className="app-chrome">
        <div className="brand-lockup">
          <div className="brand-mark">MV</div>
          <div>
            <div className="brand-line">
              <strong>Mathematical Visual Design Studio</strong>
              <span className="pro-badge">PRO</span>
            </div>
            <span className="product-subtitle">Scientific visual engineering environment</span>
          </div>
        </div>

        <div className="project-breadcrumb">
          <span>Research Studio</span>
          <b>/</b>
          <span>Differential Geometry</span>
          <b>/</b>
          <strong>{ir.name}</strong>
        </div>

        <div className="chrome-status">
          <span className="status-indicator online" />
          <span>{desktop ? 'Native macOS' : 'Web preview'}</span>
          <span className="chrome-divider" />
          <span>Visual IR {ir.schemaVersion}</span>
        </div>
      </header>

      <section className="app-body">
        <nav className="activity-rail" aria-label="Workspace modes">
          <ModeButton active={mode === 'studio'} glyph="◇" label="Studio" onClick={() => setMode('studio')} />
          <ModeButton active={mode === 'compute'} glyph="∑" label="Compute" onClick={() => setMode('compute')} />
          <ModeButton active={mode === 'engines'} glyph="⌘" label="Engines" onClick={() => setMode('engines')} />
          <ModeButton active={mode === 'quality'} glyph="✓" label="Quality" onClick={() => setMode('quality')} />
          <div className="rail-spacer" />
          <div className="rail-version">V0.4</div>
        </nav>

        <div className="mode-stage">
          {mode === 'studio' && (
            <>
              <aside className="explorer-panel surface-panel">
                <div className="panel-title-row">
                  <div>
                    <span className="section-kicker">Project</span>
                    <h2>Scene Explorer</h2>
                  </div>
                  <span className="tiny-badge">LOCAL</span>
                </div>

                <div className="object-card active-object">
                  <div className="object-icon">S</div>
                  <div>
                    <strong>{ir.name}</strong>
                    <span>{ir.id}</span>
                  </div>
                </div>

                <div className="tree-section">
                  {[
                    ['Equations', '3 expressions'],
                    ['Geometry', `${ir.geometry.resolutionU} × ${ir.geometry.resolutionV}`],
                    ['Fields', 'Gaussian curvature'],
                    ['Camera', ir.camera.projection],
                    ['Lighting', 'WebGL scene'],
                    ['Animation', 'adapter boundary'],
                  ].map(([label, value]) => (
                    <button className="explorer-row" key={label}>
                      <span className="disclosure">›</span>
                      <span>{label}</span>
                      <small>{value}</small>
                    </button>
                  ))}
                </div>

                <div className="pipeline-block">
                  <span className="section-kicker">Scientific pipeline</span>
                  <div className="pipeline-list">
                    {['Domain', 'Equation', 'Surface', 'Curvature', 'Encoding', 'Renderer', 'Validation'].map((node, index) => (
                      <div className="pipeline-step" key={node}>
                        <span>{String(index + 1).padStart(2, '0')}</span>
                        <strong>{node}</strong>
                        <i className={index < 6 ? 'complete' : failCount ? 'danger' : 'complete'} />
                      </div>
                    ))}
                  </div>
                </div>

                <div className="provenance-card">
                  <span className="section-kicker">Provenance</span>
                  <dl>
                    <div><dt>Engine</dt><dd>{ir.provenance.engine}</dd></div>
                    <div><dt>Renderer</dt><dd>{ir.provenance.renderer}</dd></div>
                    <div><dt>Seed</dt><dd>{ir.provenance.deterministicSeed}</dd></div>
                    <div><dt>Status</dt><dd>{ir.epistemicStatus}</dd></div>
                  </dl>
                </div>
              </aside>

              <section className="primary-stage">
                <div className="stage-toolbar surface-panel">
                  <div className="toolbar-group">
                    <span className="toolbar-label">VIEW</span>
                    <span className="toolbar-chip active">Perspective</span>
                    <span className="toolbar-chip">Orbit</span>
                    <span className="toolbar-chip">Curvature field</span>
                  </div>
                  <div className="toolbar-group right">
                    <span className="readout"><i className="green-dot" /> deterministic</span>
                    <span className="readout">{ir.geometry.resolutionU * ir.geometry.resolutionV} samples</span>
                    <span className="readout">WebGL</span>
                  </div>
                </div>

                <div className="canvas-stage surface-panel">
                  <div className="canvas-header">
                    <div>
                      <span className="section-kicker">Live mathematical viewport</span>
                      <h2>Gaussian-curvature encoded manifold</h2>
                    </div>
                    <div className="viewport-badges">
                      <span>{ir.epistemicStatus}</span>
                      <span>REAL-TIME</span>
                    </div>
                  </div>
                  <LiveCanvas ir={ir} />
                  <div className="equation-ribbon">
                    <span className="equation-symbol">X</span>
                    <code>{ir.equations.latex}</code>
                    <div className="equation-meta">
                      <span>K → color</span>
                      <span>metric regularity checked</span>
                    </div>
                  </div>
                </div>

                <div className="power-strip surface-panel">
                  <div className="power-copy">
                    <span className="section-kicker">One object · many engines</span>
                    <strong>Equation → computation → geometry → render → governed output</strong>
                  </div>
                  <div className="engine-flow">
                    {['SymPy', 'NumPy/JAX', 'PyVista/VTK', 'WebGL', 'SVG/PDF', 'Manim/Blender'].map((engine, index) => (
                      <div className="engine-node" key={engine}>
                        <span>{engine}</span>
                        {index < 5 && <b>→</b>}
                      </div>
                    ))}
                  </div>
                </div>
              </section>

              <aside className="inspector-panel surface-panel">
                <div className="panel-title-row">
                  <div>
                    <span className="section-kicker">Inspector</span>
                    <h2>Geometry & Encoding</h2>
                  </div>
                  <span className={`quality-score ${failCount ? 'fail' : ''}`}>{passCount}/{checks.length}</span>
                </div>

                <section className="inspector-section">
                  <div className="inspector-heading"><span>Parametric geometry</span><small>LIVE</small></div>
                  <label className="precision-control">
                    <div><span>Major radius</span><code>R</code><output>{ir.parameters.values.R.toFixed(2)}</output></div>
                    <input
                      type="range"
                      min="0.9"
                      max="3.5"
                      step="0.01"
                      value={ir.parameters.values.R}
                      onChange={(event) => updateParameter('R', Number(event.target.value))}
                    />
                  </label>
                  <label className="precision-control">
                    <div><span>Minor radius</span><code>r</code><output>{ir.parameters.values.r.toFixed(2)}</output></div>
                    <input
                      type="range"
                      min="0.15"
                      max="1.5"
                      step="0.01"
                      value={ir.parameters.values.r}
                      onChange={(event) => updateParameter('r', Number(event.target.value))}
                    />
                  </label>
                </section>

                <section className="inspector-section">
                  <div className="inspector-heading"><span>Visual encoding</span><small>SCIENTIFIC</small></div>
                  <div className="property-grid">
                    <div><span>Scalar field</span><strong>K — Gaussian curvature</strong></div>
                    <div><span>Surface</span><strong>Parametric manifold</strong></div>
                    <div><span>Projection</span><strong>{ir.camera.projection}</strong></div>
                    <div><span>Mesh</span><strong>{ir.visual.showMesh ? 'Visible' : 'Hidden'}</strong></div>
                  </div>
                </section>

                <section className="inspector-section">
                  <div className="inspector-heading"><span>Validation gates</span><small>{failCount ? 'ATTENTION' : 'PASS'}</small></div>
                  <div className="mini-validation-list">
                    {checks.map((check) => (
                      <div className={`mini-check ${check.status.toLowerCase()}`} key={check.id} title={check.detail}>
                        <i />
                        <span>{check.label}</span>
                        <strong>{check.status}</strong>
                      </div>
                    ))}
                  </div>
                </section>

                <section className="inspector-section capability-summary">
                  <div className="inspector-heading"><span>Power stack</span><small>PRO</small></div>
                  <div className="stack-tags">
                    {['Python', 'Julia', 'GLSL', 'LaTeX', 'VTK', 'JAX', 'Manim', 'Blender'].map((item) => <span key={item}>{item}</span>)}
                  </div>
                </section>
              </aside>

              <section className="bottom-dock surface-panel">
                <div className="dock-header">
                  <div className="dock-tabs">
                    {(Object.keys(code) as CodeTab[]).map((name) => (
                      <button key={name} className={tab === name ? 'active' : ''} onClick={() => setTab(name)}>
                        {name}
                      </button>
                    ))}
                  </div>
                  <div className="dock-meta">
                    <span>GENERATED FROM VISUAL IR</span>
                    <span>{desktop ? 'LOCAL DESKTOP' : 'PREVIEW'}</span>
                  </div>
                </div>
                <pre className="source-view"><code>{code[tab]}</code></pre>
              </section>
            </>
          )}

          {mode === 'compute' && (
            <section className="tool-page">
              <div className="tool-page-hero">
                <span className="section-kicker">Native Compute Lab</span>
                <h1>Write mathematics. Execute locally. Generate visual artifacts.</h1>
                <p>Python, JavaScript and Julia execution are bridged through the native Rust shell. Scientific Python profiles, runtime discovery and governed artifact previews stay inside the application.</p>
              </div>
              <RuntimeLab />
            </section>
          )}

          {mode === 'engines' && (
            <section className="tool-page engine-page">
              <div className="tool-page-hero split-hero">
                <div>
                  <span className="section-kicker">Engine architecture</span>
                  <h1>Specialized engines behind one mathematical object model.</h1>
                  <p>The studio does not force one language to do every task. Visual IR preserves the mathematical meaning while specialized engines provide symbolic, numerical, geometric, GPU, animation and publication capabilities.</p>
                </div>
                <div className="architecture-formula">Visual IR → adapters → validated outputs</div>
              </div>
              <CapabilityDeck />
              <RuntimeLab />
            </section>
          )}

          {mode === 'quality' && (
            <section className="tool-page quality-page">
              <div className="tool-page-hero split-hero">
                <div>
                  <span className="section-kicker">Scientific QA</span>
                  <h1>Professional rendering with explicit mathematical and epistemic gates.</h1>
                  <p>A successful render is not accepted merely because it looks good. Mathematical regularity, provenance, epistemic status, reproducibility and output integrity remain first-class controls.</p>
                </div>
                <div className={`quality-hero-score ${failCount ? 'fail' : ''}`}>
                  <strong>{passCount}/{checks.length}</strong>
                  <span>current gates passing</span>
                </div>
              </div>

              <div className="qa-grid">
                {checks.map((check) => (
                  <article className={`qa-card ${check.status.toLowerCase()}`} key={check.id}>
                    <span className="qa-index">{check.id}</span>
                    <strong>{check.label}</strong>
                    <p>{check.detail}</p>
                    <b>{check.status}</b>
                  </article>
                ))}
              </div>

              <div className="scientific-contract surface-panel">
                <div>
                  <span className="section-kicker">Non-compensatory rule</span>
                  <h2>Visual sophistication does not substitute for scientific validity.</h2>
                </div>
                <div className="contract-flow">
                  {['Equation', 'Computation', 'Verification', 'Geometry', 'Render', 'Provenance', 'Bounded claim'].map((step, index) => (
                    <span key={step}>{step}{index < 6 ? ' →' : ''}</span>
                  ))}
                </div>
              </div>
            </section>
          )}
        </div>
      </section>

      <footer className="global-statusbar">
        <span><i className="status-indicator online" /> renderer ready</span>
        <span>Object: {ir.id}</span>
        <span>Epistemic: {ir.epistemicStatus}</span>
        <span>Seed: {ir.provenance.deterministicSeed}</span>
        <span className="statusbar-spacer" />
        <strong>{failCount ? `${failCount} validation issue${failCount > 1 ? 's' : ''}` : 'All current validation gates pass'}</strong>
      </footer>
    </main>
  );
}
