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
from llm_openai import call_openai

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.post("/run_action")
async def run_action(request: Request):
    data = await request.json()
    logging.info(f"Received action request: {data}")
    agent_name = "GitHub Copilot (GPT-4.1)"
    provenance = {
        "agent": agent_name,
        "llm_type": "local or cloud",
        "workflow_step": data.get("action", "unknown")
    }
    output = f"Simulated LLM response for action '{data.get('action', 'unknown')}'."
    # If action is 'llm_prompt', call real LLM
    if data.get("action") == "llm_prompt":
        prompt = data.get("context", {}).get("prompt", "")
        output = call_openai(prompt)
        provenance["llm_type"] = "OpenAI"
    result = {
        "status": "completed",
        "provenance": provenance,
        "input": data,
        "output": output
    }
    logging.info(f"Agentic Provenance: {provenance}")
    logging.info(f"Returning result: {result}")
    return JSONResponse(content=result)

# To run locally: `uvicorn main:app --reload`

# As we build, this file will be updated to add real LLM integration, workflow orchestration, and provenance logging.
