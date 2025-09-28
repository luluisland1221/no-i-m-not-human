#!/usr/bin/env python3
"""
Simple Keyword Density Analyzer
"""

import re
import html

def extract_text_from_html(html_content):
    """Extract visible text from HTML content"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html_content)
    # Remove HTML entities
    text = html.unescape(text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def analyze_keywords(text, keywords):
    """Analyze keyword frequency and density"""
    words = text.lower().split()
    total_words = len(words)

    results = {}
    for keyword in keywords:
        count = text.lower().count(keyword.lower())
        density = (count / total_words * 100) if total_words > 0 else 0
        results[keyword] = {'count': count, 'density': density}

    return results, total_words

def read_file_content(file_path):
    """Read file content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def main():
    keywords = ['human', 'game', 'endings', 'guides', 'visitors', 'horror', 'guide', 'steam', 'characters', 'survival', 'identification']

    files = [
        r'G:\ai编程\100个网站\07 noimnothuman.xyz\code\index.html',
        r'G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide.html'
    ]

    print("Keyword Density Analysis for No, I'm not a Human Website")
    print("=" * 70)

    for file_path in files:
        print(f"\nKeyword Analysis for {file_path.split(chr(92))[-1]}:")

        content = read_file_content(file_path)
        if content:
            text = extract_text_from_html(content)
            results, total_words = analyze_keywords(text, keywords)

            print(f"Total words: {total_words}")
            print("\nKeyword    Count    Density")
            print("-" * 35)

            # Sort by count
            sorted_results = sorted(results.items(), key=lambda x: x[1]['count'], reverse=True)

            for keyword, data in sorted_results:
                print(f"{keyword:<12} {data['count']:<8} {data['density']:.2f}%")

        print("-" * 70)

if __name__ == "__main__":
    main()