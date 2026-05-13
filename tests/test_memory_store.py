from aerma.core.episode import AgentEpisode
from aerma.core.memory_store import AgentMemoryStore


def test_memory_store_add_get():
    store = AgentMemoryStore()
    episode = AgentEpisode(
        episode_id="E001",
        context="ctx",
        content="content",
        time="2026-01-01T00:00:00",
        source_ref="doc://x",
        ledger_ref="L001",
    )
    store.add_episode(episode)
    assert len(store) == 1
    assert store.get_episode("E001") is not None
