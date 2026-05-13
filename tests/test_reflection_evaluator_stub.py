from aerma.agent.reflection_evaluator_stub import ReflectionEvaluatorStub


def test_reflection_evaluator_stub():
    result = ReflectionEvaluatorStub().evaluate()
    assert result["reflection_executed"] is False
