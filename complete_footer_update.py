#!/usr/bin/env python3
"""
批量更新角色指南页面footer的Python脚本
"""

import os
import re
import glob

def update_footer(file_path):
    """更新单个HTML文件的footer结构"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 定义旧footer模式的正则表达式
        old_footer_pattern = r'<div class="footer-section">\s*<h4>Quick Links</h4>\s*<ul>\s*<li><a href="\.\.\/index\.html">Home</a></li>\s*<li><a href="\.\.\/\.\.\/guide\.html">Game Guide</a></li>\s*<li><a href="\.\.\/\.\.\/guide\.html#characters">Characters</a></li>\s*<li><a href="\.\.\/download\.html">Download</a></li>\s*</ul>\s*</div>\s*<div class="footer-section">\s*<h4>Resources</h4>\s*<ul>\s*<li><a href="\.\.\/\.\.\/guide\.html#achievements">Achievements</a></li>\s*<li><a href="\.\.\/\.\.\/guide\.html#character-scripts">Character Scripts</a></li>\s*<li><a href="\.\.\/\.\.\/guide\.html#edible-items">Edible Items</a></li>\s*<li><a href="\.\.\/community\.html">Community</a></li>\s*</ul>'

        # 定义新的footer结构
        new_footer = '''<div class="footer-section">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../characters.html">Characters</a></li>
                    <li><a href="../achievements.html">Achievements</a></li>
                    <li><a href="../ending.html">Endings</a></li>
                    <li><a href="../download.html">Download</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Game Content</h4>
                <ul>
                    <li><a href="../characters.html">Character Identification Guide</a></li>
                    <li><a href="../achievements.html">Complete Achievement List</a></li>
                    <li><a href="../ending.html">All Game Endings</a></li>
                    <li><a href="https://store.steampowered.com/app/3180070/No_Im_not_a_Human/" target="_blank">Steam Store</a></li>
                </ul>'''

        # 检查是否需要更新
        if re.search(old_footer_pattern, content, re.MULTILINE | re.DOTALL):
            # 执行替换
            new_content = re.sub(old_footer_pattern, new_footer, content, flags=re.MULTILINE | re.DOTALL)

            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True
        else:
            # 文件已经是正确的格式，不需要更新
            return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """主函数"""
    # 获取所有角色指南HTML文件
    characters_dir = "G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide/characters"
    os.chdir(characters_dir)

    # 获取所有HTML文件
    html_files = glob.glob("*.html")

    # 排除已经完成的文件
    completed_files = {'angry-guy.html', 'armchair-lawyer-guy.html', 'bandana-guy.html'}
    files_to_update = [f for f in html_files if f not in completed_files]

    print(f"开始更新 {len(files_to_update)} 个角色指南页面的footer...")

    updated_count = 0
    for i, filename in enumerate(files_to_update, 1):
        print(f"正在处理: {filename} ({i}/{len(files_to_update)})")

        if update_footer(filename):
            updated_count += 1
            print(f"✓ 已更新: {filename}")
        else:
            print(f"- 跳过: {filename} (已经是正确格式)")

    print(f"\n更新完成!")
    print(f"成功更新文件数: {updated_count}")
    print(f"总文件数: {len(files_to_update)}")

if __name__ == "__main__":
    main()