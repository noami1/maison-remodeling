#!/usr/bin/env python3
"""
Navbar Sync Script for Maison Remodeling Website

This script extracts the navbar (top bar + header + mobile menu) from index.html
and replaces it in all other HTML files, adjusting paths for subdirectories.

Usage:
    python sync-navbar.py [--dry-run]

Options:
    --dry-run    Show what would be changed without making actual changes
"""

import os
import re
import sys
from pathlib import Path

# Configuration
ROOT_DIR = Path(__file__).parent
INDEX_FILE = ROOT_DIR / "index.html"

# Files to process (relative to ROOT_DIR)
HTML_FILES = [
    # Root level pages
    "about.html",
    "contact.html",
    "blog.html",
    "projects.html",
    "testimonials.html",
    "products.html",
    "locations.html",
    "privacy-policy.html",
    "terms-of-use.html",
    "kitchen-remodeling.html",
    "bathroom-remodeling.html",
    "home-remodeling.html",
    "home-additions.html",
    "adu.html",
    "exterior-remodeling.html",
    "custom-homes.html",
    "commercial-remodeling.html",
    "design-build.html",
    # Blog pages (subdirectory)
    "blog/adu-building-guide.html",
    "blog/bathroom-design-ideas.html",
    "blog/home-addition-ideas.html",
    "blog/home-remodeling-guide-2025.html",
    "blog/kitchen-cabinets-guide.html",
    "blog/kitchen-remodeling-trends-2025.html",
    # Project pages (subdirectory)
    "projects/bathroom-remodeling.html",
    "projects/complete-home-remodeling.html",
    "projects/condo-remodeling.html",
    "projects/kitchen-remodeling.html",
    "projects/outdoor-remodeling.html",
]


def extract_navbar(html_content):
    """
    Extract the navbar section from HTML content.
    Navbar includes: Top Bar + Header + Mobile Menu
    """
    # Find the start - either with comment or the actual top bar div
    # Pattern 1: With comment
    start_match = re.search(r"(<body[^>]*>)\s*\n(\s*)(<!-- Top Bar -->)", html_content)

    if start_match:
        body_tag = start_match.group(1)
        indent = start_match.group(2)
        start_pos = start_match.start(3)  # Start from the comment
    else:
        # Pattern 2: Without comment - look for body tag followed by top bar div
        start_match = re.search(
            r'(<body[^>]*>)\s*\n(\s*)(<div class="bg-dark-900 text-white py-2)',
            html_content,
        )
        if start_match:
            body_tag = start_match.group(1)
            indent = start_match.group(2)
            start_pos = start_match.start(3)
        else:
            print("ERROR: Could not find navbar start in index.html")
            return None

    # Find the end - after mobile menu closes
    # The mobile menu is: <div id="mobile-menu" ...>...</div>
    # We need to find where it ends

    # Look for mobile-menu div and find its closing
    mobile_start = html_content.find('id="mobile-menu"', start_pos)
    if mobile_start == -1:
        print("ERROR: Could not find mobile-menu")
        return None

    # Count divs to find the matching closing tag
    search_start = html_content.rfind("<div", start_pos, mobile_start + 20)
    div_count = 1
    pos = search_start + 5  # Skip past the opening <div

    while div_count > 0 and pos < len(html_content):
        next_open = html_content.find("<div", pos)
        next_close = html_content.find("</div>", pos)

        if next_close == -1:
            break

        if next_open != -1 and next_open < next_close:
            div_count += 1
            pos = next_open + 4
        else:
            div_count -= 1
            pos = next_close + 6

    # pos now points right after the closing </div> of mobile-menu
    end_pos = pos

    # Extract navbar
    navbar_html = html_content[start_pos:end_pos].rstrip()

    return navbar_html


def adjust_paths_for_subdirectory(navbar_html, depth=1):
    """
    Adjust relative paths in navbar for subdirectory pages.
    depth=1 means one level deep (e.g., blog/article.html)
    """
    prefix = "../" * depth

    # Replace href="something.html" with href="../something.html"
    # But not href="http...", href="#", href="tel:", href="mailto:", href="projects/..." (already relative)
    def replace_href(match):
        url = match.group(1)
        # Skip absolute URLs and special protocols
        if url.startswith(("http", "//", "#", "tel:", "mailto:")):
            return match.group(0)
        # Skip if already has ../ prefix
        if url.startswith("../"):
            return match.group(0)
        return f'href="{prefix}{url}"'

    navbar_html = re.sub(r'href="([^"]+)"', replace_href, navbar_html)

    # Replace src="assets/..." with src="../assets/..."
    def replace_src(match):
        url = match.group(1)
        if url.startswith(("http", "//", "data:")):
            return match.group(0)
        if url.startswith("../"):
            return match.group(0)
        return f'src="{prefix}{url}"'

    navbar_html = re.sub(r'src="([^"]+)"', replace_src, navbar_html)

    return navbar_html


