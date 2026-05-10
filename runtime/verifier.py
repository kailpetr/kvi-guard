from runtime.truth_engine import truth_alignment
from runtime.contradiction_detector import detect_contradictions
from runtime.domain_classifier import classify_domains
from runtime.cognitive_telemetry import analyze_telemetry
from runtime.knowledge_loader import load_knowledge_domains


STABLE_THRESHOLD = 0.85
WARNING_THRESHOLD = 0.65
UNSTABLE_THRESHOLD = 0.40


KNOWLEDGE_DOMAINS = load_knowledge_domains()


class VerificationResult:

    def __init__(self):
        self.score = 1.0
        self.warnings = []
        self.telemetry = {}
        self.state = "STABLE"

    def apply_penalty(self, amount: float, warning: str):
        self.score -= amount
        self.warnings.append(warning)

    def apply_bonus(self, amount: float):
        self.score += amount

    def finalize(self):

        self.score = round(min(max(self.score, 0.0), 1.0), 2)

        if self.score >= STABLE_THRESHOLD:
            self.state = "STABLE"
        elif self.score >= WARNING_THRESHOLD:
            self.state = "WARNING"
        elif self.score >= UNSTABLE_THRESHOLD:
            self.state = "UNSTABLE"
        else:
            self.state = "CRITICAL"

        return {
            "score": self.score,
            "state": self.state,
            "warnings": self.warnings,
            "telemetry": self.telemetry
        }


def detect_domain_density(text: str):

    lowered = text.lower()
    matches = {}

    for domain, data in KNOWLEDGE_DOMAINS.items():

        anchors = data.get("anchors", [])

        count = 0

        for anchor in anchors:
            if anchor.lower() in lowered:
                count += 1

        if count > 0:
            matches[domain] = count

    return matches


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
            result.apply_penalty(0.15, f"hallucination risk: {term}")

    for term in contradiction_terms:
        if term in lowered:
            result.apply_penalty(0.25, f"contradiction detected: {term}")

    alignment = truth_alignment(text, "sky_blue")
    contradictions = detect_contradictions(text)
    domains = classify_domains(text)
    telemetry = analyze_telemetry(text)
    domain_density = detect_domain_density(text)

    entropy = telemetry.get("entropy", 0)
    collision_risk = domains.get("collision_risk", 0)
    contradiction_risk = contradictions.get("risk", 0)
    alignment_score = alignment.get("alignment", 0)

    unstable_signal_count = 0

    if alignment_score < 0.25:
        unstable_signal_count += 1

    if entropy > 0.6:
        unstable_signal_count += 1

    if collision_risk > 0:
        unstable_signal_count += 1

    if contradiction_risk > 0:
        unstable_signal_count += 1

    if len(domain_density.keys()) > 2:
        unstable_signal_count += 1
        result.apply_penalty(0.05, "high semantic domain mixing")

    if unstable_signal_count >= 2:
        result.apply_penalty(0.15, "multi-signal instability")

    if contradiction_risk > 0:
        result.apply_penalty(contradiction_risk, "semantic contradiction detected")

    if collision_risk > 0:
        result.apply_penalty(collision_risk, "domain collision risk")

    if entropy > 0.75:
        result.apply_penalty(0.1, "entropy escalation")

    stable_structure = 0

    if entropy < 0.3:
        stable_structure += 1

    if contradiction_risk == 0:
        stable_structure += 1

    if collision_risk == 0:
        stable_structure += 1

    if stable_structure >= 2:
        result.apply_bonus(0.1)

    result.telemetry = {
        "entropy": entropy,
        "signals": telemetry.get("signals", {}),
        "domains": domain_density,
        "alignment": alignment_score,
        "unstable_signal_count": unstable_signal_count,
        "stable_structure": stable_structure
    }

    return result.finalize()
