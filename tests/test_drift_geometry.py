from aerma.drift.drift_geometry import DriftGeometryEngine


def test_drift_geometry_dimensionless():
    report = DriftGeometryEngine().compute(0.75)
    assert 0.0 <= report.retrieval_drift <= 1.0
    assert 0.0 < report.omega <= 1.0
