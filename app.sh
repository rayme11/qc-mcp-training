#!/bin/bash
# Hugging Face Spaces entry point script
uvicorn mcp_server.main:app --host 0.0.0.0 --port 8000 &
sleep 2
streamlit run mcp_client/ui_streamlit.py --server.port=8000 --server.address=0.0.0.0
