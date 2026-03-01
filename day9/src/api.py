import psycopg
from fastapi import FastAPI, Header, HTTPException
from qdrant_client import QdrantClient
from src.settings import get_settings

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/config")
async def config():
    s = get_settings()
    return {
        "app_name": s.app_name,
        "environment": s.environment,
        "debug": s.debug,
    }


@app.get("/secure-data")
async def secure_data(x_api_key: str = Header(None)):
    s = get_settings()
    if x_api_key != s.api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"secret": "This is protected data"}


@app.get("/db/health")
async def db_health():
    s = get_settings()
    try:
        with psycopg.connect(s.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                cur.fetchone()
        return {"postgres": "ok"}
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"postgres not ready: {e}",
        ) from e


@app.get("/qdrant/health")
async def qdrant_health():
    s = get_settings()
    try:
        client = QdrantClient(url=s.qdrant_url)
        client.get_collections()
        return {"qdrant": "ok"}
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"qdrant not ready: {e}",
        ) from e
