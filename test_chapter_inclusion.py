#!/usr/bin/env python3
"""
Direct test of the chapter parsing and retrieval logic
"""

from server import MarkdownParser

def test_chapter_inclusion():
    """Test that get_chapter includes sub-chapters."""
    print("Testing chapter inclusion functionality...")
    
    # Parse the markdown file
    parser = MarkdownParser("file.md")
    chapters = parser.parse()
    
    # Test with "Enumerations" chapter which should have many sub-chapters
    test_title = "Enumerations"
    
    # Find the chapter
    chapter = parser.get_chapter_by_title(test_title)
    if not chapter:
        print(f"ERROR: Chapter '{test_title}' not found!")
        return
    
    print(f"\nFound chapter: {chapter.title} (Level {chapter.level})")
    
    # Find the index of this chapter
    chapter_index = parser.chapters.index(chapter)
    
    # Show what chapters follow this one
    print(f"\nChapters following '{test_title}':")
    for i in range(chapter_index + 1, min(chapter_index + 10, len(parser.chapters))):
        next_ch = parser.chapters[i]
        print(f"  - {next_ch.title} (Level {next_ch.level})")
        if next_ch.level <= chapter.level:
            print(f"    ^ This chapter has same/lower level, would stop here")
            break
    
    # Now simulate what get_chapter does
    print(f"\n{'='*60}")
    print("Simulating get_chapter logic:")
    print('='*60)
    
    # Collect content from this chapter and all its sub-chapters
    content_parts = [chapter.content]
    sub_chapter_count = 0
    
    # Look for sub-chapters
    for i in range(chapter_index + 1, len(parser.chapters)):
        next_chapter = parser.chapters[i]
        if next_chapter.level <= chapter.level:
            break
        content_parts.append(next_chapter.content)
        sub_chapter_count += 1
        print(f"Including sub-chapter: {next_chapter.title} (Level {next_chapter.level})")
    
    print(f"\nTotal sub-chapters included: {sub_chapter_count}")
    
    # Join all content
    full_content = '\n'.join(content_parts)
    
    # Show statistics
    print(f"\nContent statistics:")
    print(f"- Original chapter content length: {len(chapter.content)} chars")
    print(f"- Full content with sub-chapters length: {len(full_content)} chars")
    print(f"- Number of headers in full content: {full_content.count('#')}")
    
    # Show a preview
    print(f"\nFirst 1000 characters of full content:")
    print(full_content[:1000])

if __name__ == "__main__":
    test_chapter_inclusion()