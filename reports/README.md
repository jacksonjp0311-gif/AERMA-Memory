# reports

<!-- RCC-MINI-README:START -->

## Purpose

Human-readable benchmark, scorecard, and analysis reports for AERMA-Memory.

## S - Formal specification

This folder stores generated and maintained reports. Reports summarize evidence artifacts; they do not replace source, tests, run outputs, ledgers, or evidence packages.

## H - Hooks and integration edges

- `reports/rcc_nexus/` stores RCC-N benchmark reports.
- README links to key report files.
- RCC-N benchmark scripts write here.

## A - Artifacts

- `rcc_nexus/`

## T - Theory or method basis

Reports are downstream summaries. They must preserve non-claim locks and evidence boundaries.

## I - Invariants

- Reports are not proof of correctness.
- Reports must identify source artifacts.
- Reports must preserve evidence boundaries.

## E - Example

Generate RCC-N reports:

    python scripts/rcc/benchmark_rcc_nexus.py

<!-- RCC-MINI-README:END -->
