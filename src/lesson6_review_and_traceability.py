import os
import json
"""
Lesson 6: Review & Traceability
import os
import json

This script reviews automation results, updates the traceability matrix, and identifies gaps for continuous improvement.
"""

# Absolute path for out folder
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'out'))
AUTOMATION_RESULTS_PATH = os.path.join(OUT_DIR, 'automation_results.json')
TEST_DESIGN_PATH = os.path.join(OUT_DIR, 'test_design_documentation.json')
TRACEABILITY_MATRIX_PATH = os.path.join(OUT_DIR, 'traceability_matrix.json')

def save_json(data, path):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# Absolute path for out folder
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'out'))
AUTOMATION_RESULTS_PATH = os.path.join(OUT_DIR, 'automation_results.json')
TEST_DESIGN_PATH = os.path.join(OUT_DIR, 'test_design_documentation.json')
TRACEABILITY_MATRIX_PATH = os.path.join(OUT_DIR, 'traceability_matrix.json')

AUTOMATION_RESULTS_PATH = "../out/automation_results.json"
TEST_DESIGN_PATH = "../out/test_design_documentation.json"
TRACEABILITY_MATRIX_PATH = "../out/traceability_matrix.json"


def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return []


def build_traceability_matrix(test_cases, automation_results):
    matrix = []
    for tc in test_cases:
        result = next((r for r in automation_results if r["id"] == tc["id"]), None)
        matrix.append({
            "test_case_id": tc["id"],
            "endpoint": tc["endpoint"],
            "method": tc["method"],
            "priority": tc["priority"],
            "automation_result": result["passed"] if result else "Not Run",
            "details": result["details"] if result else "No result"
        })
    return matrix


    os.makedirs(OUT_DIR, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def main():
    test_cases = load_json(TEST_DESIGN_PATH)
    automation_results = load_json(AUTOMATION_RESULTS_PATH)
    if test_cases and automation_results:
        matrix = build_traceability_matrix(test_cases, automation_results)
        print("Traceability matrix:")
        print(json.dumps(matrix, indent=2))
        save_json(matrix, TRACEABILITY_MATRIX_PATH)
        print(f"Traceability matrix saved to {TRACEABILITY_MATRIX_PATH}")
    else:
        print("Missing test cases or automation results. Skipping traceability matrix.")


if __name__ == "__main__":
    main()
