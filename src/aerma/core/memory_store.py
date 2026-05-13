from typing import Dict, Iterable, List, Optional
from aerma.core.episode import AgentEpisode


class AgentMemoryStore:
    def __init__(self) -> None:
        self._episodes: Dict[str, AgentEpisode] = {}

    def add_episode(self, episode: AgentEpisode) -> None:
        episode.ensure_fingerprint()
        self._episodes[episode.episode_id] = episode

    def load_episodes(self, episodes: Iterable[AgentEpisode]) -> None:
        for episode in episodes:
            self.add_episode(episode)

    def get_episode(self, episode_id: str) -> Optional[AgentEpisode]:
        return self._episodes.get(episode_id)

    def all_episodes(self) -> List[AgentEpisode]:
        return list(self._episodes.values())

    def __len__(self) -> int:
        return len(self._episodes)
