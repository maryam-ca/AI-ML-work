from fastapi import FastAPI

from .rag import answer_with_rag

app = FastAPI()


@app.get("/rag")
def rag(question: str):
    return answer_with_rag(question)
