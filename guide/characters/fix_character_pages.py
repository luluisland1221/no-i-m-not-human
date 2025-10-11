#!/usr/bin/env python3
"""
批量修复角色页面HTML格式问题的脚本
修复未闭合的<li>标签和footer中的HTML标签问题
"""

import os
import re

def fix_html_issues(file_path):
    """修复单个HTML文件中的格式问题"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 修复1: 修复Quick Navigation中的未闭合的<li>标签
        # 匹配形如 <li><a href="#strategy">Strategy</a> 的模式，后面没有</li>
        nav_pattern = r'(<li><a href="#[^"]*">[^<]*</a>)(?!</li>)(\s*$)'
        content = re.sub(nav_pattern, r'\1</li>', content, flags=re.MULTILINE)
        
        # 修复2: 修复Game Content section中Steam链接的未闭合<li>标签
        steam_pattern = r'(<li><a href="https://store\.steampowered\.com[^"]*" target="_blank">[^<]*</a>)(?!</li>)(\s*</ul>)'
        content = re.sub(steam_pattern, r'\1</li>\2', content)
        
        # 修复3: 确保Quick Navigation的ul标签正确闭合
        # 查找</div>前缺少</ul>的情况
        nav_ul_fix_pattern = r'(<li><a href="#strategy">Strategy</a></li>\s+)(</div>)'
        content = re.sub(nav_ul_fix_pattern, r'\1</ul>\n                    \2', content)
        
        # 只有内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 修复完成: {os.path.basename(file_path)}")
            return True
        else:
            print(f"⏭️  无需修复: {os.path.basename(file_path)}")
            return False
            
    except Exception as e:
        print(f"❌ 修复失败 {file_path}: {e}")
        return False

def main():
    """主函数：批量修复所有角色页面"""
    # 需要修复的文件列表
    files_to_fix = [
        "bandana-guy.html",
        "bearded-guy.html", 
        "best-son.html",
        "big-momma.html",
        "blinded-man.html",
        "blonde-guy.html",
        "border-patrol-agent.html",
        "brunette-guy.html",
        "cabby-man.html",
        "cashier-girl.html",
        "cat-lady.html",
        "cheerful-man.html",
        "child.html",
        "coat-guy.html",
        "cozy-man.html",
        "death.html",
        "death-cult-leader.html",
        "death-cult-peon.html",
        "delivery-man.html",
        "delivery-man-backup.html",
        "disfigured-guy.html",
        "egghead-guy.html",
        "factory-guy.html",
        "fema-agent.html",
        "fetus.html",
        "fortune-teller.html",
        "gravedigger.html",
        "homeless-man.html",
        "husband-and-wife.html",
        "immortal-man.html",
        "intruder.html",
        "kindergarten-teacher.html",
        "little-girl.html",
        "miner.html",
        "mushroom-man.html",
        "music-conductor.html",
        "neglectful-mother.html",
        "neighbor.html",
        "nikita-the-wind-based-intruder.html",
        "nun.html",
        "old-lady.html",
        "parentless-teenager.html",
        "positive-guy.html",
        "protagonist.html",
        "raincoat-child.html",
        "reporter.html",
        "seductive-woman.html",
        "stand-up-guy.html",
        "stoner.html",
        "suit-guy.html",
        "sun-guy.html",
        "surgeon.html",
        "sweaty-man.html",
        "theorist.html",
        "the-sisters.html",
        "vigilante.html",
        "weather-reporter.html",
        "widowed-woman.html",
        "wireface.html",
        "wounded-man.html"
    ]
    
    current_dir = os.getcwd()
    fixed_count = 0
    total_count = len(files_to_fix)
    
    print(f"开始批量修复 {total_count} 个角色页面...")
    print("=" * 50)
    
    for filename in files_to_fix:
        file_path = os.path.join(current_dir, filename)
        if os.path.exists(file_path):
            if fix_html_issues(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  文件不存在: {filename}")
    
    print("=" * 50)
    print(f"批量修复完成！")
    print(f"总文件数: {total_count}")
    print(f"已修复: {fixed_count}")
    print(f"无需修复: {total_count - fixed_count}")

if __name__ == "__main__":
    main()