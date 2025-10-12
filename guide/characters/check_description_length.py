#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查所有角色页面Description字符数脚本
验证是否在140-160字符范围内
"""

import re
import os

def extract_description_from_file(file_path):
    """从HTML文件中提取description内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找meta description标签
        pattern = r'<meta name="description" content="([^"]*)"'
        match = re.search(pattern, content, re.IGNORECASE)
        
        if match:
            return match.group(1)
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def main():
    # 工作目录
    directory = r"G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide\characters"
    
    # 获取所有HTML文件
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    print("=" * 60)
    print("角色页面Description字符数检查报告")
    print("=" * 60)
    
    total_files = len(html_files)
    files_with_description = 0
    files_in_range = 0
    files_out_of_range = []
    
    results = []
    
    for html_file in sorted(html_files):
        file_path = os.path.join(directory, html_file)
        description = extract_description_from_file(file_path)
        
        if description:
            files_with_description += 1
            char_count = len(description)
            
            # 检查是否在140-160范围内
            in_range = 140 <= char_count <= 160
            if in_range:
                files_in_range += 1
            else:
                files_out_of_range.append({
                    'file': html_file,
                    'count': char_count,
                    'description': description
                })
            
            results.append({
                'file': html_file,
                'description': description,
                'count': char_count,
                'in_range': in_range
            })
    
    print(f"\n📊 统计摘要:")
    print(f"总页面数: {total_files}")
    print(f"有Description的页面数: {files_with_description}")
    print(f"在140-160字符范围内的页面数: {files_in_range}")
    print(f"不在范围内的页面数: {len(files_out_of_range)}")
    
    # 计算覆盖率
    coverage_rate = (files_with_description / total_files) * 100 if total_files > 0 else 0
    range_rate = (files_in_range / files_with_description) * 100 if files_with_description > 0 else 0
    
    print(f"Description覆盖率: {coverage_rate:.1f}%")
    print(f"符合字符数范围比例: {range_rate:.1f}%")
    
    if files_out_of_range:
        print(f"\n❌ 不在140-160字符范围内的页面:")
        print("-" * 80)
        for item in files_out_of_range:
            status = "太短" if item['count'] < 140 else "太长"
            print(f"📄 {item['file']}")
            print(f"📏 字符数: {item['count']} ({status})")
            print(f"📝 Description: {item['description']}")
            print("-" * 80)
    
    # 显示所有详细结果
    print(f"\n📋 详细结果 (按字符数排序):")
    print("-" * 100)
    
    # 按字符数排序
    sorted_results = sorted(results, key=lambda x: x['count'])
    
    for result in sorted_results:
        status = "✅" if result['in_range'] else "❌"
        print(f"{status} {result['file']:40} | {result['count']:3d} 字符 | {result['description'][:60]}...")
    
    print("\n" + "=" * 60)
    print("检查完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()