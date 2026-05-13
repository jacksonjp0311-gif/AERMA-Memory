# AERMA-Memory RCC Drift Report

<!-- RCC-DRIFT-REPORT:START -->

## Current drift status

Manual review required.

## Current known context state

- RCC has been inserted after the first successful local run.
- Mini READMEs are generated from current repository structure and intended AERMA v1.2-MVP behavior.
- RCC records are useful for orientation but should not be treated as verified audit output.
- Runtime code remains source of truth.

## Known drift surfaces

- Scoring logic is early and needs hardening.
- Current classification may be too permissive for public claims.
- Attribution logs are not yet implemented.
- Regression guard is not yet implemented.
- RCC linter is not yet implemented.
- Evidence dashboards are placeholders.

## Required update triggers

Update RCC records when:

- package structure changes,
- CLI commands change,
- task suite changes,
- scoring/classification thresholds change,
- evidence package schema changes,
- ledgers move or change format,
- new benchmark tasks are added,
- recursive/reflection stubs become real implementations,
- README claims change.

<!-- RCC-DRIFT-REPORT:END -->
