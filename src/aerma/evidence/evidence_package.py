import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


class EvidencePackageCompiler:
    def compile(self, output_path: str | Path, payload: Dict[str, Any]) -> Dict[str, Any]:
        package = {
            "package_type": "AERMA-v1.2-evidence-package",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "payload": payload,
        }
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
        return package
