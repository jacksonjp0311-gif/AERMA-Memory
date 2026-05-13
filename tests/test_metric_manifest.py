from aerma.core.metric_manifest import MetricManifest


def test_metric_manifest_defaults():
    manifest = MetricManifest()
    assert manifest.drift_fallback_threshold > manifest.drift_allow_threshold
    assert "source_attribution_accuracy" in manifest.primary_metrics
