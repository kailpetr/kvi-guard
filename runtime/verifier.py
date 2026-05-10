from runtime.truth_engine import truth_alignment
from runtime.contradiction_detector import detect_contradictions
from runtime.domain_classifier import classify_domains
from runtime.cognitive_telemetry import analyze_telemetry
from runtime.knowledge_loader import load_knowledge_domains
from runtime.confidence import confidence_band
from runtime.topic_router import detect_topic


KNOWLEDGE_DOMAINS = load_knowledge_domains()


class VerificationResult:

    def __init__(self):
        self.score = 1.0
        self.risk = 0.0
        self.warnings = []
        self.telemetry = {}
        self.state = "STABLE"
        self.confidence_band = "HIGH"

    def add_risk(self, amount: float, warning: str):
        self.risk += amount

        if warning not in self.warnings:
            self.warnings.append(warning)

    def finalize(self):

        self.risk = round(min(max(self.risk, 0.0), 1.0), 2)

        self.score = round(1.0 - self.risk, 2)

        if self.risk >= 0.75:
            self.state = "CRITICAL"
        elif self.risk >= 0.45:
            self.state = "UNSTABLE"
        elif self.risk >= 0.20:
            self.state = "WARNING"
        else:
            self.state = "STABLE"

        self.confidence_band = confidence_band(self.score)

        return {
            "score": self.score,
            "risk": self.risk,
            "confidence_band": self.confidence_band,
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
            result.add_risk(0.30, f"hallucination risk: {term}")

    for term in contradiction_terms:
        if term in lowered:
            result.add_risk(0.45, f"contradiction detected: {term}")

    detected_topic = detect_topic(text)

    if detected_topic == "unknown":
        alignment = {
            "alignment": 0.5,
            "matched": [],
            "missing": []
        }
    else:
        alignment = truth_alignment(text, detected_topic)

    contradictions = detect_contradictions(text)
    domains = classify_domains(text)
    telemetry = analyze_telemetry(text)
    domain_density = detect_domain_density(text)

    entropy = telemetry.get("entropy", 0)
    collision_risk = domains.get("collision_risk", 0)
    contradiction_risk = contradictions.get("risk", 0)
    alignment_score = alignment.get("alignment", 0.5)

    unstable_signal_count = 0

    if alignment_score < 0.10:
        unstable_signal_count += 1
        result.add_risk(0.35, "truth anchor divergence")

    elif alignment_score < 0.25:
        unstable_signal_count += 1
        result.add_risk(0.15, "weak semantic alignment")

    if entropy > 0.2:
        unstable_signal_count += 1
        result.add_risk(0.15, "entropy instability")

    if collision_risk > 0:
        unstable_signal_count += 1
        result.add_risk(0.25, "domain collision risk")

    if contradiction_risk > 0:
        unstable_signal_count += 1
        result.add_risk(0.40, "semantic contradiction detected")

    signal_map = telemetry.get("signals", {})

    collapse_count = signal_map.get("collapse", 0)
    instability_count = signal_map.get("instability", 0)
    overconfidence_count = signal_map.get("overconfidence", 0)

    if collapse_count > 0 and alignment_score < 0.10:
        result.add_risk(collapse_count * 0.08, "semantic collapse")

    if instability_count > 0:
        result.add_risk(instability_count * 0.20, "instability accumulation")

    if overconfidence_count > 0:
        result.add_risk(overconfidence_count * 0.10, "overconfidence pressure")

    if len(domain_density.keys()) >= 2:
        unstable_signal_count += 1
        result.add_risk(0.20, "cross-domain semantic drift")

    result.telemetry = {
        "topic": detected_topic,
        "entropy": entropy,
        "signals": signal_map,
        "domains": domain_density,
        "alignment": alignment_score,
        "unstable_signal_count": unstable_signal_count
    }

    return result.finalize()
