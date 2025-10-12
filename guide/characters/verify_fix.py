#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证angry-guy.html的Description修复
"""

import re

def extract_description(html_content):
    """从HTML内容中提取description meta标签的内容"""
    pattern = r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']'
    match = re.search(pattern, html_content, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def main():
    # 读取angry-guy.html文件
    filepath = r"G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide\characters\angry-guy.html"
    
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        description = extract_description(content)
        
        if description:
            char_count = len(description)
            print(f"文件: angry-guy.html")
            print(f"Description: {description}")
            print(f"字符数: {char_count}")
            
            if 140 <= char_count <= 160:
                print("✅ 符合SEO要求 (140-160字符)")
            else:
                print("❌ 不符合SEO要求")
                if char_count < 140:
                    print(f"   需要增加 {140 - char_count} 个字符")
                else:
                    print(f"   需要减少 {char_count - 160} 个字符")
        else:
            print("❌ 未找到Description")
            
    except Exception as e:
        print(f"读取文件时出错: {e}")

if __name__ == "__main__":
    main()