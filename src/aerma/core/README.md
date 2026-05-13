# src/aerma/core

<!-- RCC-MINI-README:START -->

## Purpose

Core memory objects and deterministic retrieval primitives.

## S - Formal specification

This folder defines `AgentEpisode`, `AgentMemoryStore`, `MetricManifest`, and `RetrievalEngine`. These are the base objects used by the benchmark runner.

## H - Hooks and integration edges

- `benchmarks/benchmark_runner.py` imports core objects.
- `tasks/*.json` are converted into `AgentEpisode` instances.
- `drift/` consumes retrieval scores.

## A - Artifacts

- `episode.py` - source-bound memory episode schema.
- `memory_store.py` - in-memory episode store.
- `metric_manifest.py` - declared thresholds and primary metrics.
- `retrieval_engine.py` - deterministic lexical retrieval.

## T - Theory or method basis

Core memory is source-bound and cue-dependent. Retrieval is reconstructive and must remain downstream of declared task data and upstream of drift and gating.

## I - Invariants

- Episodes must preserve source and ledger references.
- Fingerprints must remain deterministic.
- MetricManifest must be declared before interpretation.
- Retrieval score must remain dimensionless.

## E - Example

Run the source recall task:

    python -m aerma.cli.main run-benchmark --task ".\tasks\source_recall\source_recall_001.json"

<!-- RCC-MINI-README:END -->
