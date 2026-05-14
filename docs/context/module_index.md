# AERMA-Memory RCC Module Index

<!-
- RCC-CONTEXT:START -->

#
# Declared RCC profile

AERMA-Memory currently declares `RCC-Core`.

#
# Major modules

| Module 
| Path | Role | Runtime claim sensitivity |
|
---
|
---
|
---
|
---
|
| Core memory primitives 
| `src/aerma/core` | Episode schema, memory store, metric manifest, retrieval | High |
| Drift geometry 
| `src/aerma/drift` | Retrieval drift and Ω calculation | High |
| Gate and fallback 
| `src/aerma/gate` | ActionGate and SourceFallback | High |
| Benchmarks 
| `src/aerma/benchmarks` | BenchmarkRunner, SuiteRunner, baselines, task-aware scoring, classifier | Very high |
| Evidence 
| `src/aerma/evidence` | RuntimeLedger and EvidencePackageCompiler | Very high |
| Agent stubs 
| `src/aerma/agent` | RecursiveExecutorStub and ReflectionEvaluatorStub | Medium |
| CLI 
| `src/aerma/cli` | Human command surface | High |
| Tasks 
| `tasks` | Benchmark task definitions | Very high |
| Configs 
| `configs` | Runtime, baseline, metric, and suite config | High |
| Logs 
| `logs` | Attribution and regression guard outputs | High |
| Runs 
| `runs` | Generated suite outputs including attribution and guard files | High |
| Ledgers 
| `ledgers` | Persistent run records | High |
| Evidence packages 
| `evidence_packages` | Suite evidence artifacts | High |
| Memory 
| `memory` | Promoted invariants and rejected overclaims | Medium |
| RCC scripts 
| `scripts/rcc` | RCC generation/checking and hardening scripts | Medium |

#
# Source-fidelity status

These RCC records are derived from the current scaffold and latest local run results. They are not independent audit results.

#
# Primary validation commands

    pytest -q
    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"
    aerma run-suite --suite ".\tasks\suite_v1_2.json"
    python scripts/run_aerma_regression_guard.py

#
# Current validation snapshot

    15 passed
    suite_score: 1.0
    classification: AERMA-B

#
# Boundary

The validation snapshot is local controlled-suite evidence only.

<!-
- RCC-CONTEXT:END -->

#
# Software Architecture Surface

| Module 
| Path | Role | Runtime claim sensitivity |
|
---
|
---
|
---
|
---
|
| Software architecture 
| `docs/software_architecture` | Locked architecture documents before major implementation changes | Medium |
| RCC Echo Architecture 
| `docs/software_architecture/aerma_rcc_echo_location_architecture_v0_1_2.md` | Defines planned AGENTS.md, CLAUDE.md, `rcc/`, route maps, checks, reports, templates, and schemas | Medium |

Architecture documents define intended structure and validation surfaces. They do not prove implementation correctness.

## RCC-N Nexus Architecture Surface

| Module | Path | Role | Runtime claim sensitivity |
|---|---|---|---|
| RCC-N software architecture | `docs/software_architecture/rcc_nexus_software_architecture_v1_0.md` | Defines Human/RCC Nexus/AI trisection, sphere, coordinates, Echo Location, route maps, NCI, and drift | Medium |
| RCC-N implementation contract | `docs/software_architecture/rcc_nexus_implementation_contract_v1_0.md` | Defines exact local implementation surfaces for RCC-N integration | Medium |

Boundary: These documents lock implementation direction. They do not prove code correctness or runtime validity.

## RCC-N Local Nexus Layer

| Module | Path | Role | Runtime claim sensitivity |
|---|---|---|---|
| RCC Nexus index | `docs/context/rcc_nexus_index.json` | Machine-readable sphere, coordinates, NCI, route maps, and locks | Medium |
| RCC Nexus local layer | `rcc/nexus/` | Route maps, protocol, task matrix, handoff, Echo template | Medium |
| RCC Nexus checker | `scripts/rcc/check_rcc_nexus.py` | Validates trisection, index, route map, NCI, and Echo blocks | Medium |
| RCC Nexus reports | `docs/context/drift/latest_rcc_nexus_report.*` | Generated Nexus integrity reports | Medium |

Boundary: RCC-N is navigation/context integrity only, not code correctness.

## RCC-N Reports and Visuals

| Module | Path | Role | Runtime claim sensitivity |
|---|---|---|---|
| RCC-N reports | `reports/rcc_nexus/` | Human-readable benchmark reports, scorecards, and metrics history | Medium |
| RCC-N visuals | `visuals/rcc_nexus/` | SVG charts for NCI components, coverage, trend, and surface map | Medium |
| RCC-N benchmark script | `scripts/rcc/benchmark_rcc_nexus.py` | Gathers RCC-N data and writes reports | Medium |
| RCC-N chart script | `scripts/rcc/generate_rcc_nexus_charts.py` | Generates SVG visual diagnostics | Medium |

Boundary: reports and visuals are diagnostic only. They do not prove code correctness.
