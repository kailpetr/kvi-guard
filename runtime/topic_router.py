TOPIC_HINTS = {
    "sky_blue": [
        "sky",
        "blue",
        "atmosphere",
        "scattering",
        "light",
        "rayleigh"
    ],
    "earth_shape": [
        "earth",
        "planet",
        "gravity",
        "sphere",
        "orbit",
        "satellite"
    ],
    "logic": [
        "logic",
        "reasoning",
        "proof",
        "therefore",
        "if",
        "then"
    ]
}


def detect_topic(text: str):

    lowered = text.lower()

    best_topic = None
    best_score = 0

    for topic, hints in TOPIC_HINTS.items():

        score = 0

        for hint in hints:
            if hint in lowered:
                score += 1

        if score > best_score:
            best_score = score
            best_topic = topic

    if best_topic is None:
        return "unknown"

    return best_topic
