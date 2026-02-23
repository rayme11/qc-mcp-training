# Jira Access Setup Guide
#
# Folder Structure
#
# The project is organized as follows:
#
# qc-mcp-training/
# ├── config_and_tests/           # All configuration and test scripts
# │   └── jira_access_test.py     # Example: Jira access test script
# ├── .env                       # Environment variables (not committed)
# ├── .env.example               # Example environment file
# ├── requirements.txt           # Python dependencies
# ├── MCP_training_agenda.md     # Main training agenda
# ├── jira_access_setup.md       # Jira access setup guide
# ├── fetch_jira_requirements.md # Guide for fetching Jira requirements
# ├── secure_development_practices.md # Secure coding practices
# ├── jira_mcp_prompts.md        # Reusable Jira MCP prompts
# ...                            # Other guides and files
#
# Place all new config and test scripts in config_and_tests for consistency and easy maintenance.

This guide will help you configure secure access to Jira for automation and MCP workflows.

---

## 1. Create a Jira API Token
- Go to [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
- Click "Create API token"
- Name your token (e.g., "MCP Automation")
- Copy and save the token securely (you won't see it again)

## 2. Set Up Environment Variables
Create a `.env` file in your project root (add `.env` to `.gitignore`):

```
JIRA_SERVER=https://yourcompany.atlassian.net
JIRA_USER=your.email@company.com
JIRA_API_TOKEN=your_api_token_here
```

**Never commit `.env` or secrets to source control!**

## 3. Install Required Python Packages

```sh
pip install jira python-dotenv
Create a requirements.txt file in your project root with:

```

Create a file named `jira_access_test.py`:

```

Install all packages with:

```sh
pip install -r requirements.txt
```
```python
Create a requirements.txt file in your project root with:

```
## Troubleshooting
- Double-check your API token and email.
- Ensure your user has permission to access the relevant Jira project.
```

Install all packages with:

```sh
pip install -r requirements.txt
```

## 4. Minimal Python Example to Test Access

Create a file named `jira_access_test.py` with only the following Python code:

```python
import os
from jira import JIRA
from dotenv import load_dotenv

load_dotenv()

jira = JIRA(
    server=os.environ['JIRA_SERVER'],
    basic_auth=(os.environ['JIRA_USER'], os.environ['JIRA_API_TOKEN'])
)

# Fetch your user info as a test
me = jira.current_user()
print(f"Authenticated as: {me}")
```

Run:
```
python jira_access_test.py
```

If you see your Jira username, access is configured!
- If using SSO, API tokens still work for REST API access.

---

Continue to the next step once you have confirmed access.
