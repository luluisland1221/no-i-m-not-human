#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基于Fandom CSV数据创建准确的角色信息映射
"""

import csv
import json
from pathlib import Path

def parse_csv_data(csv_file):
    """解析CSV文件中的角色信息"""
    characters = {}

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # 提取关键信息
            wiki_title = row.get('wiki_title-0', '')
            article_title = row.get('article_title-0', '')
            title = row.get('title-0', '')
            title1 = row.get('title-1', '')
            title2 = row.get('title-2', '')

            # 确定主要角色名称
            character_name = title or title1 or title2 or wiki_title or article_title

            if not character_name or character_name in ['', '⚠️MAJOR SPOILERS⚠️']:
                continue

            # 构建角色信息
            character_info = {
                'name': character_name,
                'aliases': row.get('Aliases-0', ''),
                'species': row.get('Species-0', ''),
                'gender': row.get('Gender-0', ''),
                'status': row.get('Status-0', ''),
                'relatives': row.get('Relatives-0', ''),
                'occupation': row.get('Occupation-0', ''),
                'debut': row.get('Debut-0', ''),
                'room': row.get('Room-0', ''),
                'background': row.get('Background-0', ''),
                'personality': row.get('Personality-0', ''),
                'relationships': row.get('Relationships - The Protagonist-0', ''),
                'image': row.get('image-0-src', ''),
                'category': row.get('data-page-selector', ''),
                'url': row.get('data-page-selector-href', '')
            }

            characters[character_name.lower()] = character_info

    return characters

def create_file_mapping(characters):
    """创建文件名到角色信息的映射"""
    file_mapping = {}

    # 手动映射文件名到角色名
    name_mappings = {
        'angry-guy': 'Angry Guy',
        'armchair-lawyer-guy': 'Armchair Lawyer Guy',
        'bandana-guy': 'Bandana Guy',
        'bar-guy': 'Bar Guy',  # 可能需要确认
        'bearded-guy': 'Bearded Guy',
        'best-son': 'Best Son',
        'big-momma': 'Big Momma',  # 可能需要确认
        'blinded-man': 'Blinded Man',
        'blonde-guy': 'Blonde Guy',  # 可能需要确认
        'border-patrol-agent': 'Border Patrol Agent',
        'brunette-guy': 'Brunette Guy',  # 可能需要确认
        'cabby-man': 'Taxi Driver',
        'cashier-girl': 'Cashier',  # CSV中没有明确，基于entertainment14.net
        'cat-lady': 'Cat Lady',
        'cheerful-man': 'Cheerful Man',
        'child': 'Child',  # 可能需要确认
        'coat-guy': 'Coat Guy',  # 可能需要确认
        'cozy-man': 'Cozy Man',  # 可能需要确认
        'death': 'Death',  # 可能需要确认
        'death-cult-leader': 'Cult Leader',
        'death-cult-peon': 'Death Cult Peons',
        'delivery-man': 'Delivery Man',
        'delivery-man-backup': 'Delivery Man Backup',  # 可能需要确认
        'disfigured-guy': 'Disfigured Firefighter',
        'egghead-guy': 'Egghead Guy',  # 可能需要确认
        'factory-guy': 'Man in Hazmat',
        'fema-agent': 'Man in Hazmat',  # CSV中的前FEMA特工
        'fetus': 'Mushroom Eater',  # 可能需要确认
        'fortune-teller': 'Fortune Teller',
        'gravedigger': 'Gravedigger',
        'homeless-man': 'Homeless Man',
        'husband-and-wife': 'Husband and Wife',
        'immortal-man': 'Immortal Man',
        'intruder': 'Sleepless Intruder',
        'kindergarten-teacher': 'Kindergarten Teacher',
        'little-girl': 'Little Girl',  # 可能需要确认
        'miner': 'Miner',  # 可能需要确认
        'mushroom-man': 'Mushroom Man',  # 可能需要确认
        'music-conductor': 'Music Conductor',
        'neglectful-mother': 'Deadbeat Mom',
        'neighbor': 'Neighbor',  # CSV中可能没有，基于entertainment14.net
        'nikita-the-wind-based-intruder': 'Sleepless Intruder',
        'nun': 'Nun',
        'old-lady': 'Old Lady',  # 可能需要确认
        'parentless-teenager': 'Parentless Teenager',
        'positive-guy': 'Wheelchair Guy',
        'protagonist': 'Protagonist',  # 可能需要确认
        'raincoat-child': 'Raincoat Child',
        'reporter': 'Reporter',  # 可能需要确认
        'seductive-woman': 'Seductive Woman',
        'stand-up-guy': 'Stand Up Guy',
        'stoner': 'Stoner',
        'suit-guy': 'Suit Guy',
        'sun-guy': 'Sun Guy',  # 可能需要确认
        'surgeon': 'Surgeon',  # 可能需要确认
        'sweaty-man': 'Sweaty Man',
        'theorist': 'Conspiracy Theorist',
        'the-sisters': 'The Sisters',
        'vigilante': 'Vigilante',
        'weather-reporter': 'Weather Reporter',  # 可能需要确认
        'widowed-woman': 'Widowed Woman',  # 可能需要确认
        'wireface': 'Wireface',
        'wounded-man': 'Wounded Man'
    }

    for file_key, character_name in name_mappings.items():
        character_key = character_name.lower()
        if character_key in characters:
            file_mapping[file_key] = characters[character_key]
        else:
            # 如果找不到，创建一个基础映射
            file_mapping[file_key] = {
                'name': character_name,
                'occupation': 'Randomized',
                'debut': 'Randomized',
                'species': 'Unknown',
                'gender': 'Unknown',
                'status': 'Unknown'
            }

    return file_mapping

def main():
    csv_file = Path("no-i-am-not-a-human-fandom-com-2025-10-10.csv")

    if not csv_file.exists():
        print(f"❌ CSV文件不存在: {csv_file}")
        return

    print("📊 解析CSV数据...")
    characters = parse_csv_data(csv_file)
    print(f"✅ 解析完成，共找到 {len(characters)} 个角色")

    print("📋 创建文件映射...")
    file_mapping = create_file_mapping(characters)
    print(f"✅ 映射完成，共映射 {len(file_mapping)} 个文件")

    # 保存映射结果
    with open('character_mapping.json', 'w', encoding='utf-8') as f:
        json.dump(file_mapping, f, ensure_ascii=False, indent=2)

    print("💾 映射结果已保存到 character_mapping.json")

    # 显示一些示例映射
    print("\n📝 示例角色信息:")
    examples = ['angry-guy', 'bandana-guy', 'neighbor', 'fema-agent', 'cheerful-man']

    for key in examples:
        if key in file_mapping:
            info = file_mapping[key]
            print(f"\n🔸 {key}:")
            print(f"   姓名: {info['name']}")
            print(f"   性别: {info['gender']}")
            print(f"   职业: {info['occupation']}")
            print(f"   首次出现: {info['debut']}")
            print(f"   房间: {info['room']}")
            if info['background']:
                bg_preview = info['background'][:100] + "..." if len(info['background']) > 100 else info['background']
                print(f"   背景: {bg_preview}")

if __name__ == "__main__":
    main()