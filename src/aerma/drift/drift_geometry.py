from dataclasses import dataclass


@dataclass
class DriftReport:
    retrieval_score: float
    retrieval_drift: float
    omega: float


class DriftGeometryEngine:
    def compute(self, retrieval_score: float) -> DriftReport:
        score = max(0.0, min(1.0, retrieval_score))
        drift = 1.0 - score
        omega = 1.0 / (1.0 + abs(drift))
        return DriftReport(
            retrieval_score=score,
            retrieval_drift=drift,
            omega=omega,
        )
