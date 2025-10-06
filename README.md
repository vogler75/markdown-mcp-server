# Markdown MCP Server

A Model Context Protocol (MCP) server built with FastMCP that reads markdown files and exposes chapters as resources and tools.

## Features

- **Resources**: Exposes each chapter as a separate resource, plus a table of contents
- **Tools**:
  - `get_chapter`: Get the full content of a chapter by its title
  - `list_chapters`: List all available chapters with their titles and levels
  - `search_chapters`: Search for chapters containing specific text (keyword search)
  - `semantic_search`: **NEW!** AI-powered semantic search using vector embeddings
- **Built with FastMCP**: Uses the modern FastMCP framework for simplified server development
- **Vector Search**: Uses sentence-transformers and FAISS for fast semantic similarityMCP Server

A Model Context Protocol (MCP) server that reads markdown files and exposes chapters as resources and tools.

## Features

- **Resources**: Exposes each chapter as a separate resource, plus a table of contents
- **Tools**: 
  - `get-chapter`: Get the full content of a chapter by its title
  - `list-chapters`: List all available chapters with their titles and levels
  - `search-chapters`: Search for chapters containing specific text

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using the virtual environment:
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Usage

### Running the Server

#### Default Mode (stdio - for MCP clients like Claude Desktop)
Using the launch script (recommended):
```bash
./run_server.sh --file file.md
```

Or directly with Python:
```bash
python server.py --file file.md
```

If using a virtual environment:
```bash
.venv/bin/python server.py --file file.md
```

#### HTTP Mode (for web/API access)

**Streamable-HTTP** (recommended for HTTP):
```bash
python server.py --file file.md --transport streamable-http --host 127.0.0.1 --port 8000
```
- **Endpoint**: `http://127.0.0.1:8000/mcp`
- Default path: `/mcp`

**SSE (Server-Sent Events)**:
```bash
python server.py --file file.md --transport sse --host 127.0.0.1 --port 8000
```
- **Endpoint**: `http://127.0.0.1:8000/sse`
- Default path: `/sse`

**Stateless HTTP** (no session persistence):
```bash
python server.py --file file.md --stateless --json-response --host 127.0.0.1 --port 8000
```

### Command Line Options

- `--file`: Path to the markdown file to serve (default: `file.md`)
- `--log-level`: Set logging level (DEBUG, INFO, WARNING, ERROR)
- `--transport`: Transport protocol - `stdio` (default), `streamable-http`, or `sse`
- `--host`: Host address for HTTP server (default: `127.0.0.1`)
- `--port`: Port for HTTP server (default: `8000`)
- `--stateless`: Run as stateless HTTP server (no session persistence)
- `--json-response`: Use JSON response format instead of SSE (for stateless HTTP)

### Examples

**Basic usage with stdio:**
```bash
python server.py --file file.md --log-level DEBUG
```

**HTTP server with semantic search:**
```bash
python server.py --file documentation.md --transport streamable-http --port 8000
# Access at: http://127.0.0.1:8000/mcp
```

**Custom port and host:**
```bash
python server.py --file file.md --transport streamable-http --host 0.0.0.0 --port 3000
# Access at: http://0.0.0.0:3000/mcp
```

## How it Works

The server uses FastMCP to create a simplified MCP server that:

1. **Parses** markdown files and identifies chapters based on header levels (# ## ### etc.)
2. **Exposes Resources**: Each chapter becomes a resource accessible via URI like `markdown://chapter/0`
3. **Provides Tools**: Three tools for interacting with the chapters
4. **Automatic Registration**: FastMCP automatically handles resource and tool registration

### Resources

- `markdown://table-of-contents`: Complete table of contents
- `markdown://chapter/{index}`: Individual chapters by index

### Tools

#### get_chapter
Retrieves a chapter by its title.

**Parameters:**
- `title` (string): The title of the chapter to retrieve

**Example:**
```json
{
  "name": "get_chapter",
  "arguments": {
    "title": "API documentation for WinCC OA JavaScript Manager for Node.js®"
  }
}
```

#### list_chapters
Lists all available chapters with their titles and hierarchy levels.

**Parameters:** None

#### search_chapters
Searches for chapters containing specific text in titles or content (keyword-based).

**Parameters:**
- `query` (string): Text to search for

#### semantic_search
**NEW!** Searches for chapters using AI-powered semantic similarity. Understands meaning and context, not just exact keyword matches.

**Parameters:**
- `query` (string): Natural language query describing what you're looking for
- `top_k` (int, optional): Number of results to return (default: 5)

**Example:**
```json
{
  "name": "semantic_search",
  "arguments": {
    "query": "How do I handle errors in async functions?",
    "top_k": 3
  }
}
```

**Benefits over keyword search:**
- Understands synonyms and related concepts
- Finds relevant content even without exact keyword matches
- Ranks results by semantic relevance
- Works well with natural language queries

## File Structure

The server expects markdown files with clear header structure:

```markdown
# Main Title
Content here...

## Chapter 1
Chapter content...

### Subsection 1.1
Subsection content...

## Chapter 2
More content...
```

## Testing

Run the test script to verify everything works:

```bash
python test_server.py
```

## MCP Client Integration

This server follows the Model Context Protocol specification and uses FastMCP for simplified development. The server communicates via stdio and provides:

- **Resource listing and reading**: Access to all chapters and table of contents
- **Tool listing and execution**: Three tools for chapter interaction
- **FastMCP Features**: Automatic schema generation, simplified decorators, and built-in error handling
- **MCP Inspector Compatible**: Works perfectly with MCP Inspector and other MCP clients

The FastMCP framework provides:
- Automatic JSON schema generation for tools
- Simplified resource and tool registration using decorators
- Built-in error handling and logging
- Compatible with all MCP transport protocols

## Example Chapter Structure

Based on the provided `file.md`, the server will expose chapters like:

- API documentation for WinCC OA JavaScript Manager for Node.js®
- Enumerations
- Classes  
- Interfaces
- Type Aliases
- Variables
- Functions

Each with their respective subsections and content.
