.PHONY: clean-venv clean-pycache clean-uv clean-all install help

help:
	@echo "Available commands:"
	@echo "  make install        - Install uv and setup environment (.env)"
	@echo "  make clean-venv     - Remove all .venv directories in the project"
	@echo "  make clean-pycache  - Remove all __pycache__ and .pyc files"
	@echo "  make clean-uv       - Clean the uv cache"
	@echo "  make clean-all      - Run all clean commands to save maximum space"

install:
	@echo "Checking for uv installation..."
	@if ! command -v uv > /dev/null; then \
		echo "Installing uv..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	else \
		echo "uv is already installed."; \
	fi
	@if [ ! -f .env ]; then \
		echo "Creating .env from .env.example..."; \
		cp .env.example .env; \
		echo "Please update your .env file with your API keys."; \
	else \
		echo ".env file already exists."; \
	fi
	@echo "Installation and setup complete."

clean-venv:
	@echo "Removing all .venv directories..."
	find . -type d -name ".venv" -exec rm -rf {} +
	@echo "Done."

clean-pycache:
	@echo "Removing Python cache files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Done."

clean-uv:
	@echo "Cleaning uv cache..."
	uv cache clean
	@echo "Done."

clean-all: clean-venv clean-pycache clean-uv
	@echo "All clean-up tasks completed successfully."
