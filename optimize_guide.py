#!/usr/bin/env python3
"""
优化guide.html的Python脚本
移除重复内容并添加新的高质量内容
"""

import re
import os

def optimize_guide_html():
    """优化guide.html文件"""

    input_file = "G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide.html"
    template_file = "G:/ai编程/100个网站/07 noimnothuman.xyz/code/new_guide_template.html"
    output_file = "G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide_optimized.html"

    # 读取原始文件
    with open(input_file, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # 读取新内容模板
    with open(template_file, 'r', encoding='utf-8') as f:
        new_content = f.read()

    # 移除重复的大章节
    sections_to_remove = [
        r'<section id="characters".*?</section>',
        r'<section id="achievements".*?</section>',
        r'<section id="endings".*?</section>'
    ]

    cleaned_content = original_content
    for pattern in sections_to_remove:
        cleaned_content = re.sub(pattern, '', cleaned_content, flags=re.DOTALL)

    # 找到合适的位置插入新内容（在现有sections之后）
    # 我们将在最后一个section之前插入新内容
    last_section_pattern = r'(<section id="[^"]*"[^>]*>.*?</section>\s*)'

    # 在最后一个主要section前插入新内容
    insertion_point = cleaned_content.rfind('<section id="pro-strategies"')
    if insertion_point == -1:
        insertion_point = cleaned_content.rfind('<section id="common-mistakes"')
    if insertion_point == -1:
        insertion_point = len(cleaned_content) // 2  # 备用位置

    # 插入新内容
    optimized_content = (
        cleaned_content[:insertion_point] +
        new_content +
        cleaned_content[insertion_point:]
    )

    # 更新sidebar导航，移除重复项目，添加新项目
    sidebar_old_pattern = r'''<div class="sidebar-section">
                        <h3>No, I'm not a Human Game Information</h3>
                        <ul>
                            <li><a href="#achievements" data-tooltip="Achievements"><span class="nav-icon">🏆</span> <span class="nav-text">Achievements</span></a></li>
                            <li><a href="#characters" data-tooltip="Characters"><span class="nav-icon">👥</span> <span class="nav-text">Characters</span></a></li>
                            <li><a href="#character-scripts" data-tooltip="Character Scripts"><span class="nav-icon">📝</span> <span class="nav-text">Character Scripts</span></a></li>
                            <li><a href="#edible-items" data-tooltip="Edible Items"><span class="nav-icon">🍔</span> <span class="nav-text">Edible Items</span></a></li>
                        </ul>'''

    sidebar_new_content = '''<div class="sidebar-section">
                        <h3>Game Systems</h3>
                        <ul>
                            <li><a href="#game-mechanics-enhanced" data-tooltip="Core Mechanics"><span class="nav-icon">⚙️</span> <span class="nav-text">Core Mechanics</span></a></li>
                            <li><a href="#daily-detection-methods" data-tooltip="Daily Detection"><span class="nav-icon">🔍</span> <span class="nav-text">Daily Detection</span></a></li>
                            <li><a href="#energy-management" data-tooltip="Energy Management"><span class="nav-icon">⚡</span> <span class="nav-text">Energy Management</span></a></li>
                            <li><a href="#story-timeline" data-tooltip="Story Timeline"><span class="nav-icon">📅</span> <span class="nav-text">Story Timeline</span></a></li>
                        </ul>
                    </div>
                    <div class="sidebar-section">
                        <h3>Content Hubs</h3>
                        <ul>
                            <li><a href="./characters.html" data-tooltip="Characters"><span class="nav-icon">👥</span> <span class="nav-text">Characters →</span></a></li>
                            <li><a href="./achievements.html" data-tooltip="Achievements"><span class="nav-icon">🏆</span> <span class="nav-text">Achievements →</span></a></li>
                            <li><a href="./ending.html" data-tooltip="Endings"><span class="nav-icon">🎭</span> <span class="nav-text">Endings →</span></a></li>
                        </ul>
                    </div>
                    <div class="sidebar-section">
                        <h3>Game Mechanics</h3>
                        <ul>
                            <li><a href="#character-scripts" data-tooltip="Character Scripts"><span class="nav-icon">📝</span> <span class="nav-text">Character Scripts</span></a></li>
                            <li><a href="#edible-items" data-tooltip="Edible Items"><span class="nav-icon">🍔</span> <span class="nav-text">Edible Items</span></a></li>
                            <li><a href="#save-method" data-tooltip="Save Method"><span class="nav-icon">💾</span> <span class="nav-text">Save Method</span></a></li>
                            <li><a href="#day-night-cycle" data-tooltip="Day & Night Cycle"><span class="nav-icon">🌙</span> <span class="nav-text">Day & Night</span></a></li>
                        </ul>'''

    optimized_content = re.sub(sidebar_old_pattern, sidebar_new_content, optimized_content)

    # 更新页面标题和描述
    title_old = r'<title>No, I\'m not a Human - Complete Game Guide & Walkthrough</title>'
    title_new = '<title>No, I\'m not a Human - Game Mechanics & Advanced Strategy Guide</title>'
    optimized_content = re.sub(title_old, title_new, optimized_content)

    # 写入优化后的文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(optimized_content)

    print(f"✅ Guide optimization complete!")
    print(f"Original file: {input_file}")
    print(f"Optimized file: {output_file}")
    print(f"Template content added from: {template_file}")

    return output_file

if __name__ == "__main__":
    optimize_guide_html()