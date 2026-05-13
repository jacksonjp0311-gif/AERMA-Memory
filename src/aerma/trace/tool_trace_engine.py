from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class ToolTraceRecord:
    event_type: str
    payload: Dict[str, Any]
    timestamp: str

    @classmethod
    def create(cls, event_type: str, payload: Dict[str, Any]) -> "ToolTraceRecord":
        return cls(
            event_type=event_type,
            payload=payload,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
