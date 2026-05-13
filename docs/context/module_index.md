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
