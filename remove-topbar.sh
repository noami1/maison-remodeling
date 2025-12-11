#!/bin/bash

# Script to remove the top bar from all HTML files
# The top bar contains: "Licensed, Bonded & Insured #1097881" and "408-766-7272"

echo "Removing top bar from all HTML files..."

# Find all HTML files and process them
find . -name "*.html" -type f | while read -r file; do
    # Use sed to remove the top bar div block
    # The pattern matches the entire top bar section from <div class="bg-dark-900 to its closing </div>
    
    # Create a temp file
    temp_file=$(mktemp)
    
    # Use awk to remove the top bar block (handles multi-line)
    awk '
    BEGIN { skip = 0 }
    /<div class="bg-dark-900 text-white py-2 text-sm">/ { skip = 1 }
    skip && /<\/div>/ && !found_inner {
        # First </div> closes inner div
        found_inner = 1
        next
    }
    skip && /<\/div>/ && found_inner {
        # Second </div> closes outer div
        skip = 0
        found_inner = 0
        next
    }
    !skip { print }
    ' "$file" > "$temp_file"
    
    # Replace original with temp
    mv "$temp_file" "$file"
    
    echo "Processed: $file"
done

echo ""
echo "Done! Top bar removed from all HTML files."
