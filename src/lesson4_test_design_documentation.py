
"""
Lesson 4: Test Design Documentation

This script generates test design documentation from API contract and requirements, creating structured test cases and saving them for traceability.
"""
import os
import json

# Absolute path for out folder
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'out'))
CONTRACT_PATH = os.path.join(OUT_DIR, 'posts_contract.json')
REQUIREMENTS_PATH = os.path.join(OUT_DIR, 'requirements.json')
TEST_DESIGN_PATH = os.path.join(OUT_DIR, 'test_design_documentation.json')

def save_json(data, path):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None

def generate_test_cases(contract, requirements):
    test_cases = []
    for field in contract:
        test_cases.append({
            "id": f"TC_{field.upper()}",
            "title": f"Validate field '{field}' in /posts",
            "endpoint": "/posts",
            "method": "GET",
            "expected_type": contract[field],
            "priority": "Normal"
        })
    return test_cases

def main():
    contract = load_json(CONTRACT_PATH)
    requirements = load_json(REQUIREMENTS_PATH)
    if contract and requirements:
        test_cases = generate_test_cases(contract, requirements)
        print("Generated test design documentation:")
        print(json.dumps(test_cases, indent=2))
        save_json(test_cases, TEST_DESIGN_PATH)
        print(f"Test design documentation saved to {TEST_DESIGN_PATH}")
    else:
        print("Missing contract or requirements. Skipping test design documentation.")

if __name__ == "__main__":
    main()


def main():
    contract = load_json(CONTRACT_PATH)
    requirements = load_json(REQUIREMENTS_PATH)
    if contract and requirements:
        test_cases = generate_test_cases(contract, requirements)
        print("Generated test design documentation:")
        print(json.dumps(test_cases, indent=2))
        save_json(test_cases, TEST_DESIGN_PATH)
        print(f"Test design documentation saved to {TEST_DESIGN_PATH}")
    else:
        print("Missing contract or requirements. Skipping test design documentation.")


if __name__ == "__main__":
    main()
