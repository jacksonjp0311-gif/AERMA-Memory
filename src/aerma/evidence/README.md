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
