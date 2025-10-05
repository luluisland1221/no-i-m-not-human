#!/usr/bin/env python3
import os
import re

# Directory containing character HTML files
characters_dir = "guide/characters"

# Read the template navigation HTML
template_nav = '''            <ul class="nav-menu">
                <li class="nav-item">
                    <a href="../../index.html" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                    <a href="../../characters.html" class="nav-link">Characters</a>
                </li>
                <li class="nav-item">
                    <a href="../../achievements.html" class="nav-link">Achievements</a>
                </li>
                <li class="nav-item">
                    <a href="../../ending.html" class="nav-link">Endings</a>
                </li>
                <li class="nav-item">
                    <a href="../../guide.html" class="nav-link">Guide</a>
                </li>
                <li class="nav-item">
                    <a href="../../download.html" class="nav-link">Download</a>
                </li>
                <li class="nav-item">
                    <a href="../../about.html" class="nav-link">About</a>
                </li>
                <li class="nav-item">
                    <a href="../../contact.html" class="nav-link">Contact</a>
                </li>
            </ul>'''

def update_character_navbar(file_path):
    """Update the navigation menu in a character HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the navigation menu section and replace it
        nav_pattern = r'<ul class="nav-menu">.*?</ul>'

        # Check if Contact link already exists
        if 'href="../../contact.html"' in content:
            print(f"✅ {os.path.basename(file_path)} already has Contact link")
            return False

        # Replace the navigation menu
        new_content = re.sub(nav_pattern, template_nav, content, flags=re.DOTALL)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated {os.path.basename(file_path)}")
            return True
        else:
            print(f"⚠️  No changes needed for {os.path.basename(file_path)}")
            return False

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Process all character HTML files"""
    print("Updating navigation bars for character pages...")

    updated_count = 0
    total_count = 0

    # Get all HTML files in the characters directory
    for filename in os.listdir(characters_dir):
        if filename.endswith('.html'):
            total_count += 1
            file_path = os.path.join(characters_dir, filename)

            if update_character_navbar(file_path):
                updated_count += 1

    print(f"\n📊 Summary:")
    print(f"   Total files: {total_count}")
    print(f"   Updated: {updated_count}")
    print(f"   Already had Contact: {total_count - updated_count}")

if __name__ == "__main__":
    main()