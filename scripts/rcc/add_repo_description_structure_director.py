from pathlib import Path
import json
import re
from datetime import datetime, timezone

root = Path.cwd()

DESCRIPTION = "Governed agentic episodic memory workbench with RCC-N repo-context navigation, source-bound recall, fallback/abstention benchmarks, evidence packages, and regression guards."

TOPICS = [
    "agentic-memory",
    "episodic-memory",
    "governed-ai",
    "ai-safety",
    "benchmark-suite",
    "repository-context",
    "rcc",
    "rcc-nexus",
    "agent-navigation",
    "evidence-packages",
]

def read(path: str) -> str:
    p = root / path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8-sig", errors="replace")

def write(path: str, content) -> None:
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, list):
        text = "\n".join(content)
    else:
        text = str(content)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"[WRITE] {path}")

def load_json(path: str):
    return json.loads(read(path))

def save_json(path: str, data) -> None:
    write(path, json.dumps(data, indent=2, sort_keys=True))

def replace_between(text: str, start_heading: str, end_heading: str, replacement_lines: list[str]) -> str:
    start = text.find(start_heading)
    if start == -1:
        return text.rstrip() + "\n\n" + "\n".join(replacement_lines).strip() + "\n"

    end = text.find(end_heading, start + len(start_heading))
    replacement = "\n".join(replacement_lines).strip() + "\n\n"

    if end == -1:
        return text[:start].rstrip() + "\n\n" + replacement

    return text[:start].rstrip() + "\n\n" + replacement + text[end:].lstrip()

def insert_after_title_if_missing(text: str) -> str:
    marker = "## Repository Description"
    if marker in text:
        return text

    lines = [
        "## Repository Description",
        "",
        DESCRIPTION,
        "",
        "This repo combines two layers:",
        "",
        "1. AERMA runtime: source-bound episodic recall, ambiguity fallback, abstention, boundary separation, baseline comparison, regression guard, and evidence packages.",
        "2. RCC-N navigation: Human Director Box, README trisection, repository sphere, route maps, Echo Location records, Nexus reports, charts, and public Markdown integrity checks.",
        "",
        "Boundary: this description improves discoverability. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, production readiness, sentience, consciousness, or human memory.",
        "",
    ]

    title = "# AERMA-Memory: Governed Agentic Episodic Memory Workbench"
    idx = text.find(title)
    if idx == -1:
        return "\n".join(lines) + "\n" + text

    title_end = text.find("\n", idx)
    if title_end == -1:
        return text + "\n\n" + "\n".join(lines)

    return text[:title_end + 1] + "\n" + "\n".join(lines) + "\n" + text[title_end + 1:]

