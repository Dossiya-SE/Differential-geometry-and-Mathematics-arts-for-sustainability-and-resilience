import { useEffect, useMemo, useState } from 'react';
import { invoke } from '@tauri-apps/api/core';

type RuntimeInfo = {
  id: string;
  label: string;
  installed: boolean;
  path?: string | null;
  version?: string | null;
  role: string;
};

type ArtifactInfo = {
  name: string;
  kind: string;
  sizeBytes: number;
};

type ExecutionResult = {
  language: string;
  executable: string;
  workspace: string;
  success: boolean;
  exitCode?: number | null;
  stdout: string;
  stderr: string;
  artifacts: ArtifactInfo[];
};

type ExecutableLanguage = 'python' | 'javascript' | 'julia';
type PythonProfile = 'core' | 'geometry' | 'advanced' | 'animation' | 'full';

const STARTER_CODE: Record<ExecutableLanguage, string> = {
  python: `import math\nfrom pathlib import Path\n\nW, H = 900, 600\npoints = []\nfor i in range(721):\n    t = 2 * math.pi * i / 720\n    r = 180 + 54 * math.sin(5 * t)\n    x = W/2 + r * math.cos(t)\n    y = H/2 + r * math.sin(t)\n    points.append(f"{x:.2f},{y:.2f}")\npolyline = " ".join(points)\nsvg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n<rect width="100%" height="100%" fill="#03070d"/>\n<polyline points="{polyline}" fill="none" stroke="#38bdf8" stroke-width="3"/>\n<circle cx="{W/2}" cy="{H/2}" r="4" fill="#e2f3ff"/>\n</svg>'''\nPath("mvs_output.svg").write_text(svg, encoding="utf-8")\nprint("Created mvs_output.svg in the studio workspace")`,
  javascript: `const fs = require('fs');\nconst W = 900, H = 600;\nconst points = [];\nfor (let i = 0; i <= 720; i++) {\n  const t = 2 * Math.PI * i / 720;\n  const r = 180 + 54 * Math.sin(5 * t);\n  points.push(\`${'${'}(W/2+r*Math.cos(t)).toFixed(2)},${'${'}(H/2+r*Math.sin(t)).toFixed(2)}\`);\n}\nconst svg = \`<svg xmlns="http://www.w3.org/2000/svg" width="${'${'}W}" height="${'${'}H}"><rect width="100%" height="100%" fill="#03070d"/><polyline points="${'${'}points.join(' ')}" fill="none" stroke="#38bdf8" stroke-width="3"/></svg>\`;\nfs.writeFileSync('mvs_output.svg', svg);\nconsole.log('Created mvs_output.svg in the studio workspace');`,
  julia: `W, H = 900, 600\npts = String[]\nfor i in 0:720\n    t = 2π * i / 720\n    r = 180 + 54sin(5t)\n    x = W/2 + r*cos(t)\n    y = H/2 + r*sin(t)\n    push!(pts, "$(round(x,digits=2)),$(round(y,digits=2))")\nend\nsvg = "<svg xmlns='http://www.w3.org/2000/svg' width='900' height='600'><rect width='100%' height='100%' fill='#03070d'/><polyline points='$(join(pts," "))' fill='none' stroke='#38bdf8' stroke-width='3'/></svg>"\nwrite("mvs_output.svg", svg)\nprintln("Created mvs_output.svg in the studio workspace")`,
};

const PROFILE_LABELS: Record<PythonProfile, string> = {
  core: 'Core Scientific',
  geometry: 'Geometry / VTK',
  advanced: 'Advanced / JAX',
  animation: 'Animation / Manim',
  full: 'Full Python Lab',
};

function isDesktopRuntime(): boolean {
  if (typeof window === 'undefined') return false;
  return '__TAURI_INTERNALS__' in (window as Window & { __TAURI_INTERNALS__?: unknown });
}

