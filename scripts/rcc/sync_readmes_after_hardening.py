from pathlib import Path
import json

root = Path.cwd()

def write(path: str, text: str):
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip() + "\n", encoding="utf-8")
    print(f"[WRITE] {path}")

def read(path: str) -> str:
    p = root / path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8-sig")

def replace_or_append(path: str, marker: str, block: str):
    text = read(path)
    if marker in text:
        start = text.index(marker)
        text = text[:start].rstrip() + "\n\n" + block.strip() + "\n"
    else:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
    write(path, text)

def mini(title, purpose, spec, hooks, artifacts, theory, invariants, example):
    return f"""# {title}

<!-- RCC-MINI-README:START -->

## Purpose

{purpose}

## S - Formal specification

{spec}

## H - Hooks and integration edges

{hooks}

## A - Artifacts

{artifacts}

## T - Theory or method basis

{theory}

## I - Invariants

{invariants}

## E - Example

{example}

<!-- RCC-MINI-README:END -->
"""

# ------------------------------------------------------------
# Root README sync
# ------------------------------------------------------------
root_readme = read("README.md")

# Normalize current status language.
root_readme = root_readme.replace(
    "RCC context layer.",
    "RCC context layer,\n- v0.1.1 task-family-aware scoring,\n- per-task attribution records,\n- regression guard baseline."
)

hardening_block = """
## v0.1.1 Hardening Layer

The v0.1.1 hardening layer is now active.

Current local validation:

    pytest -q

Expected result:

    15 passed

Current local controlled-suite result:

    suite_score: 1.0
    classification: AERMA-B
    source_attribution_accuracy: 1.0
    fallback_correctness: 1.0
    abstention_correctness: 1.0
    boundary_separation_score: 1.0
    false_memory_frequency: 0.0
    regression_frequency: 0.0

New hardening artifacts:

- `runs/suite_*/attribution_records.json`
- `runs/suite_*/regression_guard.json`
- `logs/phase2/attribution/latest_aerma_attribution.json`
- `logs/phase2/regression_guard/latest_aerma_regression_guard.json`
- `scripts/run_aerma_regression_guard.py`
- `tests/test_hardened_scoring.py`
- `tests/test_hardened_suite_outputs.py`

Run the regression guard viewer:

    python scripts/run_aerma_regression_guard.py

### Hardening Boundary

The `suite_score: 1.0` result applies only to the current small controlled task suite. It is local scaffold evidence, not broad validation, not production readiness, and not evidence of human memory, sentience, consciousness, biological memory, clinical memory, autonomous self-improvement, or universal AI mechanism.

Next evidence expansion should add harder distractors, multiple queries per task, adversarial ambiguity, source collision, stale-memory conflict, and baseline delta reports.
"""

replace_or_append("README.md", "## v0.1.1 Hardening Layer", hardening_block)

# ------------------------------------------------------------
# RCC validation surface
# ------------------------------------------------------------
write("docs/context/validation_surface.md", r"""
# AERMA-Memory RCC Validation Surface

<!-- RCC-VALIDATION-SURFACE:START -->

## Install

    python -m pip install -e ".[dev]"

## Test

    pytest -q

Expected current result:

    15 passed

## Suite execution

    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

Alternative console command:

    aerma run-suite --suite ".\tasks\suite_v1_2.json"

## Regression guard viewer

    python scripts/run_aerma_regression_guard.py

## Expected artifacts

- `runs/suite_*/aggregate_metrics.json`
- `runs/suite_*/suite_classification.json`
- `runs/suite_*/attribution_records.json`
- `runs/suite_*/regression_guard.json`
- `evidence_packages/*_evidence_package.json`
- `ledgers/aerma_suite_ledger.jsonl`
- `logs/phase2/attribution/latest_aerma_attribution.json`
- `logs/phase2/regression_guard/latest_aerma_regression_guard.json`

## Current local controlled-suite result

- `suite_score`: 1.0
- `classification`: AERMA-B
- `source_attribution_accuracy`: 1.0
- `fallback_correctness`: 1.0
- `abstention_correctness`: 1.0
- `boundary_separation_score`: 1.0
- `false_memory_frequency`: 0.0
- `regression_frequency`: 0.0

## Runtime claim boundary

Passing the validation surface proves that the local reference scaffold installs, imports, tests, and runs the declared controlled suite. It does not prove production readiness, human memory equivalence, autonomous self-improvement, sentience, consciousness, biological memory, or universal agent-memory validity.

## Known current evidence limitation

The current `suite_score: 1.0` is produced on a small controlled task suite. Stronger evidence requires harder distractors, multiple queries per task, adversarial ambiguity, source collision, stale-memory conflict, and baseline delta reports.

<!-- RCC-VALIDATION-SURFACE:END -->
""")

