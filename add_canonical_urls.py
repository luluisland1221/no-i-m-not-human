#!/usr/bin/env python3
import os
import re

# 设置路径
characters_dir = "G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide/characters"

def add_canonical_to_file(filepath):
    """为单个HTML文件添加canonical URL"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取文件名作为URL路径
    filename = os.path.basename(filepath)
    canonical_url = f"https://noimnothuman.xyz/guide/characters/{filename}"

    # 查找description meta标签的位置
    description_pattern = r'(<meta name="description" content="[^"]+">)'
    match = re.search(description_pattern, content)

    if match:
        # 在description标签后添加canonical URL
        insertion_point = match.end()
        canonical_tag = f'\n    <link rel="canonical" href="{canonical_url}">'

        # 插入canonical标签
        new_content = content[:insertion_point] + canonical_tag + content[insertion_point:]

        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Added canonical URL to {filename}")
        return True
    else:
        print(f"❌ Could not find description tag in {filename}")
        return False

def main():
    """处理所有角色页面"""
    print("开始为角色页面添加canonical URL...")

    processed_files = 0
    success_files = 0

    # 遍历所有HTML文件
    for filename in os.listdir(characters_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(characters_dir, filename)
            processed_files += 1

            if add_canonical_to_file(filepath):
                success_files += 1

    print(f"\n📊 处理完成:")
    print(f"   总文件数: {processed_files}")
    print(f"   成功添加: {success_files}")
    print(f"   失败数量: {processed_files - success_files}")

if __name__ == "__main__":
    main()