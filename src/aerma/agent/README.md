# src/aerma/agent

<!-- RCC-MINI-README:START -->

## Purpose

Bounded agentic interfaces currently implemented as stubs.

## S - Formal specification

This folder holds `RecursiveExecutorStub` and `ReflectionEvaluatorStub`. They define future interfaces but do not execute full recursion or self-improvement.

## H - Hooks and integration edges

- `SuiteRunner` emits stub status into suite payload.
- Future AERMA versions may replace stubs with bounded implementations after evidence hardening.

## A - Artifacts

- `recursive_executor_stub.py`.
- `reflection_evaluator_stub.py`.

## T - Theory or method basis

A stub may define a future interface but must not be used as evidence of recursive capability or self-improvement.

## I - Invariants

- Do not claim recursion is implemented.
- Do not claim reflection-based improvement.
- Preserve stub boundary until measured implementation exists.

## E - Example

Run stub tests:

    pytest tests/test_recursive_executor_stub.py tests/test_reflection_evaluator_stub.py -q

<!-- RCC-MINI-README:END -->
