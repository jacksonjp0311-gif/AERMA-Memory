# src/aerma

<!-- RCC-MINI-README:START -->

## Purpose

Main AERMA package namespace.

## S - Formal specification

This folder defines the runtime package containing core memory primitives, drift geometry, action gating, benchmark execution, evidence compilation, agent stubs, and CLI entry points.

## H - Hooks and integration edges

- `core/` provides memory primitives.
- `benchmarks/` orchestrates tasks and scoring.
- `evidence/` writes ledgers and evidence packages.
- `cli/` exposes command surfaces.

## A - Artifacts

- `__init__.py` with package version.
- `core/`, `drift/`, `gate/`, `trace/`, `benchmarks/`, `evidence/`, `agent/`, `cli/`.

## T - Theory or method basis

AERMA is built as a governed memory workbench: source-bound episodes flow through retrieval, drift, gate, fallback, baseline comparison, and evidence packaging.

## I - Invariants

- Preserve package import.
- Do not claim human memory or sentience.
- Keep recursive and reflection behavior stubbed until implemented and measured.
- Runtime changes require test updates.

## E - Example

Verify import:

    python -c "import aerma; print(aerma.__version__)"

<!-- RCC-MINI-README:END -->
