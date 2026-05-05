from fastapi import FastAPI
from pydantic import BaseModel

from day18.agent import run_agent_loop
from day18.logging_utils import save_agent_log

app = FastAPI(title="Day18 Agent Loop API")


class AgentRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Day18 Agent API Running"}


@app.post("/agent-rag")
def agent_rag(payload: AgentRequest):

    result = run_agent_loop(payload.question)

    # Save logs in database
    save_agent_log(
        result["question"], result["action"], result["reason"], result["answer"]
    )

    return result
