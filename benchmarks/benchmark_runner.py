import json
from pathlib import Path


def run_simulated_benchmark():
    benchmark_file = Path(__file__).parent / 'sample_benchmark_suite.json'

    with open(benchmark_file, 'r', encoding='utf-8') as f:
        suite = json.load(f)

    print('\n=== KVI Guard Benchmark Suite ===\n')

    results = []

    for benchmark in suite['benchmarks']:
        name = benchmark['name']
        prompt = benchmark['prompt']

        print(f'Running: {name}')
        print(f'Prompt: {prompt}')

        simulated_score = 0.65 + (hash(name) % 30) / 100

        passed = simulated_score > 0.7

        results.append({
            'name': name,
            'score': round(simulated_score, 2),
            'passed': passed
        })

        print(f'Score: {simulated_score:.2f}')
        print(f'Passed: {passed}\n')

    passed_count = sum(r['passed'] for r in results)

    print('=== Summary ===')
    print(f'Total tests: {len(results)}')
    print(f'Passed: {passed_count}')
    print(f'Failed: {len(results) - passed_count}')


if __name__ == '__main__':
    run_simulated_benchmark()
