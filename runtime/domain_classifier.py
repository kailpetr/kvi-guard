DOMAIN_FIELDS = {
    "physics": ["wavelength", "scattering", "gravity", "quantum"],
    "biology": ["cell", "dna", "organism", "evolution"],
    "mythology": ["dragon", "magic", "ancient gods", "prophecy"],
    "astronomy": ["planet", "galaxy", "orbit", "star"]
}


def classify_domains(text: str):
    lowered = text.lower()

    detected = {}

    for domain, keywords in DOMAIN_FIELDS.items():
        score = 0

        for keyword in keywords:
            if keyword in lowered:
                score += 1

        if score > 0:
            detected[domain] = score

    collision_risk = 0.0

    if len(detected.keys()) > 2:
        collision_risk = 0.35

    return {
        "domains": detected,
        "collision_risk": collision_risk
    }
