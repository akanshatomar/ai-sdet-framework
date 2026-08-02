# AI-SDET Framework

An AI-powered Software Development Engineer in Test (AI-SDET) framework that leverages Large Language Models (LLMs) to generate structured test plans and execute automated browser-based testing using Playwright.

This project demonstrates how AI agents, prompt engineering, validation, observability, and browser automation can be combined to build an intelligent test automation framework.

---

## Features

- AI-generated test plans using Google Gemini
- Prompt-driven test generation
- Structured JSON validation using Pydantic
- Retry mechanism for invalid AI responses
- Browser automation with Playwright
- Structured logging using Loguru
- Modular project architecture
- Unit testing with Pytest

---

## Architecture

```
                User Request
                      │
                      ▼
              Login Agent
                      │
                      ▼
            Prompt Loader
                      │
                      ▼
               Gemini API
                      │
                      ▼
         Structured JSON Test Plan
                      │
                      ▼
            JSON Validator
                      │
          Valid? ───────────── No
             │                  │
             │                  ▼
             │            Retry Manager
             │                  │
             ▼                  │
      Playwright Executor ◄─────┘
             │
             ▼
      Browser Execution
             │
             ▼
      Logging & Reporting
```

---

## Project Structure

```
ai-sdet-framework/
│
├── agents/
│   └── login_agent.py
│
├── executor/
│   └── runner.py
│
├── prompts/
│   └── login_prompt.txt
│
├── tests/
│
├── utils/
│   ├── gemini_client.py
│   ├── json_validator.py
│   ├── logger.py
│   ├── prompt_loader.py
│   ├── retry_manager.py
│
├── logs/
│
├── main.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## Technologies Used

- Python
- Google Gemini API
- Playwright
- Pydantic
- Loguru
- Pytest
- Tenacity
- python-dotenv

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/ai-sdet-framework.git
```

Navigate to the project

```bash
cd ai-sdet-framework
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browser

```bash
playwright install chromium
```

---

## Environment Variables

Create a `.env` file in the project root.

Example

```text
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Project

```bash
python main.py
```

---

## Running Tests

```bash
pytest
```

---

## Example Workflow

1. User requests a login test.
2. Prompt Loader loads the prompt template.
3. Gemini generates a structured JSON test plan.
4. JSON Validator validates the response.
5. Retry Manager retries if validation fails.
6. Playwright executes browser actions.
7. Logger records execution details.

---

## Current Capabilities

- Login workflow generation
- Prompt-based AI interaction
- JSON schema validation
- Retry on invalid AI output
- Browser automation
- Structured logging

---

## Future Improvements

- Multi-agent architecture
- Role-based access control testing
- API testing agent
- Database validation agent
- LangGraph integration
- Support for multiple LLM providers
- Parallel test execution
- HTML execution reports

---

## Design Principles

This framework follows:

- Modular architecture
- Separation of concerns
- Prompt engineering best practices
- AI output validation
- Retry and failure recovery
- Observability through structured logging
- Extensible agent-based design

---

## Author

**Akansha Tomar**

M.Tech – Artificial Intelligence

Python | AI | Machine Learning | Test Automation | Generative AI

LinkedIn: https://linkedin.com/in/<your-linkedin>

GitHub: https://github.com/<your-github>
