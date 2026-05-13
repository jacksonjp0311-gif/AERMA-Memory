# src/aerma/cli

<!-- RCC-MINI-README:START -->

## Purpose

Command-line entry points for AERMA benchmark and suite execution.

## S - Formal specification

This folder exposes `run-benchmark` and `run-suite` commands through module execution and the installed `aerma` console script.

## H - Hooks and integration edges

- `pyproject.toml` maps `aerma = aerma.cli.main:main`.
- CLI calls `BenchmarkRunner` and `SuiteRunner`.

## A - Artifacts

- `main.py`.

## T - Theory or method basis

CLI commands are validation surfaces. If command behavior changes, README and RCC validation records must be updated.

## I - Invariants

- Keep commands runnable from the repo root.
- Do not hide claim-affecting behavior behind CLI defaults.
- Suite execution must emit evidence outputs.

## E - Example

Run CLI:

    aerma run-suite --suite ".\tasks\suite_v1_2.json"

<!-- RCC-MINI-README:END -->
