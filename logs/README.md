# logs

<!-- RCC-MINI-README:START -->

## Purpose

Runtime and phase logs for diagnostics, attribution, regression guards, accepted deltas, and rejected deltas.

## S - Formal specification

This folder preserves operational logs and phase artifacts. v0.1.1 now writes latest attribution and regression guard outputs under `logs/phase2`.

## H - Hooks and integration edges

- `SuiteRunner` writes `logs/phase2/attribution/latest_aerma_attribution.json`.
- `SuiteRunner` writes `logs/phase2/regression_guard/latest_aerma_regression_guard.json`.
- Rejected memory-policy deltas should write under `logs/phase2/rejected_deltas` in future passes.

## A - Artifacts

- `phase1/`.
- `phase2/attribution/latest_aerma_attribution.json`.
- `phase2/regression_guard/latest_aerma_regression_guard.json`.
- `runtime/`.

## T - Theory or method basis

Failure learning is part of evidence governance. Rejected deltas should be preserved instead of deleted. Attribution explains runtime choice; it does not prove correctness.

## I - Invariants

- Do not delete rejected-delta evidence to clean history.
- Do not treat logs as evidence unless linked to commands and configs.
- Claim-affecting logs must preserve task and run IDs.
- Regression guard is a local baseline lock, not independent validation.

## E - Example

Inspect latest hardening logs:

    Get-ChildItem .\logs\phase2 -Recurse

<!-- RCC-MINI-README:END -->
