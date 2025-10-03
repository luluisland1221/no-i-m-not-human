#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple batch update character pages with table-based layout
"""

import os
import re
from pathlib import Path

def update_character_files():
    """Update all character files with table layout"""

    characters_dir = Path(r"G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide\characters")
    template_file = characters_dir / "bandana-guy.html"

    # Read template
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Files to skip
    skip_files = {"bandana-guy.html", "delivery-man.html", "angry-guy.html"}

    # Get all HTML files
    html_files = [f for f in os.listdir(characters_dir) if f.endswith('.html') and f not in skip_files]

    print(f"Updating {len(html_files)} character files...")

    for i, filename in enumerate(html_files, 1):
        try:
            print(f"[{i}/{len(html_files)}] Processing {filename}")

            file_path = characters_dir / filename

            # Read original file
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # Extract character-specific information
            # Get character name from title
            title_match = re.search(r'<title>([^<]+)</title>', original_content)
            if title_match:
                char_title = title_match.group(1)
                char_name = char_title.replace(' - Character Guide | No, I\'m not a Human', '')
            else:
                char_name = filename.replace('.html', '').replace('-', ' ').title()

            # Get character image
            img_match = re.search(r'<img src="([^"]+)" alt="[^"]*" class="char-image">', original_content)
            if img_match:
                char_image = img_match.group(1)
            else:
                # Default image name
                char_image = f"https://images.noimnothuman.xyz/assets/images/characters/{filename.replace('.html', '.png')}"

            # Get character subtitle
            subtitle_match = re.search(r'<p class="character-subtitle">"([^"]+)"</p>', original_content)
            if subtitle_match:
                char_subtitle = subtitle_match.group(1)
            else:
                char_subtitle = f"A mysterious visitor with unknown origins and intentions"

            # Get basic info items
            info_match = re.search(r'<div class="character-info">(.*?)</div>', original_content, re.DOTALL)
            if info_match:
                char_info = info_match.group(1)
            else:
                char_info = "<h3>Basic Information</h3>"

            # Get main content sections
            main_match = re.search(r'<div class="character-main">(.*?)</div>', original_content, re.DOTALL)
            if main_match:
                char_main = main_match.group(1)
            else:
                char_main = ""

            # Create new content by updating template
            new_content = template_content

            # Update title
            new_content = re.sub(r'<title>.*?</title>', f'<title>{char_name} - Character Guide | No, I\'m not a Human</title>', new_content)

            # Update structured data
            new_content = re.sub(r'"name": "[^"]*"', f'"name": "{char_name}"', new_content)

            # Update character title
            new_content = re.sub(r'<h1 class="character-title">[^<]*</h1>', f'<h1 class="character-title">{char_name}</h1>', new_content)

            # Update character subtitle
            new_content = re.sub(r'<p class="character-subtitle">"[^"]*"</p>', f'<p class="character-subtitle">"{char_subtitle}"</p>', new_content)

            # Update character image
            new_content = re.sub(r'<img src="[^"]*" alt="[^"]*" class="char-image">', f'<img src="{char_image}" alt="{char_name}" class="char-image">', new_content)

            # Update character info (preserve original)
            info_section_match = re.search(r'<!-- Character Information -->.*?<div class="character-info">(.*?)</div>', new_content, re.DOTALL)
            if info_section_match and char_info:
                new_content = re.sub(r'(<div class="character-info">)(.*?)(</div>)',
                                   f'\\1{char_info}\\3', new_content, count=1, flags=re.DOTALL)

            # Update main content sections (preserve original content structure)
            if char_main:
                # Extract individual sections from original main content
                sections = re.findall(r'<section[^>]*id="([^"]*)"[^>]*class="character-section">(.*?)</section>', char_main, re.DOTALL)

                for section_id, section_content in sections:
                    # Find corresponding section in template and update it
                    section_pattern = f'<section id="{section_id}" class="character-section">(.*?)</section>'
                    if re.search(section_pattern, new_content, re.DOTALL):
                        new_content = re.sub(section_pattern, f'<section id="{section_id}" class="character-section">{section_content}</section>', new_content, count=1, flags=re.DOTALL)

            # Write updated file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"OK: {filename}")

        except Exception as e:
            print(f"ERROR: {filename} - {str(e)}")

    print(f"Batch update completed!")

if __name__ == "__main__":
    update_character_files()