# ------------------------------------------------------------
# RCC module index sync
# ------------------------------------------------------------
write("docs/context/module_index.md", r"""
# AERMA-Memory RCC Module Index

<!-- RCC-CONTEXT:START -->

## Declared RCC profile

AERMA-Memory currently declares `RCC-Core`.

## Major modules

| Module | Path | Role | Runtime claim sensitivity |
|---|---|---|---|
| Core memory primitives | `src/aerma/core` | Episode schema, memory store, metric manifest, retrieval | High |
| Drift geometry | `src/aerma/drift` | Retrieval drift and Ω calculation | High |
| Gate and fallback | `src/aerma/gate` | ActionGate and SourceFallback | High |
| Benchmarks | `src/aerma/benchmarks` | BenchmarkRunner, SuiteRunner, baselines, task-aware scoring, classifier | Very high |
| Evidence | `src/aerma/evidence` | RuntimeLedger and EvidencePackageCompiler | Very high |
| Agent stubs | `src/aerma/agent` | RecursiveExecutorStub and ReflectionEvaluatorStub | Medium |
| CLI | `src/aerma/cli` | Human command surface | High |
| Tasks | `tasks` | Benchmark task definitions | Very high |
| Configs | `configs` | Runtime, baseline, metric, and suite config | High |
| Logs | `logs` | Attribution and regression guard outputs | High |
| Runs | `runs` | Generated suite outputs including attribution and guard files | High |
| Ledgers | `ledgers` | Persistent run records | High |
| Evidence packages | `evidence_packages` | Suite evidence artifacts | High |
| Memory | `memory` | Promoted invariants and rejected overclaims | Medium |
| RCC scripts | `scripts/rcc` | RCC generation/checking and hardening scripts | Medium |

## Source-fidelity status

These RCC records are derived from the current scaffold and latest local run results. They are not independent audit results.

## Primary validation commands

    pytest -q
    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"
    aerma run-suite --suite ".\tasks\suite_v1_2.json"
    python scripts/run_aerma_regression_guard.py

## Current validation snapshot

    15 passed
    suite_score: 1.0
    classification: AERMA-B

## Boundary

The validation snapshot is local controlled-suite evidence only.

<!-- RCC-CONTEXT:END -->
""")

# ------------------------------------------------------------
# RCC context index update
# ------------------------------------------------------------
idx_path = root / "docs/context/repository_context_index.json"
idx = json.loads(idx_path.read_text(encoding="utf-8-sig"))

idx["repository"]["last_verified"] = "2026-05-13"
idx["repository"]["current_runtime_layer"] = "AERMA-Memory-v0.1.1-hardening"

idx["validation"]["test"] = ["pytest -q"]
idx["validation"]["suite"] = [
    "python -m aerma.cli.main run-suite --suite \".\\tasks\\suite_v1_2.json\"",
    "aerma run-suite --suite \".\\tasks\\suite_v1_2.json\""
]
idx["validation"]["regression_guard"] = [
    "python scripts/run_aerma_regression_guard.py"
]
idx["validation"]["expected_artifacts"] = [
    "runs/suite_*/aggregate_metrics.json",
    "runs/suite_*/suite_classification.json",
    "runs/suite_*/attribution_records.json",
    "runs/suite_*/regression_guard.json",
    "evidence_packages/*_evidence_package.json",
    "ledgers/aerma_suite_ledger.jsonl",
    "logs/phase2/attribution/latest_aerma_attribution.json",
    "logs/phase2/regression_guard/latest_aerma_regression_guard.json"
]
idx["latest_validation_snapshot"] = {
    "test_result": "15 passed",
    "suite_score": 1.0,
    "classification": "AERMA-B",
    "source_attribution_accuracy": 1.0,
    "fallback_correctness": 1.0,
    "abstention_correctness": 1.0,
    "boundary_separation_score": 1.0,
    "false_memory_frequency": 0.0,
    "regression_frequency": 0.0,
    "boundary": "local controlled-suite evidence only"
}
idx["drift_linter"]["status"] = "manual_review_required_after_v0_1_1_hardening"
idx["repository_context_integrity"]["validation_surface_completeness"] = 0.90
idx["repository_context_integrity"]["hook_topology_completeness"] = 0.70
idx["repository_context_integrity"]["update_rule_compliance"] = 0.80
idx["repository_context_integrity"]["repository_context_integrity_index"] = 0.80

write("docs/context/repository_context_index.json", json.dumps(idx, indent=2, sort_keys=True))

