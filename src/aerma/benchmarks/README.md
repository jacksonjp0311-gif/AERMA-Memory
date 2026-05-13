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
