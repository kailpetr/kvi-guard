class RiskEngine:
    def analyze(self, text: str) -> float:
        risk_keywords = [
            "uncertain",
            "possibly",
            "not verified",
            "conflicting"
        ]

        score = 0.0

        for keyword in risk_keywords:
            if keyword in text.lower():
                score += 0.2

        return min(score, 1.0)
