#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速批量修正脚本
修正所有页面中的Bandana Guy错误描述
"""

import os
from pathlib import Path

def get_character_description(filename):
    """根据文件名生成角色描述"""
    base_name = filename.replace('.html', '').replace('-', ' ').title()

    # 特殊处理一些角色名称
    name_mapping = {
        'Blonde Guy': 'The Blonde Guy is a character who presents himself with distinctive blonde hair and casual appearance. His light-colored hair gives him a noticeable look, and his friendly demeanor makes him seem more approachable than other characters.',
        'Border Patrol Agent': 'The Border Patrol Agent is a character who presents herself with law enforcement authority and official demeanor. Her experience in border security gives her a distinctive approach to screening, and her professional manner makes her seem more authoritative than other characters.',
        'Brunette Guy': 'The Brunette Guy is a character who presents himself with brown hair and standard appearance. His ordinary looks give him a common presence, and his neutral demeanor makes him seem more typical than other characters.',
        'Cabby Man': 'The Cabby Man is a character who presents himself with transportation experience and local knowledge. His familiarity with routes gives him a distinctive navigational skill, and his service background makes him seem more helpful than other characters.',
        'Cat Lady': 'The Cat Lady is a character who presents herself with a connection to felines and unique personality. Her love for cats gives her a distinctive nurturing nature, and her mysterious demeanor makes her seem more intriguing than other characters.',
        'Cheerful Man': 'The Cheerful Man is a character who presents himself with optimism and positive attitude. His upbeat nature gives him a distinctive outlook, and his friendly demeanor makes him seem more uplifting than other characters.',
        'Child': 'The Child is a character who presents themselves with innocence and vulnerability. Their young age gives them a distinctive perspective, and their dependent nature makes them seem more protected than other characters.',
        'Coat Guy': 'The Coat Guy is a character who presents himself with practical outerwear and prepared appearance. His distinctive coat gives him a weather-ready look, and his cautious demeanor makes him seem more self-sufficient than other characters.',
        'Cozy Man': 'The Cozy Man is a character who presents himself with comfort-seeking and relaxed demeanor. His preference for comfort gives him a distinctive approach, and his easy-going nature makes him seem more approachable than other characters.',
        'Death': 'Death is a character who presents itself with supernatural authority and inevitable presence. Its personification gives it a distinctive ominous appearance, and its impartial nature makes it seem more fearsome than other characters.',
        'Death Cult Leader': 'The Death Cult Leader is a character who presents himself with religious devotion and charismatic authority. His leadership role gives him a distinctive influential presence, and his fanatical demeanor makes him seem more dangerous than other characters.',
        'Death Cult Peon': 'The Death Cult Peons are characters who present themselves with religious devotion and follower mentality. Their group identity gives them a distinctive unified appearance, and their zealous nature makes them seem more unpredictable than other characters.',
        'Delivery Man': 'The Delivery Man is a character who presents himself with service background and logistical skills. His delivery experience gives him a distinctive purpose-driven approach, and his professional demeanor makes him seem more reliable than other characters.',
        'Disfigured Guy': 'The Disfigured Guy is a character who presents himself with visible injuries and traumatic past. His disfigurement gives him a distinctive sympathetic appearance, and his pained demeanor makes him seem more vulnerable than other characters.',
        'Egghead Guy': 'The Egghead Guy is a character who presents himself with intellectual appearance and thoughtful demeanor. His distinctive head shape gives him a memorable look, and his analytical nature makes him seem more intelligent than other characters.',
        'Factory Guy': 'The Factory Guy is a character who presents himself with industrial background and work experience. His connection to manufacturing gives him a distinctive practical skill set, and his laborer demeanor makes him seem more hardworking than other characters.',
        'Fema Agent': 'The FEMA Agent is a character who presents himself with government authority and emergency response training. His official role gives him a distinctive authoritative presence, and his professional demeanor makes him seem more serious than other characters.',
        'Fetus': 'The Fetus is a character who presents itself with undeveloped form and mysterious nature. Its prenatal state gives it a distinctive unusual appearance, and its enigmatic presence makes it seem more unsettling than other characters.',
        'Fortune Teller': 'The Fortune Teller is a character who presents herself with mystical abilities and esoteric knowledge. Her divination skills give her a distinctive insight into future events, and her mysterious demeanor makes her seem more intriguing than other characters.',
        'Gravedigger': 'The Gravedigger is a character who presents himself with mortuary experience and death-related knowledge. His work with the deceased gives him a distinctive morbid expertise, and his solemn demeanor makes him seem more serious than other characters.',
        'Homeless Man': 'The Homeless Man is a character who presents himself with transient lifestyle and survival skills. His street experience gives him a distinctive resourceful nature, and his weathered appearance makes him seem more resilient than other characters.',
        'Husband And Wife': 'The Husband and Wife are characters who present themselves with marital relationship and shared history. Their partnership gives them a distinctive dynamic, and their coupled nature makes them seem more complex than other characters.',
        'Immortal Man': 'The Immortal Man is a character who presents himself with eternal existence and timeless wisdom. His immortality gives him a distinctive supernatural quality, and his ancient perspective makes him seem more knowledgeable than other characters.',
        'Intruder': 'The Intruder is a character who presents himself with threatening presence and invasive behavior. His unauthorized entry gives him a distinctive dangerous aura, and his aggressive demeanor makes him seem more menacing than other characters.',
        'Kindergarten Teacher': 'The Kindergarten Teacher is a character who presents herself with educational background and nurturing nature. Her teaching experience gives her a distinctive patient demeanor, and her caring attitude makes her seem more gentle than other characters.',
        'Little Girl': 'The Little Girl is a character who presents herself with childhood innocence and dependent nature. Her young age gives her a distinctive vulnerable appearance, and her sweet demeanor makes her seem more endearing than other characters.',
        'Miner': 'The Miner is a character who presents himself with underground experience and excavation skills. His mining background gives him a distinctive rugged appearance, and his labor-intensive nature makes him seem more hardworking than other characters.',
        'Mushroom Man': 'The Mushroom Man is a character who presents himself with fungal characteristics and mysterious origins. His connection to mushrooms gives him a distinctive unusual appearance, and his strange demeanor makes him seem more enigmatic than other characters.',
        'Music Conductor': 'The Music Conductor is a character who presents himself with artistic talent and leadership skills. His musical background gives him a distinctive cultural refinement, and his expressive demeanor makes him seem more sophisticated than other characters.',
        'Neglectful Mother': 'The Neglectful Mother is a character who presents herself with parental irresponsibility and exhausted demeanor. Her neglectful behavior gives her a distinctive troubled appearance, and her apathetic nature makes her seem more problematic than other characters.',
        'Neighbor': 'The Neighbor is a character who presents himself with local knowledge and community connection. His residential proximity gives him a distinctive familiar presence, and his helpful nature makes him seem more trustworthy than other characters.',
        'Nikita The Wind Based Intruder': 'Nikita the Wind is a character who presents himself with elemental powers and mysterious abilities. His wind-based nature gives him a distinctive supernatural quality, and his elusive demeanor makes him seem more unpredictable than other characters.',
        'Nun': 'The Nun is a character who presents herself with religious devotion and spiritual authority. Her monastic life gives her a distinctive pious appearance, and her disciplined demeanor makes her seem more righteous than other characters.',
        'Old Lady': 'The Old Lady is a character who presents herself with elderly wisdom and life experience. Her advanced age gives her a distinctive venerable appearance, and her traditional values make her seem more respectable than other characters.',
        'Parentless Teenager': 'The Parentless Teenager is a character who presents herself with youthful independence and survival skills. Her lack of parental guidance gives her a distinctive resilient nature, and her defiant demeanor makes her seem more self-reliant than other characters.',
        'Positive Guy': 'The Positive Guy is a character who presents himself with optimistic outlook and encouraging personality. His positive attitude gives him a distinctive uplifting presence, and his supportive nature makes him seem more inspiring than other characters.',
        'Protagonist': 'The Protagonist is a character who presents himself with central role and decision-making authority. His main character status gives him a distinctive narrative importance, and his resourceful nature makes him seem more capable than other characters.',
        'Raincoat Child': 'The Raincoat Child is a character who presents himself with weather-protected appearance and youthful vulnerability. His raincoat gives him a distinctive prepared look, and his childlike nature makes him seem more innocent than other characters.',
        'Reporter': 'The Reporter is a character who presents himself with journalistic skills and investigative nature. His media background gives him a distinctive information-gathering ability, and his curious demeanor makes him seem more inquisitive than other characters.',
        'Seductive Woman': 'The Seductive Woman is a character who presents herself with alluring charm and romantic intentions. Her attractive qualities give her a distinctive captivating presence, and her flirtatious demeanor makes her seem more enchanting than other characters.',
        'Stand Up Guy': 'The Stand Up Guy is a character who presents himself with comedic talent and entertainment skills. His performance background gives him a distinctive humorous approach, and his friendly demeanor makes him seem more entertaining than other characters.',
        'Stoner': 'The Stoner is a character who presents himself with relaxed attitude and alternative lifestyle. His drug use gives him a distinctive altered perception, and his carefree demeanor makes him seem more unpredictable than other characters.',
        'Suit Guy': 'The Suit Guy is a character who presents himself with formal attire and business-like appearance. His professional clothing gives him a distinctive sophisticated look, and his polished demeanor makes him seem more refined than other characters.',
        'Sun Guy': 'The Sun Guy is a character who presents himself with solar associations and radiant qualities. His connection to sunlight gives him a distinctive luminous appearance, and his energetic demeanor makes him seem more vibrant than other characters.',
        'Surgeon': 'The Surgeon is a character who presents himself with medical expertise and surgical skills. His medical background gives him a distinctive professional authority, and his precise demeanor makes him seem more competent than other characters.',
        'Sweaty Man': 'The Sweaty Man is a character who presents himself with anxious disposition and nervous energy. His constant perspiration gives him a distinctive stressed appearance, and his uneasy demeanor makes him seem more tense than other characters.',
        'Theorist': 'The Theorist is a character who presents himself with intellectual curiosity and analytical mindset. His theoretical knowledge gives him a distinctive academic approach, and his inquisitive nature makes him seem more thoughtful than other characters.',
        'The Sisters': 'The Sisters are characters who present themselves with sibling bond and shared experiences. Their sisterly relationship gives them a distinctive supportive dynamic, and their connected nature makes them seem more unified than other characters.',
        'Vigilante': 'The Vigilante is a character who presents himself with justice-seeking attitude and self-appointed authority. His crime-fighting mission gives him a distinctive righteous appearance, and his determined demeanor makes him seem more resolute than other characters.',
        'Weather Reporter': 'The Weather Reporter is a character who presents himself with meteorological knowledge and forecasting skills. His weather expertise gives him a distinctive scientific background, and his informative demeanor makes him seem more knowledgeable than other characters.',
        'Widowed Woman': 'The Widowed Woman is a character who presents herself with grief-stricken demeanor and recent loss. Her widowhood gives her a distinctive sorrowful appearance, and her mourning nature makes her seem more tragic than other characters.',
        'Wireface': 'The Wireface is a character who presents himself with facial modifications and mysterious background. His wired features give him a distinctive unsettling appearance, and his silent demeanor makes him seem more enigmatic than other characters.',
        'Wounded Man': 'The Wounded Man is a character who presents himself with injuries and traumatic past. His wounds give him a distinctive damaged appearance, and his suffering demeanor makes him seem more sympathetic than other characters.'
    }

    return name_mapping.get(base_name, f"The {base_name} is a character with unique characteristics and distinctive features.")

def fix_file(file_path):
    """修正单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = file_path.name
        # 跳过bandana-guy.html，这是正确的页面
        if filename == 'bandana-guy.html':
            return False

        # 生成新的描述
        new_description = get_character_description(filename)

        # 替换主要的错误描述
        old_text = '<p>The Bandana Guy is a visitor who presents himself with a casual, relaxed appearance. His bandana accessory gives him a distinctive look, and his approachable demeanor makes him seem less threatening than other characters.</p>'

        if old_text in content:
            content = content.replace(old_text, f'<p>{new_description}</p>')

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    characters_dir = Path("guide/characters")

    print("🚀 开始批量修正...")

    fixed_count = 0
    total_files = 0

    for html_file in characters_dir.glob("*.html"):
        total_files += 1
        if fix_file(html_file):
            fixed_count += 1
            print(f"✅ 修正完成: {html_file.name}")

    print(f"\n📊 修正结果:")
    print(f"   总文件数: {total_files}")
    print(f"   修正成功: {fixed_count}")
    print(f"   无需修正: {total_files - fixed_count}")

if __name__ == "__main__":
    main()