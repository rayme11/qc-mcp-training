## Purpose of This Step
This step is only to verify that you can successfully retrieve Jira items and display their details (summary, description, etc.) using your script. You are not testing the API or business logic here—just confirming access and data retrieval from Jira.

# Fetching Jira Requirements Guide

This guide helps you fetch requirements from Jira for a specific project, epic, or feature using Python.

---

## 1. Example JQL Queries
- Fetch all stories in a project:
  ```
  project = "QC" AND issuetype = "Story" AND status = "Ready for Test"
  ```
- Fetch issues for a specific epic:
  ```
  "Epic Link" = EPIC-123
  ```
# Folder Structure
- Place scripts in `config_and_tests/`.
- Use `.env` for credentials and config.

## 2. Python Script: Fetch Requirements
Create a file named `fetch_jira_requirements.py`:

```python
Create a file named `fetch_jira_requirements.py` in `config_and_tests/`:

```python
"""
Fetch Jira requirements for a project, epic, or feature.
Prints key details for each issue.
"""
import os
from jira import JIRA
from dotenv import load_dotenv

load_dotenv()
jira = JIRA(
  server=os.environ['JIRA_SERVER'],
  basic_auth=(os.environ['JIRA_USER'], os.environ['JIRA_API_TOKEN'])
)

# Change JQL as needed
jql = 'project = "QC" AND issuetype = "Story" AND status = "Ready for Test"'
issues = jira.search_issues(jql, maxResults=10)

for issue in issues:
  print(f"Key: {issue.key}")
  print(f"Summary: {issue.fields.summary}")
  print(f"Description: {issue.fields.description}")
  # Add more fields as needed
```
```

---

## 3. Output
The script prints key details for each issue, such as:
  - Key: CXE-101922
  - Summary: [uls] cannot read property of null (reading "displayAddress")
  - Description: *Current Behavior* ...

You can redirect output to a file in the out/ folder for further analysis. The script or your command should ensure the out/ folder exists:
```
python config_and_tests/fetch_jira_requirements.py CXE-101922 > out/requirements_output.txt
```

> Best practice: Always use the out/ folder for output files. The script should create this folder automatically if it does not exist.

Example output:
```
Key: CXE-101922
Summary: [uls] cannot read property of null (reading "displayAddress")
Description: *Current Behavior*

User are making this request

... (rest of the description) ...
```
  python config_and_tests/fetch_jira_requirements.py > requirements_output.txt

---

## 4. Next Steps
- Review requirements_output.txt for acceptance criteria, endpoints, and business rules.
- Proceed to extraction and summary creation.

---

## Standards Checklist
- Script has docstring and comments
- Script is in config_and_tests/
- .env is used for credentials
- Output is redirected for analysis

---

## Troubleshooting
- Check JQL syntax and permissions
- Ensure .env values are correct
- Review output for completeness

---

Continue to the next step once requirements are fetched.
  ```

---

## 4. Next Steps
- Review requirements_output.txt for acceptance criteria, endpoints, and business rules.
- Proceed to extraction and summary creation.
