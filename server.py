#!/usr/bin/env python3
"""
Markdown MCP Server

A Model Context Protocol server that reads markdown files and exposes chapters
as resources and provides tools to get chapter content.
"""

import asyncio
import logging
import re
from typing import Dict, List, Optional, Any
from pathlib import Path
import argparse

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.resources import FunctionResource
from pydantic import AnyUrl
import mcp.server.stdio
import mcp.types as types


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("markdown-mcp-server")


class MarkdownChapter:
    """Represents a markdown chapter with its content and metadata."""
    
    def __init__(self, title: str, content: str, level: int, line_number: int):
        self.title = title
        self.content = content
        self.level = level
        self.line_number = line_number
    
    def __repr__(self):
        return f"MarkdownChapter(title='{self.title}', level={self.level}, line={self.line_number})"


class MarkdownParser:
    """Parses markdown files and extracts chapters."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.chapters: List[MarkdownChapter] = []
        self.content = ""
        
    def parse(self) -> List[MarkdownChapter]:
        """Parse the markdown file and extract chapters."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
        except FileNotFoundError:
            logger.error(f"File not found: {self.file_path}")
            return []
        except Exception as e:
            logger.error(f"Error reading file {self.file_path}: {e}")
            return []
        
        lines = self.content.split('\n')
        chapters = []
        current_chapter = None
        
        for i, line in enumerate(lines):
            # Check for headers (# ## ### etc.)
            header_match = re.match(r'^(#{1,6})\s+(.+)', line.strip())
            if header_match:
                # Save previous chapter if exists
                if current_chapter:
                    chapters.append(current_chapter)
                
                # Start new chapter
                level = len(header_match.group(1))
                title = header_match.group(2).strip()
                current_chapter = {
                    'title': title,
                    'level': level,
                    'line_number': i + 1,
                    'content_lines': [line]
                }
            elif current_chapter:
                # Add line to current chapter
                current_chapter['content_lines'].append(line)
        
        # Add the last chapter
        if current_chapter:
            chapters.append(current_chapter)
        
        # Convert to MarkdownChapter objects
        self.chapters = []
        for chapter_data in chapters:
            content = '\n'.join(chapter_data['content_lines'])
            chapter = MarkdownChapter(
                title=chapter_data['title'],
                content=content,
                level=chapter_data['level'],
                line_number=chapter_data['line_number']
            )
            self.chapters.append(chapter)
        
        logger.info(f"Parsed {len(self.chapters)} chapters from {self.file_path}")
        return self.chapters
    
    def get_chapter_by_title(self, title: str) -> Optional[MarkdownChapter]:
        """Get a chapter by its title (case-insensitive)."""
        for chapter in self.chapters:
            if chapter.title.lower() == title.lower():
                return chapter
        return None
    
    def get_table_of_contents(self) -> str:
        """Generate a table of contents from all chapters."""
        toc_lines = ["# Table of Contents\n"]
        for chapter in self.chapters:
            indent = "  " * (chapter.level - 1)
            toc_lines.append(f"{indent}- {chapter.title}")
        
        return '\n'.join(toc_lines)


# Global parser instance
parser: Optional[MarkdownParser] = None


