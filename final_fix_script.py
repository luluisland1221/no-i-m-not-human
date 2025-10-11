#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终修正脚本 - 快速修正所有剩余页面
"""

import os
from pathlib import Path

# 角色描述映射
character_descriptions = {
    'nikita-the-wind-based-intruder.html': 'Nikita the Wind is a character who presents himself with elemental powers and mysterious abilities. His wind-based nature gives him a distinctive supernatural quality, and his elusive demeanor makes him seem more unpredictable than other characters.',
    'nun.html': 'The Nun is a character who presents herself with religious devotion and spiritual authority. Her monastic life gives her a distinctive pious appearance, and her disciplined demeanor makes her seem more righteous than other characters.',
    'old-lady.html': 'The Old Lady is a character who presents herself with elderly wisdom and life experience. Her advanced age gives her a distinctive venerable appearance, and her traditional values make her seem more respectable than other characters.',
    'parentless-teenager.html': 'The Parentless Teenager is a character who presents herself with youthful independence and survival skills. Her lack of parental guidance gives her a distinctive resilient nature, and her defiant demeanor makes her seem more self-reliant than other characters.',
    'positive-guy.html': 'The Positive Guy is a character who presents himself with optimistic outlook and encouraging personality. His positive attitude gives him a distinctive uplifting presence, and his supportive nature makes him seem more inspiring than other characters.',
    'protagonist.html': 'The Protagonist is a character who presents himself with central role and decision-making authority. His main character status gives him a distinctive narrative importance, and his resourceful nature makes him seem more capable than other characters.',
    'raincoat-child.html': 'The Raincoat Child is a character who presents himself with weather-protected appearance and youthful vulnerability. His raincoat gives him a distinctive prepared look, and his childlike nature makes him seem more innocent than other characters.',
    'reporter.html': 'The Reporter is a character who presents himself with journalistic skills and investigative nature. His media background gives him a distinctive information-gathering ability, and his curious demeanor makes him seem more inquisitive than other characters.',
    'seductive-woman.html': 'The Seductive Woman is a character who presents herself with alluring charm and romantic intentions. Her attractive qualities give her a distinctive captivating presence, and her flirtatious demeanor makes her seem more enchanting than other characters.',
    'stand-up-guy.html': 'The Stand Up Guy is a character who presents himself with comedic talent and entertainment skills. His performance background gives him a distinctive humorous approach, and his friendly demeanor makes him seem more entertaining than other characters.',
    'stoner.html': 'The Stoner is a character who presents himself with relaxed attitude and alternative lifestyle. His drug use gives him a distinctive altered perception, and his carefree demeanor makes him seem more unpredictable than other characters.',
    'suit-guy.html': 'The Suit Guy is a character who presents himself with formal attire and business-like appearance. His professional clothing gives him a distinctive sophisticated look, and his polished demeanor makes him seem more refined than other characters.',
    'sun-guy.html': 'The Sun Guy is a character who presents himself with solar associations and radiant qualities. His connection to sunlight gives him a distinctive luminous appearance, and his energetic demeanor makes him seem more vibrant than other characters.',
    'surgeon.html': 'The Surgeon is a character who presents himself with medical expertise and surgical skills. His medical background gives him a distinctive professional authority, and his precise demeanor makes him seem more competent than other characters.',
    'sweaty-man.html': 'The Sweaty Man is a character who presents himself with anxious disposition and nervous energy. His constant perspiration gives him a distinctive stressed appearance, and his uneasy demeanor makes him seem more tense than other characters.',
    'theorist.html': 'The Theorist is a character who presents himself with intellectual curiosity and analytical mindset. His theoretical knowledge gives him a distinctive academic approach, and his inquisitive nature makes him seem more thoughtful than other characters.',
    'the-sisters.html': 'The Sisters are characters who present themselves with sibling bond and shared experiences. Their sisterly relationship gives them a distinctive supportive dynamic, and their connected nature makes them seem more unified than other characters.',
    'vigilante.html': 'The Vigilante is a character who presents himself with justice-seeking attitude and self-appointed authority. His crime-fighting mission gives him a distinctive righteous appearance, and his determined demeanor makes him seem more resolute than other characters.',
    'weather-reporter.html': 'The Weather Reporter is a character who presents himself with meteorological knowledge and forecasting skills. His weather expertise gives him a distinctive scientific background, and his informative demeanor makes him seem more knowledgeable than other characters.',
    'widowed-woman.html': 'The Widowed Woman is a character who presents herself with grief-stricken demeanor and recent loss. Her widowhood gives her a distinctive sorrowful appearance, and her mourning nature makes her seem more tragic than other characters.',
    'wireface.html': 'The Wireface is a character who presents himself with facial modifications and mysterious background. His wired features give him a distinctive unsettling appearance, and his silent demeanor makes him seem more enigmatic than other characters.',
    'wounded-man.html': 'The Wounded Man is a character who presents himself with injuries and traumatic past. His wounds give him a distinctive damaged appearance, and his suffering demeanor makes him seem more sympathetic than other characters.',
    'cozy-man.html': 'The Cozy Man is a character who presents himself with comfort-seeking and relaxed demeanor. His preference for comfort gives him a distinctive approach, and his easy-going nature makes him seem more approachable than other characters.',
    'death.html': 'Death is a character who presents itself with supernatural authority and inevitable presence. Its personification gives it a distinctive ominous appearance, and its impartial nature makes it seem more fearsome than other characters.',
    'delivery-man.html': 'The Delivery Man is a character who presents himself with service background and logistical skills. His delivery experience gives him a distinctive purpose-driven approach, and his professional demeanor makes him seem more reliable than other characters.',
    'egghead-guy.html': 'The Egghead Guy is a character who presents himself with intellectual appearance and thoughtful demeanor. His distinctive head shape gives him a memorable look, and his analytical nature makes him seem more intelligent than other characters.',
    'factory-guy.html': 'The Factory Guy is a character who presents himself with industrial background and work experience. His connection to manufacturing gives him a distinctive practical skill set, and his laborer demeanor makes him seem more hardworking than other characters.',
    'fetus.html': 'The Fetus is a character who presents itself with undeveloped form and mysterious nature. Its prenatal state gives it a distinctive unusual appearance, and its enigmatic presence makes it seem more unsettling than other characters.',
    'fortune-teller.html': 'The Fortune Teller is a character who presents herself with mystical abilities and esoteric knowledge. Her divination skills give her a distinctive insight into future events, and her mysterious demeanor makes her seem more intriguing than other characters.'
}

def fix_character_file(file_path, correct_description):
    """修正单个角色文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找并替换错误的描述
        old_pattern = '<p>The.*is a character who presents.*bandana accessory gives him a distinctive look, and his approachable demeanor makes him seem less threatening than other characters.</p>'

        if 'bandana accessory' in content:
            # 使用更简单的替换模式
            old_text = '<p>The Bandana Guy is a visitor who presents himself with a casual, relaxed appearance. His bandana accessory gives him a distinctive look, and his approachable demeanor makes him seem less threatening than other characters.</p>'
            if old_text in content:
                content = content.replace(old_text, f'<p>{correct_description}</p>')

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True

        return False

    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    characters_dir = Path("guide/characters")

    print("🚀 开始最终修正...")

    fixed_count = 0
    total_files = 0

    for filename, description in character_descriptions.items():
        file_path = characters_dir / filename
        if file_path.exists():
            total_files += 1
            if fix_character_file(file_path, description):
                fixed_count += 1
                print(f"✅ 修正完成: {filename}")
            else:
                print(f"⚪ 无需修正: {filename}")

    print(f"\n📊 最终修正结果:")
    print(f"   处理文件数: {total_files}")
    print(f"   成功修正: {fixed_count}")

if __name__ == "__main__":
    main()