FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip \
 && python -m pip install "fastapi[standard]" \
    pydantic-settings \
    "psycopg[binary]" \
    qdrant-client

EXPOSE 8000

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
