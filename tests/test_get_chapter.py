#!/usr/bin/env python3
"""
Test script specifically for testing the get_chapter functionality
"""

import asyncio
from server import setup_markdown_server

async def test_get_chapter():
    """Test the get_chapter tool to ensure it includes sub-chapters."""
    print("Testing get_chapter functionality...")
    
    # Set up the server
    mcp = setup_markdown_server("file.md")
    
    # Get the get_chapter tool
    tools = mcp._tool_manager.list_tools()
    get_chapter_tool = None
    for tool in tools:
        if tool.name == "get_chapter":
            get_chapter_tool = tool
            break
    
    if not get_chapter_tool:
        print("ERROR: get_chapter tool not found!")
        return
    
    # Test getting a chapter that should have sub-chapters
    test_chapters = [
        "Enumerations",  # This should include all enumeration sub-chapters
        "WinccoaCnsAction",  # This should include its enumeration members
        "API documentation for WinCC OA JavaScript Manager for Node.js®"  # Top level chapter
    ]
    
    for chapter_title in test_chapters:
        print(f"\n{'='*60}")
        print(f"Testing chapter: '{chapter_title}'")
        print('='*60)
        
        # Get the actual function from the server's tools
        get_chapter_fn = None
        for name, fn in mcp._tools.items():
            if name == "get_chapter":
                get_chapter_fn = fn
                break
        
        if not get_chapter_fn:
            print(f"ERROR: Could not find get_chapter function!")
            continue
            
        # Call the function
        result = get_chapter_fn(title=chapter_title)
        
        # Count the number of headers in the result to see if sub-chapters are included
        lines = result.split('\n')
        header_count = sum(1 for line in lines if line.strip().startswith('#'))
        
        print(f"Found {header_count} headers in the chapter content")
        print(f"First 500 characters of content:")
        print(result[:500] + "..." if len(result) > 500 else result)
        
        # Check if sub-chapters are included by looking for nested headers
        has_subchapters = any(line.strip().startswith('##') for line in lines)
        print(f"\nContains sub-chapters: {has_subchapters}")

if __name__ == "__main__":
    asyncio.run(test_get_chapter())