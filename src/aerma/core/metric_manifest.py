from dataclasses import dataclass
from typing import List


@dataclass
class MetricManifest:
    drift_allow_threshold: float = 0.45
    drift_fallback_threshold: float = 0.60
    suite_score_threshold: float = 0.90
    regression_threshold: float = 0.05
    primary_metrics: List[str] = None

    def __post_init__(self) -> None:
        if self.primary_metrics is None:
            self.primary_metrics = [
                "source_attribution_accuracy",
                "false_memory_frequency",
                "fallback_correctness",
                "boundary_separation_score",
                "abstention_correctness",
            ]
