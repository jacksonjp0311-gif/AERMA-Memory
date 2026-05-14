# Software Architecture

<!-- RCC-MINI-README:START -->

## Purpose

Canonical software architecture documents for AERMA-Memory. This folder locks implementation direction before large structural changes are made.

## S - Formal specification

Architecture documents in this folder define intended repository structure, runtime boundaries, validation surfaces, artifact contracts, RCC obligations, and non-claim locks. They do not replace source code, tests, evidence packages, or human review.

## H - Hooks and integration edges

- `README.md` links to this folder as the architecture anchor.
- `docs/context/repository_context_index.json` references active architecture documents.
- `docs/context/module_index.md` lists this folder as the architecture surface.
- Future RCC Echo implementation should conform to the locked architecture here.

## A - Artifacts

- `aerma_rcc_echo_location_architecture_v0_1_2.md`

## T - Theory or method basis

This folder follows Codex architecture discipline: lock the architecture, declare claim boundaries, define validation surfaces, then implement additively.

## I - Invariants

- Architecture is not implementation proof.
- Architecture must not overclaim runtime behavior.
- Architecture must preserve AERMA non-claim locks.
- Implementation should stay aligned with the locked architecture or explicitly document deviations.

## E - Example

Read the RCC Echo architecture:

    Get-Content .\docs\software_architecture\aerma_rcc_echo_location_architecture_v0_1_2.md

<!-- RCC-MINI-README:END -->
