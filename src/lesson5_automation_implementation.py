
"""
Lesson 5: Automation Implementation

This script automates API testing for the /posts endpoint using test cases generated from previous steps. Results are saved for traceability.
"""
import os
import json
import requests

# Absolute path for out folder
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'out'))
TEST_DESIGN_PATH = os.path.join(OUT_DIR, 'test_design_documentation.json')
AUTOMATION_RESULTS_PATH = os.path.join(OUT_DIR, 'automation_results.json')

def save_results(results, path):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2)


def load_test_cases(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading test cases from {path}: {e}")
        return []


def run_test_case(test_case):
    endpoint = test_case["endpoint"]
    method = test_case.get("method", "GET")
    url = f"https://jsonplaceholder.typicode.com{endpoint}"
    response = requests.request(method, url)
    result = {
        "id": test_case["id"],
        "status_code": response.status_code,
        "passed": False,
        "details": ""
    }
    if response.status_code == 200:
        data = response.json()
        # Validate expected type for field
        field = test_case.get("expected_type")
        if field:
            # For demonstration, just check type of first item
            if isinstance(data, list) and data:
                actual_type = type(data[0].get(field, None)).__name__
                result["passed"] = actual_type == test_case["expected_type"]
                result["details"] = f"Expected {test_case['expected_type']}, got {actual_type}"
            else:
                result["details"] = "No data returned"
        else:
            result["passed"] = True
    else:
        result["details"] = f"HTTP {response.status_code}"
    return result



def run_all_tests(test_cases):
    results = []
    for tc in test_cases:
        results.append(run_test_case(tc))
    return results



def main():
    test_cases = load_test_cases(TEST_DESIGN_PATH)
    if test_cases:
        results = run_all_tests(test_cases)
        print("Automation results:")
        print(json.dumps(results, indent=2))
        save_results(results, AUTOMATION_RESULTS_PATH)
        print(f"Results saved to {AUTOMATION_RESULTS_PATH}")
    else:
        print("No test cases found. Skipping automation.")

if __name__ == "__main__":
    main()
