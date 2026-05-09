from app.providers.openai_provider import OpenAIProvider
from app.engines.embedding_similarity import EmbeddingSimilarityEngine
from app.engines.risk_engine import RiskEngine
from app.engines.contradiction_detector import ContradictionDetector


class SafeGenerateService:
    def __init__(self):
        self.provider = OpenAIProvider()
        self.similarity = EmbeddingSimilarityEngine()
        self.risk_engine = RiskEngine()
        self.contradiction_detector = ContradictionDetector()

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

        contradiction_result = self.contradiction_detector.analyze(
            responses
        )

        risk_score = self.risk_engine.analyze(
            ' '.join(responses)
        )

        contradiction_score = contradiction_result[
            "contradiction_score"
        ]

        confidence = max(
            0.0,
            min(
                1.0,
                similarity_score - risk_score - contradiction_score
            )
        )

        return {
            "responses": responses,
            "confidence": round(confidence, 2),
            "risk": round(risk_score, 2),
            "semantic_similarity": round(similarity_score, 2),
            "contradiction_analysis": contradiction_result,
            "selected_response": responses[0]
        }
