#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速为角色页面添加Description的脚本
"""

import os
import re

# 角色Description配置
CHARACTER_DESCRIPTIONS = {
    'cashier-girl': 'Explore Cashier Girl character: her retail expertise, customer service skills, payment processing knowledge, and business environment familiarity in our comprehensive guide.',
    'cat-lady': 'Discover Cat Lady character: her animal care expertise, feline behavior knowledge, protective instincts, and potential animal-human relationship dynamics in our detailed guide.',
    'cheerful-man': 'Meet Cheerful Man character: his optimistic outlook, positive energy, social connections, and potentially suspicious perpetual happiness in our character analysis.',
    'child': 'Protect Child character: innocence, vulnerability, dependency needs, developmental psychology, and potential supernatural abilities in our comprehensive child guide.',
    'delivery-man-backup': 'Analyze Backup Delivery Man character: his secondary delivery routes, alternative access points, backup logistics knowledge, and potential coordinated operations.',
    'disfigured-guy': 'Examine Disfigured Guy character: his facial injuries, traumatic backstory, medical needs, and potential Visitor伪装 abilities in our detailed analysis.',
    'egghead-guy': 'Study Egghead Guy character: his intellectual abilities, academic knowledge, problem-solving skills, and potential enhanced cognitive capabilities in our guide.',
    'factory-guy': 'Investigate Factory Guy character: his industrial knowledge, machinery expertise, production experience, and potential manufacturing sector insights in our analysis.',
    'gravedigger': 'Meet Gravedigger character: his cemetery knowledge, death industry expertise, burial procedures, and potential supernatural death-related abilities in our guide.',
    'homeless-man': 'Help Homeless Man character: his street survival skills, resource knowledge, disadvantaged status, and potential hidden capabilities in our comprehensive guide.',
    'husband-and-wife': 'Evaluate Husband and Wife characters: their marital dynamics, shared history, family relationships, and potential coordinated Visitor activities in our analysis.',
    'intruder': 'Confront Intruder character: his unauthorized access, trespassing skills, potential threats, and security system knowledge in our security-focused guide.',
    'little-girl': 'Protect Little Girl character: her childhood innocence, parental dependency, vulnerability factors, and potential supernatural manifestation in our child guide.',
    'music-conductor': 'Follow Music Conductor character: his musical expertise, leadership abilities, artistic temperament, and potential sound-based Visitor identification in our cultural guide.',
    'nun': 'Trust Nun character: her religious devotion, spiritual authority, moral compass, and potential faith-based Visitor resistance in our religious character guide.',
    'old-lady': 'Assist Old Lady character: her elderly wisdom, life experience, vulnerability factors, and potential age-related Visitor traits in our senior character guide.',
    'protagonist': 'Guide Protagonist character: the player character with survival abilities, decision-making skills, narrative importance, and human resilience in our hero guide.',
    'reporter': 'Interview Reporter character: her investigative skills, media knowledge, information gathering abilities, and potential truth-seeking mission in our press guide.',
    'seductive-woman': 'Resist Seductive Woman character: her attractive appearance, persuasion skills, temptation tactics, and potential manipulation abilities in our deception guide.',
    'stand-up-guy': 'Trust Stand Up Guy character: his moral integrity, reliability, protective instincts, and potential human leadership qualities in our virtue character guide.',
    'stoner': 'Analyze Stoner character: his relaxed demeanor, drug influence, altered perception, and potential enhanced Visitor detection in our consciousness guide.',
    'suit-guy': 'Evaluate Suit Guy character: his professional appearance, business knowledge, corporate connections, and potential white-collar Visitor traits in our professional guide.',
    'surgeon': 'Trust Surgeon character: his medical expertise, surgical skills, healing abilities, and potential life-saving human qualities in our medical professional guide.',
    'vigilante': 'Face Vigilante character: his justice-seeking behavior, protective instincts, potential threats, and self-appointed security role in our law enforcement guide.',
    'weather-reporter': 'Watch Weather Reporter character: her meteorological knowledge, forecasting abilities, environmental awareness, and potential weather-based Visitor detection in our climate guide.',
    'widowed-woman': 'Comfort Widowed Woman character: her grief experience, emotional vulnerability, resilience capacity, and potential human empathy qualities in our emotional guide.',
    'wireface': 'Confront Wireface character: his cybernetic enhancements, technological abilities, non-human features, and potential machine-based Visitor traits in our tech guide.',
    'wounded-man': 'Treat Wounded Man character: his injury severity, medical needs, vulnerability factors, and potential healing capabilities in our medical emergency guide.'
}

def add_description_to_file(file_path, description):
    """为文件添加description"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 检查是否已有description
        if '<meta name="description"' in content:
            return False

        # 查找title标签
        title_pattern = r'(<title>.*?</title>\s*)'
        title_match = re.search(title_pattern, content)

        if title_match:
            title_end = title_match.end()
            description_tag = f'\n    <meta name="description" content="{description}">\n'
            new_content = content[:title_end] + description_tag + content[title_end:]

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            return True
        return False
    except:
        return False

def main():
    characters_dir = os.path.join(os.getcwd(), 'guide', 'characters')

    updated_count = 0
    for character, description in CHARACTER_DESCRIPTIONS.items():
        file_path = os.path.join(characters_dir, f'{character}.html')
        if os.path.exists(file_path):
            if add_description_to_file(file_path, description):
                print(f"✅ {character}")
                updated_count += 1
            else:
                print(f"⚪ {character} (已有或失败)")
        else:
            print(f"❌ {character} (文件不存在)")

    print(f"\n完成! 更新了 {updated_count} 个角色页面")

if __name__ == "__main__":
    main()