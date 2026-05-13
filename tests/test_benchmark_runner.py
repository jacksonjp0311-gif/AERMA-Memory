from aerma.benchmarks.benchmark_runner import BenchmarkRunner


def test_source_recall_task_runs():
    result = BenchmarkRunner().run_task("tasks/source_recall/source_recall_001.json")
    assert result["result"]["task_id"] == "source_recall_001"
    assert "metrics" in result
