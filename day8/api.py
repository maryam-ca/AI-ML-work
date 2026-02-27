import os

from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = os.getenv("API_KEY", "default-key")


@app.get("/")
def root():
    return {"message": "Day 8 Docker API Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/secure-data")
def secure_data(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"secret": "This is secure data"}
