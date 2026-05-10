TRUTH_ANCHORS = {
    "sky_blue": {
        "primary": [
            "rayleigh scattering",
            "rayleigh",
            "scattering"
        ],
        "secondary": [
            "atmosphere",
            "blue light",
            "wavelength",
            "light",
            "molecules",
            "air"
        ]
    },
    "earth_shape": {
        "primary": [
            "gravity",
            "sphere",
            "orbit"
        ],
        "secondary": [
            "satellite",
            "planet",
            "curvature"
        ]
    }
}


def calculate_alignment(primary_matches, secondary_matches, primary_total, secondary_total):

    primary_score = 0.0
    secondary_score = 0.0

    if primary_total > 0:
        primary_score = primary_matches / primary_total

    if secondary_total > 0:
        secondary_score = secondary_matches / secondary_total

    alignment = (primary_score * 0.7) + (secondary_score * 0.3)

    return round(min(alignment, 1.0), 2)


def truth_alignment(text: str, topic: str):

    anchor_data = TRUTH_ANCHORS.get(topic, {})

    if not anchor_data:
        return {
            "alignment": 1.0,
            "matched": [],
            "missing": []
        }

    primary = anchor_data.get("primary", [])
    secondary = anchor_data.get("secondary", [])

    lowered = text.lower()

    matched = []
    missing = []

    primary_matches = 0
    secondary_matches = 0

    for anchor in primary:
        if anchor.lower() in lowered:
            primary_matches += 1
            matched.append(anchor)
        else:
            missing.append(anchor)

    for anchor in secondary:
        if anchor.lower() in lowered:
            secondary_matches += 1
            matched.append(anchor)

    alignment = calculate_alignment(
        primary_matches,
        secondary_matches,
        len(primary),
        len(secondary)
    )

    return {
        "alignment": alignment,
        "matched": matched,
        "missing": missing
    }
