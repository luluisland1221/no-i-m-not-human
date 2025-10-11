#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
角色页面基本信息修正脚本
将所有角色页面的错误"Bandana Guy"信息替换为正确的角色信息
"""

import os
import re
from pathlib import Path

# 角色文件名到正确角色名称的映射
CHARACTER_MAPPING = {
    'angry-guy.html': 'Angry Guy',
    'armchair-lawyer-guy.html': 'Armchair Lawyer Guy',
    'bandana-guy.html': 'Bandana Guy',
    'bar-guy.html': 'Bar Guy',
    'bearded-guy.html': 'Bearded Guy',
    'best-son.html': 'Best Son',
    'big-momma.html': 'Big Momma',
    'blinded-man.html': 'Blinded Man',
    'blonde-guy.html': 'Blonde Guy',
    'border-patrol-agent.html': 'Border Patrol Agent',
    'brunette-guy.html': 'Brunette Guy',
    'cabby-man.html': 'Cabby Man',
    'cashier-girl.html': 'Cashier Girl',
    'cat-lady.html': 'Cat Lady',
    'cheerful-man.html': 'Cheerful Man',
    'child.html': 'Child',
    'coat-guy.html': 'Coat Guy',
    'cozy-man.html': 'Cozy Man',
    'death.html': 'Death',
    'death-cult-leader.html': 'Death Cult Leader',
    'death-cult-peon.html': 'Death Cult Peons',
    'delivery-man.html': 'Delivery Man',
    'delivery-man-backup.html': 'Delivery Man Backup',
    'disfigured-guy.html': 'Disfigured Guy',
    'egghead-guy.html': 'Egghead Guy',
    'factory-guy.html': 'Factory Guy',
    'fema-agent.html': 'FEMA Agent',
    'fetus.html': 'Fetus',
    'fortune-teller.html': 'Fortune Teller',
    'gravedigger.html': 'Gravedigger',
    'homeless-man.html': 'Homeless Man',
    'husband-and-wife.html': 'Husband and Wife',
    'immortal-man.html': 'Immortal Man',
    'intruder.html': 'Intruder',
    'kindergarten-teacher.html': 'Kindergarten Teacher',
    'little-girl.html': 'Little Girl',
    'miner.html': 'Miner',
    'mushroom-man.html': 'Mushroom Man',
    'music-conductor.html': 'Music Conductor',
    'neglectful-mother.html': 'Neglectful Mother',
    'neighbor.html': 'Neighbor',
    'nikita-the-wind-based-intruder.html': 'Nikita the Wind',
    'nun.html': 'Nun',
    'old-lady.html': 'Old Lady',
    'parentless-teenager.html': 'Parentless Teenager',
    'positive-guy.html': 'Positive Guy',
    'protagonist.html': 'Protagonist',
    'raincoat-child.html': 'Raincoat Child',
    'reporter.html': 'Reporter',
    'seductive-woman.html': 'Seductive Woman',
    'stand-up-guy.html': 'Stand Up Guy',
    'stoner.html': 'Stoner',
    'suit-guy.html': 'Suit Guy',
    'sun-guy.html': 'Sun Guy',
    'surgeon.html': 'Surgeon',
    'sweaty-man.html': 'Sweaty Man',
    'theorist.html': 'Theorist',
    'the-sisters.html': 'The Sisters',
    'vigilante.html': 'Vigilante',
    'weather-reporter.html': 'Weather Reporter',
    'widowed-woman.html': 'Widowed Woman',
    'wireface.html': 'Wireface',
    'wounded-man.html': 'Wounded Man'
}

def fix_character_page(file_path, correct_name):
    """修复单个角色页面的基本信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 修复角色名称 - 在基本信息部分
        content = re.sub(
            r'(<span class="info-label">Name:</span>\s*<span class="info-value">)(.+?)(</span>)',
            f'\\1{correct_name}\\3',
            content
        )

        # 修复页面标题中的角色名称（如果有的话）
        # 先从文件名推断标题格式
        title_name = correct_name.replace(' ', ' - ')
        # 这里我们可以选择性地更新页面标题，但为了安全起见，暂时只修复基本信息

        # 修复overview部分的角色描述
        # 将"The Bandana Guy"替换为正确的角色名称（使用冠词规则）
        if correct_name.lower().startswith(('a', 'e', 'i', 'o', 'u')):
            article = "An"
        else:
            article = "The"

        content = re.sub(
            r'The Bandana Guy is a visitor',
            f'{article} {correct_name} is a character',
            content
        )

        # 修复角色描述中的bandana相关内容
        if 'Bandana Guy' not in correct_name:  # 只有不是真正的Bandana Guy时才修复
            content = re.sub(
                r'bandana accessory gives him a distinctive look',
                f'distinctive appearance makes {correct_name} memorable',
                content
            )
            content = re.sub(
                r'His bandana could suggest various backgrounds',
                f'Their background and motivations remain mysterious',
                content
            )

        # 只有内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 修复完成: {file_path} -> {correct_name}")
            return True
        else:
            print(f"⚪ 无需修复: {file_path}")
            return False

    except Exception as e:
        print(f"❌ 修复失败: {file_path} - {str(e)}")
        return False

def main():
    """主函数：修复所有角色页面"""
    characters_dir = Path("guide/characters")

    if not characters_dir.exists():
        print(f"❌ 目录不存在: {characters_dir}")
        return

    fixed_count = 0
    total_count = 0

    print("🔧 开始修复角色页面基本信息...")

    for html_file in characters_dir.glob("*.html"):
        if html_file.name in CHARACTER_MAPPING:
            total_count += 1
            correct_name = CHARACTER_MAPPING[html_file.name]

            if fix_character_page(html_file, correct_name):
                fixed_count += 1
        else:
            print(f"⚠️  未找到映射: {html_file.name}")

    print(f"\n📊 修复完成:")
    print(f"   总文件数: {total_count}")
    print(f"   已修复: {fixed_count}")
    print(f"   无需修复: {total_count - fixed_count}")

if __name__ == "__main__":
    main()