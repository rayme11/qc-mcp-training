# Jira MCP Prompts & Reusable Learning

This file contains prompts and reusable learning content for extracting and analyzing requirements from Jira using MCP integrations. Use these templates and notes to standardize and accelerate your workflow.

---

## Secure Practices
- **Never commit API tokens, passwords, or secrets to source control.**
- Store secrets in environment variables or secure vaults (e.g., Azure Key Vault, AWS Secrets Manager).
- Use `.env` files for local development and add them to `.gitignore`.
- Rotate credentials regularly and use least-privilege access.

---

## Example Jira MCP Prompt

```
Using the Atlassian MCP, retrieve all requirements for [Project/Epic/Feature]:
– Jira keys: [list keys if known, or use JQL filter]
– Include: summary, description, acceptance criteria, API endpoints mentioned
Analyze and summarize:
1. Which API endpoints are involved
2. Expected behaviors and business rules
3. Data validation requirements
4. Authentication/authorization needs
5. Any non-functional requirements (performance, security)
6. Any dependencies
```

---

## Example Python Code Snippet

```python
from jira import JIRA
import os

jira = JIRA(
    server=os.environ['JIRA_SERVER'],
    basic_auth=(os.environ['JIRA_USER'], os.environ['JIRA_API_TOKEN'])
)
issues = jira.search_issues('project = "QC" AND status = "Ready for Test"')

for issue in issues:
    print(f"Key: {issue.key}")
    print(f"Summary: {issue.fields.summary}")
    print(f"Description: {issue.fields.description}")
    # Extract custom fields for acceptance criteria, endpoints, etc.
```

---

## Learning Resources
- [Jira REST API Guide](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Python jira package documentation](https://jira.readthedocs.io/en/master/)
- [Xray for Jira Documentation](https://docs.getxray.app/display/XRAYCLOUD/Getting+Started)

---

## Checklist for Secure & Reusable Practice
- [ ] Store secrets in environment variables or vaults
- [ ] Add `.env` to `.gitignore`
- [ ] Use prompts/templates from this file for consistency
- [ ] Update this file with new reusable patterns as you learn
