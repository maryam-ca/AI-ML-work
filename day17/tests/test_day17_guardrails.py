from app.guardrails import choose_rag_action, is_query_too_vague


def test_vague_query():
    assert is_query_too_vague("help") is True


def test_refuse_when_no_results():
    decision = choose_rag_action("what is this", [])
    assert decision["action"] in {"clarify", "refuse"}


def test_answer_when_good_results():
    results = [
        {"score": 0.9},
        {"score": 0.8},
        {"score": 0.85},
    ]

    decision = choose_rag_action("What is AI?", results)
    assert decision["action"] == "answer"
