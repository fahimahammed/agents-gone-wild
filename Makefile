# Makefile for Agents Gone Wild

.PHONY: clean-venv clean-pycache clean-uv clean-all help

help:
	@echo "Available commands:"
	@echo "  make clean-venv     - Remove all .venv directories in the project"
	@echo "  make clean-pycache  - Remove all __pycache__ and .pyc files"
	@echo "  make clean-uv       - Clean the uv cache"
	@echo "  make clean-all      - Run all clean commands to save maximum space"

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
