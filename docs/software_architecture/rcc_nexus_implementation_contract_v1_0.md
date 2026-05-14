# RCC-N v1.0 Implementation Contract for AERMA-Memory

## Purpose

This contract defines the exact local implementation surfaces required to make RCC-N v1.0 real inside AERMA-Memory.

## Implementation Mode

Mode: local repository integration.

Boundary: RCC-N improves repository navigation and context integrity. It does not change AERMA runtime behavior unless a later runtime pass explicitly does so.

## Files to Add

- `rcc/nexus/README.md`
- `rcc/nexus/rcc_nexus_protocol.md`
- `rcc/nexus/route_map.json`
- `rcc/nexus/task_routing_matrix.md`
- `rcc/nexus/echo_location_template.md`
- `rcc/nexus/agent_handoff_contract.md`
- `docs/context/rcc_nexus_index.json`
- `scripts/rcc/check_rcc_nexus.py`
- `docs/context/drift/latest_rcc_nexus_report.json`
- `docs/context/drift/latest_rcc_nexus_report.md`

## Files to Update

- `README.md`
- `docs/context/repository_context_index.json`
- `docs/context/module_index.md`
- `docs/context/validation_surface.md`
- major folder `README.md` files

## README Change

The root README must become a trisection:

1. PART I - Human README
2. PART II - RCC Nexus README
3. PART III - AI Agent README

## Required Nexus Index

Canonical path:

    docs/context/rcc_nexus_index.json

Required top-level fields:

- schema
- repository
- readme_trisection
- sphere
- nodes
- nci
- route_maps
- non_claim_locks

## Required Major Nodes

Initial AERMA nodes:

- README.md
- docs/context
- docs/software_architecture
- src/aerma/core
- src/aerma/benchmarks
- src/aerma/evidence
- tasks
- tests
- logs
- runs
- evidence_packages
- ledgers
- scripts/rcc
- rcc/nexus

## Echo Location Blocks

Echo Location blocks should be added first to:

- `docs/software_architecture/README.md`
- `docs/context/module_index.md` if appropriate
- `src/aerma/benchmarks/README.md`
- `src/aerma/evidence/README.md`
- `tasks/README.md`
- `tests/README.md`
- `scripts/README.md` or `scripts/rcc` documentation
- `rcc/nexus/README.md`

## Nexus Checker Requirements

The initial checker must validate:

- root README trisection
- `docs/context/rcc_nexus_index.json` exists and parses
- required non-claim locks exist
- NCI mode is present
- NCI components are present
- required nodes have shell/meridian/sector
- route map exists
- Nexus report is emitted

## Validation Commands

Full validation after RCC-N implementation:

    pytest -q
    python -m aerma.cli.main run-suite --suite .\tasks\suite_v1_2.json
    python scripts/run_aerma_regression_guard.py
    powershell -ExecutionPolicy Bypass -File .\scripts\rcc\check_rcc_drift.ps1
    python scripts/rcc/check_rcc_nexus.py

## Done Criteria

RCC-N local integration is complete when:

- README trisection exists.
- `docs/context/rcc_nexus_index.json` exists.
- `rcc/nexus/` exists.
- route map exists.
- at least key folders have Echo Location blocks.
- checker emits PASS or WARN with explicit non-claim boundary.
- validation commands pass.
- Git commit is clean.

## Non-Claim Locks

- Geometry is not correctness.
- Navigation is not validation.
- NCI is not code quality proof.
- Context reconstruction is not runtime truth.
- README quality is not benchmark evidence.
- RCC-N does not imply AI understanding.

## Next Implementation Pass

The next pass should implement this contract in one script. That script must avoid nested Markdown code fences inside the outer PowerShell block by using line arrays or plain indented code examples.
