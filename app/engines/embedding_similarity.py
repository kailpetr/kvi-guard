from sentence_transformers import SentenceTransformer
from numpy import dot
from numpy.linalg import norm


class EmbeddingSimilarityEngine:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def compare(self, a: str, b: str) -> float:
        embedding_a = self.model.encode(a)
        embedding_b = self.model.encode(b)

        similarity = dot(embedding_a, embedding_b) / (
            norm(embedding_a) * norm(embedding_b)
        )

        return float(similarity)
