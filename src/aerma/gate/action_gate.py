from dataclasses import dataclass
from typing import Optional

from aerma.core.metric_manifest import MetricManifest
from aerma.drift.drift_geometry import DriftReport


@dataclass
class GateDecision:
    decision: str
    reason: str
    caveat: Optional[str] = None


class ActionGate:
    def __init__(self, manifest: MetricManifest) -> None:
        self.manifest = manifest

    def decide(
        self,
        drift_report: DriftReport,
        expected_behavior: Optional[str] = None,
        ambiguous: bool = False,
        source_missing: bool = False,
    ) -> GateDecision:
        if expected_behavior in {"abstain", "fallback"}:
            return GateDecision("fallback", "task_expected_fallback_or_abstention")

        if ambiguous:
            return GateDecision("fallback", "ambiguous_retrieval")

        if source_missing:
            return GateDecision("fallback", "source_missing")

        if drift_report.retrieval_drift >= self.manifest.drift_fallback_threshold:
            return GateDecision("fallback", "retrieval_drift_exceeded_fallback_threshold")

        if drift_report.retrieval_drift >= self.manifest.drift_allow_threshold:
            return GateDecision(
                "allow_with_caveat",
                "retrieval_drift_requires_caveat",
                caveat="Retrieved memory should be treated as source-bound and caveated.",
            )

        return GateDecision("allow", "retrieval_within_threshold")
