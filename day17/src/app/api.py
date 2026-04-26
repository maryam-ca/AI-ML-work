from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import answer_with_rag

app = FastAPI()


class Query(BaseModel):
    question: str


@app.post("/rag")
def rag_api(query: Query):
    return answer_with_rag(query.question)
