from pathlib import Path
import json
import subprocess
import sys

root = Path.cwd()

def write(path: str, text: str):
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip() + "\n", encoding="utf-8")
    print(f"[WRITE] {path}")

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
# Root README
# ------------------------------------------------------------
write("README.md", r"""
# AERMA-Memory

> AERMA-Memory is a local-first reference implementation and benchmark workbench for governed agentic episodic memory. It tests source-bound recall, ambiguity fallback, boundary separation, abstention, baseline comparison, repeat-run evidence, and audit-ready evidence packages.

AERMA-Memory is not a claim of sentience, consciousness, human episodic memory, biological memory, clinical memory, autonomous self-improvement, or a universal AI mechanism.

It is best understood as a governed memory workbench:

    source-bound episodes
    -> cue-dependent retrieval
    -> drift geometry
    -> action gate
    -> fallback / abstention
    -> baseline comparison
    -> repeat-run benchmark
    -> evidence package
    -> accepted / rejected memory-policy ledger

## Current Status

AERMA-Memory currently has:

- importable Python package boundary,
- deterministic local benchmark tasks,
- source recall task,
- ambiguity fallback task,
- boundary separation task,
- abstention task,
- baseline class scaffold,
- repeat-run suite runner,
- runtime ledgers,
- suite evidence package emission,
- RecursiveExecutor stub,
- ReflectionEvaluator stub,
- RCC context layer.

## Current Commands

Install editable package:

    python -m pip install -e ".[dev]"

Run tests:

    pytest -q

Run suite:

    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

Run console command:

    aerma run-suite --suite ".\tasks\suite_v1_2.json"

## Evidence Boundary

The current implementation is an early reference scaffold. Passing tests and producing a suite evidence package proves that the local package executes under declared tasks. It does not prove production readiness, broad agent-memory validity, sentience, consciousness, human-memory equivalence, or autonomous self-improvement.

The current classification should be treated as implementation evidence only. Stronger claims require hardened scoring, stronger negative controls, attribution logs, baseline fairness review, repeated evidence, and downgrade-preserving classification.

## Project Structure

    AERMA-Memory/
    ├── src/aerma/              # Importable package
    ├── scripts/                # Human-facing helper scripts
    ├── tasks/                  # Benchmark task JSON files
    ├── configs/                # Runtime, metric, baseline, and suite configs
    ├── logs/                   # Runtime and phase logs
    ├── runs/                   # Generated suite run outputs
    ├── evidence_packages/      # Generated evidence packages
    ├── ledgers/                # Runtime, suite, tool trace, and decision ledgers
    ├── docs/                   # Theory, architecture, benchmark, evidence, RCC context
    ├── memory/                 # Promoted invariants and rejected overclaims
    └── tests/                  # Pytest suite

## RCC / Repository Context Canon

AERMA-Memory declares an RCC-Core adoption profile.

RCC here is a repository-context layer. It does not change runtime behavior. It makes the repo easier to navigate, audit, extend, and hand off to humans or AI agents by exposing purpose, hooks, artifacts, validation surfaces, claim boundaries, evidence links, and drift obligations.

RCC artifacts:

- `docs/context/repository_context_index.json`
- `docs/context/module_index.md`
- `docs/context/validation_surface.md`
- `docs/context/context_budget.md`
- `docs/context/drift_report.md`
- `docs/context/llm_reconstruction_prompt.md`
- mini READMEs across major folders

## RCC Claim Boundary

RCC process documentation does not prove code correctness. Generated or inserted RCC files are repository context records and must be kept synchronized with source, tests, command surfaces, runtime outputs, and evidence packages.

## Non-Claim Locks

AERMA-Memory is:

- not sentience,
- not consciousness,
- not human memory,
- not biological memory,
- not clinical memory,
- not autonomous self-improvement,
- not a universal AI mechanism,
- not production-ready agent memory,
- not proof that coherence equals truth.

## Evidence Artifacts

Suite runs produce outputs under:

    runs/suite_*/

Suite evidence packages are written under:

    evidence_packages/

Suite ledgers are written under:

    ledgers/aerma_suite_ledger.jsonl

## Next Hardening Targets

- Harden scoring logic.
- Make abstention and fallback scoring task-family aware.
- Add per-query attribution logs.
- Add stronger baseline comparison.
- Add regression guard.
- Prevent AERMA-B classification unless stricter thresholds are satisfied.
- Add RCC drift checker.
""")

