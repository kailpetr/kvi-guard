def map_inference_topology(verification_result: dict):

    topology = {
        "stability_nodes": [],
        "fracture_nodes": [],
        "risk_gradient": 0.0
    }

    if verification_result.get("truth_alignment", {}).get("alignment", 0) > 0.7:
        topology["stability_nodes"].append("truth-coherence")

    if verification_result.get("contradictions", {}).get("risk", 0) > 0:
        topology["fracture_nodes"].append("semantic-contradiction")
        topology["risk_gradient"] += 0.3

    if verification_result.get("domains", {}).get("collision_risk", 0) > 0:
        topology["fracture_nodes"].append("domain-collision")
        topology["risk_gradient"] += 0.2

    telemetry = verification_result.get("telemetry", {})

    if telemetry.get("entropy", 0) > 0.6:
        topology["fracture_nodes"].append("entropy-escalation")
        topology["risk_gradient"] += 0.25

    topology["risk_gradient"] = round(topology["risk_gradient"], 2)

    return topology
