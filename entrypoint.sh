#!/bin/bash
set -e

# Default markdown file path
MARKDOWN_FILE="${MARKDOWN_FILE:-/data/file.md}"

# Check if markdown file exists
if [ ! -f "$MARKDOWN_FILE" ]; then
    echo "Warning: Markdown file not found at $MARKDOWN_FILE"
    echo "Please mount a markdown file using:"
    echo "  docker run -v /path/to/your/file.md:/data/file.md ..."
    echo ""
    echo "Creating a sample file for demonstration..."
    mkdir -p /data
    cat > "$MARKDOWN_FILE" << 'EOF'
# Sample Markdown File

## Introduction
This is a sample markdown file for the MCP server.

## Getting Started
Mount your own markdown file to /data/file.md to use your content.

### Example Command
```
docker run -v /path/to/your/file.md:/data/file.md -p 8000:8000 markdown-mcp-server
```
EOF
fi

# Run the server with the markdown file and any additional arguments
echo "Starting Markdown MCP Server..."
echo "Markdown file: $MARKDOWN_FILE"
echo "Arguments: $@"
echo ""

exec python /app/server.py --file "$MARKDOWN_FILE" --transport streamable-http --host 0.0.0.0 --port 3000 "$@"
