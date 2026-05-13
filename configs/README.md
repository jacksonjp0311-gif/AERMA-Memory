# configs

<!-- RCC-MINI-README:START -->

## Purpose

Declared runtime, metric, baseline, and suite configuration.

## S - Formal specification

This folder stores configuration surfaces used to document runtime assumptions, metric thresholds, baseline fairness, and suite policy.

## H - Hooks and integration edges

- `metric_manifest.json` mirrors default metric thresholds.
- `baseline_config.json` declares baseline fairness policy.
- `runtime_config.json` declares deterministic local scaffold mode.
- `suite_config.json` declares suite policy.

## A - Artifacts

- `runtime_config.json`.
- `metric_manifest.json`.
- `baseline_config.json`.
- `suite_config.json`.

## T - Theory or method basis

Metrics selected after results weaken classification. Configs declare intended evidence boundaries before interpretation.

## I - Invariants

- Keep thresholds explicit.
- Do not silently change baseline policy.
- Runtime configs must not imply LLM or embedding support before implementation.

## E - Example

Inspect configs:

    Get-ChildItem .\configs

<!-- RCC-MINI-README:END -->
