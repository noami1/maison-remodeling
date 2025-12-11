#!/bin/bash

# Script to add Font Awesome CDN to all HTML files
# Adds it right after the Lucide Icons script

echo "Adding Font Awesome CDN to all HTML files..."

# The line to search for
SEARCH='<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>'

# The lines to insert (Font Awesome CDN)
INSERT='    <!-- Font Awesome for social icons -->\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'

# Find all HTML files and process them
find . -name "*.html" -type f | while read -r file; do
    # Check if Font Awesome is already present
    if grep -q "font-awesome" "$file"; then
        echo "SKIP (already has Font Awesome): $file"
        continue
    fi
    
    # Check if Lucide line exists
    if grep -q "unpkg.com/lucide" "$file"; then
        # Use sed to add Font Awesome after Lucide
        sed -i '' "s|$SEARCH|$SEARCH\\
    \\
    <!-- Font Awesome for social icons -->\\
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css\"|" "$file"
        echo "Added Font Awesome: $file"
    else
        echo "SKIP (no Lucide found): $file"
    fi
done

echo ""
echo "Done!"
