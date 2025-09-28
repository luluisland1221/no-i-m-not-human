#!/usr/bin/env python3
"""
Keyword Density Analyzer for No, I'm not a Human Website
Extracts visible text from HTML and calculates keyword density for specific keywords
"""

import re
from bs4 import BeautifulSoup
from collections import Counter

def extract_visible_text(html_content):
    """Extract visible text content from HTML, excluding scripts, styles, and tags"""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style", "meta", "link", "noscript"]):
        script.decompose()

    # Get text and normalize whitespace
    text = soup.get_text()
    # Replace multiple whitespace with single space and strip
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def calculate_keyword_density(text, keywords):
    """Calculate keyword density for specified keywords"""
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()

    # Split into words (simple split by spaces)
    words = text_lower.split()
    total_words = len(words)

    # Count keyword occurrences
    keyword_counts = {}
    for keyword in keywords:
        keyword_counts[keyword] = text_lower.count(keyword.lower())

    # Calculate density (percentage)
    keyword_density = {}
    for keyword, count in keyword_counts.items():
        density = (count / total_words * 100) if total_words > 0 else 0
        keyword_density[keyword] = density

    return keyword_counts, keyword_density, total_words

def analyze_file(file_path, keywords):
    """Analyze a single HTML file for keyword density"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        visible_text = extract_visible_text(html_content)
        keyword_counts, keyword_density, total_words = calculate_keyword_density(visible_text, keywords)

        return {
            'file_path': file_path,
            'visible_text': visible_text,
            'keyword_counts': keyword_counts,
            'keyword_density': keyword_density,
            'total_words': total_words
        }
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

def main():
    # Keywords to analyze
    keywords = ['human', 'game', 'endings', 'guides', 'visitors', 'horror', 'guide', 'steam', 'characters', 'survival', 'identification']

    # Files to analyze
    files = [
        r'G:\ai编程\100个网站\07 noimnothuman.xyz\code\index.html',
        r'G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide.html'
    ]

    print("Keyword Density Analysis for No, I'm not a Human Website")
    print("=" * 60)

    for file_path in files:
        print(f"\nAnalyzing: {file_path}")
        result = analyze_file(file_path, keywords)

        if result:
            print(f"Total words: {result['total_words']}")
            print("\nKeyword    Count    Density")
            print("-" * 30)

            # Sort by count (descending)
            sorted_keywords = sorted(result['keyword_counts'].items(), key=lambda x: x[1], reverse=True)

            for keyword, count in sorted_keywords:
                density = result['keyword_density'][keyword]
                print(f"{keyword:<12} {count:<8} {density:.2f}%")

        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()