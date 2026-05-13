# memory

<!-- RCC-MINI-README:START -->

## Purpose

Repository-local memory records for promoted invariants, rejected overclaims, runtime failure lessons, and stable thresholds.

## S - Formal specification

This folder records lessons that survive evidence review. It should not be used to promote speculative claims without runtime support.

## H - Hooks and integration edges

- Future hardening passes should update these files after repeated evidence review.
- RCC drift report should reflect memory-promotion rule changes.

## A - Artifacts

- `promoted_invariants.md`.
- `rejected_overclaims.md`.
- `runtime_failure_lessons.md`.
- `stable_thresholds.md`.

## T - Theory or method basis

Memory is an alignment attractor, not proof. Promotion requires repeated evidence, logs, and downgrade discipline.

## I - Invariants

- Do not promote one-run results as stable invariants.
- Keep rejected overclaims visible.
- Stable thresholds require repeat-run evidence.

## E - Example

Inspect rejected overclaims:

    Get-Content .\memory\rejected_overclaims.md

<!-- RCC-MINI-README:END -->
