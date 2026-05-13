# src/aerma/reconstruction

<!-- RCC-MINI-README:START -->

## Purpose

Reserved context reconstruction layer.

## S - Formal specification

This folder is reserved for future context reconstruction logic. It currently contains only package scaffolding.

## H - Hooks and integration edges

- Future `ContextReconstructionEngine` should sit between retrieval and drift/gating.
- Future benchmark attribution should reference reconstruction decisions.

## A - Artifacts

- `__init__.py`

## T - Theory or method basis

Context reconstruction must remain source-bound and should not rewrite measured retrieval geometry through narrative interpretation.

## I - Invariants

- Do not claim reconstruction capability until implemented.
- Do not promote reconstructed context as fact without source fallback.
- Add tests before enabling runtime use.

## E - Example

Current placeholder check:

    Get-ChildItem .\src\aerma\reconstruction

<!-- RCC-MINI-README:END -->
