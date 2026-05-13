# scripts

<!-- RCC-MINI-README:START -->

## Purpose

Human-facing helper scripts for benchmark execution, suite execution, evidence compilation placeholders, repository dumps, RCC checks, and future metrics dashboards.

## S - Formal specification

This folder provides command surfaces that call into the `aerma` package. Scripts should remain runnable from the repository root and should not hide claim-affecting behavior.

## H - Hooks and integration edges

- `run_benchmark.py` calls `BenchmarkRunner`.
- `run_suite.py` calls `SuiteRunner`.
- `metrics/` contains dashboard generator placeholders.
- `repo/` contains repo dump utilities.
- `rcc/` contains RCC context tooling placeholders.

## A - Artifacts

- `run_benchmark.py`.
- `run_suite.py`.
- `metrics/generate_aerma_process_dashboard.py`.
- `metrics/generate_aerma_quality_dashboard.py`.
- `repo/repo_dump_light.ps1`.
- `rcc/check_rcc_drift.ps1`.

## T - Theory or method basis

Scripts are operational entry points. Diagnostic and benchmark scripts analyze evidence artifacts and should not alter runtime behavior unless explicitly declared.

## I - Invariants

- Keep commands runnable from repo root.
- Do not change script behavior without updating README command surfaces.
- Scripts affecting public claims must preserve validation and evidence boundaries.

## E - Example

Run suite helper script:

    python scripts/run_suite.py --suite ".\tasks\suite_v1_2.json"

<!-- RCC-MINI-README:END -->
