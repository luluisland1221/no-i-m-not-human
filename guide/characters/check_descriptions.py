#!/usr/bin/env python3
import os
import re

def check_descriptions():
    directory = "g:\\ai编程\\100个网站\\07 noimnothuman.xyz\\code\\guide\\characters"
    files_to_check = []

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract description
                desc_match = re.search(r'name="description" content="([^"]+)"', content)
                if desc_match:
                    description = desc_match.group(1)
                    char_count = len(description)

                    if char_count < 140 or char_count > 160:
                        files_to_check.append({
                            'filename': filename,
                            'description': description,
                            'char_count': char_count
                        })
                        print(f"{filename}: {char_count} characters - NEEDS OPTIMIZATION")
                        print(f"  Description: {description}")
                    else:
                        print(f"{filename}: {char_count} characters - OK")

            except Exception as e:
                print(f"Error reading {filename}: {e}")

    print(f"\nTotal files needing optimization: {len(files_to_check)}")
    return files_to_check

if __name__ == "__main__":
    check_descriptions()