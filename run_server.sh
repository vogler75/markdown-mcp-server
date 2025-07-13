#!/bin/bash

# Markdown MCP Server Launch Script

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

# Check if virtual environment exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "Error: Python virtual environment not found at $VENV_PYTHON"
    echo "Please run: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
    exit 1
fi

# Run the server with any additional arguments
echo "Starting Markdown MCP Server with stdio transport..."
exec "$VENV_PYTHON" "$SCRIPT_DIR/server.py" "$@"
