#!/bin/bash

# Generate a random auth token
AUTH_TOKEN=$(openssl rand -hex 32)

# Get the absolute path to the current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Docker container name
CONTAINER_NAME="markdown-mcp-server"

# Stop and remove existing container if it exists
docker rm -f "$CONTAINER_NAME" 2>/dev/null

# Run the Docker container
docker run -d \
  --name "$CONTAINER_NAME" \
  -p 3000:8000 \
  -v "$SCRIPT_DIR":/data:ro \
  -e AUTH_TOKEN="$AUTH_TOKEN" \
  markdown-mcp-server:latest \
  --file /data/WinccoaManager.md \
  --transport streamable-http \
  --host 0.0.0.0 \
  --port 8000 \
  --auth-token "$AUTH_TOKEN"

echo "Container started: $CONTAINER_NAME"
echo "Auth token: $AUTH_TOKEN"
echo "Server running on http://localhost:8000/mcp"
echo ""
echo "To view logs: docker logs -f $CONTAINER_NAME"
echo "To stop: docker stop $CONTAINER_NAME"
