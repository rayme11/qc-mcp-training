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
    validation_passed = True
    for issue in issues:
        output_lines.append("--- Output ---")
        output_lines.append(f"Key: {issue.key}")
        summary = getattr(issue.fields, 'summary', None)
        description = getattr(issue.fields, 'description', None)
        acceptance_criteria = getattr(issue.fields, 'customfield_10034', None)  # Example custom field
        endpoints = getattr(issue.fields, 'customfield_12345', None)  # Example custom field
        output_lines.append(f"Summary: {summary}")
        output_lines.append(f"Description: {description}")
        # Try to infer acceptance criteria from description if missing
        if not acceptance_criteria and description:
            import re
            match = re.search(r"[*_-]?Expected behavior[*_-]?\s*(.+?)(?:\n\s*\n|$)", description, re.IGNORECASE | re.DOTALL)
            if match:
                acceptance_criteria = match.group(1).strip()
                output_lines.append("[INFERRED] Acceptance Criteria from 'Expected behavior' in description.")
        # Try to extract API endpoint from description if endpoints field is missing
        if not endpoints and description:
            import re
            url_matches = re.findall(r"https?://[\w\.-]+(?:/[\w\.-]*)*", description)
            if url_matches:
                endpoints = ", ".join(url_matches)
                output_lines.append("[INFERRED] Endpoints from URLs in description.")
        output_lines.append(f"Acceptance Criteria: {acceptance_criteria}")
        output_lines.append(f"Endpoints: {endpoints}")
        # Validation
        if not summary or not acceptance_criteria or not endpoints:
            validation_passed = False
            output_lines.append("[VALIDATION] Missing required fields!")
        else:
            output_lines.append("[VALIDATION] All required fields present.")

    # Write output to file
    with open("out/requirements_output.txt", "w") as f:
        for line in output_lines:
            f.write(line + "\n")

    if validation_passed:
        print("Validation: PASS - All required fields present in all issues.")
    else:
        print("Validation: FAIL - Some issues are missing required fields. See output file for details.")
else:
    print("Execution Status: FAIL")
    print("No issues found for the request.")
