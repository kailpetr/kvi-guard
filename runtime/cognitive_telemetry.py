from collections import Counter


SIGNAL_PATTERNS = {
    "uncertainty": ["maybe", "possibly", "perhaps", "might"],
    "overconfidence": ["always", "certainly", "undeniable", "never wrong"],
    "instability": ["however", "but", "although", "on the other hand"],
    "collapse": ["impossible", "contradiction", "paradox"]
}


def analyze_telemetry(text: str):
    lowered = text.lower()

    signals = Counter()

    for category, patterns in SIGNAL_PATTERNS.items():
        for pattern in patterns:
            if pattern in lowered:
                signals[category] += 1

    entropy = round(sum(signals.values()) / 10.0, 2)

    observability_state = "STABLE"

    if entropy > 0.6:
        observability_state = "UNSTABLE"

    if entropy > 1.2:
        observability_state = "COLLAPSING"

    return {
        "signals": dict(signals),
        "entropy": entropy,
        "observability_state": observability_state
    }
