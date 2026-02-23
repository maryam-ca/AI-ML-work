from app.settings import get_settings
from fastapi import FastAPI, Header, HTTPException

settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/config")
def config():
    s = get_settings()
    return {
        "app_name": s.app_name,
        "environment": s.environment,
        "debug": s.debug,
        "host": s.host,
        "port": s.port,
        "allowed_origins": s.allowed_origins,
    }


@app.get("/secure-data")
def secure_data(x_api_key: str | None = Header(default=None)):
    s = get_settings()
    if x_api_key != s.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return {"secret_data": "approved"}
