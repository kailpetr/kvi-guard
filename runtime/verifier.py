from runtime.truth_engine import truth_alignment
from runtime.contradiction_detector import detect_contradictions
from runtime.domain_classifier import classify_domains
from runtime.cognitive_telemetry import analyze_telemetry


STABLE_THRESHOLD = 0.85
UNSTABLE_THRESHOLD = 0.60


class VerificationResult:

    def __init__(self):
        self.score = 1.0
        self.warnings = []
        self.telemetry = {}
        self.state = "STABLE"

    def apply_penalty(self, amount: float, warning: str):
        self.score -= amount
        self.warnings.append(warning)

    def finalize(self):
        self.score = round(max(self.score, 0.0), 2)

        if self.score > STABLE_THRESHOLD:
            self.state = "STABLE"
        elif self.score > UNSTABLE_THRESHOLD:
            self.state = "UNSTABLE"
        else:
            self.state = "CRITICAL"

        return {
            "score": self.score,
            "state": self.state,
            "warnings": self.warnings,
            "telemetry": self.telemetry
        }


def verify_response(text: str):

    result = VerificationResult()

    hallucination_terms = [
        "dragons existed",
        "mars olympics",
        "quantum pyramid"
    ]

    contradiction_terms = [
        "flat earth",
        "2+2=5"
    ]

    lowered = text.lower()

    for term in hallucination_terms:
        if term in lowered:
            result.apply_penalty(0.2, f"hallucination risk: {term}")

    for term in contradiction_terms:
        if term in lowered:
            result.apply_penalty(0.3, f"contradiction detected: {term}")

    alignment = truth_alignment(text, "sky_blue")

    if alignment.get("alignment", 0) < 0.5:
        result.apply_penalty(0.3, "truth-anchor divergence")

    contradictions = detect_contradictions(text)

    if contradictions.get("risk", 0) > 0:
        result.apply_penalty(
            contradictions["risk"],
            "semantic contradiction detected"
        )

    domains = classify_domains(text)

    if domains.get("collision_risk", 0) > 0:
        result.apply_penalty(
            domains["collision_risk"],
            "domain collision risk"
        )

    telemetry = analyze_telemetry(text)

    if telemetry.get("entropy", 0) > 0.6:
        result.apply_penalty(0.2, "entropy escalation")

    result.telemetry = {
        "entropy": telemetry.get("entropy", 0),
        "signals": telemetry.get("signals", {})
    }

    return result.finalize()
