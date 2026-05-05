from __future__ import annotations


def build_agent_plan(question: str) -> list[str]:

    return [
        "Inspect the user question",
        "Retrieve related information",
        "Judge if retrieved data is enough",
        "Generate final answer",
    ]


def retrieve_data(question: str) -> list[dict]:

    dummy_results = [
        {
            "doc_id": "doc1",
            "title": "Qdrant Database",
            "text": "Qdrant is a vector database used in AI systems.",
        },
        {
            "doc_id": "doc2",
            "title": "FastAPI",
            "text": "FastAPI is used for building APIs.",
        },
    ]

    return dummy_results


def judge_retrieval(question: str, results: list[dict]):

    if question.lower() == "help":
        return {"action": "clarify", "reason": "Question too short"}

    if len(results) == 0:
        return {"action": "refuse", "reason": "No evidence found"}

    return {"action": "answer", "reason": "Enough evidence found"}


def generate_answer(results: list[dict]):

    context = ""

    for item in results:
        context += item["text"] + "\n"

    return context


def run_agent_loop(question: str):

    plan = build_agent_plan(question)

    retrieved_results = retrieve_data(question)

    decision = judge_retrieval(question, retrieved_results)

    if decision["action"] == "clarify":
        return {
            "question": question,
            "plan": plan,
            "action": "clarify",
            "reason": decision["reason"],
            "answer": "Please ask a clearer question.",
        }

    if decision["action"] == "refuse":
        return {
            "question": question,
            "plan": plan,
            "action": "refuse",
            "reason": decision["reason"],
            "answer": "I cannot answer safely.",
        }

    answer = generate_answer(retrieved_results)

    return {
        "question": question,
        "plan": plan,
        "action": "answer",
        "reason": decision["reason"],
        "answer": answer,
    }