def setup_markdown_server(file_path: str, stateless: bool = False, json_response: bool = False, host: str = "127.0.0.1", port: int = 8000) -> FastMCP:
    """Set up the FastMCP server with markdown functionality."""
    global parser
    
    # Initialize parser
    parser = MarkdownParser(file_path)
    chapters = parser.parse()
    
    # Create FastMCP server with appropriate configuration
    if stateless:
        mcp = FastMCP(
            name="markdown-mcp-server", 
            instructions=f"A stateless server that provides access to {len(chapters)} chapters from a markdown file.",
            stateless_http=True,
            json_response=json_response,
            host=host,
            port=port
        )
    else:
        mcp = FastMCP(
            name="markdown-mcp-server", 
            instructions=f"A server that provides access to {len(chapters)} chapters from a markdown file.",
            host=host,
            port=port
        )
    
    # Add table of contents resource
    def get_table_of_contents() -> str:
        return parser.get_table_of_contents() if parser else ""
    
    toc_resource = FunctionResource(
        uri=AnyUrl("markdown://table-of-contents"),
        name="Table of Contents",
        description="Table of contents for the markdown file",
        fn=get_table_of_contents
    )
    mcp.add_resource(toc_resource)
    
    # Add chapter resources
    for i, chapter in enumerate(chapters):
        def get_chapter_content(chapter_content=chapter.content):
            return chapter_content
        
        chapter_resource = FunctionResource(
            uri=AnyUrl(f"markdown://chapter/{i}"),
            name=f"Chapter: {chapter.title}",
            description=f"Level {chapter.level} chapter: {chapter.title}",
            fn=get_chapter_content
        )
        mcp.add_resource(chapter_resource)
    
    # Add tools
    @mcp.tool()
    def get_chapter(title: str) -> str:
        """Get the full content of a chapter by its title, including all sub-chapters."""
        if not parser:
            return "Error: Parser not initialized"
        
        if not title:
            return "Error: Chapter title is required"
        
        chapter = parser.get_chapter_by_title(title)
        if chapter:
            # Find the index of this chapter
            chapter_index = parser.chapters.index(chapter)
            
            # Collect content from this chapter and all its sub-chapters
            content_parts = [chapter.content]
            
            # Look for sub-chapters (chapters with higher level that follow this one)
            for i in range(chapter_index + 1, len(parser.chapters)):
                next_chapter = parser.chapters[i]
                # If we hit a chapter with same or lower level, stop
                if next_chapter.level <= chapter.level:
                    break
                # Otherwise, include this sub-chapter
                content_parts.append(next_chapter.content)
            
            # Join all content parts
            full_content = '\n'.join(content_parts)
            return full_content
        else:
            # Try to find similar chapters
            similar_chapters = []
            for ch in parser.chapters:
                if title.lower() in ch.title.lower():
                    similar_chapters.append(ch.title)
            
            if similar_chapters:
                suggestion = f"Chapter '{title}' not found. Did you mean one of these?\n"
                for similar in similar_chapters[:5]:
                    suggestion += f"- {similar}\n"
                return suggestion
            else:
                return f"Chapter '{title}' not found. Use 'list-chapters' to see available chapters."
    
    @mcp.tool()
    def list_chapters() -> str:
        """List all available chapters with their titles and levels."""
        if not parser:
            return "Error: Parser not initialized"
        
        chapter_list = "# Available Chapters\n\n"
        for i, chapter in enumerate(parser.chapters):
            indent = "  " * (chapter.level - 1)
            chapter_list += f"{indent}{i+1}. {chapter.title} (Level {chapter.level})\n"
        
        return chapter_list
    
    @mcp.tool()
    def search_chapters(query: str) -> str:
        """Search for chapters containing specific text."""
        if not parser:
            return "Error: Parser not initialized"
        
        if not query:
            return "Error: Search query is required"
        
        query_lower = query.lower()
        matching_chapters = []
        
        for chapter in parser.chapters:
            if (query_lower in chapter.title.lower() or 
                query_lower in chapter.content.lower()):
                matching_chapters.append(chapter)
        
        if matching_chapters:
            results = f"# Search Results for '{query}'\n\n"
            results += f"Found {len(matching_chapters)} matching chapter(s):\n\n"
            for chapter in matching_chapters:
                results += f"## {chapter.title}\n"
                results += f"- Level: {chapter.level}\n"
                results += f"- Line: {chapter.line_number}\n\n"
            return results
        else:
            return f"No chapters found containing '{query}'"
    
    return mcp


def main():
    """Main entry point."""
    arg_parser = argparse.ArgumentParser(description="Markdown MCP Server")
    arg_parser.add_argument(
        "--file",
        type=str,
        default="file.md",
        help="Path to the markdown file to serve (default: file.md)"
    )
    arg_parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Log level (default: INFO)"
    )
    arg_parser.add_argument(
        "--transport",
        type=str,
        default="stdio",
        choices=["stdio", "streamable-http"],
        help="Transport protocol to use (default: stdio)"
    )
    arg_parser.add_argument(
        "--stateless",
        action="store_true",
        help="Run as stateless HTTP server (no session persistence)"
    )
    arg_parser.add_argument(
        "--json-response",
        action="store_true",
        help="Use JSON response format instead of SSE (for stateless HTTP)"
    )
    arg_parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host address for HTTP server (default: 127.0.0.1)"
    )
    arg_parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for HTTP server (default: 8000)"
    )
    
    args = arg_parser.parse_args()
    
    # Set up logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create and run server
    mcp = setup_markdown_server(args.file, args.stateless, args.json_response, args.host, args.port)
    mcp.run(transport=args.transport)


if __name__ == "__main__":
    main()
