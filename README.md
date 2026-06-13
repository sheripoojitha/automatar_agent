# AutomatR Intelligence: Type-Safe Invoice Processing Agent

An enterprise-grade, asynchronous data-extraction pipeline built with **Pydantic AI** and powered by the **Groq Llama-3.3** model. This agent acts as an automated backend assistant that ingests messy, unstructured conversation blocks or invoice texts and instantly normalizes them into strict, type-validated data schemas.

## 🚀 Key Features
- **Structured Outputs:** Automatically parses conversational text directly into robust Python data objects without unpredictable string operations or regex.
- **Enterprise Dependency Injection:** Leverages Pydantic AI's `RunContext` to securely manage corporate environment scopes and mock database states.
- **Strict Data Validation:** Prevents schema drift or format corruption down the pipeline by enforcing explicit data blueprints at the execution layer.

## 🛠️ Project Architecture
The application layout is designed with clean separation of concerns:
- `models.py`: Defines the immutable Pydantic output data structures (`ProcessedInvoice`, `LineItem`).
- `service.py`: Encapsulates infrastructure dependencies, database verification methods, and runtime context trackers.
- `agent.py`: Houses system prompts, guardrails, and initializes the core Groq execution brain.
- `main.py`: The orchestrator and execution script that handles the asynchronous run loop.

## 💻 Tech Stack
- **Languages:** Python
- **AI Framework:** Pydantic AI
- **LLM Engine:** Groq Cloud API (`llama-3.3-70b-versatile`)
- **Validation:** Pydantic v2

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/automatr_agent.git](https://github.com/YOUR_GITHUB_USERNAME/automatr_agent.git)
   cd automatr_agent
