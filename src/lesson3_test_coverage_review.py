"""
Lesson 3: Test Coverage Review

This script reviews test coverage by comparing requirements and API contract to a set of test cases. It outputs a coverage report for traceability.
"""

import json
import os

# Absolute path for out folder
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'out'))
REQUIREMENTS_PATH = os.path.join(OUT_DIR, 'requirements.json')
CONTRACT_PATH = os.path.join(OUT_DIR, 'posts_contract.json')
TEST_CASES_PATH = os.path.join(OUT_DIR, 'test_cases.json')
COVERAGE_REPORT_PATH = os.path.join(OUT_DIR, 'coverage_report.json')

REQUIREMENTS_PATH = "../out/requirements.json"
CONTRACT_PATH = "../out/posts_contract.json"
TEST_CASES_PATH = "../out/test_cases.json"
COVERAGE_REPORT_PATH = "../out/coverage_report.json"

# Example test cases for demonstration
TEST_CASES = [
    {"id": "TC01", "endpoint": "/posts", "method": "GET"},
    {"id": "TC02", "endpoint": "/posts/1", "method": "GET"},
    {"id": "TC04", "endpoint": "/posts", "method": "POST"},
    {"id": "TC08", "endpoint": "/posts/1", "method": "DELETE"},
]

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return []


    os.makedirs(OUT_DIR, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def review_coverage(requirements, contract, test_cases):
    endpoints = set(["/posts", "/posts/1"])
    tested = set(tc["endpoint"] for tc in test_cases)
    coverage = {"tested": list(tested), "untested": list(endpoints - tested)}
    return coverage


def main():
    def save_json(data, path):
        os.makedirs(OUT_DIR, exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    # Example test cases for demonstration
    TEST_CASES = [
        {"id": "TC01", "endpoint": "/posts", "method": "GET"},
        {"id": "TC02", "endpoint": "/posts/1", "method": "GET"},
        {"id": "TC04", "endpoint": "/posts", "method": "POST"},
        {"id": "TC08", "endpoint": "/posts/1", "method": "DELETE"},
    ]

    def load_json(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {path}: {e}")
            return []
