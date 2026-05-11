# CodeCoach AI 🤖

An intelligent programming tutor built with **Python**, **Flask**, and **LangChain**, with Hexagonal Architecture.
The system acts as a mentor, generating personalized coding challenges and providing architectural feedback on user submissions.

##  Project Goals
This project demonstrates **AI Software Engineering** practices, focusing on:
- **Hexagonal Architecture (Ports & Adapters):** Ensuring the core logic is decoupled from LLM providers and web frameworks.
- **TDD (Test-Driven Development):** High-test coverage to ensure domain reliability.
- **Structured Output:** Utilizing Pydantic to enforce data integrity on non-deterministic LLM responses.
- **Observability:** Full tracing of AI chains to monitor latency, cost, and performance.

---

## Tech Stack
- **Backend:** Flask (Python 3.11)
- **AI Orchestration:** LangChain (LCEL)
- **Data Validation:** Pydantic v2
- **Infrastructure:** Docker & Docker Compose
- **Testing:** Pytest & Pytest-Mock

---

##  Architecture Overview
The project follows **Hexagonal Architecture** principles to maintain a clean separation of concerns:

- `src/domain`: Pure Python business logic and entities (Validation via Pydantic).
- `src/application`: Use cases that orchestrate system flow.
- `src/infrastructure`: 
    - `web/`: Flask blueprints, routes, and request handling.
    - `ai/`: LangChain implementations, Prompt Templates, and LLM Adapters.

---

##  Getting Started

### Prerequisites
- Docker & Docker Compose
- OpenAI API Key (configured in `.env`)

### Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JonathanWG/code-coach-ai.git](https://github.com/JonathanWG/code-coach-ai.git)
   cd code-coach-ai

2. **Configure Enviroment:**
   ```bash
   docker-compose up --build

The API will be available at http://localhost:5000.
   
