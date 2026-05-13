from aerma.evidence.evidence_package import EvidencePackageCompiler


def test_evidence_package(tmp_path):
    path = tmp_path / "evidence.json"
    package = EvidencePackageCompiler().compile(path, {"ok": True})
    assert path.exists()
    assert package["package_type"] == "AERMA-v1.2-evidence-package"
