# KVI Runtime Signal Map

This document explains the lightweight telemetry model used by KVI Guard.

## entropy

Approximate instability pressure inside the evaluated reasoning structure.

Lower values indicate:

- more coherent structure
- less branching drift
- lower semantic turbulence

Higher values indicate:

- unstable transitions
- domain collapse
- contradiction pressure

---

## alignment

Measures consistency between detected domains and local reasoning structure.

Examples:

- physics + astronomy => higher alignment
- physics + fantasy => lower alignment

---

## unstable_signal_count

Counts detected instability events.

Signals may include:

- collapse
- instability
- overconfidence
- contradiction

---

## stable_structure

Represents how many structural anchors remained coherent during evaluation.

Higher values imply:

- preserved semantic continuity
- lower drift
- stronger internal consistency

---

## Design Philosophy

KVI Guard intentionally avoids:

- giant symbolic graphs
- opaque neural scoring layers
- heavyweight runtime orchestration

Instead it uses:

- lightweight telemetry
- interpretable signals
- structural consistency checks
- runtime semantic stability
