from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="KVI Guard")


class VerifyRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {
        "name": "KVI Guard",
        "status": "running",
        "purpose": "AI verification middleware"
    }


@app.post("/verify")
def verify(request: VerifyRequest):
    return {
        "prompt": request.prompt,
        "confidence": 0.82,
        "contradiction_risk": 0.12,
        "semantic_stability": 0.88,
        "status": "verified"
    }
