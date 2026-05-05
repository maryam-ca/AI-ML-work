from day18.db import SessionLocal
from day18.models import AgentLog


def show_logs():

    db = SessionLocal()

    logs = db.query(AgentLog).all()

    print("\n===== AGENT LOGS =====\n")

    for log in logs:
        print("=" * 50)

        print("Question:", log.question)

        print("Action:", log.action)

        print("Reason:", log.reason)

        print("Answer:", log.answer)

    db.close()


show_logs()
