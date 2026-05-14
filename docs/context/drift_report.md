# AERMA-Memory RCC Drift Report

<!-
- RCC-DRIFT-REPORT:START -->

#
# Current drift status

Manual review required, but v0.1.1 hardening reduces known scoring drift.

#
# Current known context state

- RCC has been inserted after successful local runs.
- Mini READMEs are generated from current repository structure and intended AERMA v1.2-MVP behavior.
- Runtime code remains source of truth.
- v0.1.1 hardening adds task-family-aware scoring, per-task attribution logs, and a regression guard baseline.

#
# Known drift surfaces

- Current attribution logs are deterministic scaffold attribution, not model-quality proof.
- Regression guard is a local baseline lock, not independent validation.
- RCC linter is still placeholder/manual-review mode.
- Evidence dashboards are placeholders.
- RecursiveExecutor and ReflectionEvaluator remain stubs.

#
# Required update triggers

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

<!-
- RCC-DRIFT-REPORT:END -->
