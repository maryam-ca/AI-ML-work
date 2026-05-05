from sqlalchemy import Column, Integer, String, Text

from day18.db import Base


class AgentLog(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True)

    question = Column(Text)

    action = Column(String)

    reason = Column(Text)

    answer = Column(Text)
