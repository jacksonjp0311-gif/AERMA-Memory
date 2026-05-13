from __future__ import annotations

from typing import Any, Dict


def classify_claim(
    aerma_score: float,
    suite_score: float,
    regression_frequency: float,
    false_memory_frequency: float = 0.0,
    fallback_correctness: float = 0.0,
    abstention_correctness: float = 0.0,
    source_attribution_accuracy: float = 0.0,
    boundary_separation_score: float = 0.0,
) -> Dict[str, Any]:
    """Downgrade-preserving AERMA classification.

    AERMA-A is intentionally unreachable for the current scaffold unless the
    implementation completeness score reaches 1.0 and all primary evidence
    surfaces are near-perfect. AERMA-B now requires actual suite performance,
    not just scaffold existence.
    """

    reasons = []

    if false_memory_frequency > 0.0:
        reasons.append("false_memory_detected")

    if suite_score < 0.90:
        reasons.append("suite_score_below_B_threshold")

    if fallback_correctness < 0.90:
        reasons.append("fallback_correctness_below_B_threshold")

    if abstention_correctness < 0.90:
        reasons.append("abstention_correctness_below_B_threshold")

    if source_attribution_accuracy < 0.90:
        reasons.append("source_attribution_below_B_threshold")

    if boundary_separation_score < 0.90:
        reasons.append("boundary_separation_below_B_threshold")

    if regression_frequency > 0.05:
        reasons.append("regression_frequency_too_high")

    if (
        aerma_score >= 1.0
        and suite_score >= 0.95
        and regression_frequency <= 0.02
        and false_memory_frequency == 0.0
        and fallback_correctness >= 0.95
        and abstention_correctness >= 0.95
        and source_attribution_accuracy >= 0.95
        and boundary_separation_score >= 0.95
    ):
        label = "AERMA-A"
        classification_reason = "audit_grade_reference_evidence_threshold_met"
    elif (
        aerma_score >= 0.85
        and suite_score >= 0.90
        and regression_frequency <= 0.05
        and false_memory_frequency == 0.0
        and fallback_correctness >= 0.90
        and abstention_correctness >= 0.90
        and source_attribution_accuracy >= 0.90
        and boundary_separation_score >= 0.90
    ):
        label = "AERMA-B"
        classification_reason = "reference_scaffold_threshold_met_with_negative_controls"
    elif suite_score >= 0.70:
        label = "AERMA-C"
        classification_reason = "partial_runtime_evidence_but_not_B_threshold"
    elif aerma_score >= 0.50:
        label = "AERMA-D"
        classification_reason = "implementation_exists_but_evidence_is_insufficient"
    else:
        label = "AERMA-E"
        classification_reason = "insufficient_or_overextended_claim_surface"

    return {
        "classification": label,
        "classification_reason": classification_reason,
        "downgrade_reasons": reasons,
        "aerma_score": aerma_score,
        "suite_score": suite_score,
        "regression_frequency": regression_frequency,
        "false_memory_frequency": false_memory_frequency,
        "fallback_correctness": fallback_correctness,
        "abstention_correctness": abstention_correctness,
        "source_attribution_accuracy": source_attribution_accuracy,
        "boundary_separation_score": boundary_separation_score,
        "non_claim_locks": [
            "not_sentience",
            "not_consciousness",
            "not_human_memory",
            "not_clinical_memory",
            "not_biological_memory",
            "not_autonomous_self_improvement",
            "not_universal_ai_mechanism",
            "coherence_is_not_truth",
            "suite_execution_is_not_production_readiness",
        ],
    }
