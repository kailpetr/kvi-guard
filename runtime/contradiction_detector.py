CONTRADICTION_PAIRS = [
    ("flat", "sphere"),
    ("always", "never"),
    ("true", "false"),
    ("impossible", "certain")
]


def detect_contradictions(text: str):
    lowered = text.lower()

    contradictions = []

    for pair in CONTRADICTION_PAIRS:
        left, right = pair

        if left in lowered and right in lowered:
            contradictions.append({
                "pair": pair,
                "severity": 0.25
            })

    risk = min(sum(item["severity"] for item in contradictions), 1.0)

    return {
        "risk": round(risk, 2),
        "contradictions": contradictions
    }
