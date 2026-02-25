from fastapi import FastAPI, Header, HTTPException

from .settings import settings

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/config")
def config():
    return {"app_name": settings.app_name}


@app.get("/secure-data")
def secure_data(x_api_key: str | None = Header(default=None)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {"message": "Protected data access granted"}
