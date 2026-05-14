# AERMA-Memory: Governed Agentic Episodic Memory Workbench

> AERMA-Memory is a local-first reference implementation and benchmark workbench for governed agentic episodic memory. It tests source-bound recall, ambiguity fallback, boundary separation, abstention, baseline comparison, repeat-run evidence, RCC context, attribution records, regression guards, and audit-ready evidence packages.

**This is not a claim of sentience, consciousness, human episodic memory, biological memory, clinical memory, autonomous self-improvement, or a universal AI mechanism.**

AERMA-Memory is best understood as a governed memory workbench:

```text
source-bound episodes
-> cue-dependent retrieval
-> drift geometry
-> action gate
-> fallback / abstention
-> baseline comparison
-> repeat-run benchmark
-> attribution record
-> regression guard
-> evidence package
-> accepted / rejected memory-policy ledger
```

---

# PART I - Human README

## Current Identity

AERMA-Memory is a local Python reference workbench for testing whether an agentic memory system can:

- recall the correct source-bound episode,
- avoid forbidden distractors,
- fallback under ambiguity,
- abstain under insufficient evidence,
- preserve context boundaries,
- compare against baselines,
- emit attribution records,
- lock a regression guard,
- preserve evidence packages and ledgers,
- expose repository context through RCC mini READMEs.

The current repo is a **hardened local scaffold**, not a production memory system.

## Current Status

Current local validation snapshot:

| Surface | Current result |
|---|---:|
| Tests | 15 passed |
| Controlled suite score | 1.0 |
| Classification | AERMA-B |
| Source attribution accuracy | 1.0 |
| Fallback correctness | 1.0 |
| Abstention correctness | 1.0 |
| Boundary separation score | 1.0 |
| False memory frequency | 0.0 |
| Regression frequency | 0.0 |
| RCC drift check | required files present |

> **Evidence boundary:** The `suite_score: 1.0` result applies only to the current small controlled task suite. It is local scaffold evidence, not broad validation, not production readiness, and not evidence of human memory, sentience, consciousness, biological memory, clinical memory, autonomous self-improvement, or universal AI mechanism.

## Quick Start

Install editable package:

```powershell
python -m pip install -e ".[dev]"
```

Run tests:

```powershell
pytest -q
```

Run the controlled suite:

```powershell
python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"
```

Run the console script:

```powershell
aerma run-suite --suite ".\tasks\suite_v1_2.json"
```

View the current regression guard:

```powershell
python scripts/run_aerma_regression_guard.py
```

Run the RCC drift check:

```powershell
powershell -ExecutionPolicy Bypass -File ".\scripts\rcc\check_rcc_drift.ps1"
```

## What AERMA Tests

The current controlled suite includes:

| Task | Purpose |
|---|---|
| `source_recall_001` | Tests correct source-bound recall under a distractor. |
| `source_recall_ambiguous_001` | Tests fallback when the source does not resolve the claim. |
| `boundary_separation_001` | Tests whether similar episodes remain context-separated. |
| `abstain_insufficient_evidence_001` | Tests abstention/fallback under insufficient evidence. |

AERMA is designed to reward **safe uncertainty behavior**, not just confident recall.

## Current Hardening Layer

The v0.1.1 hardening layer added:

- task-family-aware scoring,
- non-applicable metrics represented as non-applicable instead of zero,
- stricter downgrade-preserving classification,
- per-task attribution records,
- suite-level attribution output,
- regression guard baseline,
- hardened scoring tests,
- hardened suite-output tests,
- updated RCC validation surfaces.

New hardening artifacts:

- `runs/suite_*/attribution_records.json`
- `runs/suite_*/regression_guard.json`
- `logs/phase2/attribution/latest_aerma_attribution.json`
- `logs/phase2/regression_guard/latest_aerma_regression_guard.json`
- `scripts/run_aerma_regression_guard.py`
- `tests/test_hardened_scoring.py`
- `tests/test_hardened_suite_outputs.py`

## Regression Guard

The current regression guard locks the local controlled-suite baseline:

