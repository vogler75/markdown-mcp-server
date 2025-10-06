#!/usr/bin/env python3
"""
Test script for the Markdown MCP Server
"""

import asyncio
import json
from server import MarkdownParser, setup_markdown_server


async def test_parser():
    """Test the markdown parser."""
    print("Testing Markdown Parser...")
    parser = MarkdownParser("file.md")
    chapters = parser.parse()
    
    print(f"Found {len(chapters)} chapters:")
    for i, chapter in enumerate(chapters[:5]):  # Show first 5 chapters
        print(f"  {i+1}. {chapter.title} (Level {chapter.level})")
    
    print("\nTable of Contents:")
    toc = parser.get_table_of_contents()
    print(toc[:500] + "..." if len(toc) > 500 else toc)
    
    # Test chapter retrieval
    if chapters:
        first_chapter = chapters[0]
        print(f"\nFirst chapter '{first_chapter.title}':")
        print(first_chapter.content[:200] + "..." if len(first_chapter.content) > 200 else first_chapter.content)


async def test_server_setup():
    """Test server initialization."""
    print("\nTesting FastMCP Server Setup...")
    mcp = setup_markdown_server("file.md")
    print(f"Server initialized with FastMCP")
    print(f"Server name: {mcp.name}")
    print(f"Server instructions: {mcp.instructions}")
    
    # Test tools
    tools = mcp._tool_manager.list_tools()
    print(f"\nFound {len(tools)} tools:")
    for tool in tools:
        print(f"  - {tool.name}: {tool.description}")
    
    # Test resources
    resources = mcp._resource_manager._resources
    print(f"\nFound {len(resources)} resources:")
    for uri, resource in list(resources.items())[:5]:  # Show first 5
        print(f"  - {resource.name}: {resource.description}")


if __name__ == "__main__":
    asyncio.run(test_parser())
    asyncio.run(test_server_setup())