# ------------------------------------------------------------
# Key mini README refreshes
# ------------------------------------------------------------
write("src/aerma/benchmarks/README.md", mini(
"src/aerma/benchmarks",
"Benchmark runners, baselines, task-family-aware scoring, attribution records, regression guard generation, and AERMA claim classification.",
"This folder runs task JSON files through AERMA runtime logic and declared baselines, aggregates task-aware metrics, writes attribution records, emits regression guard artifacts, and assigns bounded AERMA classifications.",
"- `cli/main.py` calls `BenchmarkRunner` and `SuiteRunner`.\n- `SuiteRunner` reads `tasks/suite_v1_2.json`.\n- `SuiteRunner` writes run outputs, attribution records, regression guard files, and evidence packages.\n- `baselines.py` provides explicit baseline classes.\n- `scoring.py` now treats non-applicable metrics as `None` so task families are scored fairly.",
"- `benchmark_runner.py`.\n- `suite_runner.py`.\n- `baselines.py`.\n- `scoring.py`.\n- `classifier.py`.",
"AERMA must be tested where it should answer and where it should fallback, preserve boundaries, or abstain. Baselines must run on the same data and metrics. Task-aware scoring prevents abstention and fallback tasks from unfairly lowering source-recall metrics.",
"- Do not select metrics after results.\n- Do not compare baselines on different task data.\n- Do not overpromote controlled-suite evidence as broad validation.\n- Benchmark claims require evidence packages.\n- Keep classification downgrade-preserving.",
"Run full suite:\n\n    python -m aerma.cli.main run-suite --suite \".\\tasks\\suite_v1_2.json\""
))

write("logs/README.md", mini(
"logs",
"Runtime and phase logs for diagnostics, attribution, regression guards, accepted deltas, and rejected deltas.",
"This folder preserves operational logs and phase artifacts. v0.1.1 now writes latest attribution and regression guard outputs under `logs/phase2`.",
"- `SuiteRunner` writes `logs/phase2/attribution/latest_aerma_attribution.json`.\n- `SuiteRunner` writes `logs/phase2/regression_guard/latest_aerma_regression_guard.json`.\n- Rejected memory-policy deltas should write under `logs/phase2/rejected_deltas` in future passes.",
"- `phase1/`.\n- `phase2/attribution/latest_aerma_attribution.json`.\n- `phase2/regression_guard/latest_aerma_regression_guard.json`.\n- `runtime/`.",
"Failure learning is part of evidence governance. Rejected deltas should be preserved instead of deleted. Attribution explains runtime choice; it does not prove correctness.",
"- Do not delete rejected-delta evidence to clean history.\n- Do not treat logs as evidence unless linked to commands and configs.\n- Claim-affecting logs must preserve task and run IDs.\n- Regression guard is a local baseline lock, not independent validation.",
"Inspect latest hardening logs:\n\n    Get-ChildItem .\\logs\\phase2 -Recurse"
))

write("runs/README.md", mini(
"runs",
"Generated suite run outputs.",
"This folder stores per-suite run directories created by `SuiteRunner`.",
"- `SuiteRunner` writes `runs/suite_*`.\n- Each hardened run includes aggregate metrics, suite classification, attribution records, regression guard, and per-task outputs.",
"- `suite_*/aggregate_metrics.json`.\n- `suite_*/suite_classification.json`.\n- `suite_*/attribution_records.json`.\n- `suite_*/regression_guard.json`.\n- `suite_*/per_task/*/repeat_*/task_result.json`.",
"Run artifacts are local evidence records. They support implementation evidence only within the declared benchmark boundary.",
"- Do not manually edit run artifacts for public claims.\n- Preserve run IDs in evidence packages.\n- Generated run outputs should remain reproducible from suite commands.\n- Local `suite_score: 1.0` is controlled-suite evidence only.",
"List runs:\n\n    Get-ChildItem .\\runs"
))

write("tests/README.md", mini(
"tests",
"Pytest validation surface for the AERMA-Memory reference scaffold and v0.1.1 hardening layer.",
"This folder tests episode schema, memory store, metric manifest, drift geometry, action gate, fallback, baseline classes, benchmark runner, suite runner, evidence package, agent stubs, hardened scoring, and hardened suite outputs.",
"- Tests import `aerma` package modules.\n- Validation surface requires `pytest -q`.\n- Runtime changes should add or update tests before claim updates.",
"- `test_episode_schema.py`.\n- `test_memory_store.py`.\n- `test_metric_manifest.py`.\n- `test_drift_geometry.py`.\n- `test_action_gate.py`.\n- `test_source_fallback.py`.\n- `test_baseline_classes.py`.\n- `test_benchmark_runner.py`.\n- `test_suite_runner.py`.\n- `test_evidence_package.py`.\n- `test_recursive_executor_stub.py`.\n- `test_reflection_evaluator_stub.py`.\n- `test_hardened_scoring.py`.\n- `test_hardened_suite_outputs.py`.",
"Tests are the first validation gate. Passing tests is implementation evidence, not broad validation.",
"- Keep tests runnable from repo root.\n- Add tests for scoring or behavior changes.\n- Do not weaken tests to preserve claims.\n- Current expected result is `15 passed`.",
"Run all tests:\n\n    pytest -q"
))

print("[SYNC] README/RCC hardening sync complete.")