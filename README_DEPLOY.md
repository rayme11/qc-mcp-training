# MCP Training Project Deployment Guide

This guide explains how to deploy the MCP Training Project to Hugging Face Spaces or Streamlit Cloud for public demos and agentic workflow visualization.

## Prerequisites
- Python 3.8+
- OpenAI API key (for LLM integration)
- GitHub account (for cloud deployment)

## 1. Prepare the Project
- Ensure all code is committed and pushed to a public GitHub repository.
- Confirm requirements.txt is present and up to date.

## 2. Hugging Face Spaces Deployment
1. Go to https://huggingface.co/spaces and create a new Space.
2. Select "Streamlit" as the SDK.
3. Link your GitHub repo or upload your code.
4. Add your OpenAI API key as a secret in the Space settings.
5. The main entry point should be `mcp_client/ui_streamlit.py`.
6. Spaces will auto-install dependencies from requirements.txt.

## 3. Streamlit Cloud Deployment
1. Go to https://streamlit.io/cloud and sign in with GitHub.
2. Create a new app and select your repo.
3. Set the main file to `mcp_client/ui_streamlit.py`.
4. Add your OpenAI API key as a secret in the app settings.
5. Streamlit Cloud will auto-install dependencies from requirements.txt.

## 4. FastAPI Server (Optional for Local/Advanced)
- For full client-server demos, deploy FastAPI separately (e.g., on Azure, Heroku, or locally).
- Update the Streamlit UI to point to the deployed server URL if not running locally.

## 5. Usage
- After deployment, share the public app URL for demos.
- Users can interact with the MCP workflow, view agentic orchestration, and download outputs.

## Troubleshooting
- If the UI cannot connect to the server, check that the FastAPI server is running and accessible.
- Ensure all secrets (API keys) are set in the cloud platform.
- Review logs for errors and consult the README for setup steps.

---

For more details, see the main README.md and docs/ folder for conceptual guides and workflow explanations.
