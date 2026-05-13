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


## v0.1.1 Hardening Layer

The v0.1.1 hardening layer adds task-family-aware scoring, per-task attribution records, suite-level attribution output, and a regression guard baseline. This improves evidence calibration but does not change the non-claim locks.

New hardening artifacts:

- `runs/suite_*/attribution_records.json`
- `runs/suite_*/regression_guard.json`
- `logs/phase2/attribution/latest_aerma_attribution.json`
- `logs/phase2/regression_guard/latest_aerma_regression_guard.json`

Run the regression guard viewer:

    python scripts/run_aerma_regression_guard.py
