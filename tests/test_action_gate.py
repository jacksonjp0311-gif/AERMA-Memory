from aerma.core.metric_manifest import MetricManifest
from aerma.drift.drift_geometry import DriftGeometryEngine
from aerma.gate.action_gate import ActionGate


def test_action_gate_fallback_on_high_drift():
    manifest = MetricManifest(drift_allow_threshold=0.45, drift_fallback_threshold=0.60)
    report = DriftGeometryEngine().compute(0.10)
    decision = ActionGate(manifest).decide(report)
    assert decision.decision == "fallback"
