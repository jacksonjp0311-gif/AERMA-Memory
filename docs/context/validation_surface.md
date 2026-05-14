# AERMA-Memory RCC Validation Surface

<!-
- RCC-VALIDATION-SURFACE:START -->

#
# Install

    python -m pip install -e ".[dev]"

#
# Test

    pytest -q

Expected current result:

    15 passed

#
# Suite execution

    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

Alternative console command:

    aerma run-suite --suite ".\tasks\suite_v1_2.json"

#
# Regression guard viewer

    python scripts/run_aerma_regression_guard.py

#
# Expected artifacts

- `runs/suite_*/aggregate_metrics.json`
- `runs/suite_*/suite_classification.json`
- `runs/suite_*/attribution_records.json`
- `runs/suite_*/regression_guard.json`
- `evidence_packages/*_evidence_package.json`
- `ledgers/aerma_suite_ledger.jsonl`
- `logs/phase2/attribution/latest_aerma_attribution.json`
- `logs/phase2/regression_guard/latest_aerma_regression_guard.json`

#
# Current local controlled-suite result

- `suite_score`: 1.0
- `classification`: AERMA-B
- `source_attribution_accuracy`: 1.0
- `fallback_correctness`: 1.0
- `abstention_correctness`: 1.0
- `boundary_separation_score`: 1.0
- `false_memory_frequency`: 0.0
- `regression_frequency`: 0.0

#
# Runtime claim boundary

Passing the validation surface proves that the local reference scaffold installs, imports, tests, and runs the declared controlled suite. It does not prove production readiness, human memory equivalence, autonomous self-improvement, sentience, consciousness, biological memory, or universal agent-memory validity.

#
# Known current evidence limitation

The current `suite_score: 1.0` is produced on a small controlled task suite. Stronger evidence requires harder distractors, multiple queries per task, adversarial ambiguity, source collision, stale-memory conflict, and baseline delta reports.

<!-
- RCC-VALIDATION-SURFACE:END -->

#
# Software Architecture Validation

Architecture-only changes must preserve runtime behavior.

Required validation after architecture changes:

    pytest -q
    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"
    python scripts/run_aerma_regression_guard.py
    powershell -ExecutionPolicy Bypass -File ".\scripts\rcc\check_rcc_drift.ps1"

Architecture documents are not runtime proof. They define implementation direction and validation expectations.

## RCC-N Architecture Validation

Architecture-only RCC-N changes must preserve current runtime behavior.

Required validation:

    pytest -q
    python -m aerma.cli.main run-suite --suite .\tasks\suite_v1_2.json
    python scripts/run_aerma_regression_guard.py
    powershell -ExecutionPolicy Bypass -File .\scripts\rcc\check_rcc_drift.ps1

After implementation, also run:

    python scripts/rcc/check_rcc_nexus.py

Boundary: RCC-N architecture is not runtime proof.

## RCC-N Local Validation

Run the local RCC Nexus checker:

    python scripts/rcc/check_rcc_nexus.py

Full validation after RCC-N changes:

    pytest -q
    python -m aerma.cli.main run-suite --suite .\tasks\suite_v1_2.json
    python scripts/run_aerma_regression_guard.py
    powershell -ExecutionPolicy Bypass -File .\scripts\rcc\check_rcc_drift.ps1
    python scripts/rcc/check_rcc_nexus.py

Boundary: RCC-N local validation does not prove code correctness.

## RCC-N Analytics Validation

Run RCC-N analytics:

    python scripts/rcc/benchmark_rcc_nexus.py
    python scripts/rcc/generate_rcc_nexus_charts.py

Full validation after README, RCC-N report, or chart changes:

    pytest -q
    python -m aerma.cli.main run-suite --suite .\tasks\suite_v1_2.json
    python scripts/run_aerma_regression_guard.py
    powershell -ExecutionPolicy Bypass -File .\scripts\rcc\check_rcc_drift.ps1
    python scripts/rcc/check_rcc_nexus.py
    python scripts/rcc/benchmark_rcc_nexus.py
    python scripts/rcc/generate_rcc_nexus_charts.py

Boundary: RCC-N analytics do not prove code correctness.
