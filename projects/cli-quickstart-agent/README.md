# 🚀 CLI Quickstart Agent (Functional)

This is the "Hello World" of agentic AI. It demonstrates a clean, **functional** ReAct loop using our modular `core` foundation.

## 🌟 Features
- Modular functional interface (no heavy class hierarchies).
- Flexible tool registration via pure functions and decorators.
- Built-in session state management through simple list append operations.

## 🛠️ Architecture
1. **Config**: `get_openrouter_config()` retrieves provider settings.
2. **Tools**: `@register_tool` maps functions to the agent's world.
3. **Execution**: `run_agent_loop()` handles the sequence of thoughts and tool calls.

## 🚥 Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**:
   Add your API keys to the `.env` file in the root.

3. **Run the agent**:
   ```bash
   python main.py
   ```

## 🧪 Key Learning Outcomes
- Understanding functional state management in agentic loops.
- Decorator-based tool isolation.
- Passing context and configurations as plain objects/dicts for maximum flexibility.
