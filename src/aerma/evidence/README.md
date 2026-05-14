# src/aerma/evidence

<!-- RCC-MINI-README:START -->

## Purpose

Runtime ledgers and evidence package compilation.

## S - Formal specification

This folder writes machine-readable runtime ledger records and compiles suite evidence packages.

## H - Hooks and integration edges

- `SuiteRunner` uses `RuntimeLedger`.
- `SuiteRunner` uses `EvidencePackageCompiler`.
- Outputs are written to `ledgers/`, `runs/`, and `evidence_packages/`.

## A - Artifacts

- `runtime_ledger.py`.
- `evidence_package.py`.

## T - Theory or method basis

Execution without logs is not evidence. Logs without baselines are weak support. Evidence packages preserve run configuration, metrics, classification, and non-claim locks.

## I - Invariants

- Evidence packages must be machine-readable.
- Runtime claims require linked run artifacts.
- Do not treat evidence packages as proof beyond their task boundary.

## E - Example

After running suite, inspect:

    Get-ChildItem .\evidence_packages

<!-- RCC-MINI-README:END -->

## RCC Nexus Echo Location

Sphere Position:
- Shell: middle
- Meridian(s): evidence, runtime, safety
- Sector: evidence
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-14

Local Role:
- Compiles runtime evidence packages and related evidence artifacts.

Inbound Hooks:
- src/aerma/benchmarks/suite_runner.py

Outbound Hooks:
- evidence_packages/

Evidence Surface:
- evidence_packages/

Validation Surface:
- pytest -q

Claim Boundary:
- Evidence packages are bounded to declared tasks and artifacts.

Non-Claim Locks:
- geometry_is_not_ai_internal_proof
- nci_is_not_code_quality_proof
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required

Agent Route:
- Read this README before modifying evidence package behavior.

Update Obligation:
- Update when evidence schema or output paths change.
