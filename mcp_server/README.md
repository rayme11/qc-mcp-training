# MCP Server

This folder contains the MCP server implementation. The server is responsible for:
- Receiving context and action requests from the MCP client
- Orchestrating agentic workflows (invoking LLMs, running scripts)
- Returning results and provenance to the client
- Logging all activity to the terminal for transparency



## Initial Scaffold
- Uses FastAPI for easy API creation and logging
- Provides `/run_action` endpoint for client requests
- Logs all incoming requests, agentic provenance, and outgoing responses to terminal
- Simulates agent/LLM orchestration (e.g., GitHub Copilot, GPT-4.1) in responses
- Placeholder for local LLM integration (OpenAI, Ollama, etc.)
- Agentic provenance is included in logs and API responses
- Step-by-step explanations will be provided as the server is built

### How to Run Locally
- Start the server: `uvicorn main:app --reload`
- The server will log all activity, agentic provenance, and simulate orchestration

### Real LLM Integration
- Real LLM orchestration is now supported via `llm_openai.py`.
- To use OpenAI, set your `OPENAI_API_KEY` environment variable.
- Send a request with action `llm_prompt` and context `{ "prompt": "your prompt here" }` to call the LLM.
- Provenance and workflow steps remain visible in logs and responses.

---

> As we proceed, this README will be updated to explain each new feature and concept added to the server.
