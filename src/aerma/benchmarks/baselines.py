from typing import Dict, List, Any
import random

from aerma.core.episode import AgentEpisode
from aerma.core.retrieval_engine import RetrievalEngine


class Baseline:
    name = "baseline"

    def retrieve(self, query: str, episodes: List[AgentEpisode], config: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError


class DatabaseLookupBaseline(Baseline):
    name = "database_lookup"

    def retrieve(self, query: str, episodes: List[AgentEpisode], config: Dict[str, Any]) -> Dict[str, Any]:
        q = query.lower()
        for episode in episodes:
            if episode.context.lower() in q or episode.episode_id.lower() in q:
                return {
                    "baseline_name": self.name,
                    "selected_episode_id": episode.episode_id,
                    "selected_source_ref": episode.source_ref,
                    "score": 1.0,
                }
        return {
            "baseline_name": self.name,
            "selected_episode_id": None,
            "selected_source_ref": None,
            "score": 0.0,
        }


class VectorOnlyBaseline(Baseline):
    name = "vector_only"

    def retrieve(self, query: str, episodes: List[AgentEpisode], config: Dict[str, Any]) -> Dict[str, Any]:
        engine = RetrievalEngine()
        candidates = engine.retrieve(query, episodes, top_k=1)
        if not candidates:
            return {
                "baseline_name": self.name,
                "selected_episode_id": None,
                "selected_source_ref": None,
                "score": 0.0,
            }
        candidate = candidates[0]
        return {
            "baseline_name": self.name,
            "selected_episode_id": candidate.episode.episode_id,
            "selected_source_ref": candidate.episode.source_ref,
            "score": candidate.score,
        }


class UngatedMemoryBaseline(VectorOnlyBaseline):
    name = "ungated_memory"


class RandomControlBaseline(Baseline):
    name = "random_control"

    def retrieve(self, query: str, episodes: List[AgentEpisode], config: Dict[str, Any]) -> Dict[str, Any]:
        seed = int(config.get("seed", 42))
        rng = random.Random(seed)
        if not episodes:
            return {
                "baseline_name": self.name,
                "selected_episode_id": None,
                "selected_source_ref": None,
                "score": 0.0,
            }
        episode = rng.choice(episodes)
        return {
            "baseline_name": self.name,
            "selected_episode_id": episode.episode_id,
            "selected_source_ref": episode.source_ref,
            "score": 0.0,
        }


def default_baselines() -> List[Baseline]:
    return [
        DatabaseLookupBaseline(),
        VectorOnlyBaseline(),
        UngatedMemoryBaseline(),
        RandomControlBaseline(),
    ]
