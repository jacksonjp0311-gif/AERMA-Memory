# src/aerma/gate

<!-- RCC-MINI-README:START -->

## Purpose

Action gating and source fallback behavior.

## S - Formal specification

This folder decides whether a retrieved memory can be returned, caveated, fallbacked, or abstained from based on declared thresholds and task expectations.

## H - Hooks and integration edges

- `BenchmarkRunner` calls `ActionGate`.
- `ActionGate` consumes `MetricManifest` and `DriftReport`.
- `SourceFallback` emits safe fallback and abstention messages.

## A - Artifacts

- `action_gate.py` - allow / caveat / fallback decision.
- `source_fallback.py` - fallback and abstention messages.

## T - Theory or method basis

AERMA treats ambiguity fallback and abstention as positive governance behaviors when evidence is insufficient.

## I - Invariants

- High-drift retrieval must not be promoted as fact.
- Ambiguity must trigger fallback instead of forced answer.
- Source-free answers must be rejected or caveated.

## E - Example

Run gate tests:

    pytest tests/test_action_gate.py tests/test_source_fallback.py -q

<!-- RCC-MINI-README:END -->
