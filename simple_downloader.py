#!/usr/bin/env python3
"""
简单网页下载脚本
专门用于下载No, I'm not a Human游戏的endings信息
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
from urllib.parse import urljoin, urlparse
import re

def download_fandom_endings():
    """下载Fandom wiki的endings页面"""
    url = "https://no-i-am-not-a-human.fandom.com/wiki/Endings"

    print(f"正在下载: {url}")

    try:
        # 设置请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # 发送请求
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        print("页面下载成功，正在解析...")

        # 解析HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # 提取页面标题
        title = soup.find('title')
        title_text = title.get_text().strip() if title else '无标题'

        # 提取endings信息
        endings = []

        # 查找所有包含ending信息的表格
        tables = soup.find_all('table')

        for table in tables:
            # 检查表格是否包含ending信息
            table_text = table.get_text().lower()
            if any(keyword in table_text for keyword in ['ending', 'requirements', 'photo', 'text']):
                print(f"找到可能的endings表格...")

                rows = table.find_all('tr')
                print(f"表格有 {len(rows)} 行")

                for i, row in enumerate(rows[1:], 1):  # 跳过表头
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 2:
                        ending_info = {
                            'row_number': i,
                            'content': cells[0].get_text().strip(),
                            'details': cells[1].get_text().strip() if len(cells) > 1 else '',
                            'requirements': cells[2].get_text().strip() if len(cells) > 2 else ''
                        }

                        # 查找图片
                        img = cells[0].find('img')
                        if img:
                            ending_info['image'] = {
                                'src': img.get('src', ''),
                                'alt': img.get('alt', ''),
                                'title': img.get('title', '')
                            }

                        endings.append(ending_info)

        # 提取所有图片
        images = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and 'static.wikia.nocookie.net' in src:
                images.append({
                    'src': src,
                    'alt': img.get('alt', ''),
                    'title': img.get('title', '')
                })

        # 提取主要内容文本
        main_content = ''
        content_area = soup.find('div', class_='mw-parser-output')
        if content_area:
            # 移除脚本和样式
            for element in content_area.find_all(['script', 'style', 'table']):
                element.decompose()
            main_content = content_area.get_text(strip=True)

        # 整理数据
        data = {
            'url': url,
            'title': title_text,
            'endings': endings,
            'images': images,
            'main_content': main_content,
            'statistics': {
                'total_endings': len(endings),
                'total_images': len(images),
                'content_length': len(main_content)
            },
            'download_time': time.strftime('%Y-%m-%d %H:%M:%S')
        }

        # 保存结果
        save_dir = "G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\参考资料\\fandom_endings"
        os.makedirs(save_dir, exist_ok=True)

        # 保存JSON
        json_file = os.path.join(save_dir, 'endings_data.json')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # 保存文本
        txt_file = os.path.join(save_dir, 'endings_text.txt')
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(f"标题: {title_text}\n")
            f.write(f"URL: {url}\n")
            f.write(f"下载时间: {data['download_time']}\n")
            f.write("="*60 + "\n\n")

            f.write(f"统计信息:\n")
            f.write(f"- 发现endings: {data['statistics']['total_endings']}\n")
            f.write(f"- 发现图片: {data['statistics']['total_images']}\n")
            f.write(f"- 内容长度: {data['statistics']['content_length']} 字符\n")
            f.write("\n" + "="*60 + "\n\n")

            f.write("Endings详情:\n")
            for i, ending in enumerate(endings, 1):
                f.write(f"\n{i}. Ending #{ending.get('row_number', '?')}\n")
                f.write(f"   内容: {ending.get('content', '')}\n")
                f.write(f"   详情: {ending.get('details', '')}\n")
                f.write(f"   要求: {ending.get('requirements', '')}\n")
                if ending.get('image'):
                    f.write(f"   图片: {ending['image'].get('src', '')}\n")

            f.write("\n" + "="*60 + "\n\n")
            f.write("主要内容:\n")
            f.write(main_content[:2000])  # 只保存前2000字符

        print(f"下载完成！")
        print(f"- 发现 {len(endings)} 个endings")
        print(f"- 发现 {len(images)} 张图片")
        print(f"- 文件保存在: {save_dir}")

        return data

    except Exception as e:
        print(f"下载失败: {e}")
        return None

def create_image_downloader():
    """创建图片下载脚本"""
    script_content = '''#!/usr/bin/env python3
"""
图片下载脚本
"""

import requests
import os
import time
import json

def download_endings_images():
    """下载endings相关的图片"""
    # 读取之前保存的数据
    data_file = "G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\参考资料\\fandom_endings\\endings_data.json"

    if not os.path.exists(data_file):
        print("找不到数据文件，请先运行主下载脚本")
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    images = data.get('images', [])
    if not images:
        print("没有找到图片信息")
        return

    # 创建图片保存目录
    save_dir = "G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\参考资料\\fandom_endings\\images"
    os.makedirs(save_dir, exist_ok=True)

    print(f"开始下载 {len(images)} 张图片...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    downloaded_files = []

    for i, img_info in enumerate(images):
        try:
            src = img_info['src']
            if not src:
                continue

            # 确保是完整的URL
            if not src.startswith('http'):
                src = 'https:' + src

            # 生成文件名
            alt_text = img_info.get('alt', '').replace(' ', '_').replace('/', '_')
            if alt_text:
                filename = f"{alt_text}_{i+1}.jpg"
            else:
                filename = f"ending_image_{i+1}.jpg"

            filepath = os.path.join(save_dir, filename)

            # 检查文件是否已存在
            if os.path.exists(filepath):
                print(f"文件已存在，跳过: {filename}")
                continue

            print(f"下载图片 {i+1}/{len(images)}: {filename}")

            # 下载图片
            response = requests.get(src, headers=headers, timeout=30)
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                f.write(response.content)

            downloaded_files.append(filepath)

            # 添加延迟避免被封
            time.sleep(1)

        except Exception as e:
            print(f"下载图片失败 {src}: {e}")

    print(f"\\n下载完成！成功下载 {len(downloaded_files)} 张图片")
    print(f"图片保存在: {save_dir}")

    # 保存下载记录
    record_file = os.path.join(save_dir, 'downloaded_images.txt')
    with open(record_file, 'w', encoding='utf-8') as f:
        f.write(f"下载时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\\n")
        f.write(f"成功下载图片: {len(downloaded_files)}\\n")
        f.write("\\n下载的文件:\\n")
        for filepath in downloaded_files:
            filename = os.path.basename(filepath)
            f.write(f"- {filename}\\n")

if __name__ == "__main__":
    download_endings_images()
'''

    script_file = "G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\code\\download_images.py"
    with open(script_file, 'w', encoding='utf-8') as f:
        f.write(script_content)

    print(f"图片下载脚本已创建: {script_file}")
    return script_file

if __name__ == "__main__":
    print("开始下载No, I'm not a Human游戏的endings信息...")
    data = download_fandom_endings()

    if data:
        # 创建图片下载脚本
        image_script = create_image_downloader()
        print(f"\\n你可以运行图片下载脚本来下载所有相关图片:")
        print(f"python {image_script}")
    else:
        print("下载失败")