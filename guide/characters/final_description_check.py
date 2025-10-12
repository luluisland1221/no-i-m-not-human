#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终验证脚本：检查所有角色页面的Description字符数是否在140-160字符范围内
"""

import os
import re

def extract_description(html_content):
    """从HTML内容中提取description meta标签的内容"""
    # 匹配meta name="description"标签
    pattern = r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']'
    match = re.search(pattern, html_content, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def count_characters(text):
    """计算字符数（包括标点符号和空格）"""
    return len(text) if text else 0

def main():
    # 设置工作目录
    directory = r"G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide\characters"
    
    # 获取所有HTML文件
    html_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            html_files.append(filename)
    
    html_files.sort()  # 按文件名排序
    
    print(f"开始检查所有角色页面的Description字符数...")
    print(f"工作目录: {directory}")
    print(f"总HTML文件数: {len(html_files)}")
    print("=" * 80)
    
    total_files = 0
    files_with_description = 0
    files_in_range = 0
    files_out_of_range = []
    files_missing_description = []
    
    results = []
    
    for filename in html_files:
        total_files += 1
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                content = f.read()
            
            description = extract_description(content)
            
            if description:
                files_with_description += 1
                char_count = count_characters(description)
                
                # 检查是否在140-160字符范围内
                if 140 <= char_count <= 160:
                    files_in_range += 1
                    status = "✅ 符合"
                else:
                    status = "❌ 不符合"
                    files_out_of_range.append({
                        'filename': filename,
                        'description': description,
                        'char_count': char_count
                    })
                
                results.append({
                    'filename': filename,
                    'description': description,
                    'char_count': char_count,
                    'status': status
                })
                
            else:
                files_missing_description.append(filename)
                results.append({
                    'filename': filename,
                    'description': None,
                    'char_count': 0,
                    'status': "⚠️ 缺失"
                })
                
        except Exception as e:
            print(f"读取文件 {filename} 时出错: {e}")
            results.append({
                'filename': filename,
                'description': None,
                'char_count': 0,
                'status': f"❌ 错误: {str(e)}"
            })
    
    # 打印详细结果
    print("\n详细检查结果:")
    print("-" * 80)
    print(f"{'文件名':<30} {'字符数':<8} {'状态':<10} {'Description预览'}")
    print("-" * 80)
    
    for result in results:
        filename = result['filename'][:27] + "..." if len(result['filename']) > 30 else result['filename']
        char_count = result['char_count']
        status = result['status']
        
        if result['description']:
            # 截取description前50个字符作为预览
            preview = result['description'][:47] + "..." if len(result['description']) > 50 else result['description']
        else:
            preview = "无description"
        
        print(f"{filename:<30} {char_count:<8} {status:<10} {preview}")
    
    # 打印统计摘要
    print("\n" + "=" * 80)
    print("最终统计摘要:")
    print("=" * 80)
    print(f"1. 总角色页面数: {total_files}")
    print(f"2. 有Description的页面数: {files_with_description}")
    print(f"3. Description在140-160字符范围内的页面数: {files_in_range}")
    print(f"4. Description不在140-160字符范围内的页面数: {len(files_out_of_range)}")
    print(f"5. 缺失Description的页面数: {len(files_missing_description)}")
    
    # 计算符合率
    if files_with_description > 0:
        compliance_rate = (files_in_range / files_with_description) * 100
        print(f"6. SEO符合率: {compliance_rate:.1f}%")
    
    # 如果有不符合的页面，列出详细信息
    if files_out_of_range:
        print(f"\n❌ 不符合140-160字符范围的页面 ({len(files_out_of_range)}个):")
        print("-" * 80)
        for item in files_out_of_range:
            filename = item['filename']
            char_count = item['char_count']
            description = item['description']
            print(f"\n📄 {filename}")
            print(f"   字符数: {char_count}")
            print(f"   Description: {description}")
            
            if char_count < 140:
                print(f"   需要增加 {140 - char_count} 个字符")
            elif char_count > 160:
                print(f"   需要减少 {char_count - 160} 个字符")
    
    # 如果有缺失description的页面
    if files_missing_description:
        print(f"\n⚠️ 缺失Description的页面 ({len(files_missing_description)}个):")
        print("-" * 40)
        for filename in files_missing_description:
            print(f"   📄 {filename}")
    
    # 最终结论
    print("\n" + "=" * 80)
    print("最终结论:")
    print("=" * 80)
    
    if len(files_out_of_range) == 0 and len(files_missing_description) == 0:
        print("🎉 恭喜！所有角色页面的Description都符合140-160字符的SEO要求！")
        print("✅ 所有页面都已优化完成，符合最佳SEO实践。")
    elif len(files_out_of_range) > 0:
        print(f"⚠️ 还有 {len(files_out_of_range)} 个页面的Description需要调整到140-160字符范围。")
        if len(files_missing_description) > 0:
            print(f"⚠️ 还有 {len(files_missing_description)} 个页面缺失Description。")
        print("请根据上述详细信息进行相应调整。")
    else:
        print(f"⚠️ 还有 {len(files_missing_description)} 个页面需要添加Description。")
    
    # 保存结果到文件
    result_file = os.path.join(directory, "final_description_audit.txt")
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write("角色页面Description最终审核报告\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"检查时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"1. 总角色页面数: {total_files}\n")
        f.write(f"2. 有Description的页面数: {files_with_description}\n")
        f.write(f"3. Description在140-160字符范围内的页面数: {files_in_range}\n")
        f.write(f"4. Description不在140-160字符范围内的页面数: {len(files_out_of_range)}\n")
        f.write(f"5. 缺失Description的页面数: {len(files_missing_description)}\n")
        
        if files_with_description > 0:
            compliance_rate = (files_in_range / files_with_description) * 100
            f.write(f"6. SEO符合率: {compliance_rate:.1f}%\n")
        
        if files_out_of_range:
            f.write(f"\n不符合140-160字符范围的页面:\n")
            f.write("-" * 30 + "\n")
            for item in files_out_of_range:
                f.write(f"\n文件: {item['filename']}\n")
                f.write(f"字符数: {item['char_count']}\n")
                f.write(f"Description: {item['description']}\n")
        
        if files_missing_description:
            f.write(f"\n缺失Description的页面:\n")
            f.write("-" * 20 + "\n")
            for filename in files_missing_description:
                f.write(f"  {filename}\n")
    
    print(f"\n📄 详细报告已保存至: {result_file}")

if __name__ == "__main__":
    main()