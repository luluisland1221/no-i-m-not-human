#!/usr/bin/env python3
"""
自动更新sitemap.txt的脚本
扫描所有HTML文件并生成sitemap.txt
"""

import os
import sys
from pathlib import Path

def generate_sitemap():
    """生成sitemap.txt文件"""
    base_url = "https://noimnothuman.xyz"
    current_dir = Path(__file__).parent

    # 查找所有HTML文件，排除node_modules目录
    html_files = []
    for html_file in current_dir.rglob("*.html"):
        if "node_modules" not in str(html_file):
            # 转换为相对路径
            relative_path = html_file.relative_to(current_dir)

            # 处理根目录的index.html
            if relative_path.name == "index.html" and relative_path.parent == Path("."):
                url = f"{base_url}/"
            else:
                # 转换路径为URL格式
                url_path = str(relative_path).replace("\\", "/")
                url = f"{base_url}/{url_path}"

            html_files.append(url)

    # 排序URLs
    html_files.sort()

    # 写入sitemap.txt
    sitemap_path = current_dir / "sitemap.txt"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        for url in html_files:
            f.write(url + "\n")

    print(f"✅ sitemap.txt已更新，共{len(html_files)}个URL")
    return len(html_files)

def main():
    """主函数"""
    try:
        count = generate_sitemap()
        print(f"🎯 成功生成sitemap.txt，包含{count}个页面")
    except Exception as e:
        print(f"❌ 生成sitemap时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()