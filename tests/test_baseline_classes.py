from aerma.benchmarks.baselines import default_baselines


def test_baseline_classes_exist():
    baselines = default_baselines()
    names = [b.name for b in baselines]
    assert "database_lookup" in names
    assert "vector_only" in names
    assert "ungated_memory" in names
    assert "random_control" in names
