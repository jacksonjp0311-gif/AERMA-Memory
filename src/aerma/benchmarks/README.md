# src/aerma/benchmarks

<!-- RCC-MINI-README:START -->

## Purpose

Benchmark runners, baselines, task-family-aware scoring, attribution records, regression guard generation, and AERMA claim classification.

## S - Formal specification

This folder runs task JSON files through AERMA runtime logic and declared baselines, aggregates task-aware metrics, writes attribution records, emits regression guard artifacts, and assigns bounded AERMA classifications.

## H - Hooks and integration edges

- `cli/main.py` calls `BenchmarkRunner` and `SuiteRunner`.
- `SuiteRunner` reads `tasks/suite_v1_2.json`.
- `SuiteRunner` writes run outputs, attribution records, regression guard files, and evidence packages.
- `baselines.py` provides explicit baseline classes.
- `scoring.py` now treats non-applicable metrics as `None` so task families are scored fairly.

## A - Artifacts

- `benchmark_runner.py`.
- `suite_runner.py`.
- `baselines.py`.
- `scoring.py`.
- `classifier.py`.

## T - Theory or method basis

AERMA must be tested where it should answer and where it should fallback, preserve boundaries, or abstain. Baselines must run on the same data and metrics. Task-aware scoring prevents abstention and fallback tasks from unfairly lowering source-recall metrics.

## I - Invariants

- Do not select metrics after results.
- Do not compare baselines on different task data.
- Do not overpromote controlled-suite evidence as broad validation.
- Benchmark claims require evidence packages.
- Keep classification downgrade-preserving.

## E - Example

Run full suite:

    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

<!-- RCC-MINI-README:END -->

## RCC Nexus Echo Location

Sphere Position:
- Shell: middle
- Meridian(s): runtime, validation, evidence, safety
- Sector: benchmark
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-14

Local Role:
- Runs benchmark tasks, scoring, classification, attribution, regression guard, and suite evidence surfaces.

Inbound Hooks:
- tasks/suite_v1_2.json
- src/aerma/cli/main.py

Outbound Hooks:
- runs/
- evidence_packages/
- ledgers/aerma_suite_ledger.jsonl

Evidence Surface:
- runs/suite_*/aggregate_metrics.json
- evidence_packages/*_evidence_package.json

Validation Surface:
- pytest -q
- python -m aerma.cli.main run-suite --suite .\tasks\suite_v1_2.json

Claim Boundary:
- Suite score is controlled-suite evidence only.

Non-Claim Locks:
- geometry_is_not_ai_internal_proof
- nci_is_not_code_quality_proof
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required

Agent Route:
- Read this README before scoring, suite, or classifier changes.

Update Obligation:
- Update when benchmark hooks, metrics, or evidence surfaces change.
