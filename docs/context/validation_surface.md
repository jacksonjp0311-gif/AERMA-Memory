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
