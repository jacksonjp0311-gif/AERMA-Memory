# rcc/nexus

<!-- RCC-MINI-README:START -->

## Purpose

Local RCC Nexus implementation layer for AERMA-Memory. This folder contains the geometric repository-context route maps, Echo Location protocol, task routing matrix, handoff contract, and templates needed for RCC-N v1.0.

## S - Formal specification

This folder implements RCC-N v1.0 as a repository-local navigation field. It defines how agents locate modules by shell, meridian, sector, hooks, evidence, validation, and update obligations before patching.

## H - Hooks and integration edges

- Root README links to the RCC Nexus layer.
- `docs/context/rcc_nexus_index.json` provides the machine-readable sphere index.
- `scripts/rcc/check_rcc_nexus.py` validates the Nexus layer.
- Major folder mini READMEs include Echo Location blocks.
- `docs/context/drift/latest_rcc_nexus_report.*` stores Nexus check results.

## A - Artifacts

- `rcc_nexus_protocol.md`
- `route_map.json`
- `task_routing_matrix.md`
- `echo_location_template.md`
- `agent_handoff_contract.md`

## T - Theory or method basis

RCC-N v1.0 extends RCC v1.3 with geometric repository context: Human/RCC Nexus/AI README trisection, repository sphere, shell/meridian/sector coordinates, Echo Location records, route maps, NCI, navigation entropy, and geometric drift.

## I - Invariants

- RCC-N is not code correctness.
- NCI is not code quality proof.
- Navigation is not validation.
- Context reconstruction is not runtime truth.
- Major changes to roles, hooks, validation, evidence, or claims require Nexus updates.
- Agents must route before patching.

## E - Example

Run the Nexus checker:

    python scripts/rcc/check_rcc_nexus.py

<!-- RCC-MINI-README:END -->

## RCC Nexus Echo Location

Sphere Position:
- Shell: middle
- Meridian(s): source, agent, safety, validation, drift
- Sector: rcc
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-14

Local Role:
- Holds the repository-local RCC Nexus route maps, protocol, templates, and handoff contract.

Inbound Hooks:
- README.md
- docs/context/rcc_nexus_index.json
- scripts/rcc/check_rcc_nexus.py

Outbound Hooks:
- docs/context/drift/latest_rcc_nexus_report.json
- docs/context/drift/latest_rcc_nexus_report.md

Evidence Surface:
- docs/context/drift/latest_rcc_nexus_report.json
- docs/context/drift/latest_rcc_nexus_report.md

Validation Surface:
- python scripts/rcc/check_rcc_nexus.py

Claim Boundary:
- This folder improves agent navigation and context integrity only. It does not prove runtime correctness.

Non-Claim Locks:
- geometry_is_not_ai_internal_proof
- nci_is_not_code_quality_proof
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required

Agent Route:
- Read README.md, docs/context/rcc_nexus_index.json, then this folder before editing Nexus routing.

Update Obligation:
- Update route map, index, protocol, and checker when repository geometry changes.
