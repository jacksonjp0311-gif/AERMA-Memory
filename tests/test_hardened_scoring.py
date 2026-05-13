from aerma.benchmarks.benchmark_runner import BenchmarkRunner
from aerma.benchmarks.scoring import aggregate_task_metrics
from aerma.benchmarks.classifier import classify_claim


def test_task_family_aware_metrics_do_not_penalize_non_applicable_tasks():
    runner = BenchmarkRunner()
    positive = runner.run_task("tasks/source_recall/source_recall_001.json")
    ambiguous = runner.run_task("tasks/source_recall/source_recall_ambiguous_001.json")
    boundary = runner.run_task("tasks/boundary_separation/boundary_separation_001.json")
    abstain = runner.run_task("tasks/abstain/abstain_insufficient_evidence_001.json")

    aggregate = aggregate_task_metrics([
        positive["metrics"],
        ambiguous["metrics"],
        boundary["metrics"],
        abstain["metrics"],
    ])

    assert aggregate["source_attribution_accuracy"] >= 0.99
    assert aggregate["fallback_correctness"] >= 0.99
    assert aggregate["abstention_correctness"] >= 0.99
    assert aggregate["boundary_separation_score"] >= 0.99
    assert aggregate["false_memory_frequency"] == 0.0
    assert aggregate["suite_score"] >= 0.90


def test_classifier_downgrades_low_suite_score():
    result = classify_claim(
        aerma_score=0.85,
        suite_score=0.70,
        regression_frequency=0.0,
        false_memory_frequency=0.0,
        fallback_correctness=0.5,
        abstention_correctness=0.5,
        source_attribution_accuracy=0.5,
        boundary_separation_score=1.0,
    )
    assert result["classification"] in {"AERMA-C", "AERMA-D", "AERMA-E"}
    assert result["classification"] != "AERMA-B"
