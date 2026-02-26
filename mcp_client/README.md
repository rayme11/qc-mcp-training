# MCP Client

This folder contains the MCP client implementation. The client is responsible for:
- Gathering context (requirements, contracts, test cases, etc.)
- Sending context and action requests to the MCP server
- Displaying/logging all requests and responses for learning
- Providing a simple UI for prompt entry and workflow triggering



## Initial Scaffold
- Uses Python script for sending requests to MCP server
- Logs all requests sent and responses received to terminal
- Example usage included in `main.py`
- Streamlit UI included in `ui_streamlit.py` for easy prompt entry and real-time response display
- Designed for local-first use, then deployable to free online platforms
- Step-by-step explanations will be provided as the client is built

### How to Run Locally
- Start the server first (`uvicorn main:app --reload` in mcp_server)
- Run the client script (`python main.py` in mcp_client) for terminal logging
- Or run the Streamlit UI (`streamlit run ui_streamlit.py` in mcp_client) for interactive prompt entry and agentic orchestration visibility
- The client will log all activity and show example agentic interaction

---

> As we proceed, this README will be updated to explain each new feature and concept added to the client.
