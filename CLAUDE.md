# CLAUDE.md

## Project Memory

AERMA-Memory uses RCC and RCC-N to make the repository self-locating for code agents.

## Claude-Specific Instructions

- Preserve Markdown formatting.
- Do not collapse headings, tables, or lists into long single lines.
- Do not treat RCC or RCC-N as proof of code correctness.
- Keep patches minimal.
- Preserve non-claim locks.
- Run validation before claiming completion.

## Required Route

README.md -> docs/context/repository_context_index.json -> docs/context/rcc_nexus_index.json -> rcc/nexus/route_map.json -> target folder README.md -> source/tests/evidence.
