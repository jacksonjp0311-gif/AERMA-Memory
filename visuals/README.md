# visuals

<!-- RCC-MINI-README:START -->

## Purpose

Visual diagnostic artifacts for AERMA-Memory.

## S - Formal specification

This folder stores generated charts and visual summaries. Visuals are explanatory artifacts only.

## H - Hooks and integration edges

- `visuals/rcc_nexus/` contains RCC-N charts.
- README embeds the NCI component chart.

## A - Artifacts

- `rcc_nexus/`

## T - Theory or method basis

Charts help humans inspect evidence surfaces. They do not replace validation or evidence packages.

## I - Invariants

- Visuals are not proof.
- Visuals must be generated from declared report data.

## E - Example

Generate RCC-N visuals:

    python scripts/rcc/generate_rcc_nexus_charts.py

<!-- RCC-MINI-README:END -->
