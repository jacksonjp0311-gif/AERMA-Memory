# src/aerma/trace

<!-- RCC-MINI-README:START -->

## Purpose

Trace records for tool-like or runtime events.

## S - Formal specification

This folder holds lightweight trace primitives used to preserve event payloads and timestamps.

## H - Hooks and integration edges

- Future benchmark attribution and tool-trace ledgers should use this layer.
- `ledgers/aerma_tool_trace_ledger.jsonl` is the persistent trace target.

## A - Artifacts

- `tool_trace_engine.py`

## T - Theory or method basis

Tool execution is evidence only when logged and reproducible. Trace records preserve auditability.

## I - Invariants

- Do not treat unlogged tool-like behavior as evidence.
- Trace records should remain machine-readable.
- Runtime trace changes must update evidence documentation.

## E - Example

Future trace usage target:

    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

<!-- RCC-MINI-README:END -->