def project_structure_director() -> list[str]:
    return [
        "## Project Structure",
        "",
        "AERMA-Memory is organized as a runtime workbench plus a repository-navigation shell.",
        "",
        "    AERMA-Memory/",
        "    ├── AGENTS.md                         # Agent entry beacon and operating contract",
        "    ├── CLAUDE.md                         # Claude-specific repo memory and patch rules",
        "    ├── configs/                          # Runtime, metric, baseline, and suite configuration",
        "    │   ├── runtime_config.json            # Runtime defaults",
        "    │   ├── metric_manifest.json           # Declared metrics and threshold surfaces",
        "    │   ├── baseline_config.json           # Baseline selection/configuration",
        "    │   └── suite_config.json              # Suite execution settings",
        "    ├── docs/                             # Theory, architecture, evidence, and RCC context",
        "    │   ├── context/                       # RCC indexes, validation surfaces, drift reports",
        "    │   ├── software_architecture/         # AERMA/RCC/RCC-N architecture locks",
        "    │   ├── benchmark_protocol/            # Benchmark method and task protocols",
        "    │   └── evidence/                      # Evidence-package and ledger contracts",
        "    ├── evidence_packages/                 # Generated evidence packages from suite runs",
        "    ├── ledgers/                           # JSONL continuity, suite, decision, and trace ledgers",
        "    ├── logs/                              # Attribution, regression guard, and phase logs",
        "    ├── memory/                            # Promoted invariants, rejected claims, failure lessons",
        "    ├── rcc/nexus/                         # RCC-N route maps, protocol, Echo template, handoff",
        "    ├── reports/rcc_nexus/                 # RCC-N benchmark reports, scorecards, metrics history",
        "    ├── runs/                              # Generated suite run outputs",
        "    ├── scripts/                           # Human-facing helper, RCC, validation, and report scripts",
        "    │   └── rcc/                           # RCC/RCC-N checkers, benchmarks, charts, repair scripts",
        "    ├── src/                               # Importable Python package",
        "    │   └── aerma/                         # AERMA runtime package",
        "    │       ├── agent/                     # Recursive/reflection stubs only",
        "    │       ├── benchmarks/                # Suite runner, baselines, scoring, classifier",
        "    │       ├── cli/                       # Command-line entry points",
        "    │       ├── core/                      # Episodes, memory store, metric manifest, retrieval",
        "    │       ├── drift/                     # Retrieval drift and Omega diagnostics",
        "    │       ├── evidence/                  # Ledger and evidence package compiler",
        "    │       └── gate/                      # ActionGate and SourceFallback",
        "    ├── tasks/                             # Controlled benchmark task JSON and suite manifest",
        "    ├── tests/                             # Pytest implementation-health validation",
        "    └── visuals/rcc_nexus/                 # RCC-N charts and visual diagnostics",
        "",
        "## Project Structure Director",
        "",
        "| Surface | What it does | Why it matters |",
        "|---|---|---|",
        "| `AGENTS.md` | Gives coding agents the entry order, route rules, and validation requirements. | Prevents blind patching. |",
        "| `CLAUDE.md` | Gives Claude-specific instructions for preserving formatting, claims, and validation. | Keeps model-specific behavior aligned. |",
        "| `configs/` | Stores runtime, metric, baseline, and suite configuration. | Makes benchmark behavior inspectable. |",
        "| `docs/context/` | Stores RCC context index, validation surface, context budget, drift reports, and RCC-N index. | Main source of repository self-description. |",
        "| `docs/software_architecture/` | Stores locked software architecture and implementation contracts. | Keeps theory-to-software direction explicit. |",
        "| `evidence_packages/` | Stores generated evidence packages from suite runs. | Links claims to task outputs and artifacts. |",
        "| `ledgers/` | Stores append-style JSONL continuity records. | Preserves run and decision history. |",
        "| `logs/` | Stores attribution and regression-guard outputs. | Supports audit and regression review. |",
        "| `memory/` | Stores promoted invariants and rejected overclaims. | Keeps memory promotion bounded. |",
        "| `rcc/nexus/` | Stores RCC-N route maps, task matrix, protocol, Echo template, and handoff contract. | Makes the repo agent-navigable. |",
        "| `reports/rcc_nexus/` | Stores RCC-N benchmark reports, scorecards, public polish reports, and metrics history. | Turns RCC-N into a measured surface. |",
        "| `runs/` | Stores generated suite run outputs. | Keeps benchmark output reproducible. |",
        "| `scripts/` | Stores helper scripts for running, checking, repairing, reporting, and charting. | Provides human/agent command surfaces. |",
        "| `scripts/rcc/` | Stores RCC/RCC-N checkers, benchmark scripts, chart generators, and repair scripts. | Enforces repository-context integrity. |",
        "| `src/aerma/` | Stores the importable runtime package. | Contains actual AERMA implementation code. |",
        "| `src/aerma/core/` | Defines AgentEpisode, memory store, metric manifest, and retrieval primitives. | Core source-bound memory mechanics. |",
        "| `src/aerma/drift/` | Computes retrieval drift and Omega diagnostic weight. | Supports bounded uncertainty and gate decisions. |",
        "| `src/aerma/gate/` | Implements ActionGate and SourceFallback. | Prevents high-drift or ambiguous returns as fact. |",
        "| `src/aerma/benchmarks/` | Runs benchmark tasks, baselines, scoring, classification, attribution, and regression guard. | Produces the controlled evidence surface. |",
        "| `src/aerma/evidence/` | Compiles ledgers and evidence packages. | Connects runtime claims to artifacts. |",
        "| `src/aerma/agent/` | Contains RecursiveExecutorStub and ReflectionEvaluatorStub. | Preserves future interface without overclaiming recursion. |",
        "| `tasks/` | Stores benchmark task definitions. | Defines what the suite actually tests. |",
        "| `tests/` | Stores pytest implementation-health checks. | Catches regressions in local scaffold behavior. |",
        "| `visuals/rcc_nexus/` | Stores NCI and RCC-N coverage/trend charts. | Helps humans inspect navigation health quickly. |",
        "",
        "## Structure Reading Route",
        "",
        "For humans:",
        "",
        "1. Read the Human Director Box.",
        "2. Read Project Structure Director.",
        "3. Open `reports/rcc_nexus/latest_rcc_nexus_benchmark.md`.",
        "4. Open `docs/context/rcc_nexus_index.json`.",
        "",
        "For AI agents:",
        "",
        "1. Read `AGENTS.md`.",
        "2. Read `README.md`.",
        "3. Read `docs/context/repository_context_index.json`.",
        "4. Read `docs/context/rcc_nexus_index.json`.",
        "5. Read `rcc/nexus/route_map.json`.",
        "6. Read the target folder README.",
        "7. Inspect source/tests/evidence before patching.",
        "8. Run declared validation.",
        "",
        "Structure boundary: project structure improves navigation. It does not prove correctness, security, patch safety, AI understanding, benchmark validity, production readiness, sentience, consciousness, or human memory.",
    ]

