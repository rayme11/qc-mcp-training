#!/bin/bash
# Boot script to run both FastAPI server and Streamlit client

echo "Starting FastAPI server on 0.0.0.0:8000..."
uvicorn mcp_server.main:app --host 0.0.0.0 --port 8000 &
sleep 2
echo "Starting Streamlit client..."
streamlit run mcp_client/ui_streamlit.py