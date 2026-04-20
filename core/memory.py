from typing import List, Dict, Any

def add_message(history: List[Dict[str, str]], role: str, content: str):
    """
    Appends a new message to the history list.
    """
    history.append({"role": role, "content": content})

def get_history_summary(history: List[Dict[str, str]]) -> str:
    """
    Returns a simple string summary of the conversation history.
    """
    return "\n".join([f"{m['role']}: {m['content']}" for m in history if 'content' in m])

def clear_history(history: List[Dict[str, str]]):
    """
    Clears the history list in-place.
    """
    history.clear()
