"""
Lesson 2: API Contract Extraction

This script fetches the API contract (schema) for the /posts endpoint from JSONPlaceholder and documents the structure for downstream testing and automation.
"""

import requests
import json
import os

# Absolute path for out folder
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'out'))
CONTRACT_PATH = os.path.join(OUT_DIR, 'posts_contract.json')

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts_sample():
    try:
        response = requests.get(POSTS_URL)
        response.raise_for_status()
        posts = response.json()
        if posts:
            return posts[0]
        else:
            print("No posts found.")
            return {}
    except Exception as e:
        print(f"Error fetching posts: {e}")
        return {}


def extract_contract(sample_post):
    contract = {}
    for key, value in sample_post.items():
        contract[key] = type(value).__name__
    return contract


def save_contract(contract, output_path):
    # Ensure out/ directory exists
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(CONTRACT_PATH, "w") as f:
        json.dump(contract, f, indent=2)


def main():
    sample_post = fetch_posts_sample()
    if sample_post:
        contract = extract_contract(sample_post)
        print("Extracted API contract:")
        print(json.dumps(contract, indent=2))
        save_contract(contract, CONTRACT_PATH)
        print(f"Contract saved to {CONTRACT_PATH}")
    else:
        print("No sample post available. Skipping contract extraction.")


if __name__ == "__main__":
    main()