| Guard | Threshold |
|---|---:|
| Minimum suite score | 0.98 |
| Minimum source attribution accuracy | 0.98 |
| Minimum fallback correctness | 0.98 |
| Minimum boundary separation score | 0.98 |
| Minimum abstention correctness | 0.98 |
| Maximum false memory frequency | 0.0 |

> **Regression-guard boundary:** The guard locks local scaffold evidence only. It does not prove production readiness or broad agent-memory validity.

## Project Structure

```text
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
```

## Main Folders

| Folder | Meaning |
|---|---|
| `src/aerma/core` | AgentEpisode, AgentMemoryStore, MetricManifest, RetrievalEngine. |
| `src/aerma/drift` | Dimensionless retrieval drift and Ω diagnostic weight. |
| `src/aerma/gate` | ActionGate and SourceFallback. |
| `src/aerma/benchmarks` | BenchmarkRunner, SuiteRunner, baselines, scoring, classifier. |
| `src/aerma/evidence` | RuntimeLedger and EvidencePackageCompiler. |
| `src/aerma/agent` | RecursiveExecutorStub and ReflectionEvaluatorStub. |
| `tasks` | Controlled benchmark tasks. |
| `logs/phase2/attribution` | Latest attribution records. |
| `logs/phase2/regression_guard` | Latest regression guard. |
| `docs/context` | RCC context layer. |
| `tests` | Pytest validation surface. |

## Evidence Artifacts

Suite runs produce outputs under:

```text
runs/suite_*/
```

Suite evidence packages are written under:

```text
evidence_packages/
```

Suite ledgers are written under:

```text
ledgers/aerma_suite_ledger.jsonl
```

Attribution records are written under:

```text
logs/phase2/attribution/latest_aerma_attribution.json
```

Regression guard records are written under:

```text
logs/phase2/regression_guard/latest_aerma_regression_guard.json
```

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
- not proof that coherence equals truth,
- not proof that a small controlled suite validates broad memory behavior.

## Roadmap

Near-term next steps:

1. Add harder benchmark tasks:
   - `source_collision_001`
   - `stale_memory_conflict_001`
   - `multi_query_boundary_001`
   - `adversarial_ambiguity_001`
   - `baseline_delta_report`
2. Upgrade runner from one-query-per-task to multi-query tasks.
3. Add baseline delta reports.
4. Add stronger evidence packages with Git commit, dirty-tree status, task count, query count, and known limitations.
5. Turn RCC drift check from file-presence checking into a real linter.
6. Enforce regression guard on future runtime/scoring changes.
7. Add accepted/rejected memory-policy delta ledgers.
8. Add optional retrieval backends without replacing deterministic lexical baseline.

---

<!-- RCC-AI-README:START -->

# PART II - AI / RCC Agent README

## AI version tracking contract

Current repository context:

- Repository: AERMA-Memory
- Purpose: governed agentic episodic memory reference implementation and benchmark workbench.
- Current runtime layer: AERMA-Memory v0.1.1 hardening layer.
- Conceptual architecture: AERMA v1.2 reference implementation and multi-task evidence layer.
- Primary package: `aerma`.
- Current classification: AERMA-B on the local controlled suite only.
- Current tests: `15 passed`.
- Current controlled suite score: `1.0`.
- Current non-claim boundary: local scaffold evidence only, not broad validation.
- RCC mode: repository-context layer plus mini READMEs.
- No runtime behavior is changed by RCC documentation.
- Current hardening surfaces:
  - task-family-aware scoring,
  - per-task attribution records,
  - suite-level attribution output,
  - regression guard baseline,
  - stricter downgrade-preserving classification,
  - updated RCC validation records.

Primary source files:

- `src/aerma/core/episode.py`
- `src/aerma/core/memory_store.py`
- `src/aerma/core/metric_manifest.py`
- `src/aerma/core/retrieval_engine.py`
- `src/aerma/drift/drift_geometry.py`
- `src/aerma/gate/action_gate.py`
- `src/aerma/gate/source_fallback.py`
- `src/aerma/benchmarks/benchmark_runner.py`
- `src/aerma/benchmarks/suite_runner.py`
- `src/aerma/benchmarks/scoring.py`
- `src/aerma/benchmarks/classifier.py`
- `src/aerma/benchmarks/baselines.py`
- `src/aerma/evidence/runtime_ledger.py`
- `src/aerma/evidence/evidence_package.py`
- `src/aerma/agent/recursive_executor_stub.py`
- `src/aerma/agent/reflection_evaluator_stub.py`
- `src/aerma/cli/main.py`

