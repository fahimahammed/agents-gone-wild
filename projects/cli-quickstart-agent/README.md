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

## Setup

1. Install uv:
   curl -LsSf https://astral.sh/uv/install.sh | sh

2. Run the agent:
   uv run main.py

## Examples

Example 1: Basic Greeting
Input: Hello, who are you?
Output: I am a CLI agent designed to help you with various tasks.

Example 2: Time Check
Input: What is the current time?
Output: The current time is 2026-04-20 20:15:00.

## 🧪 Key Learning Outcomes
- Understanding functional state management in agentic loops.
- Decorator-based tool isolation.
- Passing context and configurations as plain objects/dicts for maximum flexibility.
