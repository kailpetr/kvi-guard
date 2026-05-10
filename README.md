# KVI Guard

Lightweight runtime stability layer for Large Language Models.

KVI Guard analyzes LLM responses for:

- semantic instability
- contradiction signals
- reasoning drift
- hallucination pressure
- response consistency

The project focuses on lightweight runtime verification rather than universal truth checking.

---

# Core Idea

Traditional AI pipeline:

```text
Prompt -> Model -> Response
```

KVI Guard pipeline:

```text
Prompt
  ↓
LLM Response
  ↓
KVI Verification Layer
  ↓
Stability Score
  ↓
Warnings + Telemetry
```

---

# Current Capabilities

## Included

- local llama.cpp runtime
- semantic stability scoring
- contradiction detection
- lightweight telemetry
- domain drift analysis
- local Termux/mobile support

---

# Philosophy

KVI Guard does not attempt to become a universal truth engine.

Instead, it estimates:

- semantic coherence
- inference stability
- contradiction pressure
- epistemic drift

through lightweight runtime analysis.

---

# Quick Start

## Clone repository

```bash
git clone https://github.com/kailpetr/kvi-guard.git
cd kvi-guard
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run local verification demo

```bash
python local_test.py
```

---

# Example Output

```json
{
  "score": 0.72,
  "state": "UNSTABLE",
  "warnings": [
    "truth-anchor divergence"
  ],
  "telemetry": {
    "entropy": 0.2
  }
}
```

---

# Core Components

## runtime/verifier.py
Central verification and scoring layer.

## runtime/truth_engine.py
Lightweight semantic anchor matching.

## runtime/contradiction_detector.py
Contradiction signal detection.

## runtime/cognitive_telemetry.py
Inference telemetry analysis.

## runtime/domain_classifier.py
Semantic domain drift analysis.

---

# Design Principles

KVI Guard should remain:

- lightweight
- understandable
- locally runnable
- low dependency
- benchmarkable
- model agnostic

---

# Explicit Non-Goals

KVI Guard intentionally avoids:

- AGI systems
- universal truth verification
- massive ontology graphs
- autonomous agents
- speculative cognitive frameworks
- heavy orchestration layers

---

# Vision

KVI Guard explores runtime observability for language model inference.

The project aims to make LLM outputs:

- more measurable
- more observable
- more stability-aware

without introducing unnecessary architectural complexity.