# ------------------------------------------------------------
# RCC context files
# ------------------------------------------------------------
write("docs/context/repository_context_index.json", json.dumps({
    "schema": "RCC-v1.2-repository-context-index",
    "repository": {
        "name": "AERMA-Memory",
        "root": ".",
        "declared_profile": "RCC-Core",
        "profile_claim_verified": False,
        "last_verified": "2026-05-13",
        "verification_mode": "manual"
    },
    "context_budget_policy": {
        "default_budget": "B2",
        "patch_budget": "B3",
        "integration_debug_budget": "B4",
        "deep_audit_budget": "B5",
        "lowest_sufficient_context_rule": True,
        "b5_escalation_allowed": True
    },
    "rci_weight_policy": {
        "profile": "default",
        "weights": {
            "source_fidelity": 0.20,
            "validation_surface": 0.20,
            "hook_topology": 0.20,
            "context_budget": 0.10,
            "drift_control": 0.20,
            "update_compliance": 0.10
        },
        "declared": True,
        "reason": "Default RCC v1.2 weighting for an early RCC-Core implementation."
    },
    "modules": [
        {"module_id": "src.aerma.core", "path": "src/aerma/core", "rcc_record": "src/aerma/core/README.md", "status": "implemented", "source_fidelity": "derived_from_current_scaffold", "minimum_budget": "B2", "source_budget": "B3", "drift_status": "manual_review_required"},
        {"module_id": "src.aerma.benchmarks", "path": "src/aerma/benchmarks", "rcc_record": "src/aerma/benchmarks/README.md", "status": "implemented", "source_fidelity": "derived_from_current_scaffold", "minimum_budget": "B2", "source_budget": "B3", "drift_status": "manual_review_required"},
        {"module_id": "src.aerma.evidence", "path": "src/aerma/evidence", "rcc_record": "src/aerma/evidence/README.md", "status": "implemented", "source_fidelity": "derived_from_current_scaffold", "minimum_budget": "B2", "source_budget": "B3", "drift_status": "manual_review_required"},
        {"module_id": "tasks", "path": "tasks", "rcc_record": "tasks/README.md", "status": "implemented", "source_fidelity": "derived_from_current_scaffold", "minimum_budget": "B2", "source_budget": "B3", "drift_status": "manual_review_required"}
    ],
    "hooks": [
        {"source": "tasks/suite_v1_2.json", "target": "src/aerma/benchmarks/suite_runner.py", "hook_type": "runtime_input", "evidence": "SuiteRunner loads suite task references and executes BenchmarkRunner.", "fidelity": "derived", "weight": 0.9},
        {"source": "src/aerma/benchmarks/benchmark_runner.py", "target": "src/aerma/core", "hook_type": "imports", "evidence": "BenchmarkRunner imports AgentEpisode, AgentMemoryStore, MetricManifest, and RetrievalEngine.", "fidelity": "derived", "weight": 0.9},
        {"source": "src/aerma/benchmarks/suite_runner.py", "target": "src/aerma/evidence", "hook_type": "writes", "evidence": "SuiteRunner writes ledgers, run outputs, aggregate metrics, classifications, and evidence packages.", "fidelity": "derived", "weight": 0.9}
    ],
    "validation": {
        "install": ["python -m pip install -e \".[dev]\""],
        "test": ["pytest -q"],
        "suite": [
            "python -m aerma.cli.main run-suite --suite \".\\tasks\\suite_v1_2.json\"",
            "aerma run-suite --suite \".\\tasks\\suite_v1_2.json\""
        ],
        "expected_artifacts": [
            "runs/suite_*/aggregate_metrics.json",
            "runs/suite_*/suite_classification.json",
            "evidence_packages/*_evidence_package.json",
            "ledgers/aerma_suite_ledger.jsonl"
        ]
    },
    "evidence_packages": [
        {"name": "AERMA suite evidence package", "path": "evidence_packages/*_evidence_package.json", "required_for_claims": True, "status": "generated_by_suite_runs"}
    ],
    "drift_linter": {"enabled": False, "last_run": None, "status": "manual_review_required", "failures": []},
    "repository_context_integrity": {
        "source_fidelity_completeness": 0.70,
        "validation_surface_completeness": 0.80,
        "hook_topology_completeness": 0.60,
        "context_budget_completeness": 1.00,
        "rcc_drift_score": 0.30,
        "update_rule_compliance": 0.70,
        "repository_context_integrity_index": 0.72
    },
    "non_claim_locks": [
        "context_reconstruction_is_not_correctness_proof",
        "generated_or_inserted_rcc_is_not_verified_context",
        "benchmark_claims_require_evidence_packages",
        "suite_execution_is_not_production_readiness",
        "agent_memory_is_not_human_memory"
    ]
}, indent=2))

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
| Benchmarks | `src/aerma/benchmarks` | BenchmarkRunner, SuiteRunner, baselines, scoring, classifier | Very high |
| Evidence | `src/aerma/evidence` | RuntimeLedger and EvidencePackageCompiler | Very high |
| Agent stubs | `src/aerma/agent` | RecursiveExecutorStub and ReflectionEvaluatorStub | Medium |
| CLI | `src/aerma/cli` | Human command surface | High |
| Tasks | `tasks` | Benchmark task definitions | Very high |
| Configs | `configs` | Runtime, baseline, metric, and suite config | High |
| Ledgers | `ledgers` | Persistent run records | High |
| Evidence packages | `evidence_packages` | Suite evidence artifacts | High |
| Memory | `memory` | Promoted invariants and rejected overclaims | Medium |

