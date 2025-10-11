#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
阶段1：紧急名称修正
将所有"Bandana Guy"替换为正确的角色名称
基于现有文件名映射，避免编造信息
"""

import os
import re
from pathlib import Path

def get_character_name_from_file(filename):
    """从文件名推断角色名称"""
    # 移除.html扩展名
    base_name = filename.replace('.html', '')

    # 将连字符转换为空格并标题化
    name_parts = base_name.split('-')
    name = ' '.join(part.capitalize() for part in name_parts)

    # 特殊处理一些常见的命名模式
    name_mapping = {
        'Angry Guy': 'Angry Guy',
        'Armchair Lawyer Guy': 'Armchair Lawyer Guy',
        'Bandana Guy': 'Bandana Guy',
        'Bar Guy': 'Bar Guy',
        'Bearded Guy': 'Bearded Guy',
        'Best Son': 'Best Son',
        'Big Momma': 'Big Momma',
        'Blinded Man': 'Blinded Man',
        'Blonde Guy': 'Blonde Guy',
        'Border Patrol Agent': 'Border Patrol Agent',
        'Brunette Guy': 'Brunette Guy',
        'Cabby Man': 'Cabby Man',
        'Cashier Girl': 'Cashier Girl',
        'Cat Lady': 'Cat Lady',
        'Cheerful Man': 'Cheerful Man',
        'Child': 'Child',
        'Coat Guy': 'Coat Guy',
        'Cozy Man': 'Cozy Man',
        'Death': 'Death',
        'Death Cult Leader': 'Death Cult Leader',
        'Death Cult Peon': 'Death Cult Peon',
        'Delivery Man': 'Delivery Man',
        'Delivery Man Backup': 'Delivery Man Backup',
        'Disfigured Guy': 'Disfigured Guy',
        'Egghead Guy': 'Egghead Guy',
        'Factory Guy': 'Factory Guy',
        'Fema Agent': 'FEMA Agent',
        'Fetus': 'Fetus',
        'Fortune Teller': 'Fortune Teller',
        'Gravedigger': 'Gravedigger',
        'Homeless Man': 'Homeless Man',
        'Husband And Wife': 'Husband and Wife',
        'Immortal Man': 'Immortal Man',
        'Intruder': 'Intruder',
        'Kindergarten Teacher': 'Kindergarten Teacher',
        'Little Girl': 'Little Girl',
        'Miner': 'Miner',
        'Mushroom Man': 'Mushroom Man',
        'Music Conductor': 'Music Conductor',
        'Neglectful Mother': 'Neglectful Mother',
        'Neighbor': 'Neighbor',
        'Nikita The Wind Based Intruder': 'Nikita the Wind',
        'Nun': 'Nun',
        'Old Lady': 'Old Lady',
        'Parentless Teenager': 'Parentless Teenager',
        'Positive Guy': 'Positive Guy',
        'Protagonist': 'Protagonist',
        'Raincoat Child': 'Raincoat Child',
        'Reporter': 'Reporter',
        'Seductive Woman': 'Seductive Woman',
        'Stand Up Guy': 'Stand Up Guy',
        'Stoner': 'Stoner',
        'Suit Guy': 'Suit Guy',
        'Sun Guy': 'Sun Guy',
        'Surgeon': 'Surgeon',
        'Sweaty Man': 'Sweaty Man',
        'Theorist': 'Theorist',
        'The Sisters': 'The Sisters',
        'Vigilante': 'Vigilante',
        'Weather Reporter': 'Weather Reporter',
        'Widowed Woman': 'Widowed Woman',
        'Wireface': 'Wireface',
        'Wounded Man': 'Wounded Man'
    }

    return name_mapping.get(name, name)

def fix_character_file(file_path):
    """修正单个角色文件中的Bandana Guy错误"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        filename = file_path.name
        character_name = get_character_name_from_file(filename)

        # 统计替换次数
        replacement_count = 0

        # 修正主要描述模式
        patterns_to_fix = [
            (r'The Bandana Guy is a visitor', f'The {character_name} is a character'),
            (r'The Bandana Guy presents himself', f'The {character_name} presents'),
            (r'The Bandana Guy appears', f'The {character_name} appears'),
            (r'His bandana accessory', 'Their distinctive features'),
            (r'His bandana', 'Their appearance'),
            (r'he presents himself', 'they present'),
            (r'he appears', 'they appear'),
            (r'his casual', 'their approach'),
            (r'his relaxed', 'their demeanor'),
            (r'his distinctive', 'their unique'),
            (r'his approachable', 'their manner'),
            (r'the Bandana Guy', f'the {character_name}'),
            (r'"Bandana Guy"', f'"{character_name}"'),
            (r'Bandana Guy\'s', f'{character_name}\'s'),
            (r'with Bandana Guy', f'with {character_name}'),
            (r'for Bandana Guy', f'for {character_name}')
        ]

        for pattern, replacement in patterns_to_fix:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                replacement_count += len(matches)
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

        # 只有内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, replacement_count
        return False, 0

    except Exception as e:
        print(f"修复文件失败 {file_path}: {e}")
        return False, 0

def main():
    """主函数：执行阶段1紧急修正"""
    characters_dir = Path("guide/characters")

    if not characters_dir.exists():
        print("❌ 角色目录不存在")
        return

    print("🚨 阶段1：紧急名称修正开始...")
    print("📂 处理目录:", characters_dir)

    fixed_count = 0
    total_replacements = 0
    processed_files = 0

    # 获取所有HTML文件
    html_files = list(characters_dir.glob("*.html"))
    print(f"📊 找到 {len(html_files)} 个HTML文件")

    for html_file in html_files:
        processed_files += 1
        fixed, replacements = fix_character_file(html_file)

        if fixed:
            fixed_count += 1
            total_replacements += replacements
            character_name = get_character_name_from_file(html_file.name)
            print(f"✅ 修正完成: {html_file.name} -> {character_name} ({replacements}处替换)")

    print(f"\n📊 阶段1修正结果:")
    print(f"   处理文件数: {processed_files}")
    print(f"   成功修正: {fixed_count}")
    print(f"   总替换次数: {total_replacements}")

    if fixed_count > 0:
        print(f"\n🎯 阶段1完成！已修正{fixed_count}个文件的Bandana Guy错误。")
        print(f"🔄 准备进入阶段2：基本信息完善")
    else:
        print(f"\n✅ 未发现需要修正的Bandana Guy错误。")

if __name__ == "__main__":
    main()