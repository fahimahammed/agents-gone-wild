import sys
import os

# Add the root directory to sys.path to access the core package for config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from core.config import get_openrouter_config
from agent import run_agent_loop, create_message
from tools import register_tool

# Register Arithmetic Tools
@register_tool(
    name="add_numbers",
    description="Calculate the sum of two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "required": ["a", "b"]
    }
)
def add_numbers(a: float, b: float):
    return a + b

@register_tool(
    name="subtract_numbers",
    description="Calculate the difference between two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "required": ["a", "b"]
    }
)
def subtract_numbers(a: float, b: float):
    return a - b

@register_tool(
    name="multiply_numbers",
    description="Calculate the product of two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "required": ["a", "b"]
    }
)
def multiply_numbers(a: float, b: float):
    return a * b

@register_tool(
    name="divide_numbers",
    description="Calculate the quotient of two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "required": ["a", "b"]
    }
)
def divide_numbers(a: float, b: float):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    print("Agentic AI Practice: Smart Calculator")
    print("This agent uses tools for arithmetic to ensure 100% accuracy.")
    print("Type 'exit' to quit.")
    
    config = get_openrouter_config()
    messages = [
        create_message("system", "You are a calculator agent. Use tools for all math operations.")
    ]
    
    while True:
        try:
            user_input = input("\nMath Query: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            messages.append(create_message("user", user_input))
            
            print("Processing calculation...")
            response = run_agent_loop(messages, config)
            print(f"Result: {response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
