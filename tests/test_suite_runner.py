from aerma.benchmarks.suite_runner import SuiteRunner
from pathlib import Path


def test_suite_runner_runs(tmp_path):
    root = Path(".")
    result = SuiteRunner(root=root).run_suite("tasks/suite_v1_2.json")
    assert result["suite_id"] == "aerma_suite_v1_2"
    assert "aggregate_metrics" in result
