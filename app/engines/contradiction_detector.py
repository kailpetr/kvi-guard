from sentence_transformers import SentenceTransformer
from numpy import dot
from numpy.linalg import norm


class ContradictionDetector:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def _similarity(self, a: str, b: str) -> float:
        emb_a = self.model.encode(a)
        emb_b = self.model.encode(b)

        return float(
            dot(emb_a, emb_b) /
            (norm(emb_a) * norm(emb_b))
        )

    def analyze(self, responses: list[str]) -> dict:
        if len(responses) < 2:
            return {
                "contradiction_score": 0.0,
                "status": "insufficient_data"
            }

        similarities = []

        for i in range(len(responses)):
            for j in range(i + 1, len(responses)):
                similarities.append(
                    self._similarity(responses[i], responses[j])
                )

        avg_similarity = sum(similarities) / len(similarities)
        contradiction_score = max(0.0, 1.0 - avg_similarity)

        return {
            "average_similarity": round(avg_similarity, 3),
            "contradiction_score": round(contradiction_score, 3),
            "status": "stable" if contradiction_score < 0.4 else "unstable"
        }