export function RuntimeLab() {
  const desktop = isDesktopRuntime();
  const [runtimes, setRuntimes] = useState<RuntimeInfo[]>([]);
  const [packages, setPackages] = useState<RuntimeInfo[]>([]);
  const [language, setLanguage] = useState<ExecutableLanguage>('python');
  const [code, setCode] = useState(STARTER_CODE.python);
  const [result, setResult] = useState<ExecutionResult | null>(null);
  const [error, setError] = useState<string>('');
  const [message, setMessage] = useState<string>('');
  const [running, setRunning] = useState(false);
  const [scanning, setScanning] = useState(false);
  const [installing, setInstalling] = useState<PythonProfile | null>(null);
  const [previewData, setPreviewData] = useState<string>('');
  const [previewName, setPreviewName] = useState<string>('');

  const executable = useMemo(
    () => runtimes.find((runtime) => runtime.id === (language === 'javascript' ? 'node' : language)),
    [language, runtimes]
  );

  const scan = async () => {
    if (!desktop) return;
    setScanning(true);
    setError('');
    try {
      const [runtimeData, packageData] = await Promise.all([
        invoke<RuntimeInfo[]>('runtime_inventory'),
        invoke<RuntimeInfo[]>('python_package_inventory').catch(() => []),
      ]);
      setRuntimes(runtimeData);
      setPackages(packageData);
    } catch (cause) {
      setError(String(cause));
    } finally {
      setScanning(false);
    }
  };

  useEffect(() => {
    void scan();
  }, [desktop]);

  const changeLanguage = (next: ExecutableLanguage) => {
    setLanguage(next);
    setCode(STARTER_CODE[next]);
    setResult(null);
    setError('');
    setMessage('');
    setPreviewData('');
    setPreviewName('');
  };

  const runCode = async () => {
    if (!desktop || running) return;
    setRunning(true);
    setError('');
    setMessage('');
    setResult(null);
    setPreviewData('');
    setPreviewName('');
    try {
      const execution = await invoke<ExecutionResult>('execute_code', {
        request: { language, code },
      });
      setResult(execution);
      const firstPreview = execution.artifacts.find((artifact) => ['svg', 'png', 'jpeg', 'webp'].includes(artifact.kind));
      if (firstPreview) {
        const data = await invoke<string>('read_workspace_artifact', { name: firstPreview.name });
        setPreviewData(data);
        setPreviewName(firstPreview.name);
      }
    } catch (cause) {
      setError(String(cause));
    } finally {
      setRunning(false);
    }
  };

  const openArtifact = async (artifact: ArtifactInfo) => {
    if (!['svg', 'png', 'jpeg', 'webp'].includes(artifact.kind)) return;
    try {
      const data = await invoke<string>('read_workspace_artifact', { name: artifact.name });
      setPreviewData(data);
      setPreviewName(artifact.name);
    } catch (cause) {
      setError(String(cause));
    }
  };

  const installProfile = async (profile: PythonProfile) => {
    if (!desktop || installing) return;
    setInstalling(profile);
    setError('');
    setMessage(`Installing ${PROFILE_LABELS[profile]}… this can take several minutes.`);
    try {
      const response = await invoke<string>('install_python_profile', { profile });
      setMessage(response);
      await scan();
    } catch (cause) {
      setMessage('');
      setError(String(cause));
    } finally {
      setInstalling(null);
    }
  };

  return (
    <section className="runtime-panel panel">
      <div className="runtime-heading">
        <div>
          <span className="eyebrow">Native Compute Lab</span>
          <h2>Run mathematical code, generate visual artifacts, and manage scientific engines inside the application</h2>
        </div>
        <button className="runtime-action" onClick={() => void scan()} disabled={!desktop || scanning}>
          {scanning ? 'Scanning…' : 'Scan tools'}
        </button>
      </div>

      {!desktop ? (
        <div className="runtime-notice">
          Runtime execution is intentionally disabled in the browser preview. Open the installed Tauri desktop app to use local Python, Node.js and Julia engines.
        </div>
      ) : (
        <div className="runtime-layout">
          <div className="runtime-catalog">
            <h3>Language & rendering engines</h3>
            <div className="runtime-cards">
              {runtimes.map((runtime) => (
                <div className={`runtime-card ${runtime.installed ? 'available' : 'missing'}`} key={runtime.id}>
                  <div className="runtime-card-title">
                    <strong>{runtime.label}</strong>
                    <span>{runtime.installed ? 'READY' : 'NOT FOUND'}</span>
                  </div>
                  <p>{runtime.role}</p>
                  {runtime.version && <code>{runtime.version}</code>}
                  {runtime.path && <small>{runtime.path}</small>}
                </div>
              ))}
            </div>

            <h3>One-click managed Python profiles</h3>
            <div className="profile-grid">
              {(Object.keys(PROFILE_LABELS) as PythonProfile[]).map((profile) => (
                <button
                  key={profile}
                  className="profile-button"
                  onClick={() => void installProfile(profile)}
                  disabled={Boolean(installing)}
                >
                  <strong>{PROFILE_LABELS[profile]}</strong>
                  <span>
                    {profile === 'core' && 'NumPy · SciPy · SymPy · Matplotlib · pandas · NetworkX · Plotly'}
                    {profile === 'geometry' && 'Core + PyVista + VTK'}
                    {profile === 'advanced' && 'Geometry + JAX automatic differentiation'}
                    {profile === 'animation' && 'Core + Manim Python package'}
                    {profile === 'full' && 'Geometry + JAX + Manim'}
                  </span>
                  {installing === profile && <em>Installing…</em>}
                </button>
              ))}
            </div>

            <h3>Python scientific stack</h3>
            <div className="package-grid">
              {packages.length === 0 ? (
                <span className="runtime-muted">Python packages will appear after a successful scan.</span>
              ) : packages.map((pkg) => (
                <div className={`package-chip ${pkg.installed ? 'available' : 'missing'}`} key={pkg.id} title={pkg.role}>
                  <span>{pkg.label}</span>
                  <strong>{pkg.installed ? pkg.version ?? 'ready' : 'missing'}</strong>
                </div>
              ))}
            </div>
          </div>

          <div className="runtime-editor">
            <div className="runtime-toolbar">
              <div className="language-tabs">
                {(['python', 'javascript', 'julia'] as ExecutableLanguage[]).map((name) => (
                  <button key={name} className={language === name ? 'active' : ''} onClick={() => changeLanguage(name)}>
                    {name === 'javascript' ? 'JavaScript' : name[0].toUpperCase() + name.slice(1)}
                  </button>
                ))}
              </div>
              <button className="run-button" onClick={() => void runCode()} disabled={running || !executable?.installed}>
                {running ? 'Running…' : 'Run + render'}
              </button>
            </div>

            <textarea
              className="runtime-code-editor"
              spellCheck={false}
              value={code}
              onChange={(event) => setCode(event.target.value)}
              aria-label={`${language} code editor`}
            />

            <div className="runtime-console">
              <div className="console-title">
                <span>Execution output</span>
                {executable && <code>{executable.installed ? executable.path : `${language} runtime missing`}</code>}
              </div>
              {message && <div className="console-message">{message}</div>}
              {error && <pre className="console-error">{error}</pre>}
              {result && (
                <>
                  {result.stdout && <pre>{result.stdout}</pre>}
                  {result.stderr && <pre className="console-error">{result.stderr}</pre>}
                  <div className={`execution-status ${result.success ? 'pass' : 'fail'}`}>
                    {result.success ? 'PASS' : 'FAIL'} · exit {result.exitCode ?? 'unknown'} · workspace {result.workspace}
                  </div>
                </>
              )}
              {!error && !message && !result && <span className="runtime-muted">Run code to see stdout, stderr, artifacts and execution status.</span>}
            </div>

            {result && result.artifacts.length > 0 && (
              <div className="artifact-panel">
                <div className="artifact-list">
                  <h3>Generated design artifacts</h3>
                  {result.artifacts.map((artifact) => (
                    <button
                      className={`artifact-item ${previewName === artifact.name ? 'active' : ''}`}
                      key={artifact.name}
                      onClick={() => void openArtifact(artifact)}
                      disabled={!['svg', 'png', 'jpeg', 'webp'].includes(artifact.kind)}
                    >
                      <strong>{artifact.name}</strong>
                      <span>{artifact.kind.toUpperCase()} · {(artifact.sizeBytes / 1024).toFixed(1)} kB</span>
                    </button>
                  ))}
                </div>
                <div className="artifact-preview">
                  {previewData ? <img src={previewData} alt={`Generated artifact ${previewName}`} /> : <span>No image preview available.</span>}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      <div className="runtime-safety">
        Local execution is a trusted-workstation capability. Python, JavaScript and Julia code can access resources permitted to your macOS user account. The studio intentionally does not expose an unrestricted shell command box; use reviewed project code and keep untrusted scripts isolated.
      </div>
    </section>
  );
}
