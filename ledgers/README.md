# ledgers

<!-- RCC-MINI-README:START -->

## Purpose

Persistent JSONL ledgers for runtime, suite, tool trace, decision, evolution, and rejected-delta records.

## S - Formal specification

This folder stores append-only ledger surfaces used to preserve continuity and audit trails.

## H - Hooks and integration edges

- `RuntimeLedger` appends suite events to `aerma_suite_ledger.jsonl`.
- Future tool trace logic should write to `aerma_tool_trace_ledger.jsonl`.
- Future rejected changes should write to `aerma_rejected_delta_ledger.jsonl`.

## A - Artifacts

- `aerma_evolution_ledger.jsonl`.
- `aerma_runtime_ledger.jsonl`.
- `aerma_suite_ledger.jsonl`.
- `aerma_decision_ledger.jsonl`.
- `aerma_tool_trace_ledger.jsonl`.
- `aerma_rejected_delta_ledger.jsonl`.

## T - Theory or method basis

Execution without logs is not evidence. Ledgers preserve trace continuity and downgrade history.

## I - Invariants

- Treat ledgers as append-oriented records.
- Do not hide failed runs.
- Ledger claims must match evidence packages and run artifacts.

## E - Example

View suite ledger tail:

    Get-Content .\ledgers\aerma_suite_ledger.jsonl -Tail 5

<!-- RCC-MINI-README:END -->