def update_readme() -> None:
    text = read("README.md")
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\ufeff", "")

    text = insert_after_title_if_missing(text)
    text = replace_between(text, "## Project Structure", "## Evidence Artifacts", project_structure_director())

    # Ensure GitHub screenshot area remains readable by adding a compact subsection before evidence artifacts.
    if "## Evidence Artifacts" not in text:
        text = text.rstrip() + "\n\n## Evidence Artifacts\n\nEvidence artifacts are generated under `runs/`, `evidence_packages/`, `ledgers/`, `logs/`, `reports/rcc_nexus/`, and `visuals/rcc_nexus/`.\n"

    write("README.md", text)

def write_repo_description_doc() -> None:
    lines = [
        "# AERMA-Memory Repository Description",
        "",
        DESCRIPTION,
        "",
        "## Public Summary",
        "",
        "AERMA-Memory is a governed agentic episodic memory workbench with two coupled surfaces:",
        "",
        "1. Runtime evidence: source-bound recall, fallback, abstention, boundary separation, baseline comparison, regression guard, and evidence packages.",
        "2. Repository navigation: RCC/RCC-N context indexes, Human Director Box, route maps, Echo Location records, Nexus reports, charts, and Markdown integrity checks.",
        "",
        "## Suggested GitHub About Description",
        "",
        DESCRIPTION,
        "",
        "## Suggested Topics",
        "",
    ]

    for topic in TOPICS:
        lines.append(f"- {topic}")

    lines += [
        "",
        "## Non-Claim Boundary",
        "",
        "This repository does not prove sentience, consciousness, human memory, biological memory, clinical memory, autonomous self-improvement, production readiness, security, patch safety, or universal AI mechanism. RCC-N improves navigation and context integrity; it does not prove code correctness.",
    ]

    write("docs/context/repo_description.md", lines)

def update_context_index() -> None:
    path = "docs/context/repository_context_index.json"
    data = load_json(path) if (root / path).exists() else {}

    data.setdefault("repository", {})
    data["repository"]["description"] = DESCRIPTION
    data["repository"]["suggested_topics"] = TOPICS
    data["repository"]["project_structure_director"] = "README.md#project-structure-director"
    data["repository"]["repo_description_doc"] = "docs/context/repo_description.md"
    data["repository"]["last_structure_director_update"] = datetime.now(timezone.utc).isoformat()

    data.setdefault("validation", {})
    data["validation"]["remote_raw_integrity"] = [
        "python scripts/rcc/verify_remote_raw_integrity.py"
    ]

    save_json(path, data)

