"""
Jira access test script
Checks authentication and prints current user.
Place this script in config_and_tests/.
"""
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
