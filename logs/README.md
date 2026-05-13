# logs

<!-- RCC-MINI-README:START -->

## Purpose

Runtime and phase logs for diagnostics, benchmarks, attribution, candidates, regression guards, accepted deltas, and rejected deltas.

## S - Formal specification

This folder preserves operational logs and future phase artifacts. Current AERMA-Memory uses ledgers and run folders for primary evidence, while logs are reserved for richer diagnostics and hardening passes.

## H - Hooks and integration edges

- Future attribution should write under `logs/phase2/attribution`.
- Future regression guards should write under `logs/phase2/regression_guard`.
- Rejected memory-policy deltas should write under `logs/phase2/rejected_deltas`.

## A - Artifacts

- `phase1/`.
- `phase2/`.
- `runtime/`.

## T - Theory or method basis

Failure learning is part of evidence governance. Rejected deltas should be preserved instead of deleted.

## I - Invariants

- Do not delete rejected-delta evidence to clean history.
- Do not treat logs as evidence unless linked to commands and configs.
- Claim-affecting logs must preserve task and run IDs.

## E - Example

Inspect logs:

    Get-ChildItem .\logs -Recurse

<!-- RCC-MINI-README:END -->
