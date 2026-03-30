from app.llm_client import generate_answer_from_prompt
from app.retrieval import search_chunks


def build_context(results):
    parts = []
    for idx, item in enumerate(results, start=1):
        parts.append(
            f"[Source {idx}]\n"
            f"doc_id: {item['doc_id']}\n"
            f"chunk_id: {item['chunk_id']}\n"
            f"title: {item['title']}\n"
            f"text: {item['text']}\n"
        )
    return "\n".join(parts)


def build_prompt(question, results):
    context = build_context(results)

    return f"""
Answer the question using ONLY the context below.

Question:
{question}

Context:
{context}

Rules:
- Use only the provided context
- Do not make up answers
- If answer is not found, say: "Not enough information"
- Mention sources like [Source 1]
""".strip()


def answer_with_rag(question, limit):
    results = search_chunks(question, limit)
    prompt = build_prompt(question, results)
    answer = generate_answer_from_prompt(prompt)

    return {"question": question, "answer": answer, "sources": results}
