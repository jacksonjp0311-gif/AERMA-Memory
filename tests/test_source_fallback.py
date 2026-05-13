from aerma.gate.source_fallback import SourceFallback


def test_source_fallback():
    result = SourceFallback().fallback("ambiguous")
    assert result.decision == "fallback"