def write_remote_verifier() -> None:
    lines = [
        "from __future__ import annotations",
        "",
        "import json",
        "import urllib.request",
        "from datetime import datetime, timezone",
        "from pathlib import Path",
        "",
        "ROOT = Path('.').resolve()",
        "REPO = 'jacksonjp0311-gif/AERMA-Memory'",
        "BRANCH = 'main'",
        "BASE = f'https://raw.githubusercontent.com/{REPO}/{BRANCH}'",
        "",
        "TARGETS = [",
        "    {",
        "        'name': 'README',",
        "        'path': 'README.md',",
        "        'min_lines': 220,",
        "        'required': [",
        "            'Repository Description',",
        "            'Project Structure Director',",
        "            'PART II - RCC Nexus README',",
        "            'PART III - AI Agent README',",
        "            'reports/rcc_nexus/latest_rcc_nexus_benchmark.md',",
        "            'visuals/rcc_nexus/nci_components.svg',",
        "        ],",
        "    },",
        "    {",
        "        'name': 'Repo description doc',",
        "        'path': 'docs/context/repo_description.md',",
        "        'min_lines': 20,",
        "        'required': ['Suggested GitHub About Description', 'Suggested Topics', 'Non-Claim Boundary'],",
        "    },",
        "    {",
        "        'name': 'RCC-N benchmark report',",
        "        'path': 'reports/rcc_nexus/latest_rcc_nexus_benchmark.md',",
        "        'min_lines': 20,",
        "        'required': ['RCC-N Benchmark Report', 'Status: pass', 'Computed NCI: 0.96', 'readme_format_health'],",
        "    },",
        "    {",
        "        'name': 'NCI chart',",
        "        'path': 'visuals/rcc_nexus/nci_components.svg',",
        "        'min_lines': 5,",
        "        'required': ['<svg', 'RCC-N NCI Components'],",
        "    },",
        "]",
        "",
        "def fetch_text(path: str) -> str:",
        "    url = f'{BASE}/{path}?cacheBust={datetime.now(timezone.utc).timestamp()}'",
        "    with urllib.request.urlopen(url, timeout=30) as response:",
        "        return response.read().decode('utf-8', errors='replace')",
        "",
        "def check_target(target: dict) -> dict:",
        "    try:",
        "        text = fetch_text(target['path'])",
        "    except Exception as exc:",
        "        return {",
        "            'name': target['name'],",
        "            'path': target['path'],",
        "            'status': 'fail',",
        "            'line_count': 0,",
        "            'max_line_length': 0,",
        "            'missing': ['fetch_failed'],",
        "            'error': str(exc),",
        "        }",
        "",
        "    lines = text.splitlines()",
        "    missing = [item for item in target['required'] if item not in text]",
        "",
        "    if len(lines) < int(target['min_lines']):",
        "        missing.append('line_count_below_minimum')",
        "",
        "    if any(len(line) > 1200 for line in lines):",
        "        missing.append('very_long_line_over_1200')",
        "",
        "    if '\\x07' in text:",
        "        missing.append('control_char_bell')",
        "",
        "    return {",
        "        'name': target['name'],",
        "        'path': target['path'],",
        "        'status': 'pass' if not missing else 'warn',",
        "        'line_count': len(lines),",
        "        'max_line_length': max((len(line) for line in lines), default=0),",
        "        'missing': missing,",
        "    }",
        "",
        "def write_reports(payload: dict) -> None:",
        "    out = ROOT / 'reports' / 'rcc_nexus'",
        "    out.mkdir(parents=True, exist_ok=True)",
        "    (out / 'latest_remote_raw_integrity_report.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\\n', encoding='utf-8')",
        "",
        "    md = [",
        "        '# Remote Raw Integrity Report',",
        "        '',",
        "        f\"Timestamp: {payload['timestamp']}\",",
        "        '',",
        "        f\"Status: {payload['status']}\",",
        "        '',",
        "        '## Targets',",
        "        '',",
        "        '| Target | Status | Lines | Max line length | Findings |',",
        "        '|---|---|---:|---:|---|',",
        "    ]",
        "",
        "    for item in payload['targets']:",
        "        md.append(f\"| {item['name']} | {item['status']} | {item['line_count']} | {item['max_line_length']} | {', '.join(item['missing'])} |\")",
        "",
        "    md += [",
        "        '',",
        "        '## Boundary',",
        "        '',",
        "        'Remote raw integrity verifies public parseability after push. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.',",
        "    ]",
        "",
        "    (out / 'latest_remote_raw_integrity_report.md').write_text('\\n'.join(md) + '\\n', encoding='utf-8')",
        "",
        "def main() -> int:",
        "    results = [check_target(target) for target in TARGETS]",
        "    status = 'pass'",
        "    if any(item['status'] == 'fail' for item in results):",
        "        status = 'fail'",
        "    elif any(item['status'] == 'warn' for item in results):",
        "        status = 'warn'",
        "",
        "    payload = {",
        "        'schema': 'AERMA-remote-raw-integrity-v1',",
        "        'timestamp': datetime.now(timezone.utc).isoformat(),",
        "        'repo': REPO,",
        "        'branch': BRANCH,",
        "        'status': status,",
        "        'targets': results,",
        "        'claim_boundary': 'Remote raw integrity verifies public parseability after push; it does not prove runtime correctness.',",
        "    }",
        "",
        "    write_reports(payload)",
        "    print(json.dumps(payload, indent=2, sort_keys=True))",
        "    return 0 if status in {'pass', 'warn'} else 1",
        "",
        "if __name__ == '__main__':",
        "    raise SystemExit(main())",
    ]

    write("scripts/rcc/verify_remote_raw_integrity.py", lines)

def update_reports_readme() -> None:
    path = "reports/rcc_nexus/README.md"
    text = read(path)
    addition = [
        "",
        "## Remote Raw Integrity",
        "",
        "Remote raw integrity checks verify that public GitHub raw files remain parseable after push.",
        "",
        "Run:",
        "",
        "    python scripts/rcc/verify_remote_raw_integrity.py",
        "",
        "Outputs:",
        "",
        "- `latest_remote_raw_integrity_report.json`",
        "- `latest_remote_raw_integrity_report.md`",
        "",
        "Boundary: remote raw integrity checks public readability and parseability only.",
    ]

    if "## Remote Raw Integrity" not in text:
        text = text.rstrip() + "\n\n" + "\n".join(addition).strip() + "\n"
        write(path, text)

update_readme()
write_repo_description_doc()
update_context_index()
write_remote_verifier()
update_reports_readme()

print("[OK] Repo description, project structure director, and remote verifier added.")