#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use serde::{Deserialize, Serialize};
use std::env;
use std::path::{Path, PathBuf};
use std::process::Command;

#[derive(Debug, Clone, Serialize)]
#[serde(rename_all = "camelCase")]
struct RuntimeInfo {
    id: String,
    label: String,
    installed: bool,
    path: Option<String>,
    version: Option<String>,
    role: String,
}

#[derive(Debug, Deserialize)]
#[serde(rename_all = "camelCase")]
struct ExecutionRequest {
    language: String,
    code: String,
}

#[derive(Debug, Serialize)]
#[serde(rename_all = "camelCase")]
struct ExecutionResult {
    language: String,
    executable: String,
    success: bool,
    exit_code: Option<i32>,
    stdout: String,
    stderr: String,
}

fn candidate_dirs() -> Vec<PathBuf> {
    let mut dirs: Vec<PathBuf> = env::var_os("PATH")
        .map(|value| env::split_paths(&value).collect())
        .unwrap_or_default();

    for candidate in [
        "/opt/homebrew/bin",
        "/usr/local/bin",
        "/usr/bin",
        "/bin",
        "/opt/anaconda3/bin",
    ] {
        dirs.push(PathBuf::from(candidate));
    }

    if let Some(home) = env::var_os("HOME") {
        let home = PathBuf::from(home);
        dirs.push(home.join(".cargo/bin"));
        dirs.push(home.join(".local/bin"));
        dirs.push(home.join("miniconda3/bin"));
    }

    dirs.sort();
    dirs.dedup();
    dirs
}

fn resolve_executable(names: &[&str]) -> Option<PathBuf> {
    for name in names {
        let direct = Path::new(name);
        if direct.is_absolute() && direct.is_file() {
            return Some(direct.to_path_buf());
        }
        for dir in candidate_dirs() {
            let candidate = dir.join(name);
            if candidate.is_file() {
                return Some(candidate);
            }
        }
    }
    None
}

fn read_version(path: &Path) -> Option<String> {
    let output = Command::new(path).arg("--version").output().ok()?;
    let stdout = String::from_utf8_lossy(&output.stdout).trim().to_string();
    let stderr = String::from_utf8_lossy(&output.stderr).trim().to_string();
    let value = if !stdout.is_empty() { stdout } else { stderr };
    if value.is_empty() {
        None
    } else {
        Some(value.lines().next().unwrap_or_default().to_string())
    }
}

fn runtime(id: &str, label: &str, names: &[&str], role: &str) -> RuntimeInfo {
    let resolved = resolve_executable(names);
    RuntimeInfo {
        id: id.to_string(),
        label: label.to_string(),
        installed: resolved.is_some(),
        version: resolved.as_deref().and_then(read_version),
        path: resolved.map(|path| path.to_string_lossy().to_string()),
        role: role.to_string(),
    }
}

#[tauri::command]
fn runtime_inventory() -> Vec<RuntimeInfo> {
    vec![
        runtime("python", "Python", &["python3", "python"], "Scientific computing, symbolic mathematics, plotting and geometry adapters"),
        runtime("node", "Node.js", &["node"], "JavaScript and TypeScript computation"),
        runtime("julia", "Julia", &["julia"], "High-performance numerical mathematics and Makie adapters"),
        runtime("blender", "Blender", &["blender"], "Cinematic 3D, Geometry Nodes and Python-driven rendering"),
        runtime("manim", "Manim", &["manim"], "Equation-driven mathematical animation"),
        runtime("tectonic", "Tectonic", &["tectonic"], "Reproducible LaTeX/PDF compilation"),
        runtime("ffmpeg", "FFmpeg", &["ffmpeg"], "Animation and video encoding"),
        runtime("graphviz", "Graphviz", &["dot"], "Graph and dependency-layout rendering"),
        runtime("asymptote", "Asymptote", &["asy"], "Precise mathematical vector and 3D diagrams"),
    ]
}

#[tauri::command]
async fn execute_code(request: ExecutionRequest) -> Result<ExecutionResult, String> {
    if request.code.len() > 200_000 {
        return Err("Code payload exceeds the 200 kB local execution limit.".to_string());
    }

    tauri::async_runtime::spawn_blocking(move || {
        let (names, args): (&[&str], Vec<&str>) = match request.language.as_str() {
            "python" => (&["python3", "python"], vec!["-c"]),
            "javascript" | "node" => (&["node"], vec!["-e"]),
            "julia" => (&["julia"], vec!["-e"]),
            other => return Err(format!("Unsupported executable language: {other}")),
        };

        let executable = resolve_executable(names)
            .ok_or_else(|| format!("Required runtime is not installed for {}.", request.language))?;

        let mut command = Command::new(&executable);
        command.args(args);
        command.arg(&request.code);
        command.env("PYTHONNOUSERSITE", "0");

        let output = command
            .output()
            .map_err(|error| format!("Failed to launch {}: {error}", executable.display()))?;

        Ok(ExecutionResult {
            language: request.language,
            executable: executable.to_string_lossy().to_string(),
            success: output.status.success(),
            exit_code: output.status.code(),
            stdout: String::from_utf8_lossy(&output.stdout).to_string(),
            stderr: String::from_utf8_lossy(&output.stderr).to_string(),
        })
    })
    .await
    .map_err(|error| format!("Runtime task failed: {error}"))?
}

#[tauri::command]
async fn python_package_inventory() -> Result<Vec<RuntimeInfo>, String> {
    tauri::async_runtime::spawn_blocking(move || {
        let python = resolve_executable(&["python3", "python"])
            .ok_or_else(|| "Python 3 was not found on this Mac.".to_string())?;

        let packages = [
            ("numpy", "NumPy", "Array mathematics and numerical kernels"),
            ("scipy", "SciPy", "Scientific algorithms, integration, optimization and statistics"),
            ("sympy", "SymPy", "Exact symbolic mathematics and equation verification"),
            ("matplotlib", "Matplotlib", "Publication-grade scientific plotting"),
            ("pyvista", "PyVista", "VTK-backed scientific 3D geometry and scalar fields"),
            ("vtk", "VTK", "High-performance scientific visualization toolkit"),
            ("networkx", "NetworkX", "Networks, graph geometry and topology"),
            ("pandas", "pandas", "Tabular research-data workflows"),
            ("plotly", "Plotly", "Interactive scientific charts"),
            ("jax", "JAX", "Accelerated numerical computing and automatic differentiation"),
            ("manim", "Manim Python", "Programmatic mathematical animation"),
        ];

        let mut result = Vec::new();
        for (module, label, role) in packages {
            let code = format!(
                "import importlib.util, importlib.metadata; m={module:?}; s=importlib.util.find_spec(m); print(importlib.metadata.version(m) if s else '')"
            );
            let output = Command::new(&python).args(["-c", &code]).output();
            let version = output
                .ok()
                .map(|o| String::from_utf8_lossy(&o.stdout).trim().to_string())
                .filter(|value| !value.is_empty());
            result.push(RuntimeInfo {
                id: module.to_string(),
                label: label.to_string(),
                installed: version.is_some(),
                path: Some(python.to_string_lossy().to_string()),
                version,
                role: role.to_string(),
            });
        }
        Ok(result)
    })
    .await
    .map_err(|error| format!("Python inventory task failed: {error}"))?
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            runtime_inventory,
            execute_code,
            python_package_inventory
        ])
        .run(tauri::generate_context!())
        .expect("error while running Mathematical Visual Design Studio");
}
