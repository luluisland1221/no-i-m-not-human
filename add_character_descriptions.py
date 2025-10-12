#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为所有角色页面批量添加 Description 的脚本
要求: 140-160字符，包含关键词，有营销吸引力
"""

import os
import re
import glob

# 角色描述配置 - 每个角色的 SEO 优化描述
CHARACTER_DESCRIPTIONS = {
    'angry-guy': {
        'description': 'Discover Angry Guy in No, I\'m not a Human! Learn to identify this aggressive character with hostile behavior. Master visitor identification with our complete guide. Check his identification methods now!'
    },
    'neighbor': {
        'description': 'Meet the Neighbor in No, I\'m not a Human! Is this friendly character human or Visitor? Complete identification guide with physical checks and behavior analysis. Uncover the truth in our game guide!'
    },
    'fema-agent': {
        'description': 'Analyze the FEMA Agent in No, I\'m not a Human! Official authority figure with identification documents. Learn to verify government characters. Master the horror survival game with our expert guide!'
    },
    'bandana-guy': {
        'description': 'Identify Bandana Guy in No, I\'m not a Human! Street-wise character with distinctive appearance. Complete visitor identification guide with physical checks and behavior analysis. Survive the paranoia-driven horror!'
    },
    'cabby-man': {
        'description': 'Examine Cabby Man in No, I\'m not a Human! Professional driver character with knowledge of city areas. Master identification techniques for transportation workers. Download our complete survival guide now!'
    },
    'cashier-girl': {
        'description': 'Analyze Cashier Girl in No, I\'m not a Human! Young retail worker with customer service skills. Learn to identify service industry characters. Get our complete visitor identification guide for the horror survival game!'
    },
    'cat-lady': {
        'description': 'Meet Cat Lady in No, I\'m not a Human! Animal lover with distinctive behavior patterns. Complete identification guide for eccentric characters. Master the horror survival game with our expert walkthrough and strategies!'
    },
    'cheerful-man': {
        'description': 'Discover Cheerful Man in No, I\'m not a Human! Is his happiness genuine or suspicious? Complete visitor identification guide with behavior analysis. Uncover the truth in our comprehensive game guide!'
    },
    'child': {
        'description': 'Protect or deny the Child in No, I\'m not a Human! Innocent appearance or dangerous Visitor? Complete identification guide for young characters. Master moral decisions in our horror survival walkthrough!'
    },
    'coat-guy': {
        'description': 'Analyze Coat Guy in No, I\'m not a Human! Well-dressed character with formal appearance. Learn to identify business-type visitors. Get our complete identification guide and survival strategies!'
    },
    'cozy-man': {
        'description': 'Meet Cozy Man in No, I\'m not a Human! Comfortable character with relaxed demeanor. Complete visitor identification guide for calm personalities. Master the horror survival game with expert tips and strategies!'
    },
    'death': {
        'description': 'Face Death in No, I\'m not a Human! Ultimate Visitor or supernatural being? Complete identification guide for paranormal characters. Master the horror survival game with our comprehensive walkthrough!'
    },
    'death-cult-leader': {
        'description': 'Confront Death Cult Leader in No, I\'m not a Human! Dangerous religious figure with followers. Complete identification guide for cult members. Survive the apocalypse with our expert game guide and strategies!'
    },
    'death-cult-peon': {
        'description': 'Identify Death Cult Peon in No, I\'m not a Human! Religious follower with devotion to cult. Complete identification guide for cult characters. Master the horror survival game with our detailed walkthrough!'
    },
    'delivery-man': {
        'description': 'Verify Delivery Man in No, I\'m not a Human! Professional service character with access permissions. Complete identification guide for delivery workers. Master the horror survival game with our expert strategies!'
    },
    'delivery-man-backup': {
        'description': 'Analyze Backup Delivery Man in No, I\'m not a Human! Alternative delivery character with similar access. Complete identification guide for service workers. Get our comprehensive game guide and survival tips!'
    },
    'disfigured-guy': {
        'description': 'Examine Disfigured Guy in No, I\'m not a Human! Character with physical deformities - injury or Visitor trait? Complete identification guide for damaged individuals. Master the horror game now!'
    },
    'egghead-guy': {
        'description': 'Study Egghead Guy in No, I\'m not a Human! Intellectual character with distinctive head shape. Complete visitor identification guide for unique appearances. Survive the paranoia with our expert game guide!'
    },
    'factory-guy': {
        'description': 'Investigate Factory Guy in No, I\'m not a Human! Industrial worker with practical skills. Complete identification guide for labor characters. Master the horror survival game with our comprehensive walkthrough!'
    },
    'fetus': {
        'description': 'Analyze the Fetus in No, I\'m not a Human! Unborn Visitor or paranormal entity? Complete identification guide for supernatural characters. Master the horror survival game with our expert strategies and tips!'
    },
    'fortune-teller': {
        'description': 'Consult Fortune Teller in No, I\'m not a Human! Mystical character with supernatural abilities. Complete identification guide for psychic characters. Uncover the truth in our horror survival game guide!'
    },
    'gravedigger': {
        'description': 'Meet Gravedigger in No, I\'m not a Human! Cemetery worker with knowledge of death. Complete identification guide for funeral industry characters. Master the horror survival game with our expert walkthrough!'
    },
    'homeless-man': {
        'description': 'Help or deny Homeless Man in No, I\'m not a Human! Disadvantaged character or deceptive Visitor? Complete identification guide for homeless characters. Make tough decisions in our survival game guide!'
    },
    'husband-and-wife': {
        'description': 'Evaluate Husband and Wife in No, I\'m not a Human! Married couple with shared story. Complete identification guide for paired characters. Master relationship dynamics in our horror survival walkthrough!'
    },
    'immortal-man': {
        'description': 'Confront Immortal Man in No, I\'m not a Human! Undying character with supernatural powers. Complete identification guide for immortal beings. Survive the paranormal threat with our expert game guide!'
    },
    'intruder': {
        'description': 'Face Intruder in No, I\'m not a Human! Uninvited character with suspicious motives. Complete identification guide for trespassing characters. Master security in our horror survival game guide!'
    },
    'kindergarten-teacher': {
        'description': 'Trust Kindergarten Teacher in No, I\'m not a Human! Educator with child care experience. Complete identification guide for school characters. Make crucial decisions in our survival game walkthrough!'
    },
    'little-girl': {
        'description': 'Protect Little Girl in No, I\'m not a Human! Innocent child or dangerous Visitor? Complete identification guide for young characters. Face moral dilemmas in our horror survival game guide!'
    },
    'miner': {
        'description': 'Analyze Miner in No, I\'m not a Human! Underground worker with excavation knowledge. Complete identification guide for industrial characters. Master the horror survival game with our expert strategies!'
    },
    'mushroom-man': {
        'description': 'Study Mushroom Man in No, I\'m not a Human! Fungal character with unique biology. Complete identification guide for parasitic characters. Survive the infection threat with our game guide and tips!'
    },
    'music-conductor': {
        'description': 'Follow Music Conductor in No, I\'m not a Human! Artistic character with musical talents. Complete identification guide for creative characters. Master the horror survival game with our comprehensive walkthrough!'
    },
    'neglectful-mother': {
        'description': 'Evaluate Neglectful Mother in No, I\'m not a Human! Parent with concerning behavior. Complete identification guide for family characters. Face moral challenges in our horror survival game guide!'
    },
    'nikita-the-wind-based-intruder': {
        'description': 'Battle Nikita in No, I\'m not a Human! Wind-powered Visitor with supernatural speed. Complete identification guide for elemental characters. Master combat strategies in our horror survival walkthrough!'
    },
    'nun': {
        'description': 'Trust Nun in No, I\'m not a Human! Religious character with spiritual authority. Complete identification guide for faith-based characters. Make crucial decisions in our survival game guide!'
    },
    'old-lady': {
        'description': 'Help Old Lady in No, I\'m not a Human! Elderly character with frail appearance. Complete identification guide for aged characters. Master the horror survival game with our expert tips and strategies!'
    },
    'parentless-teenager': {
        'description': 'Guide Parentless Teenager in No, I\'m not a Human! Youth without family support. Complete identification guide for orphan characters. Face moral choices in our horror survival game walkthrough!'
    },
    'positive-guy': {
        'description': 'Meet Positive Guy in No, I\'m not a Human! Optimistic character with upbeat attitude. Complete identification guide for cheerful personalities. Master the horror survival game with our comprehensive guide!'
    },
    'protagonist': {
        'description': 'Play as Protagonist in No, I\'m not a Human! Main character fighting to survive. Complete guide to player abilities and survival strategies. Master the horror survival game with our expert walkthrough!'
    },
    'raincoat-child': {
        'description': 'Protect Raincoat Child in No, I\'m not a Human! Young character with protective gear. Complete identification guide for children in survival situations. Make crucial decisions in our game guide!'
    },
    'reporter': {
        'description': 'Interview Reporter in No, I\'m not a Human! Media character with investigative skills. Complete identification guide for press characters. Uncover the truth in our horror survival walkthrough!'
    },
    'seductive-woman': {
        'description': 'Resist Seductive Woman in No, I\'m not a Human! Attractive character with tempting offers. Complete identification guide for manipulative personalities. Master persuasion in our survival game guide!'
    },
    'stand-up-guy': {
        'description': 'Trust Stand Up Guy in No, I\'m not a Human! Reliable character with strong morals. Complete identification guide for trustworthy personalities. Make good decisions in our horror survival walkthrough!'
    },
    'stoner': {
        'description': 'Analyze Stoner in No, I\'m not a Human! Relaxed character with drug-influenced behavior. Complete identification guide for intoxicated characters. Master identification in our survival game guide!'
    },
    'suit-guy': {
        'description': 'Evaluate Suit Guy in No, I\'m not a Human! Business professional with formal attire. Complete identification guide for corporate characters. Master the horror survival game with our expert strategies!'
    },
    'sun-guy': {
        'description': 'Face Sun Guy in No, I\'m not a Human! Solar-powered character with light abilities. Complete identification guide for elemental beings. Survive the radiant threat in our game guide!'
    },
    'surgeon': {
        'description': 'Trust Surgeon in No, I\'m not a Human! Medical professional with surgical skills. Complete identification guide for healthcare characters. Make life-or-death decisions in our survival guide!'
    },
    'sweaty-man': {
        'description': 'Analyze Sweaty Man in No, I\'m not a Human! Nervous character with anxious behavior. Complete identification guide for stressed personalities. Master the horror survival game with our expert walkthrough!'
    },
    'theorist': {
        'description': 'Consult Theorist in No, I\'m not a Human! Intellectual character with analytical skills. Complete identification guide for smart personalities. Uncover conspiracy in our survival game guide!'
    },
    'the-sisters': {
        'description': 'Meet The Sisters in No, I\'m not a Human! Twin characters with supernatural connection. Complete identification guide for paired beings. Master the horror survival game with our expert strategies!'
    },
    'vigilante': {
        'description': 'Face Vigilante in No, I\'m not a Human! Self-appointed justice enforcer. Complete identification guide for dangerous characters. Master the horror survival game with our comprehensive walkthrough!'
    },
    'weather-reporter': {
        'description': 'Watch Weather Reporter in No, I\'m not a Human! Media character with forecasting abilities. Complete identification guide for press personalities. Stay informed in our survival game guide!'
    },
    'widowed-woman': {
        'description': 'Help Widowed Woman in No, I\'m not a Human! Grieving character with tragic backstory. Complete identification guide for mourning characters. Show compassion in our survival walkthrough!'
    },
    'wireface': {
        'description': 'Confront Wireface in No, I\'m not a Human! Technological character with cybernetic features. Complete identification guide for modified beings. Master the horror survival game with our expert guide!'
    },
    'wounded-man': {
        'description': 'Treat Wounded Man in No, I\'m not a Human! Injured character needing medical help. Complete identification guide for hurt characters. Make crucial decisions in our survival game guide!'
    },
    'best-son': {
        'description': 'Evaluate Best Son in No, I\'m not a Human! Perfect child with ideal behavior. Complete identification guide for suspiciously good characters. Master deception detection in our survival guide!'
    },
    'big-momma': {
        'description': 'Meet Big Momma in No, I\'m not a Human! Maternal figure with protective nature. Complete identification guide for caregiver characters. Make family decisions in our horror survival walkthrough!'
    },
    'blinded-man': {
        'description': 'Guide Blinded Man in No, I\'m not a Human! Vision-impaired character needing assistance. Complete identification guide for disabled characters. Show compassion in our survival game guide!'
    },
    'blonde-guy': {
        'description': 'Analyze Blonde Guy in No, I\'m not a Human! Character with distinctive hair color. Complete identification guide for appearance-based identification. Master the horror survival game with our expert tips!'
    },
    'border-patrol-agent': {
        'description': 'Verify Border Patrol Agent in No, I\'m not a Human! Authority figure with border security knowledge. Complete identification guide for government characters. Master security in our survival guide!'
    },
    'brunette-guy': {
        'description': 'Study Brunette Guy in No, I\'m not a Human! Character with brown hair features. Complete identification guide for appearance-based identification. Survive the paranoia with our expert game guide!'
    },
    'bearded-guy': {
        'description': 'Examine Bearded Guy in No, I\'m not a Human! Character with distinctive facial hair. Complete identification guide for appearance-based identification. Master the horror survival game with our comprehensive guide!'
    }
}

def count_characters(text):
    """计算字符数"""
    return len(text)

def add_description_to_file(file_path, character_name, description):
    """为单个文件添加description"""
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 查找title标签后的位置
        title_pattern = r'(<title>.*?</title>\s*)'
        title_match = re.search(title_pattern, content)

        if title_match:
            # 在title标签后插入description
            title_end = title_match.end()

            # 构建description标签
            description_tag = f'\n    <meta name="description" content="{description}">\n'

            # 检查是否已经有description
            if '<meta name="description"' in content:
                print(f"  ⚠️ {character_name} 已有description，跳过")
                return False

            # 插入description
            new_content = content[:title_end] + description_tag + content[title_end:]

            # 写入文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            print(f"  ✅ {character_name}: 已添加description ({count_characters(description)}字符)")
            return True
        else:
            print(f"  ❌ {character_name}: 未找到title标签")
            return False

    except Exception as e:
        print(f"  ❌ {character_name}: 处理出错 - {str(e)}")
        return False

def main():
    """主函数"""
    print("🔧 开始为角色页面添加Description...")
    print("要求: 140-160字符，包含关键词，有营销吸引力")
    print("=" * 70)

    # 获取角色目录
    characters_dir = os.path.join(os.getcwd(), 'guide', 'characters')

    if not os.path.exists(characters_dir):
        print(f"❌ 角色目录不存在: {characters_dir}")
        return

    # 获取所有HTML文件
    html_files = glob.glob(os.path.join(characters_dir, '*.html'))

    print(f"📁 找到 {len(html_files)} 个角色页面")
    print()

    updated_count = 0

    # 处理每个文件
    for file_path in html_files:
        # 提取角色名称
        filename = os.path.basename(file_path)
        character_name = filename.replace('.html', '')

        print(f"📄 处理 {character_name}:")

        # 获取描述配置
        if character_name in CHARACTER_DESCRIPTIONS:
            description = CHARACTER_DESCRIPTIONS[character_name]

            # 验证描述长度
            char_count = count_characters(description)
            if 140 <= char_count <= 160:
                # 添加description
                if add_description_to_file(file_path, character_name, description):
                    updated_count += 1
            else:
                print(f"  ⚠️ 描述长度不合适: {char_count}字符")
                print(f"     描述: {description}")
        else:
            print(f"  ⚠️ 未找到 {character_name} 的描述配置")

        print()

    print("=" * 70)
    print(f"✨ 完成! 共为 {updated_count} 个角色页面添加了Description")

    # 统计信息
    print(f"\n📊 统计信息:")
    print(f"  - 总角色页面: {len(html_files)}")
    print(f"  - 已更新页面: {updated_count}")
    print(f"  - 配置覆盖率: {len(CHARACTER_DESCRIPTIONS)}/{len(html_files)}")

if __name__ == "__main__":
    main()