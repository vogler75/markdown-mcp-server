#!/bin/bash
set -e

# Docker image name
IMAGE_NAME="markdown-mcp-server"

echo "Building Docker image: $IMAGE_NAME"
docker build -t "$IMAGE_NAME" .

echo ""
echo "Build complete!"
echo "Image: $IMAGE_NAME"
echo ""
echo "Run with:"
echo "  docker run -v /path/to/your/file.md:/data/file.md -p 3000:3000 $IMAGE_NAME"
