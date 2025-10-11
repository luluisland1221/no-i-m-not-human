#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证角色图片与角色名称的匹配准确性
基于CSV数据和HTML文件对比图片URL
"""

import csv
import re
from pathlib import Path
import urllib.parse

def extract_image_from_html(html_file):
    """从HTML文件中提取角色图片URL"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找角色图片
        img_pattern = r'<img[^>]*src="([^"]*characters/[^"]*)"[^>]*alt="([^"]*)"'
        matches = re.findall(img_pattern, content, re.IGNORECASE)

        if matches:
            img_url, alt_text = matches[0]
            return img_url, alt_text
        return None, None
    except Exception as e:
        print(f"读取HTML文件失败 {html_file}: {e}")
        return None, None

def extract_csv_images(csv_file):
    """从CSV文件中提取角色图片URL"""
    csv_images = {}

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                title = row.get('title-0', '') or row.get('title-1', '') or row.get('title-2', '')
                image_url = row.get('image-0-src', '')

                if title and image_url:
                    csv_images[title.lower()] = image_url

    except Exception as e:
        print(f"读取CSV文件失败 {csv_file}: {e}")

    return csv_images

def verify_image_matches():
    """验证图片匹配"""
    characters_dir = Path("guide/characters")
    csv_file = Path("no-i-am-not-a-human-fandom-com-2025-10-10.csv")

    if not characters_dir.exists():
        print(f"❌ 角色目录不存在: {characters_dir}")
        return

    if not csv_file.exists():
        print(f"❌ CSV文件不存在: {csv_file}")
        return

    # 提取CSV中的图片
    print("📊 提取CSV图片数据...")
    csv_images = extract_csv_images(csv_file)
    print(f"✅ CSV中找到 {len(csv_images)} 个角色图片")

    # 角色名称映射
    name_mapping = {
        'angry-guy': 'Angry Guy',
        'bandana-guy': 'Bandana Guy',
        'cheerful-man': 'Cheerful Man',
        'immortal-man': 'Immortal Man',
        'border-patrol-agent': 'Border Patrol Agent',
        'the-sisters': 'The Sisters',
        'vigilante': 'Vigilante',
        'kindergarten-teacher': 'Kindergarten Teacher',
        'nun': 'Nun',
        'homeless-man': 'Homeless Man',
        'gravedigger': 'Gravedigger',
        'wounded-man': 'Wounded Man',
        'fortune-teller': 'Fortune Teller',
        'wireface': 'Wireface',
        'stoner': 'Stoner',
        'death-cult-leader': 'Cult Leader',
        'husband-and-wife': 'Husband and Wife',
        'stand-up-guy': 'Stand Up Guy',
        'blinded-man': 'Blinded Man',
        'parentless-teenager': 'Parentless Teenager',
        'cat-lady': 'Cat Lady',
        'best-son': 'Best Son',
        'seductive-woman': 'Seductive Woman',
        'suit-guy': 'Suit Guy',
        'delivery-man': 'Delivery Man'
    }

    print("\n🔍 验证图片匹配...")
    results = []

    for html_file in characters_dir.glob("*.html"):
        file_key = html_file.stem

        if file_key not in name_mapping:
            continue

        character_name = name_mapping[file_key]

        # 从HTML提取图片
        html_img_url, html_alt = extract_image_from_html(html_file)

        # 检查CSV中对应的图片
        csv_img_url = csv_images.get(character_name.lower(), '')

        result = {
            'file': file_key,
            'character_name': character_name,
            'html_url': html_img_url,
            'html_alt': html_alt,
            'csv_url': csv_img_url,
            'match': False,
            'issues': []
        }

        # 验证匹配性
        if html_img_url:
            # 检查文件名是否包含角色名称关键词
            html_filename = urllib.parse.unquote(html_img_url.split('/')[-1]).lower()
            character_keywords = character_name.lower().replace(' ', '').replace('-', '')

            # 简单的名称匹配检查
            if any(keyword in html_filename for keyword in character_keywords.split() if len(keyword) > 2):
                result['match'] = True
            else:
                result['issues'].append(f"文件名不匹配: {html_filename}")

        if csv_img_url and html_img_url:
            if csv_img_url.split('/')[-1] == html_img_url.split('/')[-1]:
                result['match'] = True
            else:
                result['issues'].append("CSV和HTML图片文件名不一致")

        if not html_img_url:
            result['issues'].append("HTML中未找到图片")

        if not csv_img_url:
            result['issues'].append("CSV中未找到对应角色")

        results.append(result)

    # 输出结果
    print(f"\n📋 图片验证结果 (共检查 {len(results)} 个角色):")

    matched = 0
    issues_found = 0

    for result in results:
        status = "✅" if result['match'] else "❌"

        print(f"\n{status} {result['file']} -> {result['character_name']}")
        print(f"   HTML: {result['html_url'] or '未找到'}")
        print(f"   CSV:  {result['csv_url'] or '未找到'}")

        if result['issues']:
            issues_found += 1
            for issue in result['issues']:
                print(f"   ⚠️  {issue}")
        else:
            matched += 1

    print(f"\n📊 总结:")
    print(f"   匹配成功: {matched}")
    print(f"   发现问题: {issues_found}")
    print(f"   总检查数: {len(results)}")

    # 输出需要修复的角色
    if issues_found > 0:
        print(f"\n🔧 需要修复的角色:")
        for result in results:
            if result['issues']:
                print(f"   - {result['file']}: {', '.join(result['issues'])}")

if __name__ == "__main__":
    verify_image_matches()