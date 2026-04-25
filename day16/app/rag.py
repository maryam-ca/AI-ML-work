from .retrieval import dual_query_search


def answer_with_rag(question):
    data = dual_query_search(question)

    context = " ".join([r["text"] for r in data["results"]])

    if context:
        answer = f"Based on data: {context}"
    else:
        answer = "No answer found."

    return {
        "question": question,
        "normalized_query": data["normalized_query"],
        "answer": answer,
        "sources": data["results"],
    }
