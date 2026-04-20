import json
from typing import List, Dict, Any, Optional
from .tools import get_tool_schemas, execute_tool

def run_agent_loop(
    messages: List[Dict[str, str]],
    config: Dict[str, Any],
    max_iterations: int = 5
) -> str:
    """
    Runs a ReAct-style loop for an agent.
    Updates the 'messages' list in-place and returns the final assistant response.
    """
    try:
        import openai
    except ImportError:
        return "Error: openai package not installed. Please install 'openai' to use the core agent."

    client = openai.OpenAI(
        api_key=config.get("api_key") or "nothing",
        base_url=config.get("base_url")
    )

    for _ in range(max_iterations):
        response = client.chat.completions.create(
            model=config["model_name"],
            messages=messages,
            tools=get_tool_schemas(),
            tool_choice="auto" if get_tool_schemas() else None,
            temperature=config.get("temperature", 0.7),
            max_tokens=config.get("max_tokens", 2000)
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        if not assistant_message.tool_calls:
            return assistant_message.content

        # Handle Tool Calls
        for tool_call in assistant_message.tool_calls:
            result = execute_tool(
                tool_call.function.name, 
                tool_call.function.arguments
            )
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": tool_call.function.name,
                "content": result
            })
        
        # Loop continues to let LLM process tool results

    return "Error: Maximum agent iterations reached."

def create_message(role: str, content: str) -> Dict[str, str]:
    """Helper to create a standard message dictionary."""
    return {"role": role, "content": content}
