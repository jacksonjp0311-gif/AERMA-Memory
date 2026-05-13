from dataclasses import dataclass


@dataclass
class FallbackResult:
    decision: str
    reason: str
    message: str


class SourceFallback:
    def fallback(self, reason: str) -> FallbackResult:
        return FallbackResult(
            decision="fallback",
            reason=reason,
            message="Insufficient or ambiguous source-bound evidence. Source check required before treating this as fact.",
        )

    def abstain(self, reason: str) -> FallbackResult:
        return FallbackResult(
            decision="abstain",
            reason=reason,
            message="The available memory evidence is insufficient. No factual answer should be promoted.",
        )
