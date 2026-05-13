# src

<!-- RCC-MINI-README:START -->

## Purpose

Source package root for the importable AERMA-Memory implementation.

## S - Formal specification

This folder contains the Python package boundary. Runtime behavior should live under `src/aerma` and remain importable through editable install.

## H - Hooks and integration edges

- `pyproject.toml` discovers packages under `src`.
- `tests/` imports modules from this package.
- CLI commands call into `src/aerma/cli/main.py`.

## A - Artifacts

- `aerma/`

## T - Theory or method basis

The source tree is the executable anchor. RCC documentation can describe it, but source and tests remain the validation surface.

## I - Invariants

- Keep package importable.
- Do not place runtime logic outside the package without documenting the hook.
- Runtime claims require tests and evidence outputs.

## E - Example

Install package from repo root:

    python -m pip install -e ".[dev]"

<!-- RCC-MINI-README:END -->
