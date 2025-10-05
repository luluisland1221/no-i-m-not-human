#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_character_layout(file_path):
    """更新单个角色页面的布局"""

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 获取角色名称（从文件名）
    character_name = Path(file_path).stem.replace('-', ' ').title()

    # 1. 更新 CSS 样式部分
    old_css_pattern = r'<style>.*?</style>'
    new_css = '''<style>
        body {
            padding-top: 80px !important;
            background: #000 !important;
        }
        .character-hero {
            margin-top: -80px !important;
            padding-top: 120px !important;
        }
        .character-container {
            background: #000 !important;
            max-width: 1400px !important;
            margin: 0 auto !important;
            padding: 2rem !important;
        }
        .character-main {
            background: #000 !important;
        }

        /* 覆盖原有的grid布局，改用table布局 */
        .character-container {
            display: block !important;
        }

        /* 确保右侧内容有合理宽度 */
        .character-section {
            max-width: none !important;
            width: 100% !important;
            background: rgba(0, 0, 0, 0.2) !important;
            border-radius: 12px !important;
            padding: 2rem !important;
            margin-bottom: 2rem !important;
            border: 1px solid rgba(0, 255, 136, 0.1) !important;
        }

        /* 确保table中的右侧td充分利用空间 */
        table {
            table-layout: fixed !important;
        }
    </style>'''

    content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

    # 2. 更新 navbar 结构
    old_navbar_pattern = r'<nav class="navbar">.*?</nav>'
    new_navbar = '''<nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h1><a href="../../index.html" style="color: #00ff88; text-decoration: none;">No, I'm not a Human</a></h1>
            </div>
            <ul class="nav-menu">
                <li class="nav-item">
                    <a href="../../index.html" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                    <a href="../../guide.html" class="nav-link">Guide</a>
                </li>
                <li class="nav-item">
                    <a href="../../characters.html" class="nav-link active">Characters</a>
                </li>
                <li class="nav-item">
                    <a href="../../achievements.html" class="nav-link">Achievements</a>
                </li>
                <li class="nav-item">
                    <a href="../../ending.html" class="nav-link">Endings</a>
                </li>
                <li class="nav-item">
                    <a href="../../download.html" class="nav-link">Download</a>
                </li>
            </ul>
            <div class="hamburger">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>'''

    content = re.sub(old_navbar_pattern, new_navbar, content, flags=re.DOTALL)

    # 3. 更新主要内容区域的布局
    old_main_pattern = r'<div class="character-container">.*?<div class="character-sidebar">(.*?)</div>.*?<div class="character-main">(.*?)</div>.*?</div>'

    # 提取左侧内容（sidebar）和右侧内容（main）
    main_match = re.search(old_main_pattern, content, re.DOTALL)
    if main_match:
        sidebar_content = main_match.group(1)
        main_content = main_match.group(2)

        # 构建新的布局结构
        new_layout = f'''<div class="character-container">
        <table style="width: 100%; max-width: 1400px; border-collapse: collapse; vertical-align: top; margin: 0 auto;">
            <tr>
                <!-- 左侧角色信息区域 -->
                <td style="width: 320px; padding-right: 2rem; vertical-align: top;">
{sidebar_content}
                </td>

                <!-- 右侧内容区域 - 明确设置宽度 -->
                <td style="width: calc(100% - 320px - 2rem); vertical-align: top; padding-left: 2rem; min-width: 800px;">
{main_content}
                </td>
            </tr>
        </table>
    </div>'''

        content = re.sub(old_main_pattern, new_layout, content, flags=re.DOTALL)

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated: {Path(file_path).name}")

def main():
    # 字符文件目录
    characters_dir = Path("g:/ai编程/100个网站/07 noimnothuman.xyz/code/guide/characters")

    # 获取所有HTML文件（排除 bandana-guy.html 和 temp_navbar.txt）
    html_files = []
    for file in characters_dir.glob("*.html"):
        if file.name not in ["bandana-guy.html"]:
            html_files.append(file)

    print(f"Found {len(html_files)} character files to update")

    # 批量更新
    for file_path in html_files:
        try:
            update_character_layout(file_path)
        except Exception as e:
            print(f"Error updating {file_path.name}: {e}")

    print("All character files have been updated!")

if __name__ == "__main__":
    main()