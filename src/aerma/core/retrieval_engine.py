from dataclasses import dataclass
from typing import List
import re

from aerma.core.episode import AgentEpisode


@dataclass
class RetrievalCandidate:
    episode: AgentEpisode
    score: float


class RetrievalEngine:
    def tokenize(self, text: str) -> set[str]:
        return set(re.findall(r"[a-zA-Z0-9_]+", text.lower()))

    def lexical_score(self, query: str, episode: AgentEpisode) -> float:
        q = self.tokenize(query)
        e = self.tokenize(" ".join([episode.context, episode.content, episode.source_ref]))
        if not q or not e:
            return 0.0
        return len(q & e) / len(q | e)

    def retrieve(self, query: str, episodes: List[AgentEpisode], top_k: int = 3) -> List[RetrievalCandidate]:
        candidates = [
            RetrievalCandidate(episode=episode, score=self.lexical_score(query, episode))
            for episode in episodes
        ]
        candidates.sort(key=lambda item: item.score, reverse=True)
        return candidates[:top_k]
