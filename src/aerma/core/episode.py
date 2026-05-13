from dataclasses import dataclass, field
from typing import Any, Dict, Optional
import hashlib
import json


@dataclass
class AgentEpisode:
    episode_id: str
    context: str
    content: str
    time: str
    source_ref: str
    ledger_ref: str
    claim_class: str = "source_bound_note"
    boundary_id: Optional[str] = None
    agent_state: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    fingerprint: Optional[str] = None

    def compute_fingerprint(self) -> str:
        payload = {
            "episode_id": self.episode_id,
            "context": self.context,
            "content": self.content,
            "time": self.time,
            "source_ref": self.source_ref,
            "ledger_ref": self.ledger_ref,
            "claim_class": self.claim_class,
            "boundary_id": self.boundary_id,
        }
        raw = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def ensure_fingerprint(self) -> str:
        if not self.fingerprint:
            self.fingerprint = self.compute_fingerprint()
        return self.fingerprint

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AgentEpisode":
        episode = cls(
            episode_id=data["episode_id"],
            context=data.get("context", ""),
            content=data.get("content", ""),
            time=data.get("time", ""),
            source_ref=data.get("source_ref", ""),
            ledger_ref=data.get("ledger_ref", ""),
            claim_class=data.get("claim_class", "source_bound_note"),
            boundary_id=data.get("boundary_id"),
            agent_state=data.get("agent_state", {}),
            metadata=data.get("metadata", {}),
            fingerprint=data.get("fingerprint"),
        )
        episode.ensure_fingerprint()
        return episode

    def to_dict(self) -> Dict[str, Any]:
        self.ensure_fingerprint()
        return {
            "episode_id": self.episode_id,
            "context": self.context,
            "content": self.content,
            "time": self.time,
            "source_ref": self.source_ref,
            "ledger_ref": self.ledger_ref,
            "claim_class": self.claim_class,
            "boundary_id": self.boundary_id,
            "agent_state": self.agent_state,
            "metadata": self.metadata,
            "fingerprint": self.fingerprint,
        }
