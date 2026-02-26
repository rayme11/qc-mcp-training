# main.py - MCP Client (Python scaffold)
"""
This is the entry point for the MCP client.
- Gathers context and prompts from the user
- Sends context and action requests to the MCP server
- Displays/logs all requests and responses for learning
- Provides a simple UI for prompt entry and workflow triggering

Concept: The client is the initiator, sending context and actions to the server and showing results.
"""

import requests
import json

def send_action(context, action):
    url = "http://localhost:8000/run_action"
    payload = {
        "context": context,
        "action": action
    }
    print(f"Sending request to MCP server: {json.dumps(payload, indent=2)}")
    response = requests.post(url, json=payload)
    print(f"Received response: {response.text}")
    return response.json()

if __name__ == "__main__":
    # Example usage
    context = {"requirement": "Test API contract extraction"}
    action = "extract_contract"
    send_action(context, action)

# As we build, this file will be updated to add UI integration, richer context, and step-by-step explanations.
