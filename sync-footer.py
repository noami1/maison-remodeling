#!/usr/bin/env python3
"""
Footer Sync Script for Maison Remodeling Website

This script extracts the footer from index.html and replaces it in all other HTML files,
adjusting paths for subdirectories.

Usage:
    python sync-footer.py [--dry-run]

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
    "blog/home-remodeling-cost-guide.html",
    # Project pages (subdirectory)
    "projects/bathroom-remodeling.html",
    "projects/complete-home-remodeling.html",
    "projects/condo-remodeling.html",
    "projects/kitchen-remodeling.html",
    "projects/outdoor-remodeling.html",
]


def extract_footer(html_content):
    """
    Extract the footer section from HTML content.
    Footer is from <!-- Footer --> comment to </footer>
    """
    # Find the start - look for <!-- Footer --> comment
    start_match = re.search(r"\n(\s*)(<!-- Footer -->)", html_content)

    if start_match:
        start_pos = start_match.start(2)
    else:
        # Try finding <footer directly
        start_match = re.search(r"\n(\s*)(<footer\s)", html_content)
        if start_match:
            start_pos = start_match.start(2)
        else:
            print("ERROR: Could not find footer start in index.html")
            return None

    # Find the end - </footer>
    end_match = re.search(r"</footer>", html_content[start_pos:])
    if not end_match:
        print("ERROR: Could not find </footer> tag")
        return None

    end_pos = start_pos + end_match.end()

    # Extract footer
    footer_html = html_content[start_pos:end_pos]

    return footer_html


def adjust_paths_for_subdirectory(footer_html, depth=1):
    """
    Adjust relative paths in footer for subdirectory pages.
    depth=1 means one level deep (e.g., blog/article.html)
    """
    prefix = "../" * depth

    # Replace href="something.html" with href="../something.html"
    def replace_href(match):
        url = match.group(1)
        # Skip absolute URLs and special protocols
        if url.startswith(("http", "//", "#", "tel:", "mailto:")):
            return match.group(0)
        # Skip if already has ../ prefix
        if url.startswith("../"):
            return match.group(0)
        return f'href="{prefix}{url}"'

    footer_html = re.sub(r'href="([^"]+)"', replace_href, footer_html)

    # Replace src="assets/..." with src="../assets/..."
    def replace_src(match):
        url = match.group(1)
        if url.startswith(("http", "//", "data:")):
            return match.group(0)
        if url.startswith("../"):
            return match.group(0)
        return f'src="{prefix}{url}"'

    footer_html = re.sub(r'src="([^"]+)"', replace_src, footer_html)

    return footer_html


def find_footer_boundaries(content):
    """
    Find the start and end positions of the footer in an HTML file.
    Returns (start_pos, end_pos) or (None, None) if not found.
    """
    # Try to find start with comment
    start_match = re.search(r"\n(\s*)(<!-- Footer -->)", content)

    if start_match:
        start_pos = start_match.start(2)
    else:
        # Try finding <footer directly
        start_match = re.search(r"\n(\s*)(<footer\s)", content)
        if start_match:
            start_pos = start_match.start(2)
        else:
            return None, None

    # Find </footer>
    end_match = re.search(r"</footer>", content[start_pos:])
    if not end_match:
        return None, None

    end_pos = start_pos + end_match.end()

    return start_pos, end_pos


def replace_footer_in_file(file_path, new_footer, dry_run=False):
    """
    Replace the footer in a single HTML file.
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
        footer_to_insert = adjust_paths_for_subdirectory(new_footer, depth)
    else:
        footer_to_insert = new_footer

    # Find footer boundaries
    start_pos, end_pos = find_footer_boundaries(content)

    if start_pos is None or end_pos is None:
        print(f"  WARNING: Could not find footer boundaries, skipping")
        return False

    old_footer_len = end_pos - start_pos

    # Build new content
    new_content = content[:start_pos] + footer_to_insert + content[end_pos:]

    if dry_run:
        print(
            f"  Would replace footer ({old_footer_len} chars -> {len(footer_to_insert)} chars)"
        )
        return True

    # Write the new content
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(
            f"  SUCCESS: Footer replaced ({old_footer_len} -> {len(footer_to_insert)} chars)"
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

    print(f"\nReading footer from: {INDEX_FILE}")

    # Read index.html
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index_content = f.read()
    except Exception as e:
        print(f"ERROR: Could not read index.html: {e}")
        sys.exit(1)

    # Extract footer
    footer_html = extract_footer(index_content)
    if not footer_html:
        print("ERROR: Failed to extract footer from index.html")
        sys.exit(1)

    print(f"Extracted footer: {len(footer_html)} characters")
    print(f"\nFooter preview:")
    print(f"  Starts: {footer_html[:60]}...")
    print(f"  Ends:   ...{footer_html[-60:]}")

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

        if replace_footer_in_file(file_path, footer_html, dry_run):
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
        print(f"\nDone! All footers have been synchronized.")


if __name__ == "__main__":
    main()
