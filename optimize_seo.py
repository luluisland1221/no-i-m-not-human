#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO标签优化脚本 - 优化所有页面的Title和Description
要求: Title 50-60字符，Description 140-160字符，包含关键词，有营销吸引力
"""

import os
import re

# 定义SEO优化配置
SEO_CONFIG = {
    'index.html': {
        'title': 'No, I\'m not a Human | Horror Survival Game Guide',
        'description': 'Master No, I\'m not a Human horror survival game! Complete visitor identification guide, all endings walkthrough. Download now for the ultimate experience!'
    },
    'characters.html': {
        'title': '62 Characters Guide | No, I\'m not a Human Identification',
        'description': 'Complete 62 characters guide for visitor identification! Detailed analysis, visual guides to distinguish humans from Visitors. Master the horror survival game!'
    },
    'achievements.html': {
        'title': 'All Achievements Guide | No, I\'m not a Human',
        'description': 'Unlock all achievements in No, I\'m not a Human! Complete achievement guide with strategies, tips, and walkthrough. Master the horror survival game now!'
    },
    'ending.html': {
        'title': 'All Endings Guide | No, I\'m not a Human Walkthrough',
        'description': 'Discover all 10 endings in No, I\'m not a Human! Complete walkthrough, strategies, and decision guide for every possible game ending. Start your journey!'
    },
    'guide.html': {
        'title': 'Complete Walkthrough | No, I\'m not a Human Strategy Guide',
        'description': 'Master No, I\'m not a Human with our complete walkthrough! 15-day strategy guide, survival tips, visitor identification. Download and survive the apocalypse!'
    },
    'download.html': {
        'title': 'Download No, I\'m not a Human | Steam Horror Game $14.99',
        'description': 'Download No, I\'m not a Human on Steam for $14.99! Ultimate horror survival game with visitor identification. Get your copy and survive the apocalypse now!'
    },
    'about.html': {
        'title': 'About No, I\'m not a Human | Horror Survival Game',
        'description': 'Learn about No, I\'m not a Human horror survival game! Story, gameplay mechanics, features, and developer info. Discover the ultimate paranoia-driven experience!'
    },
    'contact.html': {
        'title': 'Contact Us | No, I\'m not a Human Game Support',
        'description': 'Get in touch with No, I\'m not a Human game community! Share strategies, ask questions, join discussions. Connect with fellow horror survival game players!'
    }
}

def count_characters(text):
    """计算字符数（包含空格和标点）"""
    return len(text)

def optimize_html_file(file_path, seo_config):
    """优化单个HTML文件的SEO标签"""
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 备份原始内容
        original_content = content

        # 获取文件名
        filename = os.path.basename(file_path)

        if filename not in seo_config:
            print(f"跳过 {filename} (未在配置中)")
            return False

        config = seo_config[filename]

        # 更新title标签
        title_pattern = r'<title>(.*?)</title>'
        title_match = re.search(title_pattern, content)
        if title_match:
            old_title = title_match.group(1)
            new_title = config['title']
            content = content.replace(old_title, new_title)
            print(f"  标题: {old_title} ({count_characters(old_title)}字符) -> {new_title} ({count_characters(new_title)}字符)")

        # 更新description标签
        desc_pattern = r'<meta name="description" content="(.*?)">'
        desc_match = re.search(desc_pattern, content)
        if desc_match:
            old_desc = desc_match.group(1)
            new_desc = config['description']
            content = content.replace(old_desc, new_desc)
            print(f"  描述: {count_characters(old_desc)}字符 -> {count_characters(new_desc)}字符")

        # 更新Open Graph标题
        og_title_pattern = r'<meta property="og:title" content="(.*?)">'
        og_title_match = re.search(og_title_pattern, content)
        if og_title_match:
            old_og_title = og_title_match.group(1)
            new_og_title = config['title']
            content = content.replace(old_og_title, new_og_title)

        # 更新Open Graph描述
        og_desc_pattern = r'<meta property="og:description" content="(.*?)">'
        og_desc_match = re.search(og_desc_pattern, content)
        if og_desc_match:
            old_og_desc = og_desc_match.group(1)
            new_og_desc = config['description']
            content = content.replace(old_og_desc, new_og_desc)

        # 更新Twitter标题
        twitter_title_pattern = r'<meta name="twitter:title" content="(.*?)">'
        twitter_title_match = re.search(twitter_title_pattern, content)
        if twitter_title_match:
            old_twitter_title = twitter_title_match.group(1)
            new_twitter_title = config['title']
            content = content.replace(old_twitter_title, new_twitter_title)

        # 更新Twitter描述
        twitter_desc_pattern = r'<meta name="twitter:description" content="(.*?)">'
        twitter_desc_match = re.search(twitter_desc_pattern, content)
        if twitter_desc_match:
            old_twitter_desc = twitter_desc_match.group(1)
            new_twitter_desc = config['description']
            content = content.replace(old_twitter_desc, new_twitter_desc)

        # 如果内容有变化，写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"✅ 已优化 {filename}")
            return True
        else:
            print(f"⚪ {filename} 无需更改")
            return False

    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错: {str(e)}")
        return False

def main():
    """主函数"""
    print("🔧 开始优化SEO标签...")
    print("要求: Title 50-60字符，Description 140-160字符")
    print("=" * 60)

    # 获取当前目录
    current_dir = os.getcwd()
    optimized_count = 0

    # 处理每个配置的文件
    for filename in SEO_CONFIG.keys():
        file_path = os.path.join(current_dir, filename)

        if os.path.exists(file_path):
            print(f"\n📄 处理 {filename}:")
            if optimize_html_file(file_path, SEO_CONFIG):
                optimized_count += 1
        else:
            print(f"❌ 文件不存在: {file_path}")

    print("\n" + "=" * 60)
    print(f"✨ 优化完成! 共优化了 {optimized_count} 个文件")

    # 验证字符数
    print("\n📊 字符数验证:")
    for filename, config in SEO_CONFIG.items():
        title_len = count_characters(config['title'])
        desc_len = count_characters(config['description'])
        status_title = "✅" if 50 <= title_len <= 60 else "❌"
        status_desc = "✅" if 140 <= desc_len <= 160 else "❌"
        print(f"  {filename}: Title {title_len}字符 {status_title}, Description {desc_len}字符 {status_desc}")

if __name__ == "__main__":
    main()