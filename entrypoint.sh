#!/bin/bash
set -e

# Run the server with all arguments passed from docker run
echo "Starting Markdown MCP Server..."
echo "Arguments: $@"
echo ""

exec python /app/server.py "$@"
