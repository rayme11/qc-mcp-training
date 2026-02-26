# MCP Training Project

## What is MCP Training?
This project is designed to help you learn and implement Model Context Protocol (MCP) concepts for quality control, automation, and API testing. The training is hands-on, step-by-step, and uses public APIs and open-source tools so you can practice and build real skills.


## Training Structure
The training is divided into clear sections, each with its own guide and practical exercises:

1. **Requirements Analysis**
   - Learn to extract and analyze requirements from public issue trackers (e.g., GitHub Issues).
2. **API Contract Extraction**
   - Understand and document API contracts using OpenAPI/Swagger from public APIs.
3. **Test Coverage Review**
   - Review existing tests and identify gaps using public repo examples.
4. **Test Design & Documentation**
   - Design and document test cases for APIs and UI workflows.
5. **Automation Implementation**
   - Build and run automated tests using Python and open-source frameworks.
6. **Review & Traceability**
   - Validate coverage, review results, and ensure traceability.

7. **MCP Client Implementation**
   - See `mcp_client/` for the client scaffold. Gathers context, sends requests, logs activity, and provides a simple UI (Streamlit or similar).
   - All requests and responses are logged to the terminal and UI for transparency and learning.
8. **MCP Server Implementation (with FastAPI/fastmcp)**
   - See `mcp_server/` for the server scaffold. Receives requests, orchestrates workflows, logs all steps, and integrates local LLMs (OpenAI, Ollama, etc.).
   - The server logs every incoming request, workflow step, and response to the terminal or screen, showing agent/LLM involvement.
9. **Client-Server Interaction Demo**
   - Run both client and server locally to demonstrate full MCP context exchange and traceability, with real-time logs for every step.
10. **Deployment & Agentic Visualization**
   - Deploy the solution (e.g., Hugging Face Spaces) to make agent/LLM orchestration and MCP concepts visible and interactive, with UI and logs for public demos.
---

> The project now includes `mcp_client/` and `mcp_server/` folders for clear separation of roles. The client provides a simple UI and logs all activity; the server uses FastAPI for easy API creation and agentic orchestration. Local-first, then deployable for public demos.
> **Implementation Note:**
> We will use FastAPI (or a similar framework, e.g., 'fastmcp') for the MCP server to make the API clear, interactive, and easy to log. All client-server interactions will be visible in the terminal for step-by-step learning.

> **Concept:**
> The MCP (Model Context Protocol) is about structured, traceable, and automated context exchange between agents, clients, and servers. By building both a client and a server, you’ll see how context, actions, and results flow through the system—enabling true agentic automation and traceability.

**Approach:**
- First, implement and test everything locally for clarity and debugging.
- Then, deploy to a public platform (like Hugging Face Spaces) to visualize and share the full workflow, agent/LLM provenance, and MCP interactions.

Each step will include conceptual explanations, code, and practical demonstrations.



## Visual Overview: Training Goals & Architecture

```
      +---------------------+
      | Quality Analyst     |
      +---------------------+
              |
              v
      +---------------------+
      | GitHub Repo         |
      +---------------------+
              |
              v
      +---------------------+
      | Public API          |
      +---------------------+
              |
              v
      +---------------------+
      | Test Automation     |
      +---------------------+
              |
              v
      +---------------------+
      | Traceability/Output |
      +---------------------+

      < Developer implements features in Public API >
      < QA reviews results in Traceability/Output >
      < GitHub Repo links source, issues, and test coverage >
```

This ASCII diagram is GitHub-friendly and shows how MCP training connects requirements, API contracts, test design, automation, and traceability across roles and tools.

## How to Use This Project
- Each section has its own markdown file in the docs/ folder.
- Follow the guides step by step.
- Use the provided scripts and examples.
- All output and artifacts are saved in the out/ folder for traceability.


## 🚀 Deploying & Visualizing on Hugging Face Spaces

This project can be deployed as an interactive web app on [Hugging Face Spaces](https://huggingface.co/spaces) to make agent/LLM orchestration and MCP concepts fully visible and easy to follow.

### How It Works

1. **User Triggers Workflow**
    - The web UI lets you select and run any MCP lesson or the full workflow.
    - Each step is triggered by a button or menu in the app.

2. **Agent/LLM Orchestration**
    - The app clearly displays which agent or LLM (e.g., GitHub Copilot, GPT-4.1) is running each step.
    - Metadata and provenance are shown for every action (see below).

3. **Step-by-Step Outputs**
    - Results for each MCP phase (requirements, contract, tests, automation, traceability) are shown in real time.
    - All outputs are downloadable and traceable.

4. **Visual Workflow**
    - The UI uses diagrams and progress bars to show the workflow and agent involvement.
    - Example:

```
User triggers workflow
   |
   v
+-------------------------------+
| Agentic Orchestrator          |
| (GitHub Copilot, GPT-4.1)     |
+-------------------------------+
   |
   v
+-------------------------------+
| Lesson 1: Requirements        |
+-------------------------------+
   |
   v
+-------------------------------+
| Lesson 2: API Contract        |
+-------------------------------+
   |
   v
+-------------------------------+
| Lesson 4: Test Design         |
+-------------------------------+
   |
   v
+-------------------------------+
| Lesson 5: Automation          |
+-------------------------------+
   |
   v
+-------------------------------+
| Lesson 6: Traceability        |
+-------------------------------+
   |
   v
+-------------------------------+
| Outputs:                      |
| - requirements.json           |
| - posts_contract.json         |
| - test_design_documentation.json |
| - automation_results.json     |
| - traceability_matrix.json    |
+-------------------------------+
```

### Example UI Elements

- **Agent/LLM Banner:**
   > "This workflow is orchestrated by GitHub Copilot (GPT-4.1)"
- **Step Cards:**
   - Show which agent/LLM is running each step, with status and output preview.
- **Trigger Buttons:**
   - "Run All Steps", "Run Test Design Only", etc.
- **Output Download Links:**
   - Download each artifact for traceability.

### Why Hugging Face Spaces?
- Public, easy to share and demo
- Supports Streamlit, Gradio, Flask, and more
- Makes agentic workflows and LLM provenance transparent

---

> This project is designed for both beginners and experienced engineers. All steps are explained in detail, with links to further reading and practical examples. The Hugging Face Spaces deployment makes the agent/LLM orchestration and MCP concepts fully visible and interactive.
