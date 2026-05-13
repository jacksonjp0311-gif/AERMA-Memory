# tests

<!-- RCC-MINI-README:START -->

## Purpose

Pytest validation surface for the AERMA-Memory reference scaffold.

## S - Formal specification

This folder tests episode schema, memory store, metric manifest, drift geometry, action gate, fallback, baseline classes, benchmark runner, suite runner, evidence package, and agent stubs.

## H - Hooks and integration edges

- Tests import `aerma` package modules.
- Validation surface requires `pytest -q`.
- Runtime changes should add or update tests before claim updates.

## A - Artifacts

- `test_episode_schema.py`.
- `test_memory_store.py`.
- `test_metric_manifest.py`.
- `test_drift_geometry.py`.
- `test_action_gate.py`.
- `test_source_fallback.py`.
- `test_baseline_classes.py`.
- `test_benchmark_runner.py`.
- `test_suite_runner.py`.
- `test_evidence_package.py`.
- `test_recursive_executor_stub.py`.
- `test_reflection_evaluator_stub.py`.

## T - Theory or method basis

Tests are the first validation gate. Passing tests is implementation evidence, not broad validation.

## I - Invariants

- Keep tests runnable from repo root.
- Add tests for scoring or behavior changes.
- Do not weaken tests to preserve claims.

## E - Example

Run all tests:

    pytest -q

<!-- RCC-MINI-README:END -->
