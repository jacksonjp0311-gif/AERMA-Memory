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
