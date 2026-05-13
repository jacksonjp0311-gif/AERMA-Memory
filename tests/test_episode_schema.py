from aerma.core.episode import AgentEpisode


def test_episode_fingerprint():
    episode = AgentEpisode(
        episode_id="E001",
        context="ctx",
        content="content",
        time="2026-01-01T00:00:00",
        source_ref="doc://x",
        ledger_ref="L001",
    )
    assert episode.ensure_fingerprint()
