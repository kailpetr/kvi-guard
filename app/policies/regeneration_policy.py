class RegenerationPolicy:
    def __init__(self, confidence_threshold: float = 0.45):
        self.confidence_threshold = confidence_threshold

    def should_regenerate(self, confidence: float) -> bool:
        return confidence < self.confidence_threshold
