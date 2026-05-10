TRUTH_ANCHORS = {
    "sky_blue": [
        "rayleigh",
        "atmosphere",
        "wavelength",
        "scattering"
    ],
    "earth_shape": [
        "gravity",
        "sphere",
        "orbit",
        "satellite"
    ]
}


def truth_alignment(text: str, topic: str):
    anchors = TRUTH_ANCHORS.get(topic, [])

    if not anchors:
        return 1.0

    score = 0
    matched = []
    missing = []

    lowered = text.lower()

    for anchor in anchors:
        if anchor.lower() in lowered:
            score += 1
            matched.append(anchor)
        else:
            missing.append(anchor)

    alignment = score / len(anchors)

    return {
        "alignment": round(alignment, 2),
        "matched": matched,
        "missing": missing
    }
