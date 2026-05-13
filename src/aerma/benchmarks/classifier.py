from typing import Dict, Any


def classify_claim(aerma_score: float, suite_score: float, regression_frequency: float) -> Dict[str, Any]:
    if aerma_score >= 1.0 and suite_score >= 0.90 and regression_frequency <= 0.05:
        label = "AERMA-A"
    elif aerma_score >= 0.80 and suite_score >= 0.70:
        label = "AERMA-B"
    elif suite_score < 0.70:
        label = "AERMA-C"
    elif aerma_score < 0.80:
        label = "AERMA-D"
    else:
        label = "AERMA-D"

    return {
        "classification": label,
        "aerma_score": aerma_score,
        "suite_score": suite_score,
        "regression_frequency": regression_frequency,
        "non_claim_locks": [
            "not_sentience",
            "not_consciousness",
            "not_human_memory",
            "not_clinical_memory",
            "not_biological_memory",
            "not_autonomous_self_improvement",
            "not_universal_ai_mechanism",
        ],
    }
