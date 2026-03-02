from fastapi.responses import HTMLResponse
# main.py - MCP Server (FastAPI scaffold)
"""
This is the entry point for the MCP server.
- Receives context and action requests from the MCP client
- Orchestrates agentic workflows (invokes LLMs, runs scripts)
- Returns results and provenance to the client
- Logs all activity to the terminal for transparency

Concept: The server is the central orchestrator, coordinating agentic actions and providing traceability.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
from .llm_openai import call_openai


app = FastAPI()

# Root endpoint for landing page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h2>Welcome to the MCP Training Server!</h2><p>Visit <a href='/docs'>/docs</a> for API documentation.</p>"

logging.basicConfig(level=logging.INFO)

@app.post("/run_action")
async def run_action(request: Request):
    data = await request.json()
    logging.info("[SERVER] Received action request from client: %s", data)
    agent_name = "GitHub Copilot (GPT-4.1)"
    provenance = {
        "agent": agent_name,
        "llm_type": "local or cloud",
        "workflow_step": data.get("action", "unknown")
    }
    action = data.get("action")
    output = f"Simulated LLM response for action '{action}'."

    logging.info(f"[SERVER] Executing workflow step: {action}")

    if action == "llm_prompt":
        prompt = data.get("context", {}).get("prompt", "")
        logging.info(f"[SERVER] Calling LLM with prompt: {prompt}")
        output = call_openai(prompt)
        provenance["llm_type"] = "OpenAI"
    elif action == "traceability_matrix":
        reqs = data.get("context", {}).get("requirements", [])
        tcs = data.get("context", {}).get("test_cases", [])
        results = data.get("context", {}).get("results", [])
        logging.info(f"[SERVER] Generating traceability matrix for requirements: {reqs} and test_cases: {tcs}")
        output = {
            "traceability_matrix": [
                {"requirement": r, "test_case": tc, "result": results[i] if i < len(results) else "unknown"}
                for i, (r, tc) in enumerate(zip(reqs, tcs))
            ]
        }
        provenance["concept"] = "Traceability Matrix"
    elif action == "requirements_mapping":
        reqs = data.get("context", {}).get("requirements", [])
        endpoints = data.get("context", {}).get("api_endpoints", [])
        coverage = data.get("context", {}).get("test_coverage", {})
        logging.info(f"[SERVER] Mapping requirements {reqs} to endpoints {endpoints} and coverage {coverage}")
        output = {
            "requirements_mapping": [
                {
                    "requirement": r,
                    "api_endpoints": endpoints,
                    "test_coverage": coverage.get(r, [])
                }
                for r in reqs
            ]
        }
        provenance["concept"] = "Requirements Mapping"

    result = {
        "status": "completed",
        "provenance": provenance,
        "input": data,
        "output": output
    }
    logging.info(f"[SERVER] Agentic Provenance: {provenance}")
    logging.info(f"[SERVER] Returning result to client: {result}")
    return JSONResponse(content=result)

# To run locally: `uvicorn main:app --reload`

# As we build, this file will be updated to add real LLM integration, workflow orchestration, and provenance logging.
