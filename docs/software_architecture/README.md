# Software Architecture

<!-
- RCC-MINI-README:START -->

#
# Purpose

Canonical software architecture documents for AERMA-Memory. This folder locks implementation direction before large structural changes are made.

#
# S - Formal specification

Architecture documents in this folder define intended repository structure, runtime boundaries, validation surfaces, artifact contracts, RCC obligations, and non-claim locks. They do not replace source code, tests, evidence packages, or human review.

#
# H - Hooks and integration edges

- `README.md` links to this folder as the architecture anchor.
- `docs/context/repository_context_index.json` references active architecture documents.
- `docs/context/module_index.md` lists this folder as the architecture surface.
- Future RCC Echo implementation should conform to the locked architecture here.

#
# A - Artifacts

- `aerma_rcc_echo_location_architecture_v0_1_2.md`

#
# T - Theory or method basis

This folder follows Codex architecture discipline: lock the architecture, declare claim boundaries, define validation surfaces, then implement additively.

#
# I - Invariants

- Architecture is not implementation proof.
- Architecture must not overclaim runtime behavior.
- Architecture must preserve AERMA non-claim locks.
- Implementation should stay aligned with the locked architecture or explicitly document deviations.

#
# E - Example

Read the RCC Echo architecture:

    Get-Content .\docs\software_architecture\aerma_rcc_echo_location_architecture_v0_1_2.md

<!-
- RCC-MINI-README:END -->

## RCC-N v1.0 Nexus Architecture

The RCC-N v1.0 architecture documents the next local integration layer for AERMA-Memory.

Primary files:

- `rcc_nexus_software_architecture_v1_0.md`
- `rcc_nexus_implementation_contract_v1_0.md`

Boundary:

RCC-N improves repository navigation, agent self-location, Echo Location records, route maps, and Nexus Context Integrity. It does not prove code correctness, security, patch safety, model understanding, human memory, sentience, or production readiness.

## RCC Nexus Echo Location

Sphere Position:
- Shell: outer
- Meridian(s): source, agent, safety, release
- Sector: rcc
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-14

Local Role:
- Holds locked software architecture documents and implementation contracts.

Inbound Hooks:
- README.md
- docs/context/module_index.md

Outbound Hooks:
- docs/software_architecture/rcc_nexus_software_architecture_v1_0.md
- docs/software_architecture/rcc_nexus_implementation_contract_v1_0.md

Evidence Surface:
- architecture documents

Validation Surface:
- pytest -q
- python scripts/rcc/check_rcc_nexus.py

Claim Boundary:
- Architecture is not implementation proof.

Non-Claim Locks:
- geometry_is_not_ai_internal_proof
- nci_is_not_code_quality_proof
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required

Agent Route:
- Read architecture before implementing RCC-N surfaces.

Update Obligation:
- Update when architecture direction or implementation contract changes.
