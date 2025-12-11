#!/bin/bash

# Script to add UserWay Accessibility Widget to all HTML files

echo "Adding UserWay Accessibility Widget to all HTML files..."

# Find all HTML files and process them
find . -name "*.html" -type f | while read -r file; do
    # Check if UserWay is already present
    if grep -q "userway.org/widget.js" "$file"; then
        echo "SKIP (already has UserWay): $file"
        continue
    fi
    
    # Add UserWay script before </body>
    sed -i '' 's|</body>|    <!-- UserWay Accessibility Widget -->\
    <script src="https://cdn.userway.org/widget.js" data-position="5" data-account="Hs5Hy7Aqxm" defer></script>\
</body>|' "$file"
    
    echo "Added UserWay: $file"
done

echo ""
echo "Done!"
