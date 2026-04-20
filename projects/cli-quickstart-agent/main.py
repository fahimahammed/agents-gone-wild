import sys
import os
from datetime import datetime

# Add the root directory to sys.path to access the core package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from core.config import get_openrouter_config
from core.agent import run_agent_loop, create_message
from core.tools import register_tool

# 1. Register Tools (Function-Based)
@register_tool(
    name="get_current_time",
    description="Get the current time and date.",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@register_tool(
    name="calculate_sum",
    description="Add two numbers together.",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "required": ["a", "b"]
    }
)
def calculate_sum(a: float, b: float):
    return a + b

# 2. Main Logic
def main():
    print("🤖 (Functional) Agentic AI CLI Quickstart")
    print("Type 'exit' to quit.")
    
    # Configuration
    config = get_openrouter_config()
    
    # Initialize session history
    messages = [
        create_message("system", "You are a helpful CLI agent using functional core library.")
    ]
    
    while True:
        try:
            user_input = input("\n👤 You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            messages.append(create_message("user", user_input))
            
            print("⏳ Agent is thinking...")
            response = run_agent_loop(messages, config)
            print(f"\n🤖 Agent: {response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
