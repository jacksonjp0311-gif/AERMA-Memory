# AERMA-Memory RCC-Guided LLM Reconstruction Prompt

<!-- RCC-LLM-RECONSTRUCTION:START -->

Before patching this repository:

1. Declare task type.
2. Declare context budget.
3. Read `docs/context/repository_context_index.json`.
4. Read the affected folder README.
5. Inspect affected source files for runtime changes.
6. Preserve non-claim locks.
7. Run validation commands.
8. Update RCC records if command surfaces, artifacts, hooks, or claims change.
9. Do not claim benchmark improvement without evidence package linkage.
10. Do not treat generated RCC context as proof of code correctness.

Default validation:

    pytest -q
    python -m aerma.cli.main run-suite --suite ".\tasks\suite_v1_2.json"

Patch boundary:

- Documentation-only changes should not modify runtime behavior.
- Runtime changes must update tests and validation surfaces when needed.
- Benchmark/scoring changes must preserve downgrade discipline and evidence-package output.

<!-- RCC-LLM-RECONSTRUCTION:END -->