def find_navbar_boundaries(content):
    """
    Find the start and end positions of the navbar in an HTML file.
    Returns (start_pos, end_pos) or (None, None) if not found.
    """
    # Try to find start with comment
    start_match = re.search(r"\n(\s*)(<!-- Top Bar -->)", content)

    if start_match:
        start_pos = start_match.start(2)
        indent = start_match.group(1)
    else:
        # Try without comment - look for top bar div after body
        start_match = re.search(
            r'(<body[^>]*>)\s*\n(\s*)(<div class="bg-dark-900 text-white py-2)', content
        )
        if start_match:
            start_pos = start_match.start(3)
            indent = start_match.group(2)
        else:
            return None, None, None

    # Find mobile menu and its closing tag
    mobile_start = content.find('id="mobile-menu"', start_pos)
    if mobile_start == -1:
        return None, None, None

    # Find the opening <div of mobile-menu
    div_start = content.rfind("<div", start_pos, mobile_start + 20)

    # Count nested divs to find matching close
    div_count = 1
    pos = div_start + 5

    while div_count > 0 and pos < len(content):
        next_open = content.find("<div", pos)
        next_close = content.find("</div>", pos)

        if next_close == -1:
            break

        if next_open != -1 and next_open < next_close:
            div_count += 1
            pos = next_open + 4
        else:
            div_count -= 1
            pos = next_close + 6

    end_pos = pos

    return start_pos, end_pos, indent


def replace_navbar_in_file(file_path, new_navbar, dry_run=False):
    """
    Replace the navbar in a single HTML file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"  ERROR reading file: {e}")
        return False

    # Determine if this is a subdirectory file
    rel_path = file_path.relative_to(ROOT_DIR)
    depth = len(rel_path.parts) - 1  # 0 for root, 1 for blog/, projects/

    # Adjust paths if in subdirectory
    if depth > 0:
        navbar_to_insert = adjust_paths_for_subdirectory(new_navbar, depth)
    else:
        navbar_to_insert = new_navbar

    # Find navbar boundaries
    result = find_navbar_boundaries(content)

    if result[0] is None:
        print(f"  WARNING: Could not find navbar boundaries, skipping")
        return False

    start_pos, end_pos, indent = result
    old_navbar_len = end_pos - start_pos

    # Build new content
    new_content = content[:start_pos] + navbar_to_insert + content[end_pos:]

    if dry_run:
        print(
            f"  Would replace navbar ({old_navbar_len} chars -> {len(navbar_to_insert)} chars)"
        )
        return True

    # Write the new content
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(
            f"  SUCCESS: Navbar replaced ({old_navbar_len} -> {len(navbar_to_insert)} chars)"
        )
        return True
    except Exception as e:
        print(f"  ERROR writing file: {e}")
        return False


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=" * 60)
        print("DRY RUN MODE - No files will be modified")
        print("=" * 60)

    print(f"\nReading navbar from: {INDEX_FILE}")

    # Read index.html
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index_content = f.read()
    except Exception as e:
        print(f"ERROR: Could not read index.html: {e}")
        sys.exit(1)

    # Extract navbar
    navbar_html = extract_navbar(index_content)
    if not navbar_html:
        print("ERROR: Failed to extract navbar from index.html")
        sys.exit(1)

    print(f"Extracted navbar: {len(navbar_html)} characters")
    print(f"\nNavbar preview:")
    print(f"  Starts: {navbar_html[:60]}...")
    print(f"  Ends:   ...{navbar_html[-60:]}")

    # Process each file
    print(f"\n{'=' * 60}")
    print(f"Processing {len(HTML_FILES)} files...")
    print("=" * 60)

    success_count = 0
    skip_count = 0
    error_count = 0

    for html_file in HTML_FILES:
        file_path = ROOT_DIR / html_file
        print(f"\n{html_file}:")

        if not file_path.exists():
            print(f"  SKIP: File does not exist")
            skip_count += 1
            continue

        if replace_navbar_in_file(file_path, navbar_html, dry_run):
            success_count += 1
        else:
            error_count += 1

    # Summary
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print("=" * 60)
    print(f"  Processed: {success_count}")
    print(f"  Skipped:   {skip_count}")
    print(f"  Errors:    {error_count}")

    if dry_run:
        print(f"\nRun without --dry-run to apply changes.")
    else:
        print(f"\nDone! All navbars have been synchronized.")


if __name__ == "__main__":
    main()
