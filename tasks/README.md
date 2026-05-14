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

## RCC Nexus Echo Location

Sphere Position:
- Shell: middle
- Meridian(s): validation, runtime, evidence
- Sector: benchmark
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-14

Local Role:
- Stores benchmark task JSON and suite definitions.

Inbound Hooks:
- src/aerma/benchmarks/suite_runner.py

Outbound Hooks:
- runs/
- evidence_packages/

Evidence Surface:
- runs/suite_*/aggregate_metrics.json

Validation Surface:
- python -m aerma.cli.main run-suite --suite .\tasks\suite_v1_2.json

Claim Boundary:
- Controlled tasks do not prove broad generalization.

Non-Claim Locks:
- geometry_is_not_ai_internal_proof
- nci_is_not_code_quality_proof
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required

Agent Route:
- Read this README before task or suite changes.

Update Obligation:
- Update when task families, suite composition, or validation expectations change.
