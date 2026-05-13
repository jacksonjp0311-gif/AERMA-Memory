# src/aerma/drift

<!-- RCC-MINI-README:START -->

## Purpose

Retrieval drift and Ω stability calculation.

## S - Formal specification

This folder computes dimensionless retrieval drift and Ω weighting from retrieval scores.

## H - Hooks and integration edges

- `benchmarks/benchmark_runner.py` calls `DriftGeometryEngine`.
- `gate/action_gate.py` consumes `DriftReport`.

## A - Artifacts

- `drift_geometry.py`

## T - Theory or method basis

AERMA uses ΔΦ-style drift as an instability proxy. Ω = 1 / (1 + abs(drift)) is diagnostic and should not be treated as truth.

## I - Invariants

- Drift must remain dimensionless.
- Ω is diagnostic only.
- Do not silently modify task outcomes with narrative interpretation.

## E - Example

Run tests for drift behavior:

    pytest tests/test_drift_geometry.py -q

<!-- RCC-MINI-README:END -->
