from app.providers.openai_provider import OpenAIProvider
from app.engines.semantic_similarity import SemanticSimilarityEngine
from app.engines.risk_engine import RiskEngine


class SafeGenerateService:
    def __init__(self):
        self.provider = OpenAIProvider()
        self.similarity = SemanticSimilarityEngine()
        self.risk_engine = RiskEngine()

    def generate(self, prompt: str):
        responses = [
            self.provider.generate(prompt),
            self.provider.generate(prompt),
            self.provider.generate(prompt)
        ]

        similarity_score = self.similarity.compare(
            responses[0],
            responses[1]
        )

        risk_score = self.risk_engine.analyze(
            ' '.join(responses)
        )

        confidence = max(0.0, min(1.0, similarity_score - risk_score))

        return {
            "responses": responses,
            "confidence": round(confidence, 2),
            "risk": round(risk_score, 2),
            "selected_response": responses[0]
        }
