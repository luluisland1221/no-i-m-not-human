#!/usr/bin/env python3
"""
下载No, I'm not a Human游戏结局图片的脚本
"""

import requests
import os
from pathlib import Path
import time
import urllib.parse

def create_ending_images_info():
    """创建结局图片信息文件"""
    # 结局成就图片描述（基于Fandom wiki信息）
    ending_images = [
        {
            "ending_number": 1,
            "name": "The Child of Doom",
            "achievement": "Child of Doom",
            "description": "Winged creature rising from fog",
            "filename": "ending_1_child_of_doom.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/8/8e/Ending_1.png"
        },
        {
            "ending_number": 2,
            "name": "The End?",
            "achievement": "The End?",
            "description": "Dark basement with bricked windows",
            "filename": "ending_2_the_end.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/5/5a/Ending_2.png"
        },
        {
            "ending_number": 3,
            "name": "No, I'm Not Alone",
            "achievement": "No, I'm Not Alone",
            "description": "Dark figure in shadow",
            "filename": "ending_3_not_alone.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/c/c5/Ending_3.png"
        },
        {
            "ending_number": 4,
            "name": "May Death Cleanse us of Our Sins!",
            "achievement": "Death Cult",
            "description": "Cult leader figure",
            "filename": "ending_4_death_cult.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/4/4d/Ending_4.png"
        },
        {
            "ending_number": 5,
            "name": "Welcome to FEMA",
            "achievement": "FEMA Agent",
            "description": "FEMA agent figure",
            "filename": "ending_5_fema.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/6/6c/Ending_5.png"
        },
        {
            "ending_number": 6,
            "name": "Yes, I'm Alone",
            "achievement": "Intruder",
            "description": "Intruder breaking down door",
            "filename": "ending_6_intruder.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/1/1e/Ending_6.png"
        },
        {
            "ending_number": 7,
            "name": "Yes, I'm a Murderer",
            "achievement": "Murderer",
            "description": "Gun pointing figure",
            "filename": "ending_7_murderer.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/2/2d/Ending_7.png"
        },
        {
            "ending_number": 8,
            "name": "Shroom or Doom",
            "achievement": "Mushroom",
            "description": "Mushroom figure",
            "filename": "ending_8_mushroom.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/3/39/Ending_8.png"
        },
        {
            "ending_number": 9,
            "name": "Embrace The Inevitable",
            "achievement": "Underground",
            "description": "Underground tunnel figure",
            "filename": "ending_9_underground.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/9/95/Ending_9.png"
        },
        {
            "ending_number": 10,
            "name": "Wrath of the Vigilante",
            "achievement": "Vigilante",
            "description": "Vigilante with gun",
            "filename": "ending_10_vigilante.png",
            "url_template": "https://static.wikia.nocookie.net/no-i-am-not-a-human/images/7/7e/Ending_10.png"
        }
    ]

    return ending_images

def download_image(url, filename, save_dir):
    """下载单个图片"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        file_path = save_dir / filename
        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"✅ 下载成功: {filename}")
        return True

    except Exception as e:
        print(f"❌ 下载失败 {filename}: {e}")
        return False

def create_placeholder_images_info():
    """创建占位符图片信息"""
    placeholders = []

    for i in range(1, 11):
        placeholders.append({
            "ending_number": i,
            "filename": f"ending_{i}_placeholder.png",
            "description": f"Ending {i} Achievement Placeholder",
            "note": "需要手动下载或截图"
        })

    return placeholders

def main():
    """主函数"""
    current_dir = Path(__file__).parent
    images_dir = current_dir / "ending_images"

    # 创建图片目录
    images_dir.mkdir(exist_ok=True)

    print("🎮 No, I'm not a Human - 结局图片下载工具")
    print("=" * 50)

    # 获取结局图片信息
    ending_images = create_ending_images_info()

    print(f"📋 准备下载 {len(ending_images)} 个结局图片...")

    success_count = 0
    total_count = len(ending_images)

    for ending in ending_images:
        print(f"\n🎯 结局 {ending['ending_number']}: {ending['name']}")
        print(f"📸 成就: {ending['achievement']}")
        print(f"📝 描述: {ending['description']}")

        # 尝试下载
        success = download_image(ending['url_template'], ending['filename'], images_dir)

        if success:
            success_count += 1

        # 避免请求过快
        time.sleep(1)

    print(f"\n📊 下载完成: {success_count}/{total_count}")

    # 创建占位符信息
    if success_count < total_count:
        print("\n⚠️  部分图片下载失败，创建占位符信息...")
        placeholders = create_placeholder_images_info()

        # 保存占位符信息到文件
        placeholder_file = images_dir / "placeholder_info.txt"
        with open(placeholder_file, 'w', encoding='utf-8') as f:
            f.write("No, I'm not a Human - 结局图片占位符信息\n")
            f.write("=" * 50 + "\n\n")

            for placeholder in placeholders:
                f.write(f"结局 {placeholder['ending_number']}:\n")
                f.write(f"文件名: {placeholder['filename']}\n")
                f.write(f"描述: {placeholder['description']}\n")
                f.write(f"备注: {placeholder['note']}\n\n")

        print(f"📄 占位符信息已保存到: {placeholder_file}")

    print("\n🎯 下一步操作:")
    print("1. 检查 ending_images/ 目录中的下载结果")
    print("2. 手动下载缺失的图片（如有必要）")
    print("3. 使用 upload_ending_images.py 上传到R2存储桶")
    print("4. 创建 ending.html 页面")

if __name__ == "__main__":
    main()