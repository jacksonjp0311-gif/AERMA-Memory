from typing import Dict, Any


def score_task(result: Dict[str, Any], task: Dict[str, Any]) -> Dict[str, Any]:
    query = task.get("queries", [{}])[0]
    expected_episode_id = query.get("expected_episode_id")
    forbidden_episode_id = query.get("forbidden_episode_id")
    expected_behavior = query.get("expected_behavior")

    selected = result.get("selected_episode_id")
    decision = result.get("decision")

    source_attribution_accuracy = 1.0 if expected_episode_id and selected == expected_episode_id else 0.0
    false_memory_frequency = 1.0 if forbidden_episode_id and selected == forbidden_episode_id else 0.0
    fallback_correctness = 1.0 if expected_behavior in {"fallback", "abstain"} and decision in {"fallback", "abstain"} else 0.0
    abstention_correctness = 1.0 if expected_behavior == "abstain" and decision in {"fallback", "abstain"} else 0.0

    boundary_separation_score = 1.0
    if forbidden_episode_id and selected == forbidden_episode_id:
        boundary_separation_score = 0.0

    return {
        "source_attribution_accuracy": source_attribution_accuracy,
        "false_memory_frequency": false_memory_frequency,
        "fallback_correctness": fallback_correctness,
        "boundary_separation_score": boundary_separation_score,
        "abstention_correctness": abstention_correctness,
    }


def suite_score(metrics: Dict[str, float]) -> float:
    values = [
        metrics.get("source_attribution_accuracy", 0.0),
        1.0 - metrics.get("false_memory_frequency", 0.0),
        metrics.get("fallback_correctness", 0.0),
        metrics.get("boundary_separation_score", 0.0),
        metrics.get("abstention_correctness", 0.0),
        1.0 - metrics.get("regression_frequency", 0.0),
    ]
    return sum(values) / len(values)
