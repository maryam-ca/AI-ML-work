from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/ready")
def ready_health():
    return {"status": "ready"}
