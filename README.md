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
├── core/               # Language-agnostic abstractions
│   ├── python/         # Python BaseAgent, Tools, Memory
│   └── node/           # TypeScript/Node.js equivalents
├── projects/           # 15+ Feature-based standalone systems
│   ├── cli-math-agent/
│   ├── web-scout/
│   └── ...
├── practice/           # Coding challenges per concept
├── docs/               # Conceptual deep-dives
└── examples/           # Minimal snippets & notebooks
```

---

## Projects Index

| Project | Feature | Level | Tech |
| :--- | :--- | :---: | :--- |
| **CLI Quickstart** | Basic ReAct loop | 🟢 | Python |
| **Smart Calculator** | Multi-tool calling | 🟢 | Python |
| **File Organizer** | System tool integration | 🟡 | Node.js |
| **Semantic Search** | Vector DB + Memory | 🟡 | Python |
| **Voice Command** | STT/TTS Agents | 🟡 | Python |
| **Web Researcher** | Browser Automation | 🟠 | Node.js |
| **Multi-Agent Dev** | Collaborative coding | 🔴 | Python |
| **MCP Hub** | Protocol integration | 🔴 | Python/Node |

---

## Core System Design

Our `core/` library provides a standardized way to build agents:

1. **`BaseAgent`**: Modular engine for LLM interactions.
2. **`Tool Registry`**: Dynamic tool discovery and validation.
3. **`Memory Manager`**: Pluggable memory backends (Local, Redis, Vector).
4. **`Provider Abstraction`**: Switch between OpenAI, Anthropic, or Ollama with zero code changes.

---

## Getting Started

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/agents-gone-wild.git
   cd agents-gone-wild
   ```

2. **Setup your environment**:
   ```bash
   cp .env.example .env
   # Add your API keys (OpenAI, Anthropic, etc.)
   ```

3. **Explore a project**:
   ```bash
   cd projects/cli-quickstart-agent
   pip install -r requirements.txt
   python main.py
   ```

---
