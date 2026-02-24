"""
Lesson 7: Agentic MCP Solution Orchestration

This script orchestrates the end-to-end MCP workflow, automating requirements analysis, API contract extraction, test design, coverage review, automation, and traceability.
"""

import subprocess
import os

LESSONS = [
    "lesson1_requirements_analysis.py",
    "lesson2_api_contract_extraction.py",
    "lesson3_test_coverage_review.py",
    "lesson4_test_design_documentation.py",
    "lesson5_automation_implementation.py",
    "lesson6_review_and_traceability.py"
]

SRC_DIR = os.path.dirname(os.path.abspath(__file__))


def run_lesson(lesson):
    lesson_path = os.path.join(SRC_DIR, lesson)
    print(f"Running {lesson}...")
    result = subprocess.run(["python", lesson_path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error in {lesson}:\n{result.stderr}")


def main():
    # Ensure out/ directory exists
    out_dir = os.path.join(SRC_DIR, '../out')
    os.makedirs(out_dir, exist_ok=True)
    for lesson in LESSONS:
        run_lesson(lesson)
    print("Agentic MCP workflow complete. All outputs are in ../out/")


if __name__ == "__main__":
    main()
