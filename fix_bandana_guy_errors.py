#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修正角色页面中的"Bandana Guy"错误
基于现有网站信息，避免编造不准确的内容
"""

import os
import re
from pathlib import Path

# 角色名称映射和对应的保守描述
CHARACTER_FIXES = {
    'bearded-guy.html': {
        'name': 'Bearded Guy',
        'overview': 'The Bearded Guy is a character who presents himself with distinctive facial hair and a cautious demeanor.',
        'background': 'The Bearded Guy appears to be an individual with notable facial hair, often suggesting experience or maturity.'
    },
    'best-son.html': {
        'name': 'Best Son',
        'overview': 'The Best Son is a character who presents himself with a dutiful and family-oriented demeanor.',
        'background': 'The Best Son appears to be an individual who values family relationships and seeks to maintain connections with loved ones.'
    },
    'big-momma.html': {
        'name': 'Big Momma',
        'overview': 'Big Momma is a character who presents herself with a maternal and protective demeanor.',
        'background': 'Big Momma appears to be an individual with caring instincts, often showing concern for others\' wellbeing.'
    },
    'blinded-man.html': {
        'name': 'Blinded Man',
        'overview': 'The Blinded Man is a character who presents himself with visual impairments and heightened other senses.',
        'background': 'The Blinded Man appears to be an individual who has experienced significant trauma affecting his vision.'
    },
    'blonde-guy.html': {
        'name': 'Blonde Guy',
        'overview': 'The Blonde Guy is a character who presents himself with distinctive blonde hair and casual appearance.',
        'background': 'The Blonde Guy appears to be an ordinary individual seeking shelter or assistance.'
    },
    'border-patrol-agent.html': {
        'name': 'Border Patrol Agent',
        'overview': 'The Border Patrol Agent is a character who presents herself with official authority and law enforcement background.',
        'background': 'The Border Patrol Agent appears to be an individual with experience in border security and customs procedures.'
    },
    'brunette-guy.html': {
        'name': 'Brunette Guy',
        'overview': 'The Brunette Guy is a character who presents himself with brown hair and a standard appearance.',
        'background': 'The Brunette Guy appears to be an ordinary individual seeking assistance or shelter.'
    },
    'cabby-man.html': {
        'name': 'Cabby Man',
        'overview': 'The Cabby Man is a character who presents himself with transportation experience and knowledge of local areas.',
        'background': 'The Cabby Man appears to be an individual who works in transportation, familiar with various locations and routes.'
    },
    'cat-lady.html': {
        'name': 'Cat Lady',
        'overview': 'The Cat Lady is a character who presents herself with a connection to felines and unique personality.',
        'background': 'The Cat Lady appears to be an individual with distinctive interests and possibly mysterious background.'
    },
    'cheerful-man.html': {
        'name': 'Cheerful Man',
        'overview': 'The Cheerful Man is a character who presents himself with an optimistic and positive attitude.',
        'background': 'The Cheerful Man appears to be an individual who maintains positivity despite difficult circumstances.'
    },
    'child.html': {
        'name': 'Child',
        'overview': 'The Child is a character who presents themselves with innocence and vulnerability.',
        'background': 'The Child appears to be a young individual seeking protection and care.'
    },
    'coat-guy.html': {
        'name': 'Coat Guy',
        'overview': 'The Coat Guy is a character who presents himself with distinctive outerwear and practical appearance.',
        'background': 'The Coat Guy appears to be an individual prepared for various weather conditions or situations.'
    },
    'cozy-man.html': {
        'name': 'Cozy Man',
        'overview': 'The Cozy Man is a character who presents himself with a comfortable and relaxed demeanor.',
        'background': 'The Cozy Man appears to be an individual seeking comfort and peaceful surroundings.'
    }
}

def fix_character_file(file_path, fixes):
    """修正单个角色文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        character_name = fixes['name']

        # 修正主要的"Bandana Guy is a visitor"描述
        old_pattern = r'<p>The Bandana Guy is a visitor who presents himself with a casual, relaxed appearance\. His bandana accessory gives him a distinctive look, and his approachable demeanor makes him seem less threatening than other characters\.</p>'
        new_content = f'<p>{fixes["overview"]}</p>'
        content = re.sub(old_pattern, new_content, content)

        # 修正背景故事中的第一个段落
        old_bg_pattern = r'<p>The Bandana Guy appears to be an ordinary person with casual attire\. His bandana could suggest various backgrounds - from outdoor work to fashion statement to practical purposes\.</p>'
        new_bg_content = f'<p>{fixes["background"]}</p>'
        content = re.sub(old_bg_pattern, new_bg_content, content)

        # 修正其他零散的"Bandana Guy"引用
        content = content.replace('The Bandana Guy', f'The {character_name}')
        content = content.replace('His bandana', f'Their distinctive features')
        content = content.replace('bandana accessory', f'distinctive appearance')
        content = content.replace('he presents', f'they present')
        content = content.replace('he appears', f'they appear')

        # 只有内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"修复文件失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    characters_dir = Path("guide/characters")

    if not characters_dir.exists():
        print("❌ 角色目录不存在")
        return

    fixed_count = 0
    total_attempted = 0

    print("🔧 开始批量修正 Bandana Guy 错误...")

    for filename, fixes in CHARACTER_FIXES.items():
        file_path = characters_dir / filename

        if file_path.exists():
            total_attempted += 1
            if fix_character_file(file_path, fixes):
                print(f"✅ 修正完成: {filename}")
                fixed_count += 1
            else:
                print(f"⚪ 无需修正: {filename}")
        else:
            print(f"❌ 文件不存在: {filename}")

    print(f"\n📊 修正结果:")
    print(f"   尝试修复: {total_attempted}")
    print(f"   成功修复: {fixed_count}")
    print(f"   无需修复: {total_attempted - fixed_count}")

if __name__ == "__main__":
    main()