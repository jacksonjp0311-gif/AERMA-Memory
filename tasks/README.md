# tasks

<!-- RCC-MINI-README:START -->

## Purpose

Benchmark task definitions for source recall, ambiguity fallback, boundary separation, and abstention.

## S - Formal specification

This folder contains JSON benchmark tasks and the suite manifest consumed by `SuiteRunner`.

## H - Hooks and integration edges

- `tasks/suite_v1_2.json` lists task files.
- `BenchmarkRunner` loads each task and converts episodes into `AgentEpisode` objects.
- `scoring.py` reads expected task behavior and expected episode fields.

## A - Artifacts

- `suite_v1_2.json`.
- `source_recall/source_recall_001.json`.
- `source_recall/source_recall_ambiguous_001.json`.
- `boundary_separation/boundary_separation_001.json`.
- `abstain/abstain_insufficient_evidence_001.json`.

## T - Theory or method basis

AERMA must be tested not only where it should answer, but also where it should fallback, preserve boundaries, and abstain.

## I - Invariants

- Task JSON must remain valid UTF-8 without BOM or readable via utf-8-sig.
- Expected behavior must be declared before scoring.
- Negative controls must not be removed to inflate results.

## E - Example

Run suite manifest:

    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

<!-- RCC-MINI-README:END -->