## Source-fidelity status

These RCC records are derived from the current scaffold and latest local run results. They are not independent audit results.

## Primary validation commands

    pytest -q
    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"
    aerma run-suite --suite ".\tasks\suite_v1_2.json"

<!-- RCC-CONTEXT:END -->
""")

write("docs/context/validation_surface.md", r"""
# AERMA-Memory RCC Validation Surface

<!-- RCC-VALIDATION-SURFACE:START -->

## Install

    python -m pip install -e ".[dev]"

## Test

    pytest -q

Expected current result:

    12 passed

## Suite execution

    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

Alternative console command:

    aerma run-suite --suite ".\tasks\suite_v1_2.json"

## Expected artifacts

- `runs/suite_*/aggregate_metrics.json`
- `runs/suite_*/suite_classification.json`
- `evidence_packages/*_evidence_package.json`
- `ledgers/aerma_suite_ledger.jsonl`

## Runtime claim boundary

Passing the validation surface proves that the local reference scaffold installs, imports, tests, and runs the declared suite. It does not prove production readiness, human memory equivalence, autonomous self-improvement, sentience, consciousness, biological memory, or universal agent-memory validity.

## Known current evidence limitation

The current suite score and classification are early scaffold outputs. The next hardening pass should tighten scoring and prevent strong classification unless fallback, abstention, source attribution, and baseline comparison meet stricter thresholds.

<!-- RCC-VALIDATION-SURFACE:END -->
""")

write("docs/context/context_budget.md", r"""
# AERMA-Memory RCC Context Budget

<!-- RCC-CONTEXT-BUDGET:START -->

## Budget ladder

| Budget | Use |
|---|---|
| B0 | Root README only |
| B1 | Root README + repository context index |
| B2 | B1 + affected folder mini README |
| B3 | B2 + affected source files and tests |
| B4 | B3 + run artifacts, ledgers, configs, and evidence packages |
| B5 | Full repository dump or broad source ingestion |

## Default policy

- Orientation: B1 or B2.
- Small script or documentation patch: B2.
- Runtime behavior patch: B3.
- Benchmark, scoring, or evidence patch: B4.
- Cross-cutting refactor or unexplained failure: B5.

## Escalation rule

Escalate to source files when RCC records are stale, ambiguous, contradicted by tests, or insufficient for the requested patch.

<!-- RCC-CONTEXT-BUDGET:END -->
""")

write("docs/context/drift_report.md", r"""
# AERMA-Memory RCC Drift Report

<!-- RCC-DRIFT-REPORT:START -->

## Current drift status

Manual review required.

## Current known context state

- RCC has been inserted after the first successful local run.
- Mini READMEs are generated from current repository structure and intended AERMA v1.2-MVP behavior.
- RCC records are useful for orientation but should not be treated as verified audit output.
- Runtime code remains source of truth.

## Known drift surfaces

- Scoring logic is early and needs hardening.
- Current classification may be too permissive for public claims.
- Attribution logs are not yet implemented.
- Regression guard is not yet implemented.
- RCC linter is not yet implemented.
- Evidence dashboards are placeholders.

## Required update triggers

Update RCC records when:

- package structure changes,
- CLI commands change,
- task suite changes,
- scoring/classification thresholds change,
- evidence package schema changes,
- ledgers move or change format,
- new benchmark tasks are added,
- recursive/reflection stubs become real implementations,
- README claims change.

<!-- RCC-DRIFT-REPORT:END -->
""")

write("docs/context/llm_reconstruction_prompt.md", r"""
# AERMA-Memory RCC-Guided LLM Reconstruction Prompt

