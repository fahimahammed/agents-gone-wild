import json
from typing import Callable, Dict, Any, List

# Internal storage for tools
_TOOLS: Dict[str, Dict[str, Any]] = {}

def register_tool(name: str, description: str, parameters: Dict[str, Any]):
    """
    Decorator to register a function as a tool.
    """
    def decorator(func: Callable):
        _TOOLS[name] = {
            "name": name,
            "description": description,
            "func": func,
            "parameters": parameters
        }
        return func
    return decorator

def get_tool_schemas() -> List[Dict[str, Any]]:
    """
    Returns tools in OpenAI-compatible function format.
    """
    return [
        {
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["parameters"]
            }
        }
        for tool in _TOOLS.values()
    ]

def execute_tool(name: str, arguments_json: str) -> str:
    """
    Executes a registered tool by name with JSON arguments.
    """
    if name not in _TOOLS:
        return f"Error: Tool '{name}' not found."
    
    try:
        args = json.loads(arguments_json)
        result = _TOOLS[name]["func"](**args)
        return str(result)
    except Exception as e:
        return f"Error executing '{name}': {str(e)}"

def get_registered_tools() -> Dict[str, Dict[str, Any]]:
    """Returns the internal tools dictionary."""
    return _TOOLS
