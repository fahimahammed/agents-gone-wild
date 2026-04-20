import os
from dotenv import load_dotenv
from typing import Optional, Dict, Any

load_dotenv()

def get_llm_config(provider: str, model: str, **kwargs) -> Dict[str, Any]:
    """
    Returns a configuration dictionary for a given LLM provider.
    """
    config = {
        "provider": provider,
        "model_name": model,
        "temperature": kwargs.get("temperature", 0.7),
        "max_tokens": kwargs.get("max_tokens", 2000),
    }

    if provider == "openai":
        config["api_key"] = os.getenv("OPENAI_API_KEY")
    elif provider == "anthropic":
        config["api_key"] = os.getenv("ANTHROPIC_API_KEY")
    elif provider == "ollama":
        config["base_url"] = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    elif provider == "openrouter":
        config["api_key"] = os.getenv("OPENROUTER_API_KEY")
        config["base_url"] = "https://openrouter.ai/api/v1"
    
    # Merge additional kwargs
    config.update(kwargs)
    return config

def get_openai_config(model: str = "gpt-4o", **kwargs):
    return get_llm_config("openai", model, **kwargs)

def get_anthropic_config(model: str = "claude-3-5-sonnet-20240620", **kwargs):
    return get_llm_config("anthropic", model, **kwargs)

def get_ollama_config(model: str = "llama3", **kwargs):
    return get_llm_config("ollama", model, **kwargs)

def get_openrouter_config(model: str = "google/gemini-2.0-flash-001", **kwargs):
    return get_llm_config("openrouter", model, **kwargs)

def get_default_config():
    """Helper to get a default reasonable config."""
    return get_openrouter_config()
