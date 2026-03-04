#!/bin/bash
# Boot script to run both FastAPI server and Streamlit client

echo "Starting FastAPI server..."
uvicorn mcp_server.main:app --reload &
sleep 2
echo "Starting Streamlit client..."
cd mcp_client && streamlit run ui_streamlit.py &
cd ..
echo "Both services started."
echo "FastAPI: http://localhost:8000"
echo "Streamlit: http://localhost:8501"