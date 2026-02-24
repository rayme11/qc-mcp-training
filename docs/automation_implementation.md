# Step 5: Automation Implementation

## Overview
This step focuses on automating API testing and validation for the JSONPlaceholder endpoints. Automation ensures repeatability, efficiency, and traceability in MCP workflows.

## Goals
- Implement automated tests for API endpoints
- Validate contract, coverage, and edge cases
- Generate traceable output for review

## Example: Python Automation with `requests` and `pytest`

### 1. Setup
- Install dependencies:
  - `pip install requests pytest`
- Create a test folder: `tests/`

### 2. Sample Test Script

```python
# tests/test_posts.py
import requests

def test_get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert len(response.json()) == 100

def test_get_post_valid_id():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_get_post_invalid_id():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/999')
    assert response.status_code == 404
```

### 3. Running Tests
- Run all tests:
  - `pytest tests/`
- Output is generated in terminal; can be redirected to a file for traceability.

### 4. Traceability
- Map test results to test cases in documentation
- Store output in `out/` folder for review

## Best Practices
- Parameterize tests for different input scenarios
- Use fixtures for setup/teardown
- Integrate with CI/CD for continuous validation

---

## Next Steps
- Review automation results
- Link test outputs to coverage and design docs
- Expand automation to other endpoints and edge cases
