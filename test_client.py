#!/usr/bin/env python3
"""
Simple MCP client example to test the markdown server
"""

import asyncio
import json
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def test_client():
    """Test client that demonstrates server functionality."""
    
    # Create client session
    server_params = StdioServerParameters(
        command="/Users/vogler/Workspace/markdown-mcp-server/.venv/bin/python",
        args=["/Users/vogler/Workspace/markdown-mcp-server/server.py", "--file", "file.md"]
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize
                await session.initialize()
                
                print("=== Testing Resource Listing ===")
                resources = await session.list_resources()
                print(f"Found {len(resources)} resources:")
                for i, resource in enumerate(resources[:5]):  # Show first 5
                    print(f"  {i+1}. {resource.name}")
                
                print("\n=== Testing Tools ===")
                tools = await session.list_tools()
                print(f"Available tools: {[tool.name for tool in tools]}")
                
                print("\n=== Testing get-chapter tool ===")
                # Test getting a chapter
                result = await session.call_tool("list-chapters", {})
                print("Chapter list result:")
                for content in result.content:
                    print(content.text[:500] + "..." if len(content.text) > 500 else content.text)
                
                print("\n=== Testing search-chapters tool ===")
                # Test search
                result = await session.call_tool("search-chapters", {"query": "Enumeration"})
                print("Search result:")
                for content in result.content:
                    print(content.text[:500] + "..." if len(content.text) > 500 else content.text)
                
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_client())
