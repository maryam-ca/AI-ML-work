from day18.agent import build_agent_plan, run_agent_loop


def test_plan_exists():

    plan = build_agent_plan("What is AI?")

    assert isinstance(plan, list)

    assert len(plan) >= 4


def test_answer_case():

    result = run_agent_loop("What is Qdrant?")

    assert result["action"] == "answer"


def test_clarify_case():

    result = run_agent_loop("help")

    assert result["action"] == "clarify"
