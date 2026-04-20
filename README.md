# Agents Gone Wild: Zero to Hero in Agentic AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A comprehensive, feature-based repository for building and learning **Agentic AI systems**. From core concepts to production-ready multi-agent orchestration.

---

## Learning Roadmap (Zero → Hero)

We follow a **system-first approach**. Instead of learning languages, you learn how to build increasingly complex agentic capabilities.

### Phase 1: Foundations (The "Thinking" Loop)
- **Concept**: Introduction to Agentic reasoning (ReAct, Chain-of-Thought).
- **Core Skill**: Tool Calling & Function Execution.
- **Project**: `cli-quickstart-agent`

### Phase 2: State & Memory
- **Concept**: Short-term (buffer) vs. Long-term (vector) memory.
- **Core Skill**: Context management and persistence.
- **Project**: `semantic-search-assistant`

### Phase 3: Knowledge & Retrieval (RAG 2.0)
- **Concept**: Agentic Retrieval Augmented Generation.
- **Core Skill**: Self-correction and multi-step retrieval.
- **Project**: `web-researcher`

### Phase 4: Multi-Agent Orchestration
- **Concept**: Communication patterns (Debate, Hierarchical, Peer-to-peer).
- **Core Skill**: Managing state across multiple agents.
- **Project**: `multi-agent-dev-squad`

### Phase 5: Production & UI
- **Concept**: Observability, Testing, and Real-time interfaces.
- **Core Skill**: Evaluation frameworks and production deployment.
- **Project**: `saas-agent-backend`

---

## 📁 Repository Structure

```text
.
├── core/               # Global configurations (config.py)
├── projects/           # 15+ Feature-based standalone systems
│   ├── cli-quickstart-agent/
│   └── ...
├── practice/           # Hands-on learning & challenges
│   ├── smart-calculator/
│   ├── file-organizer/
│   └── ...
├── docs/               # Conceptual deep-dives
└── Makefile            # Cleanup and maintenance tasks
```

---

## Projects Index

| Project | Feature | Level | Tech |
| :--- | :--- | :---: | :--- |
| **CLI Quickstart** | Basic ReAct loop | 🟢 | Python |
| **Smart Calculator** | Multi-tool calling | 🟢 | Python |
| **File Organizer** | System tool integration | 🟡 | Python (UV) |
| **Semantic Search** | Vector DB + Memory | 🟡 | Python |
| **Voice Command** | STT/TTS Agents | 🟡 | Python |
| **Web Researcher** | Browser Automation | 🟠 | Python |
| **Multi-Agent Dev** | Collaborative coding | 🔴 | Python |
| **MCP Hub** | Protocol integration | 🔴 | Python/Node |

---

## Core Principles

1. **Project Isolation**: Every project is self-contained with its own engine (`agent.py`, `tools.py`).
2. **Minimal Core**: The global `core/` folder strictly contains shared provider configurations.
3. **Function-based**: We prioritize clean, modular functions over complex classes.
4. **UV Powered**: We use the `uv` package manager for lightning-fast execution.

---

## Getting Started

1. **Install uv**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Setup your environment**:
   ```bash
   cp .env.example .env
   # Add your API keys (OpenAI, Anthropic, or OpenRouter)
   ```

3. **Explore a project**:
   ```bash
   cd projects/cli-quickstart-agent
   uv run main.py
   ```

---

## Cleanup and Storage Management

To save disk space and clean up temporary files (like virtual environments and cache), use the provided Makefile:

```bash
# To see all available commands
make help

# To remove all .venv, pycache, and uv cache files
make clean-all
```
