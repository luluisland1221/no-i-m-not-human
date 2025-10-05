#!/usr/bin/env python3
"""
批量更新角色页面布局脚本
应用 bandana-guy.html 的布局到所有其他角色页面
"""

import os
import shutil
from pathlib import Path

def copy_template_to_all_characters():
    """将 bandana-guy.html 作为模板复制到其他角色文件，并更新特定内容"""

    characters_dir = Path("g:/ai编程/100个网站/07 noimnothuman.xyz/code/guide/characters")
    template_file = characters_dir / "bandana-guy.html"

    # 读取模板文件
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # 需要更新的文件列表（排除特殊文件）
    exclude_files = ["bandana-guy.html", "temp_navbar.txt"]
    character_files = [f for f in characters_dir.glob("*.html") if f.name not in exclude_files]

    print(f"开始更新 {len(character_files)} 个角色文件...")

    for i, char_file in enumerate(character_files, 1):
        try:
            print(f"[{i}/{len(character_files)}] 正在更新: {char_file.name}")

            # 读取原始文件以提取角色特定信息
            with open(char_file, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # 提取角色名称（从文件名）
            char_name = char_file.stem.replace('-', ' ').title()

            # 提取图片文件名（假设格式为 CharName.png/jpg）
            import re
            img_match = re.search(r'<img src="([^"]*)"[^>]*alt="[^"]*"[^>]*class="char-image"', original_content)
            if img_match:
                char_image = img_match.group(1)
            else:
                # 默认图片名格式
                char_image = f"https://images.noimnothuman.xyz/assets/images/characters/{char_name.replace(' ', '')}.png"

            # 更新模板中的角色特定信息
            updated_content = template_content

            # 更新页面标题
            updated_content = re.sub(
                r'<title>.*?</title>',
                f'<title>{char_name} - Character Guide | No, I\'m not a Human</title>',
                updated_content
            )

            # 更新角色名称
            updated_content = re.sub(
                r'<h1 class="character-title">[^<]*</h1>',
                f'<h1 class="character-title">{char_name}</h1>',
                updated_content
            )

            # 更新角色图片
            updated_content = re.sub(
                r'<img src="[^"]*" alt="[^"]*" class="char-image">',
                f'<img src="{char_image}" alt="{char_name}" class="char-image">',
                updated_content
            )

            # 更新结构化数据中的角色名称
            updated_content = re.sub(
                r'"name": "[^"]*"',
                f'"name": "{char_name}"',
                updated_content
            )

            # 保存更新后的文件
            with open(char_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"✓ 完成: {char_file.name}")

        except Exception as e:
            print(f"✗ 错误: {char_file.name} - {str(e)}")

    print(f"\n批量更新完成！")
    print(f"成功更新了 {len(character_files)} 个角色页面。")

if __name__ == "__main__":
    copy_template_to_all_characters()