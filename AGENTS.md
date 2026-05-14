# AGENTS.md

## Repository Identity

You are entering AERMA-Memory, a governed agentic episodic memory reference workbench with RCC and RCC-N repository-context layers.

## Required Read Order

1. README.md
2. docs/context/repository_context_index.json
3. docs/context/validation_surface.md
4. docs/context/rcc_nexus_index.json
5. rcc/nexus/route_map.json
6. Target folder README.md
7. Relevant source, tests, tasks, evidence, or scripts.

## Patch Rule

No route, no safe patch.

Read the local Echo Location block before modifying a major folder.

## Validation

For source, scoring, benchmark, task, evidence, or RCC-N changes, run:

    pytest -q
    python -m aerma.cli.main run-suite --suite .\tasks\suite_v1_2.json
    python scripts/run_aerma_regression_guard.py
    powershell -ExecutionPolicy Bypass -File .\scripts\rcc\check_rcc_drift.ps1
    python scripts/rcc/check_rcc_nexus.py

## Non-Claim Locks

- RCC-N is not code correctness.
- NCI is not code quality proof.
- Navigation is not validation.
- Context reconstruction is not runtime truth.
- Suite execution is not production readiness.
