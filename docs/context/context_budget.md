# AERMA-Memory RCC Context Budget

<!-- RCC-CONTEXT-BUDGET:START -->

## Budget ladder

| Budget | Use |
|---|---|
| B0 | Root README only |
| B1 | Root README + repository context index |
| B2 | B1 + affected folder mini README |
| B3 | B2 + affected source files and tests |
| B4 | B3 + run artifacts, ledgers, configs, and evidence packages |
| B5 | Full repository dump or broad source ingestion |

## Default policy

- Orientation: B1 or B2.
- Small script or documentation patch: B2.
- Runtime behavior patch: B3.
- Benchmark, scoring, or evidence patch: B4.
- Cross-cutting refactor or unexplained failure: B5.

## Escalation rule

Escalate to source files when RCC records are stale, ambiguous, contradicted by tests, or insufficient for the requested patch.

<!-- RCC-CONTEXT-BUDGET:END -->
