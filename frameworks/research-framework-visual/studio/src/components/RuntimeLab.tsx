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

type ExecutionResult = {
  language: string;
  executable: string;
  success: boolean;
  exitCode?: number | null;
  stdout: string;
  stderr: string;
};

type ExecutableLanguage = 'python' | 'javascript' | 'julia';

const STARTER_CODE: Record<ExecutableLanguage, string> = {
  python: `import math\nR, r = 2.0, 0.72\nfor i in range(5):\n    v = 2 * math.pi * i / 5\n    K = math.cos(v) / (r * (R + r * math.cos(v)))\n    print(f"v={v:.3f}, K={K:.6f}")`,
  javascript: `const R = 2.0, r = 0.72;\nfor (let i = 0; i < 5; i++) {\n  const v = 2 * Math.PI * i / 5;\n  const K = Math.cos(v) / (r * (R + r * Math.cos(v)));\n  console.log({ v, K });\n}`,
  julia: `R, r = 2.0, 0.72\nfor i in 0:4\n    v = 2π * i / 5\n    K = cos(v) / (r * (R + r * cos(v)))\n    println("v=$(round(v, digits=3)), K=$(round(K, digits=6))")\nend`,
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
  const [running, setRunning] = useState(false);
  const [scanning, setScanning] = useState(false);

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
  };

  const runCode = async () => {
    if (!desktop || running) return;
    setRunning(true);
    setError('');
    setResult(null);
    try {
      const execution = await invoke<ExecutionResult>('execute_code', {
        request: { language, code },
      });
      setResult(execution);
    } catch (cause) {
      setError(String(cause));
    } finally {
      setRunning(false);
    }
  };

  return (
    <section className="runtime-panel panel">
      <div className="runtime-heading">
        <div>
          <span className="eyebrow">Native Compute Lab</span>
          <h2>Run mathematical code inside the application</h2>
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
                {running ? 'Running…' : 'Run code'}
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
                <span>Output</span>
                {executable && <code>{executable.installed ? executable.path : `${language} runtime missing`}</code>}
              </div>
              {error && <pre className="console-error">{error}</pre>}
              {result && (
                <>
                  {result.stdout && <pre>{result.stdout}</pre>}
                  {result.stderr && <pre className="console-error">{result.stderr}</pre>}
                  <div className={`execution-status ${result.success ? 'pass' : 'fail'}`}>
                    {result.success ? 'PASS' : 'FAIL'} · exit {result.exitCode ?? 'unknown'}
                  </div>
                </>
              )}
              {!error && !result && <span className="runtime-muted">Run code to see stdout, stderr and execution status.</span>}
            </div>
          </div>
        </div>
      )}

      <div className="runtime-safety">
        Local execution is a trusted-workstation capability. Python, JavaScript and Julia code can access resources permitted to your macOS user account; use reviewed project code and keep untrusted scripts isolated.
      </div>
    </section>
  );
}
