# ui_streamlit.py - MCP Client UI (Streamlit)
"""
This file provides a simple Streamlit UI for the MCP client.
- Lets users enter context and action prompts
- Sends requests to the MCP server
- Displays/logs all requests and responses
- Makes agentic orchestration visible and interactive

Concept: The UI makes it easy to experiment with MCP workflows and see agent/LLM responses in real time.
"""

import streamlit as st
import requests
import json

st.title("MCP Client UI - Agentic Demo")
st.write("Interact with the MCP server and see agentic orchestration in action.")

# Step-by-step workflow descriptions
workflow_steps = {
    "extract_contract": "Extracts and documents the API contract from requirements/context.",
    "run_automation": "Runs automated tests based on the provided context/test cases.",
    "llm_prompt": "Sends a prompt to the LLM (OpenAI, etc.) and returns the response."
}

workflow = st.selectbox("Select MCP Workflow Step", list(workflow_steps.keys()))
st.write(f"**Step Description:** {workflow_steps[workflow]}")

# Context templates for each step
context_templates = {
    "extract_contract": '{"requirement": "Test API contract extraction"}',
    "run_automation": '{"test_cases": [{"id": "TC1", "desc": "Check /posts endpoint"}]}',
    "llm_prompt": ''
}

if workflow == "llm_prompt":
    st.write("Enter a prompt for the LLM below.")
    prompt = st.text_area("LLM Prompt", value="What is MCP?")
    context = {"prompt": prompt}
else:
    st.write("Enter context as JSON. Use the template below or customize.")
    context_input = st.text_area("Context (JSON)", value=context_templates[workflow])
    try:
        context = json.loads(context_input)
    except Exception:
        context = {}

if st.button("Send to MCP Server"):
    try:
        payload = {"context": context, "action": workflow}
        st.write("## Request Sent:")
        st.json(payload)
        response = requests.post("http://localhost:8000/run_action", json=payload)
        resp_json = response.json()
        st.write("## Response Received:")
        st.json(resp_json)
        if "provenance" in resp_json:
            st.write("### Agentic Provenance:")
            st.json(resp_json["provenance"])
    except Exception as e:
        st.error(f"Error: {e}")

st.write("---")
st.write("Logs and agentic orchestration will be visible in the server terminal.")

# As we build, this UI will be updated to support richer context, workflow selection, and LLM provenance display.
