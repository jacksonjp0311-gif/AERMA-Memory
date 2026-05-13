# docs

<!-- RCC-MINI-README:START -->

## Purpose

Theory, architecture, benchmark protocol, evidence, metrics, plots, and RCC context documentation.

## S - Formal specification

This folder holds human and AI-facing documentation surfaces. Documentation supports orientation and governance but does not replace source, tests, or evidence packages.

## H - Hooks and integration edges

- `docs/context/` exposes RCC records.
- `docs/architecture/` defines module contracts.
- `docs/benchmark_protocol/` defines benchmark task meaning.
- `docs/evidence/` defines evidence-package expectations.
- `docs/metrics/` and `docs/plots/` are future dashboards.

## A - Artifacts

- `theory/`.
- `architecture/`.
- `benchmark_protocol/`.
- `evidence/`.
- `metrics/`.
- `plots/`.
- `context/`.

## T - Theory or method basis

RCC documentation is context reconstruction, not correctness proof. Runtime and benchmark claims require validation and evidence linkage.

## I - Invariants

- Do not let docs overclaim runtime status.
- Update docs when commands, modules, or evidence paths change.
- Keep non-claim locks visible.

## E - Example

Read validation surface:

    Get-Content .\docs\context\validation_surface.md

<!-- RCC-MINI-README:END -->
