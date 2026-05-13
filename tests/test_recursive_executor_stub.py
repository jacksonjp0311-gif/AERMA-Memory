from aerma.agent.recursive_executor_stub import RecursiveExecutorStub


def test_recursive_executor_stub():
    result = RecursiveExecutorStub().run("test")
    assert result["recursion_executed"] is False
