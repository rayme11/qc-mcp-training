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

# Expanded workflow steps
workflow_steps = {
    "run_all_steps": "Run the full MCP workflow end-to-end and display all outputs.",
    "extract_contract": "Extracts and documents the API contract from requirements/context.",
    "run_automation": "Runs automated tests based on the provided context/test cases.",
    "traceability_matrix": "Generates a traceability matrix mapping requirements to test cases and results.",
    "requirements_mapping": "Maps requirements to API endpoints and test coverage for traceability.",
    "llm_prompt": "Sends a prompt to the LLM (OpenAI, etc.) and returns the response."
}

workflow = st.selectbox("Select MCP Workflow Step", list(workflow_steps.keys()))
st.write(f"**Step Description:** {workflow_steps[workflow]}")

# Context templates for each step
context_templates = {
    "extract_contract": '{"requirement": "Test API contract extraction"}',
    "run_automation": '{"test_cases": [{"id": "TC1", "desc": "Check /posts endpoint"}]}',
    "traceability_matrix": '{"requirements": ["REQ-1", "REQ-2"], "test_cases": ["TC1", "TC2"], "results": [{"TC1": "pass"}, {"TC2": "fail"}]}',
    "requirements_mapping": '{"requirements": ["REQ-1", "REQ-2"], "api_endpoints": ["/posts", "/users"], "test_coverage": {"REQ-1": ["TC1"], "REQ-2": ["TC2"]}}',
    "llm_prompt": ''
}

def download_button(label, data, file_name):
    st.download_button(label, data, file_name=file_name)

if workflow == "run_all_steps":
    st.write("This will run all MCP workflow steps and display/download outputs.")
    if st.button("Run All Steps"):
        all_outputs = {}
        provenance_list = []
        # Define the steps and their actions
        steps = [
            ("extract_contract", json.loads(context_templates["extract_contract"])),
            ("run_automation", json.loads(context_templates["run_automation"])),
            ("traceability_matrix", json.loads(context_templates["traceability_matrix"])),
            ("requirements_mapping", json.loads(context_templates["requirements_mapping"])),
        ]
        for action, context in steps:
            payload = {"context": context, "action": action}
            response = requests.post("http://localhost:8000/run_action", json=payload)
            resp_json = response.json()
            all_outputs[action] = resp_json.get("output", {})
            provenance_list.append(resp_json.get("provenance", {}))
            st.write(f"### Step: {action}")
            st.json(resp_json)
            if "output" in resp_json:
                download_button(f"Download {action} output", json.dumps(resp_json["output"], indent=2), f"{action}_output.json")
            if "provenance" in resp_json:
                st.write("#### Agentic Provenance:")
                st.json(resp_json["provenance"])
        st.write("---")
        st.write("## All Outputs Summary:")
        st.json(all_outputs)
        st.write("## All Provenance:")
        st.json(provenance_list)
else:
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
            if "output" in resp_json:
                download_button(f"Download {workflow} output", json.dumps(resp_json["output"], indent=2), f"{workflow}_output.json")
            if "provenance" in resp_json:
                st.write("### Agentic Provenance:")
                st.json(resp_json["provenance"])
        except Exception as e:
            st.error(f"Error: {e}")

st.write("---")
st.write("Logs and agentic orchestration will be visible in the server terminal.")
