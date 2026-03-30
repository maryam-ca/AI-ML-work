from fastapi import FastAPI, HTTPException

from app.rag import answer_with_rag
from app.schema import RagRequest, RagResponse

app = FastAPI(title="RAG API Day15")


@app.post("/rag", response_model=RagResponse)
def rag_endpoint(payload: RagRequest):
    try:
        result = answer_with_rag(payload.question, payload.limit)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RAG failed: {e}") from e