Primary docs and RCC files:

- `README.md`
- `docs/context/repository_context_index.json`
- `docs/context/module_index.md`
- `docs/context/validation_surface.md`
- `docs/context/context_budget.md`
- `docs/context/drift_report.md`
- `docs/context/llm_reconstruction_prompt.md`
- folder-level mini READMEs.

Primary scripts:

- `scripts/run_benchmark.py`
- `scripts/run_suite.py`
- `scripts/run_aerma_regression_guard.py`
- `scripts/rcc/check_rcc_drift.ps1`
- `scripts/rcc/generate_rcc_context.py`
- `scripts/rcc/harden_aerma_v0_1_1.py`
- `scripts/rcc/sync_readmes_after_hardening.py`
- `scripts/rcc/split_root_readme_human_ai.py`
- `scripts/rcc/repair_root_readme_format.py`

AI agents must update this section only when repository purpose, command surface, package structure, evidence artifacts, validation status, phase status, or claim boundaries change.

## AI operating contract

Any AI agent reading or modifying this repository must follow this order:

1. Read the root README first.
2. Read `docs/context/repository_context_index.json`.
3. Read `docs/context/validation_surface.md`.
4. Read the mini README in the target folder.
5. Inspect only relevant source, tests, docs, logs, tasks, or scripts.
6. Preserve source-bound memory discipline.
7. Preserve drift-gated fallback and abstention behavior.
8. Preserve the distinction between scaffold evidence and broad validation.
9. Preserve the non-claim locks.
10. Patch the smallest necessary surface.
11. Run relevant validation commands before claiming behavior changed.
12. Update local README/RCC context if folder purpose, hooks, artifacts, invariants, command surfaces, or evidence outputs change.

## RCC documentation contract

RCC means Repository Context Canon. In this repository, RCC is implemented as a documentation topology where the root README provides global context and subfolder READMEs expose local purpose, hooks, artifacts, theory or method basis, invariants, and examples.

RCC module fields:

- S = formal specification
- H = hooks and integration edges
- A = artifacts and code units
- T = theory or method basis
- I = invariants
- E = example

AI agents should reconstruct repository context through bounded README surfaces first, then inspect relevant files.

## AI file routing guide

- `src/aerma/core`: source-bound episode schema, memory store, metric manifest, and deterministic retrieval.
- `src/aerma/reconstruction`: reserved future context reconstruction layer.
- `src/aerma/drift`: retrieval drift and Ω diagnostic calculation.
- `src/aerma/gate`: ActionGate and SourceFallback behavior.
- `src/aerma/trace`: trace records for tool-like or runtime events.
- `src/aerma/benchmarks`: BenchmarkRunner, SuiteRunner, baselines, task-aware scoring, classifier, attribution output, and regression guard generation.
- `src/aerma/evidence`: runtime ledgers and evidence package compiler.
- `src/aerma/agent`: RecursiveExecutorStub and ReflectionEvaluatorStub.
- `src/aerma/cli`: command-line entry points.
- `tasks`: controlled benchmark task definitions and suite manifest.
- `configs`: runtime, metric, baseline, and suite configuration.
- `logs`: phase logs, attribution records, regression guard outputs, future accepted/rejected deltas.
- `runs`: generated suite outputs.
- `evidence_packages`: generated machine-readable evidence packages.
- `ledgers`: JSONL runtime, suite, decision, tool trace, evolution, and rejected-delta ledgers.
- `docs/context`: RCC context index, validation surface, context budget, drift report, and LLM reconstruction prompt.
- `memory`: promoted invariants, rejected overclaims, runtime failure lessons, and stable thresholds.
- `tests`: pytest validation surface.

## AI non-claim lock

Never claim or imply:

- AERMA proves sentience.
- AERMA proves consciousness.
- AERMA is human episodic memory.
- AERMA is biological memory.
- AERMA is clinical memory.
- AERMA guarantees autonomous self-improvement.
- AERMA is a universal AI mechanism.
- AERMA is production-ready agent memory.
- AERMA-B on the current suite proves broad memory validity.
- `suite_score: 1.0` proves generalization.
- A small controlled task suite proves real-world robustness.
- Drift geometry or Ω proves truth.
- Coherence equals truth.
- Attribution records prove correctness.
- Regression guards prove correctness.
- RCC documentation proves source correctness.
- Evidence packages prove beyond their declared task boundary.
- RecursiveExecutorStub is real recursive execution.
- ReflectionEvaluatorStub is real self-improvement or reflection capability.
- LLM fluency should be confused with source-grounded memory accuracy.

## AI interpretation of current evidence

AERMA-Memory is currently a hardened local reference workbench for governed agentic episodic memory. It demonstrates that a deterministic local memory scaffold can execute controlled tasks for source recall, ambiguity fallback, boundary separation, and abstention; emit task-family-aware metrics; write attribution records; lock regression guard thresholds; compile evidence packages; pass a pytest validation surface; and expose RCC context for human/AI handoff.

The current `suite_score: 1.0` and AERMA-B classification are valid only inside the current controlled suite. They do not establish production readiness, broad benchmark validity, human-memory equivalence, sentience, consciousness, biological mechanism, clinical utility, autonomous self-improvement, or universal AI mechanism.

The next evidence step should be harder task-suite expansion, including source collisions, stale-memory conflicts, multi-query boundaries, adversarial ambiguity, and baseline delta reporting.

## Required local verification

After documentation-only RCC changes, run:

```powershell
git diff -- README.md
git status
```

After README/RCC synchronization changes, run:

```powershell
pytest -q
python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"
python scripts/run_aerma_regression_guard.py
powershell -ExecutionPolicy Bypass -File ".\scripts\rcc\check_rcc_drift.ps1"
```

After source, scoring, benchmark, task, or evidence changes, run:

```powershell
python -m pip install -e ".[dev]"
pytest -q
python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"
python scripts/run_aerma_regression_guard.py
```

If the RCC context layer is changed, run:

```powershell
powershell -ExecutionPolicy Bypass -File ".\scripts\rcc\check_rcc_drift.ps1"
```

## README maintenance rule

When adding a new major folder, create a mini README with Purpose, S, H, A, T, I, and E fields.

When changing any of the following, update the root README and RCC context:

- command surface,
- task suite,
- package structure,
- validation result,
- evidence artifact path,
- classification threshold,
- non-claim lock,
- regression guard contract,
- attribution output format,
- accepted/rejected delta policy.

## Current roadmap for AI agents

Priority order:

1. Expand benchmark suite.
2. Add multi-query runner support.
3. Add baseline delta report.
4. Upgrade evidence package schema.
5. Convert RCC drift check into real linter.
6. Enforce regression guard on proposed runtime/scoring changes.
7. Add accepted/rejected memory-policy delta ledgers.
8. Add optional retrieval backend interface.
9. Add optional LLM narration layer without allowing narration to change metrics.
10. Replace recursive/reflection stubs only after bounded implementation and tests.

## Final AI warning

This repository is strongest when claim boundaries stay visible. Do not optimize documentation to sound stronger than the evidence. Preserve the distinction between local controlled-suite evidence and broad validation, the diagnostic-only nature of drift and Ω, the non-claim boundaries around human memory and sentience, the regression-guard boundary, the attribution boundary, the evidence-package boundary, and the fact that RCC improves navigation rather than proving code correctness.

<!-- RCC-AI-README:END -->

## Software Architecture

The current architecture lock for the next RCC layer is:

- `docs/software_architecture/aerma_rcc_echo_location_architecture_v0_1_2.md`

This document defines the planned AERMA-RCC-ECHO v0.1.2 Agentic Echo Location layer: root agent beacons, route maps, a modular `rcc/` folder, drift checks, reports, templates, schemas, and portability rules.

The architecture is not runtime proof. It locks the intended design before implementation.
