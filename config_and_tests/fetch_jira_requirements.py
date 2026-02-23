"""
Fetch Jira requirements for a project, epic, feature, or specific key.
Prints key details for each issue.
Usage:
    python fetch_jira_requirements.py [JIRA_KEY]
If JIRA_KEY is provided, fetches only that issue. Otherwise, fetches default JQL.
Automatically creates the out/ folder for output if it does not exist.
"""
import os
import sys
from jira import JIRA
from dotenv import load_dotenv

# Ensure output directory exists
os.makedirs("out", exist_ok=True)

load_dotenv()
jira = JIRA(
    server=os.environ['JIRA_SERVER'],
    basic_auth=(os.environ['JIRA_USER'], os.environ['JIRA_API_TOKEN'])
)

# Allow passing a Jira key as a command-line argument
if len(sys.argv) > 1:
    key = sys.argv[1]
    jql = f'key = "{key}"'
    print(f"Request: Fetching Jira item with key '{key}'")
else:
    jql = 'project = "QC" AND issuetype = "Story" AND status = "Ready for Test"'
    print("Request: Fetching Jira items with default JQL")

issues = jira.search_issues(jql, maxResults=10)

if issues:
    print("Execution Status: SUCCESS")
    # Always print request and status to terminal
    output_lines = []
    for issue in issues:
        output_lines.append("--- Output ---")
        output_lines.append(f"Key: {issue.key}")
        output_lines.append(f"Summary: {issue.fields.summary}")
        output_lines.append(f"Description: {issue.fields.description}")
        # Add more fields as needed
    # Write output to file
    with open("out/requirements_output.txt", "w") as f:
        for line in output_lines:
            f.write(line + "\n")
else:
    print("Execution Status: FAIL")
    print("No issues found for the request.")
