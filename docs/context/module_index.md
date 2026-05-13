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
