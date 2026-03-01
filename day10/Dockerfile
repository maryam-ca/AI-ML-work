FROM python:3.12-slim

WORKDIR /app

COPY src/ ./src/

RUN python -m pip install --upgrade pip \
 && python -m pip install \
 fastapi[standard] \
 pydantic-settings \
 psycopg[binary] \
 sqlalchemy \
 alembic

EXPOSE 8000

CMD ["uvicorn", "src.app.api:app", "--host", "0.0.0.0", "--port", "8000"]
