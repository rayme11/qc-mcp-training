"""
Lesson 1: Requirements Analysis

This script demonstrates how to fetch requirements from a public issue tracker (simulated with JSONPlaceholder's /todos endpoint).
"""

import requests
import json
import os

# Absolute path for out folder
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'out'))
REQUIREMENTS_PATH = os.path.join(OUT_DIR, 'requirements.json')

REQUIREMENTS_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_requirements():
    try:
        response = requests.get(REQUIREMENTS_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching requirements: {e}")
        return []


def save_requirements(requirements, output_path):
    # Ensure out/ directory exists
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(REQUIREMENTS_PATH, "w") as f:
        json.dump(requirements, f, indent=2)


def main():
    requirements = fetch_requirements()
    if requirements:
        print(f"Fetched {len(requirements)} requirements.")
        save_requirements(requirements, REQUIREMENTS_PATH)
        print(f"Requirements saved to {REQUIREMENTS_PATH}")
    else:
        print("No requirements fetched. Skipping save.")


if __name__ == "__main__":
    main()
