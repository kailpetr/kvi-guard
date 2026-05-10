from transformers import pipeline


class NLIContradictionEngine:
    def __init__(self):
        self.classifier = pipeline(
            'text-classification',
            model='facebook/bart-large-mnli'
        )

    def analyze_pair(self, a: str, b: str) -> dict:
        result = self.classifier({
            'text': a,
            'text_pair': b
        })[0]

        label = result['label'].lower()
        score = float(result['score'])

        return {
            'label': label,
            'score': round(score, 3)
        }

    def analyze(self, responses: list[str]) -> dict:
        if len(responses) < 2:
            return {
                'status': 'insufficient_data',
                'contradiction_score': 0.0
            }

        contradiction_scores = []
        entailment_scores = []

        for i in range(len(responses)):
            for j in range(i + 1, len(responses)):
                result = self.analyze_pair(
                    responses[i],
                    responses[j]
                )

                if 'contradiction' in result['label']:
                    contradiction_scores.append(result['score'])

                if 'entailment' in result['label']:
                    entailment_scores.append(result['score'])

        contradiction_score = (
            sum(contradiction_scores) / len(contradiction_scores)
            if contradiction_scores else 0.0
        )

        entailment_score = (
            sum(entailment_scores) / len(entailment_scores)
            if entailment_scores else 0.0
        )

        status = 'stable'

        if contradiction_score > 0.55:
            status = 'unstable'

        return {
            'contradiction_score': round(contradiction_score, 3),
            'entailment_score': round(entailment_score, 3),
            'status': status
        }
