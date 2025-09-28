#!/usr/bin/env python3
"""
自动生成XML sitemap的脚本
包含lastmod、priority、changefreq优化
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

def generate_xml_sitemap():
    """生成XML sitemap文件"""
    base_url = "https://noimnothuman.xyz"
    current_dir = Path(__file__).parent

    # 创建XML根元素
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 页面优先级映射
    priority_map = {
        "index.html": 1.0,
        "guide.html": 0.9,
        "characters/": 0.7,  # 所有角色页面
        "default": 0.6
    }

    # 更新频率映射
    changefreq_map = {
        "index.html": "weekly",
        "guide.html": "weekly",
        "characters/": "monthly",  # 角色页面相对稳定
        "default": "monthly"
    }

    # 查找所有HTML文件
    html_files = []
    for html_file in current_dir.rglob("*.html"):
        if "node_modules" not in str(html_file):
            relative_path = html_file.relative_to(current_dir)
            html_files.append(relative_path)

    # 排序文件
    html_files.sort()

    # 为每个文件创建URL条目
    for html_file in html_files:
        url = ET.SubElement(urlset, "url")

        # 设置loc (URL)
        if html_file.name == "index.html" and html_file.parent == Path("."):
            loc = f"{base_url}/"
        else:
            url_path = str(html_file).replace("\\", "/")
            loc = f"{base_url}/{url_path}"

        loc_elem = ET.SubElement(url, "loc")
        loc_elem.text = loc

        # 设置lastmod
        lastmod_elem = ET.SubElement(url, "lastmod")
        lastmod_elem.text = current_date

        # 设置priority
        priority = priority_map["default"]
        if html_file.name in priority_map:
            priority = priority_map[html_file.name]
        elif "characters/" in str(html_file):
            priority = priority_map["characters/"]

        priority_elem = ET.SubElement(url, "priority")
        priority_elem.text = str(priority)

        # 设置changefreq
        changefreq = changefreq_map["default"]
        if html_file.name in changefreq_map:
            changefreq = changefreq_map[html_file.name]
        elif "characters/" in str(html_file):
            changefreq = changefreq_map["characters/"]

        changefreq_elem = ET.SubElement(url, "changefreq")
        changefreq_elem.text = changefreq

    # 美化XML输出
    from xml.dom import minidom

    # 转换为字符串
    rough_string = ET.tostring(urlset, encoding='unicode')

    # 格式化XML
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="    ")

    # 移除多余的空行
    lines = [line for line in pretty_xml.split('\n') if line.strip()]
    formatted_xml = '\n'.join(lines)

    # 写入文件
    sitemap_path = current_dir / "sitemap.xml"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(formatted_xml)

    print(f"✅ sitemap.xml已更新，共{len(html_files)}个URL")
    print(f"🎯 包含SEO优化：lastmod、priority、changefreq")
    return len(html_files)

def main():
    """主函数"""
    try:
        count = generate_xml_sitemap()
        print(f"🎯 成功生成sitemap.xml，包含{count}个页面")
    except Exception as e:
        print(f"❌ 生成sitemap时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()