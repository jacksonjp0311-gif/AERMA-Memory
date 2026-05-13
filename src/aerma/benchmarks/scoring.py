from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional


NA = None


def _contains_forbidden_answer(result: Dict[str, Any], query: Dict[str, Any]) -> bool:
    forbidden_terms = [str(x).lower() for x in query.get("forbidden_answer_contains", [])]
    if not forbidden_terms:
        return False

    joined = " ".join(
        str(result.get(key, ""))
        for key in ["message", "decision", "gate_reason", "selected_episode_id", "selected_source_ref"]
    ).lower()

    return any(term in joined for term in forbidden_terms)


def score_task(result: Dict[str, Any], task: Dict[str, Any]) -> Dict[str, Optional[float]]:
    """Score one task with task-family-aware applicability.

    Metrics that do not apply to a task return None rather than 0.0.
    This prevents abstention/fallback tasks from lowering source-recall metrics
    and prevents positive recall tasks from lowering abstention metrics.
    """

    query = task.get("queries", [{}])[0]
    task_family = task.get("task_family", "")

    expected_episode_id = query.get("expected_episode_id")
    forbidden_episode_id = query.get("forbidden_episode_id")
    expected_behavior = query.get("expected_behavior")
    expected_boundary_id = query.get("expected_boundary_id")

    selected = result.get("selected_episode_id")
    decision = result.get("decision")
    selected_boundary_id = result.get("selected_boundary_id")

    metrics: Dict[str, Optional[float]] = {
        "source_attribution_accuracy": NA,
        "false_memory_frequency": NA,
        "fallback_correctness": NA,
        "boundary_separation_score": NA,
        "abstention_correctness": NA,
        "retrieval_drift": result.get("retrieval_drift"),
        "omega": result.get("omega"),
    }

    if expected_episode_id:
        metrics["source_attribution_accuracy"] = 1.0 if selected == expected_episode_id else 0.0

    if forbidden_episode_id:
        metrics["false_memory_frequency"] = 1.0 if selected == forbidden_episode_id else 0.0

    if expected_behavior in {"fallback", "abstain"}:
        metrics["fallback_correctness"] = 1.0 if decision in {"fallback", "abstain"} else 0.0
        if _contains_forbidden_answer(result, query):
            metrics["fallback_correctness"] = 0.0
            metrics["false_memory_frequency"] = 1.0

    if expected_behavior == "abstain":
        metrics["abstention_correctness"] = 1.0 if decision in {"fallback", "abstain"} else 0.0

    if task_family == "boundary_separation" or expected_boundary_id:
        boundary_ok = True
        if forbidden_episode_id and selected == forbidden_episode_id:
            boundary_ok = False
        if expected_episode_id and selected != expected_episode_id:
            boundary_ok = False
        if expected_boundary_id and selected_boundary_id and selected_boundary_id != expected_boundary_id:
            boundary_ok = False
        metrics["boundary_separation_score"] = 1.0 if boundary_ok else 0.0

    return metrics


def mean_applicable(values: Iterable[Optional[float]], default: float = 0.0) -> float:
    usable: List[float] = [float(v) for v in values if v is not None]
    if not usable:
        return default
    return sum(usable) / len(usable)


def aggregate_task_metrics(task_metrics: List[Dict[str, Optional[float]]]) -> Dict[str, float]:
    keys = [
        "source_attribution_accuracy",
        "false_memory_frequency",
        "fallback_correctness",
        "boundary_separation_score",
        "abstention_correctness",
    ]

    aggregate = {}
    for key in keys:
        default = 0.0
        if key == "false_memory_frequency":
            default = 0.0
        aggregate[key] = mean_applicable((m.get(key) for m in task_metrics), default=default)

    drift_values = [m.get("retrieval_drift") for m in task_metrics if m.get("retrieval_drift") is not None]
    omega_values = [m.get("omega") for m in task_metrics if m.get("omega") is not None]

    aggregate["mean_retrieval_drift"] = mean_applicable(drift_values, default=0.0)
    aggregate["mean_omega"] = mean_applicable(omega_values, default=0.0)
    aggregate["regression_frequency"] = 0.0
    aggregate["suite_score"] = suite_score(aggregate)
    return aggregate


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
