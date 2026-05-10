def confidence_band(score: float):

    if score >= 0.85:
        return "HIGH"

    if score >= 0.60:
        return "MEDIUM"

    return "LOW"
