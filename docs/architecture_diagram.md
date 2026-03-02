# MCP Training Project Architecture Diagram

Below is a visual diagram of the MCP agentic workflow, with notes for each component. You can view and edit this diagram in GitHub using Mermaid syntax.

```mermaid
flowchart TD
    subgraph CLIENT["MCP Client UI (Streamlit)"]
        A[User]
        B[UI: Workflow Selection & Input]
        C[Request Sender]
        D[Results Display & Download]
    end
    subgraph SERVER["MCP Server (FastAPI)"]
        E[API Endpoint /run_action]
        F[Agentic Orchestrator]
        G[LLM Integration (OpenAI/Ollama)]
        H[Workflow Logic]
        I[Provenance & Logging]
    end
    subgraph ARTIFACTS["Artifacts & Outputs"]
        J[Requirements]
        K[API Contract]
        L[Test Design]
        M[Automation Results]
        N[Traceability Matrix]
    end

    A --> B --> C --> E
    E --> F --> H
    F --> G
    H --> I
    I --> D
    H --> J
    H --> K
    H --> L
    H --> M
    H --> N
    D --> J
    D --> K
    D --> L
    D --> M
    D --> N

    %% Notes for each object
    click A "#" "User: Triggers workflows and provides input."
    click B "#" "UI: Lets user select workflow steps and enter context."
    click C "#" "Request Sender: Sends context and actions to server."
    click D "#" "Results Display: Shows outputs and allows downloads."
    click E "#" "API Endpoint: Receives requests from client."
    click F "#" "Agentic Orchestrator: Coordinates workflow steps."
    click G "#" "LLM Integration: Calls OpenAI/Ollama for agentic responses."
    click H "#" "Workflow Logic: Implements MCP steps and logic."
    click I "#" "Provenance: Logs agentic actions and workflow steps."
    click J "#" "Requirements: Extracted from issues or context."
    click K "#" "API Contract: Extracted and documented for testing."
    click L "#" "Test Design: Structured test cases for APIs."
    click M "#" "Automation Results: Outputs from automated tests."
    click N "#" "Traceability Matrix: Maps requirements to tests and results."
```

## Summary
- **User** interacts with the MCP Client UI to select workflows and provide context.
- **Client UI** sends requests to the MCP Server, displays results, and allows output downloads.
- **Server** orchestrates agentic workflows, integrates LLMs, and logs provenance.
- **Artifacts** (requirements, contracts, tests, results, traceability) are generated and made available for review and download.
- Each component is annotated for clarity. View this diagram in GitHub for interactive notes.
