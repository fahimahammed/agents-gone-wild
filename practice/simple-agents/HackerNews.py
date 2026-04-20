import sys
from pathlib import Path

# Add project root to sys.path to access core.config
root = Path(__file__).parent.parent.parent
sys.path.append(str(root))

from core.config import get_openrouter_config
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.hackernews import HackerNewsTools

def run_hn_agent():
    """
    Fetches trending startups and products from HackerNews using an Agno agent.
    """
    # Fetch configuration from the central core
    config = get_openrouter_config(model="anthropic/claude-3-haiku")

    # Initialize the Agent
    agent = Agent(
        model=OpenRouter(
            id=config["model_name"],
            api_key=config["api_key"],
            base_url=config["base_url"]
        ),
        tools=[HackerNewsTools()],
        instructions=[
            "Search for trending startups and products on HackerNews.",
            "Write a detailed report summarizing the most interesting finds.",
            "Focus on innovation, funding, and community sentiment.",
            "Output only the markdown report.",
        ],
        markdown=True,
    )

    # Print the response in a streaming fashion
    agent.print_response("Summarize trending startups and products from today's HackerNews.", stream=True)

if __name__ == "__main__":
    run_hn_agent()