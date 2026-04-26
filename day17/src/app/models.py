from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from app.db import Base


class RagLog(Base):
    __tablename__ = "rag_logs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    action = Column(String)
    reason = Column(Text)
    answer = Column(Text)

    top_score = Column(Float)
    avg_score = Column(Float)
    result_count = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)
