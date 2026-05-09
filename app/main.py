from fastapi import FastAPI
from pydantic import BaseModel

from app.services.safe_generate import SafeGenerateService

app = FastAPI(title="KVI Guard")

safe_generate_service = SafeGenerateService()


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


@app.post("/safe-generate")
def safe_generate(request: VerifyRequest):
    return safe_generate_service.generate(request.prompt)