<!-- RCC-LLM-RECONSTRUCTION:START -->

Before patching this repository:

1. Declare task type.
2. Declare context budget.
3. Read `docs/context/repository_context_index.json`.
4. Read the affected folder README.
5. Inspect affected source files for runtime changes.
6. Preserve non-claim locks.
7. Run validation commands.
8. Update RCC records if command surfaces, artifacts, hooks, or claims change.
9. Do not claim benchmark improvement without evidence package linkage.
10. Do not treat generated RCC context as proof of code correctness.

Default validation:

    pytest -q
    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

Patch boundary:

- Documentation-only changes should not modify runtime behavior.
- Runtime changes must update tests and validation surfaces when needed.
- Benchmark/scoring changes must preserve downgrade discipline and evidence-package output.

<!-- RCC-LLM-RECONSTRUCTION:END -->
""")

# ------------------------------------------------------------
# Mini READMEs
# ------------------------------------------------------------
readmes = {
"src/README.md": mini(
"src",
"Source package root for the importable AERMA-Memory implementation.",
"This folder contains the Python package boundary. Runtime behavior should live under `src/aerma` and remain importable through editable install.",
"- `pyproject.toml` discovers packages under `src`.\n- `tests/` imports modules from this package.\n- CLI commands call into `src/aerma/cli/main.py`.",
"- `aerma/`",
"The source tree is the executable anchor. RCC documentation can describe it, but source and tests remain the validation surface.",
"- Keep package importable.\n- Do not place runtime logic outside the package without documenting the hook.\n- Runtime claims require tests and evidence outputs.",
"Install package from repo root:\n\n    python -m pip install -e \".[dev]\""
),
"src/aerma/README.md": mini(
"src/aerma",
"Main AERMA package namespace.",
"This folder defines the runtime package containing core memory primitives, drift geometry, action gating, benchmark execution, evidence compilation, agent stubs, and CLI entry points.",
"- `core/` provides memory primitives.\n- `benchmarks/` orchestrates tasks and scoring.\n- `evidence/` writes ledgers and evidence packages.\n- `cli/` exposes command surfaces.",
"- `__init__.py` with package version.\n- `core/`, `drift/`, `gate/`, `trace/`, `benchmarks/`, `evidence/`, `agent/`, `cli/`.",
"AERMA is built as a governed memory workbench: source-bound episodes flow through retrieval, drift, gate, fallback, baseline comparison, and evidence packaging.",
"- Preserve package import.\n- Do not claim human memory or sentience.\n- Keep recursive and reflection behavior stubbed until implemented and measured.\n- Runtime changes require test updates.",
"Verify import:\n\n    python -c \"import aerma; print(aerma.__version__)\""
),
"src/aerma/core/README.md": mini(
"src/aerma/core",
"Core memory objects and deterministic retrieval primitives.",
"This folder defines `AgentEpisode`, `AgentMemoryStore`, `MetricManifest`, and `RetrievalEngine`. These are the base objects used by the benchmark runner.",
"- `benchmarks/benchmark_runner.py` imports core objects.\n- `tasks/*.json` are converted into `AgentEpisode` instances.\n- `drift/` consumes retrieval scores.",
"- `episode.py` - source-bound memory episode schema.\n- `memory_store.py` - in-memory episode store.\n- `metric_manifest.py` - declared thresholds and primary metrics.\n- `retrieval_engine.py` - deterministic lexical retrieval.",
"Core memory is source-bound and cue-dependent. Retrieval is reconstructive and must remain downstream of declared task data and upstream of drift and gating.",
"- Episodes must preserve source and ledger references.\n- Fingerprints must remain deterministic.\n- MetricManifest must be declared before interpretation.\n- Retrieval score must remain dimensionless.",
"Run the source recall task:\n\n    python -m aerma.cli.main run-benchmark --task \".\\tasks\\source_recall\\source_recall_001.json\""
),
"src/aerma/reconstruction/README.md": mini(
"src/aerma/reconstruction",
"Reserved context reconstruction layer.",
"This folder is reserved for future context reconstruction logic. It currently contains only package scaffolding.",
"- Future `ContextReconstructionEngine` should sit between retrieval and drift/gating.\n- Future benchmark attribution should reference reconstruction decisions.",
"- `__init__.py`",
"Context reconstruction must remain source-bound and should not rewrite measured retrieval geometry through narrative interpretation.",
"- Do not claim reconstruction capability until implemented.\n- Do not promote reconstructed context as fact without source fallback.\n- Add tests before enabling runtime use.",
"Current placeholder check:\n\n    Get-ChildItem .\\src\\aerma\\reconstruction"
),
"src/aerma/drift/README.md": mini(
"src/aerma/drift",
"Retrieval drift and Ω stability calculation.",
"This folder computes dimensionless retrieval drift and Ω weighting from retrieval scores.",
"- `benchmarks/benchmark_runner.py` calls `DriftGeometryEngine`.\n- `gate/action_gate.py` consumes `DriftReport`.",
"- `drift_geometry.py`",
"AERMA uses ΔΦ-style drift as an instability proxy. Ω = 1 / (1 + abs(drift)) is diagnostic and should not be treated as truth.",
"- Drift must remain dimensionless.\n- Ω is diagnostic only.\n- Do not silently modify task outcomes with narrative interpretation.",
"Run tests for drift behavior:\n\n    pytest tests/test_drift_geometry.py -q"
),
"src/aerma/gate/README.md": mini(
"src/aerma/gate",
"Action gating and source fallback behavior.",
"This folder decides whether a retrieved memory can be returned, caveated, fallbacked, or abstained from based on declared thresholds and task expectations.",
"- `BenchmarkRunner` calls `ActionGate`.\n- `ActionGate` consumes `MetricManifest` and `DriftReport`.\n- `SourceFallback` emits safe fallback and abstention messages.",
"- `action_gate.py` - allow / caveat / fallback decision.\n- `source_fallback.py` - fallback and abstention messages.",
"AERMA treats ambiguity fallback and abstention as positive governance behaviors when evidence is insufficient.",
"- High-drift retrieval must not be promoted as fact.\n- Ambiguity must trigger fallback instead of forced answer.\n- Source-free answers must be rejected or caveated.",
"Run gate tests:\n\n    pytest tests/test_action_gate.py tests/test_source_fallback.py -q"
),
"src/aerma/trace/README.md": mini(
"src/aerma/trace",
"Trace records for tool-like or runtime events.",
"This folder holds lightweight trace primitives used to preserve event payloads and timestamps.",
"- Future benchmark attribution and tool-trace ledgers should use this layer.\n- `ledgers/aerma_tool_trace_ledger.jsonl` is the persistent trace target.",
"- `tool_trace_engine.py`",
"Tool execution is evidence only when logged and reproducible. Trace records preserve auditability.",
"- Do not treat unlogged tool-like behavior as evidence.\n- Trace records should remain machine-readable.\n- Runtime trace changes must update evidence documentation.",
"Future trace usage target:\n\n    python -m aerma.cli.main run-suite --suite \".\\tasks\\suite_v1_2.json\""
),
"src/aerma/benchmarks/README.md": mini(
"src/aerma/benchmarks",
"Benchmark runners, baselines, scoring, and AERMA claim classification.",
"This folder runs task JSON files through AERMA runtime logic and declared baselines, aggregates metrics, and assigns bounded AERMA classifications.",
"- `cli/main.py` calls `BenchmarkRunner` and `SuiteRunner`.\n- `SuiteRunner` reads `tasks/suite_v1_2.json`.\n- `SuiteRunner` writes run outputs and evidence packages.\n- `baselines.py` provides explicit baseline classes.",
"- `benchmark_runner.py`.\n- `suite_runner.py`.\n- `baselines.py`.\n- `scoring.py`.\n- `classifier.py`.",
"AERMA must be tested where it should answer and where it should fallback, preserve boundaries, or abstain. Baselines must run on the same data and metrics.",
"- Do not select metrics after results.\n- Do not compare baselines on different task data.\n- Do not overpromote early scaffold classifications.\n- Benchmark claims require evidence packages.",
"Run full suite:\n\n    python -m aerma.cli.main run-suite --suite \".\\tasks\\suite_v1_2.json\""
),
"src/aerma/evidence/README.md": mini(
"src/aerma/evidence",
"Runtime ledgers and evidence package compilation.",
"This folder writes machine-readable runtime ledger records and compiles suite evidence packages.",
"- `SuiteRunner` uses `RuntimeLedger`.\n- `SuiteRunner` uses `EvidencePackageCompiler`.\n- Outputs are written to `ledgers/`, `runs/`, and `evidence_packages/`.",
"- `runtime_ledger.py`.\n- `evidence_package.py`.",
"Execution without logs is not evidence. Logs without baselines are weak support. Evidence packages preserve run configuration, metrics, classification, and non-claim locks.",
"- Evidence packages must be machine-readable.\n- Runtime claims require linked run artifacts.\n- Do not treat evidence packages as proof beyond their task boundary.",
"After running suite, inspect:\n\n    Get-ChildItem .\\evidence_packages"
),
"src/aerma/agent/README.md": mini(
"src/aerma/agent",
"Bounded agentic interfaces currently implemented as stubs.",
"This folder holds `RecursiveExecutorStub` and `ReflectionEvaluatorStub`. They define future interfaces but do not execute full recursion or self-improvement.",
"- `SuiteRunner` emits stub status into suite payload.\n- Future AERMA versions may replace stubs with bounded implementations after evidence hardening.",
"- `recursive_executor_stub.py`.\n- `reflection_evaluator_stub.py`.",
"A stub may define a future interface but must not be used as evidence of recursive capability or self-improvement.",
"- Do not claim recursion is implemented.\n- Do not claim reflection-based improvement.\n- Preserve stub boundary until measured implementation exists.",
"Run stub tests:\n\n    pytest tests/test_recursive_executor_stub.py tests/test_reflection_evaluator_stub.py -q"
),
"src/aerma/cli/README.md": mini(
"src/aerma/cli",
"Command-line entry points for AERMA benchmark and suite execution.",
"This folder exposes `run-benchmark` and `run-suite` commands through module execution and the installed `aerma` console script.",
"- `pyproject.toml` maps `aerma = aerma.cli.main:main`.\n- CLI calls `BenchmarkRunner` and `SuiteRunner`.",
"- `main.py`.",
"CLI commands are validation surfaces. If command behavior changes, README and RCC validation records must be updated.",
"- Keep commands runnable from the repo root.\n- Do not hide claim-affecting behavior behind CLI defaults.\n- Suite execution must emit evidence outputs.",
"Run CLI:\n\n    aerma run-suite --suite \".\\tasks\\suite_v1_2.json\""
),
"scripts/README.md": mini(
"scripts",
"Human-facing helper scripts for benchmark execution, suite execution, evidence compilation placeholders, repository dumps, RCC checks, and future metrics dashboards.",
"This folder provides command surfaces that call into the `aerma` package. Scripts should remain runnable from the repository root and should not hide claim-affecting behavior.",
"- `run_benchmark.py` calls `BenchmarkRunner`.\n- `run_suite.py` calls `SuiteRunner`.\n- `metrics/` contains dashboard generator placeholders.\n- `repo/` contains repo dump utilities.\n- `rcc/` contains RCC context tooling placeholders.",
"- `run_benchmark.py`.\n- `run_suite.py`.\n- `metrics/generate_aerma_process_dashboard.py`.\n- `metrics/generate_aerma_quality_dashboard.py`.\n- `repo/repo_dump_light.ps1`.\n- `rcc/check_rcc_drift.ps1`.",
"Scripts are operational entry points. Diagnostic and benchmark scripts analyze evidence artifacts and should not alter runtime behavior unless explicitly declared.",
"- Keep commands runnable from repo root.\n- Do not change script behavior without updating README command surfaces.\n- Scripts affecting public claims must preserve validation and evidence boundaries.",
"Run suite helper script:\n\n    python scripts/run_suite.py --suite \".\\tasks\\suite_v1_2.json\""
),
"tasks/README.md": mini(
"tasks",
"Benchmark task definitions for source recall, ambiguity fallback, boundary separation, and abstention.",
"This folder contains JSON benchmark tasks and the suite manifest consumed by `SuiteRunner`.",
"- `tasks/suite_v1_2.json` lists task files.\n- `BenchmarkRunner` loads each task and converts episodes into `AgentEpisode` objects.\n- `scoring.py` reads expected task behavior and expected episode fields.",
"- `suite_v1_2.json`.\n- `source_recall/source_recall_001.json`.\n- `source_recall/source_recall_ambiguous_001.json`.\n- `boundary_separation/boundary_separation_001.json`.\n- `abstain/abstain_insufficient_evidence_001.json`.",
"AERMA must be tested not only where it should answer, but also where it should fallback, preserve boundaries, and abstain.",
"- Task JSON must remain valid UTF-8 without BOM or readable via utf-8-sig.\n- Expected behavior must be declared before scoring.\n- Negative controls must not be removed to inflate results.",
"Run suite manifest:\n\n    python -m aerma.cli.main run-suite --suite \".\\tasks\\suite_v1_2.json\""
),
"configs/README.md": mini(
"configs",
"Declared runtime, metric, baseline, and suite configuration.",
"This folder stores configuration surfaces used to document runtime assumptions, metric thresholds, baseline fairness, and suite policy.",
"- `metric_manifest.json` mirrors default metric thresholds.\n- `baseline_config.json` declares baseline fairness policy.\n- `runtime_config.json` declares deterministic local scaffold mode.\n- `suite_config.json` declares suite policy.",
"- `runtime_config.json`.\n- `metric_manifest.json`.\n- `baseline_config.json`.\n- `suite_config.json`.",
"Metrics selected after results weaken classification. Configs declare intended evidence boundaries before interpretation.",
"- Keep thresholds explicit.\n- Do not silently change baseline policy.\n- Runtime configs must not imply LLM or embedding support before implementation.",
"Inspect configs:\n\n    Get-ChildItem .\\configs"
),
"logs/README.md": mini(
"logs",
"Runtime and phase logs for diagnostics, benchmarks, attribution, candidates, regression guards, accepted deltas, and rejected deltas.",
"This folder preserves operational logs and future phase artifacts. Current AERMA-Memory uses ledgers and run folders for primary evidence, while logs are reserved for richer diagnostics and hardening passes.",
"- Future attribution should write under `logs/phase2/attribution`.\n- Future regression guards should write under `logs/phase2/regression_guard`.\n- Rejected memory-policy deltas should write under `logs/phase2/rejected_deltas`.",
"- `phase1/`.\n- `phase2/`.\n- `runtime/`.",
"Failure learning is part of evidence governance. Rejected deltas should be preserved instead of deleted.",
"- Do not delete rejected-delta evidence to clean history.\n- Do not treat logs as evidence unless linked to commands and configs.\n- Claim-affecting logs must preserve task and run IDs.",
"Inspect logs:\n\n    Get-ChildItem .\\logs -Recurse"
),
"runs/README.md": mini(
"runs",
"Generated suite run outputs.",
"This folder stores per-suite run directories created by `SuiteRunner`.",
"- `SuiteRunner` writes `runs/suite_*`.\n- Each run should include aggregate metrics, classification, and per-task outputs.",
"- `suite_*/aggregate_metrics.json`.\n- `suite_*/suite_classification.json`.\n- `suite_*/per_task/*/task_result.json`.",
"Run artifacts are local evidence records. They support implementation evidence only within the declared benchmark boundary.",
"- Do not manually edit run artifacts for public claims.\n- Preserve run IDs in evidence packages.\n- Generated run outputs should remain reproducible from suite commands.",
"List runs:\n\n    Get-ChildItem .\\runs"
),
"evidence_packages/README.md": mini(
"evidence_packages",
"Generated suite-level evidence packages.",
"This folder stores machine-readable evidence packages emitted by `EvidencePackageCompiler` during suite runs.",
"- `SuiteRunner` writes evidence package JSON files here.\n- RCC evidence linkage points to this folder.\n- Public benchmark/runtime claims should link to these artifacts.",
"- `*_evidence_package.json`.",
"Evidence packages preserve run payloads, metrics, classification, stubs, and task results. They are evidence records, not universal proof.",
"- Benchmark claims require evidence packages or downgrade.\n- Evidence packages must remain machine-readable.\n- Do not claim outside the suite boundary.",
"Inspect latest package:\n\n    Get-ChildItem .\\evidence_packages | Sort-Object LastWriteTime -Descending | Select-Object -First 1"
),
"ledgers/README.md": mini(
"ledgers",
"Persistent JSONL ledgers for runtime, suite, tool trace, decision, evolution, and rejected-delta records.",
"This folder stores append-only ledger surfaces used to preserve continuity and audit trails.",
"- `RuntimeLedger` appends suite events to `aerma_suite_ledger.jsonl`.\n- Future tool trace logic should write to `aerma_tool_trace_ledger.jsonl`.\n- Future rejected changes should write to `aerma_rejected_delta_ledger.jsonl`.",
"- `aerma_evolution_ledger.jsonl`.\n- `aerma_runtime_ledger.jsonl`.\n- `aerma_suite_ledger.jsonl`.\n- `aerma_decision_ledger.jsonl`.\n- `aerma_tool_trace_ledger.jsonl`.\n- `aerma_rejected_delta_ledger.jsonl`.",
"Execution without logs is not evidence. Ledgers preserve trace continuity and downgrade history.",
"- Treat ledgers as append-oriented records.\n- Do not hide failed runs.\n- Ledger claims must match evidence packages and run artifacts.",
"View suite ledger tail:\n\n    Get-Content .\\ledgers\\aerma_suite_ledger.jsonl -Tail 5"
),
"docs/README.md": mini(
"docs",
"Theory, architecture, benchmark protocol, evidence, metrics, plots, and RCC context documentation.",
"This folder holds human and AI-facing documentation surfaces. Documentation supports orientation and governance but does not replace source, tests, or evidence packages.",
"- `docs/context/` exposes RCC records.\n- `docs/architecture/` defines module contracts.\n- `docs/benchmark_protocol/` defines benchmark task meaning.\n- `docs/evidence/` defines evidence-package expectations.\n- `docs/metrics/` and `docs/plots/` are future dashboards.",
"- `theory/`.\n- `architecture/`.\n- `benchmark_protocol/`.\n- `evidence/`.\n- `metrics/`.\n- `plots/`.\n- `context/`.",
"RCC documentation is context reconstruction, not correctness proof. Runtime and benchmark claims require validation and evidence linkage.",
"- Do not let docs overclaim runtime status.\n- Update docs when commands, modules, or evidence paths change.\n- Keep non-claim locks visible.",
"Read validation surface:\n\n    Get-Content .\\docs\\context\\validation_surface.md"
),
"memory/README.md": mini(
"memory",
"Repository-local memory records for promoted invariants, rejected overclaims, runtime failure lessons, and stable thresholds.",
"This folder records lessons that survive evidence review. It should not be used to promote speculative claims without runtime support.",
"- Future hardening passes should update these files after repeated evidence review.\n- RCC drift report should reflect memory-promotion rule changes.",
"- `promoted_invariants.md`.\n- `rejected_overclaims.md`.\n- `runtime_failure_lessons.md`.\n- `stable_thresholds.md`.",
"Memory is an alignment attractor, not proof. Promotion requires repeated evidence, logs, and downgrade discipline.",
"- Do not promote one-run results as stable invariants.\n- Keep rejected overclaims visible.\n- Stable thresholds require repeat-run evidence.",
"Inspect rejected overclaims:\n\n    Get-Content .\\memory\\rejected_overclaims.md"
),
"tests/README.md": mini(
"tests",
"Pytest validation surface for the AERMA-Memory reference scaffold.",
"This folder tests episode schema, memory store, metric manifest, drift geometry, action gate, fallback, baseline classes, benchmark runner, suite runner, evidence package, and agent stubs.",
"- Tests import `aerma` package modules.\n- Validation surface requires `pytest -q`.\n- Runtime changes should add or update tests before claim updates.",
"- `test_episode_schema.py`.\n- `test_memory_store.py`.\n- `test_metric_manifest.py`.\n- `test_drift_geometry.py`.\n- `test_action_gate.py`.\n- `test_source_fallback.py`.\n- `test_baseline_classes.py`.\n- `test_benchmark_runner.py`.\n- `test_suite_runner.py`.\n- `test_evidence_package.py`.\n- `test_recursive_executor_stub.py`.\n- `test_reflection_evaluator_stub.py`.",
"Tests are the first validation gate. Passing tests is implementation evidence, not broad validation.",
"- Keep tests runnable from repo root.\n- Add tests for scoring or behavior changes.\n- Do not weaken tests to preserve claims.",
"Run all tests:\n\n    pytest -q"
),
}

for path, text in readmes.items():
    write(path, text)

# ------------------------------------------------------------
# RCC drift checker
# ------------------------------------------------------------
write("scripts/rcc/check_rcc_drift.ps1", r"""
# AERMA RCC drift check placeholder
# This script currently reports manual-review mode.
# Future version should validate RCC001-RCC020 style rules.

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $Root

Write-Host "AERMA RCC drift check: manual-review mode"
Write-Host "Required files:"

$Required = @(
    "README.md",
    "docs/context/repository_context_index.json",
    "docs/context/module_index.md",
    "docs/context/validation_surface.md",
    "docs/context/context_budget.md",
    "docs/context/drift_report.md",
    "docs/context/llm_reconstruction_prompt.md",
    "src/README.md",
    "src/aerma/README.md",
    "src/aerma/core/README.md",
    "src/aerma/benchmarks/README.md",
    "src/aerma/evidence/README.md",
    "tasks/README.md",
    "tests/README.md"
)

$Missing = @()

foreach ($Path in $Required) {
    if (!(Test-Path $Path)) {
        $Missing += $Path
        Write-Host "[MISSING] $Path"
    } else {
        Write-Host "[OK] $Path"
    }
}

if ($Missing.Count -gt 0) {
    throw "RCC drift check failed: missing required RCC files."
}

Write-Host "RCC drift check complete: required RCC files present."
""")

print("[RCC] File generation complete.")