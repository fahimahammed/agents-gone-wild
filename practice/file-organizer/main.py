import sys
import os
from datetime import datetime

# Add the root directory to sys.path to access the core package for config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from core.config import get_openrouter_config
from agent import run_agent_loop, create_message
from tools import register_tool

# Register File System Tools
@register_tool(
    name="list_files",
    description="List all files in the current working directory.",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def list_files():
    try:
        files = os.listdir(".")
        return ", ".join(files)
    except Exception as e:
        return f"Error listing files: {str(e)}"

@register_tool(
    name="get_file_metadata",
    description="Get metadata for a specific file.",
    parameters={
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "The name of the file."
            }
        },
        "required": ["filename"]
    }
)
def get_file_metadata(filename: str):
    try:
        if not os.path.exists(filename):
            return f"Error: File '{filename}' not found."
        
        size = os.path.getsize(filename)
        mod_time = datetime.fromtimestamp(os.path.getmtime(filename)).strftime("%Y-%m-%d %H:%M:%S")
        return f"Size: {size} bytes, Last Modified: {mod_time}"
    except Exception as e:
        return f"Error getting metadata: {str(e)}"

def main():
    print("Agentic AI Practice: File Metadata Organizer")
    print("This agent can inspect your local directory and provide file details.")
    print("Type 'exit' to quit.")
    
    config = get_openrouter_config()
    messages = [
        create_message("system", "You are a file system assistant. Use tools to list and inspect local files.")
    ]
    
    while True:
        try:
            user_input = input("\nFile Query: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            messages.append(create_message("user", user_input))
            
            print("Inspecting file system...")
            response = run_agent_loop(messages, config)
            print(f"Agent: {response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
