# reports/rcc_nexus

<!-- RCC-MINI-README:START -->

## Purpose

RCC-N benchmark reports, scorecards, and metrics history.

## S - Formal specification

This folder stores machine-readable and human-readable snapshots of RCC-N health, NCI components, route coverage, Echo Location coverage, non-claim locks, and formatting health.

## H - Hooks and integration edges

- Written by `scripts/rcc/benchmark_rcc_nexus.py`.
- Read by README and future public reports.
- Charted by `scripts/rcc/generate_rcc_nexus_charts.py`.

## A - Artifacts

- `latest_rcc_nexus_benchmark.json`
- `latest_rcc_nexus_benchmark.md`
- `rcc_nexus_metrics_history.jsonl`
- `rcc_nexus_scorecard.md`

## T - Theory or method basis

RCC-N treats repository navigation as measurable context integrity. These reports are diagnostic and do not prove correctness.

## I - Invariants

- NCI is not code quality proof.
- Navigation is not validation.
- Reports must preserve non-claim locks.

## E - Example

Run:

    python scripts/rcc/benchmark_rcc_nexus.py

<!-- RCC-MINI-README:END -->
