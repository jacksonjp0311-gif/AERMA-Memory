from pathlib import Path
from aerma.benchmarks.suite_runner import SuiteRunner


def test_hardened_suite_outputs_attribution_and_regression_guard():
    result = SuiteRunner(root=Path(".")).run_suite("tasks/suite_v1_2.json")
    run_dir = Path("runs") / result["run_id"]

    assert result["aggregate_metrics"]["suite_score"] >= 0.90
    assert result["classification"]["classification"] in {"AERMA-B", "AERMA-A"}
    assert (run_dir / "attribution_records.json").exists()
    assert (run_dir / "regression_guard.json").exists()
    assert Path("logs/phase2/attribution/latest_aerma_attribution.json").exists()
    assert Path("logs/phase2/regression_guard/latest_aerma_regression_guard.json").exists()
