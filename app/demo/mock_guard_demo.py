from app.engines.semantic_similarity import SemanticSimilarityEngine
from app.engines.risk_engine import RiskEngine


RESPONSES = [
    "The Earth revolves around the Sun.",
    "Earth orbits the Sun in the solar system.",
    "The Earth is stationary and the Sun revolves around it."
]


def run_demo():
    similarity = SemanticSimilarityEngine()
    risk_engine = RiskEngine()

    a = RESPONSES[0]
    b = RESPONSES[1]
    c = RESPONSES[2]

    stable_score = similarity.compare(a, b)
    unstable_score = similarity.compare(a, c)

    stable_risk = risk_engine.analyze(a)
    unstable_risk = risk_engine.analyze(c + ' conflicting information')

    print('\n=== KVI Guard Demo ===\n')

    print('Stable branch comparison:')
    print(f'Similarity: {stable_score:.2f}')
    print(f'Risk: {stable_risk:.2f}\n')

    print('Unstable branch comparison:')
    print(f'Similarity: {unstable_score:.2f}')
    print(f'Risk: {unstable_risk:.2f}\n')

    if unstable_risk > stable_risk:
        print('⚠ KVI Guard detected unstable reasoning.')
    else:
        print('✓ Responses appear stable.')


if __name__ == '__main__':
    run_demo()
