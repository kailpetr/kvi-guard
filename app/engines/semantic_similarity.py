from difflib import SequenceMatcher


class SemanticSimilarityEngine:
    def compare(self, a: str, b: str) -> float:
        return SequenceMatcher(None, a, b).ratio()
