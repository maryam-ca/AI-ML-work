from statistics import mean


# Simple vague query check
def is_query_too_vague(question: str) -> bool:
    stripped = question.strip().lower()

    vague_queries = {
        "tell me",
        "explain",
        "what is this",
        "help",
        "answer this",
        "maloomat do",
    }

    if stripped in vague_queries:
        return True

    if len(stripped.split()) <= 1:
        return True

    return False


# Confidence calculation
def compute_confidence(results: list[dict]) -> dict:
    if not results:
        return {
            "top_score": 0.0,
            "avg_score": 0.0,
            "result_count": 0,
        }

    scores = [item["score"] for item in results]

    return {
        "top_score": max(scores),
        "avg_score": mean(scores),
        "result_count": len(results),
    }


# Main decision function
def choose_rag_action(question: str, results: list[dict]) -> dict:
    confidence = compute_confidence(results)

    # 1. Clarify case
    if is_query_too_vague(question):
        return {
            "action": "clarify",
            "reason": "Question is too vague.",
            "confidence": confidence,
        }

    # 2. Refuse cases
    if confidence["result_count"] < 2:
        return {
            "action": "refuse",
            "reason": "Not enough results.",
            "confidence": confidence,
        }

    if confidence["top_score"] < 0.55:
        return {
            "action": "refuse",
            "reason": "Top score too low.",
            "confidence": confidence,
        }

    if confidence["avg_score"] < 0.45:
        return {
            "action": "refuse",
            "reason": "Average score too low.",
            "confidence": confidence,
        }

    # 3. Answer case
    return {
        "action": "answer",
        "reason": "Enough data available.",
        "confidence": confidence,
    }
