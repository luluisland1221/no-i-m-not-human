#!/usr/bin/env python3
"""
批量添加相关角色链接模块到所有角色页面
"""

import json
import os
import re
from pathlib import Path

def load_character_relations():
    """加载角色关联配置"""
    with open('character_relations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_related_characters_html(character_file, relations_data, labels):
    """生成相关角色HTML"""
    if character_file not in relations_data['character_relations']:
        return ""

    character_relations = relations_data['character_relations'][character_file]
    html_parts = []

    html_parts.append('            <!-- Related Characters Section -->')
    html_parts.append('            <section id="related-characters" class="character-section">')
    html_parts.append('                <h2>Related Characters</h2>')
    html_parts.append('                <div class="related-characters-container">')

    # 为每个关联类型生成HTML
    for relation_type, related_chars in character_relations.items():
        if not related_chars:  # 跳过空列表
            continue

        label = labels.get(relation_type, relation_type.replace('_', ' ').title())
        html_parts.append(f'                    <div class="relation-group">')
        html_parts.append(f'                        <h4>{label}</h4>')
        html_parts.append(f'                        <div class="related-characters-grid">')

        for char_file in related_chars:
            # 从文件名获取角色显示名称
            char_name = char_file.replace('.html', '').replace('-', ' ').title()
            html_parts.append(f'                            <a href="{char_file}" class="related-character-link">')
            html_parts.append(f'                                <span class="character-name">{char_name}</span>')
            html_parts.append(f'                                <span class="relation-desc">View character details</span>')
            html_parts.append(f'                            </a>')

        html_parts.append(f'                        </div>')
        html_parts.append(f'                    </div>')

    html_parts.append('                </div>')
    html_parts.append('            </section>')
    html_parts.append('')

    return '\n'.join(html_parts)

def add_related_characters_to_page(character_file, relations_data, labels):
    """为单个角色页面添加相关角色模块"""
    file_path = f"guide/characters/{character_file}"

    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已经有相关角色模块
    if '<!-- Related Characters Section -->' in content:
        print(f"已包含相关角色模块: {character_file}")
        return True

    # 生成相关角色HTML
    related_html = generate_related_characters_html(character_file, relations_data, labels)

    if not related_html:
        print(f"没有关联数据: {character_file}")
        return False

    # 找到插入位置（在 Back to Guide Link 之前）
    insert_pattern = r'(\s*</section>\s*\n\s*<!-- Back to Guide Link -->)'

    if re.search(insert_pattern, content):
        new_content = re.sub(
            insert_pattern,
            f'\n{related_html}\n\\1',
            content
        )

        # 检查是否需要添加CSS样式
        if 'related-characters-container' not in content:
            # 在现有CSS中添加相关角色样式
            css_pattern = r'(\s*/\* 确保table中的右侧td充分利用空间 \*/\s*table\s*\{[^}]*\})'

            css_styles = '''

        /* Related Characters Section Styles */
        .related-characters-container {
            margin-top: 1.5rem;
        }

        .relation-group {
            margin-bottom: 2rem;
        }

        .relation-group h4 {
            color: #00ff88;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }

        .related-characters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
        }

        .related-character-link {
            display: block;
            padding: 1rem;
            background: rgba(0, 255, 136, 0.05);
            border: 1px solid rgba(0, 255, 136, 0.2);
            border-radius: 8px;
            text-decoration: none;
            color: #ffffff;
            transition: all 0.3s ease;
        }

        .related-character-link:hover {
            background: rgba(0, 255, 136, 0.1);
            border-color: rgba(0, 255, 136, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 255, 136, 0.2);
        }

        .character-name {
            display: block;
            font-weight: 600;
            font-size: 1rem;
            color: #00ff88;
            margin-bottom: 0.5rem;
        }

        .relation-desc {
            display: block;
            font-size: 0.9rem;
            color: #cccccc;
            line-height: 1.4;
        }'''

            new_content = re.sub(css_pattern, f'\\1{css_styles}', new_content)

        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ 已添加相关角色模块: {character_file}")
        return True
    else:
        print(f"❌ 找不到插入位置: {character_file}")
        return False

def main():
    """主函数"""
    # 加载配置
    relations_data = load_character_relations()
    labels = relations_data['relation_labels']

    # 获取所有角色文件
    character_dir = Path("guide/characters")
    character_files = []

    for file_path in character_dir.glob("*.html"):
        if file_path.name != "index.html":
            character_files.append(file_path.name)

    print(f"找到 {len(character_files)} 个角色页面")

    # 处理每个角色页面
    success_count = 0
    for character_file in sorted(character_files):
        if add_related_characters_to_page(character_file, relations_data, labels):
            success_count += 1

    print(f"\n处理完成！")
    print(f"成功: {success_count}/{len(character_files)} 个页面")

if __name__ == "__main__":
    main()