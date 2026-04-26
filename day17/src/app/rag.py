from app.db import SessionLocal
from app.guardrails import choose_rag_action
from app.logging_utils import create_log


def fake_retrieval(question: str):
    if "qdrant" in question.lower():
        return [
            {"score": 0.9},
            {"score": 0.8},
        ]

    if "unknown" in question.lower():
        return []

    return [{"score": 0.4}]


def answer_with_rag(question: str):
    db = SessionLocal()

    results = fake_retrieval(question)
    decision = choose_rag_action(question, results)

    confidence = decision["confidence"]

    response = {}

    if decision["action"] == "clarify":
        response = {
            "action": "clarify",
            "reason": decision["reason"],
            "answer": "Please clarify your question.",
        }

    elif decision["action"] == "refuse":
        response = {
            "action": "refuse",
            "reason": decision["reason"],
            "answer": "Not enough information.",
        }

    else:
        response = {
            "action": "answer",
            "reason": decision["reason"],
            "answer": "Generated answer.",
        }

    # 🔥 LOG SAVE
    create_log(
        db,
        {
            "question": question,
            "action": response["action"],
            "reason": response["reason"],
            "answer": response["answer"],
            "top_score": confidence["top_score"],
            "avg_score": confidence["avg_score"],
            "result_count": confidence["result_count"],
        },
    )

    db.close()

    return response
