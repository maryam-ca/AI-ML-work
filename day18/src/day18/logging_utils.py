from day18.db import SessionLocal
from day18.models import AgentLog


def save_agent_log(question, action, reason, answer):

    db = SessionLocal()

    log = AgentLog(question=question, action=action, reason=reason, answer=answer)

    db.add(log)

    db.commit()

    db.close()
