#!/usr/bin/env python3
import csv
import re
import os

def process_characters_csv():
    """处理Characters.csv并更新所有角色图片"""

    # 读取CSV文件
    characters = []
    with open('G:/ai编程/100个网站/07 noimnothuman.xyz/参考资料/Characters.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过标题行
        for row in reader:
            if len(row) >= 2:
                character_name = row[0].strip()
                image_url = row[1].strip() if len(row) > 1 and row[1].strip() else ""
                if character_name:
                    characters.append((character_name, image_url))

    print(f"从CSV读取了 {len(characters)} 个角色")

    # 读取HTML文件
    with open('G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 创建角色名到图片文件的映射
    char_to_image = {
        "Wounded Man": "WOUNDED_MAN_-_VISITOR_-_TEETH.png",
        "Wireface": "Wireface-close.png",
        "Widowed Woman": "Go_girl_go.png",
        "Vigilante": "TheVigilante.png",
        "Theorist": "VRcloseup.jpg",
        "The Sisters": "TheSisters.jpg",
        "Sweaty Man": "Swclose.jpg",
        "Surgeon": "SurgeonCloseUp.jpg",
        "Sun Guy": "SunGuyCloseUp.jpg",
        "Suit Guy": "Suitguy1.png",
        "Stoner": "Stoner-close.png",
        "Stand Up Guy": "Standupguyclose.jpg",
        "Seductive Woman": "Seductive_Woman_-_close_up.jpg",
        "Positive Guy": "Positive_Guy_close_up.jpg",
        "Parentless Teenager": "Noimnotahumancharacter1-full.png",
        "Old Lady": "Oldladycloseup.jpg",
        "Nun": "The_Nun_(close_up).png",
        "Nikita the Wind, Based Intruder": "Nikita_front.jpg",
        "Neighbor": "Neighbour1.jpg",
        "Neglectful Mother": "Mother.png",
        "Music Conductor": "Gangrene_Conductor.png",
        "Little Girl": "Girl_eyes.jpg",
        "Kindergarten Teacher": "Glasses_Woman.png",
        "Immortal Man": "Yakobclose.jpg",
        "Husband and Wife": "Husband_and_Wife_Close_Up.png",
        "Homeless Man": "Hobocloseup.jpg",
        "Gravedigger": "Grave_digger_closeup.jpg",
        "Fortune Teller": "FortuneTeller.png",
        "Factory Guy": "Factoryguyclose.jpg",
        "Disfigured Guy": "Disfigured_guy.png",
        "Death Cult Peons": "Peon1close.jpg",
        "Coat Guy": "Ignore_the_ugly_guy_at_the_back.png",
        "Cheerful Man": "Cheerfulmanclose.jpg",
        "Cat Lady": "Ball-arena-close.png",
        "Cashier Girl": "Cashier_gal.png",
        "Cabby Man": "Cabbymanclose.jpg",
        "Border Patrol Agent": "Bpaclose.jpg",
        "Blinded Man": "Blindedmanclose.jpg",
        "Big Momma": "Woman1.png",
        "Best Son": "Bestsonclose.jpg",
        "Bearded Guy": "BeardedGuyCloseUp.jpg",
        "Bar Guy": "BarGuyCloseUp.jpg",
        "Bandana Guy": "Ymipclose.jpg",
        "Armchair Lawyer Guy": "Lawguycloseup.jpg",
        "Angry Guy": "AngryGuy.png",
        "Amogus Guy": "AmogusGuyCloseUp.jpg"
    }

    # 更新计数器
    updated_count = 0

    # 为每个角色添加图片
    for char_name, _ in characters:
        # 查找角色在HTML中的位置
        pattern = f'<div class="compact-character-item">\\s*<span class="char-name">{re.escape(char_name)}</span>\\s*<span class="char-trait">([^<]+)</span>\\s*</div>'

        # 检查是否已经有图片
        img_check_pattern = f'<div class="compact-character-item">\\s*<img[^>]*alt="{re.escape(char_name)}"[^>]*>\\s*<span class="char-name">{re.escape(char_name)}</span>'
        if re.search(img_check_pattern, content):
            print(f"✓ {char_name} 已有图片")
            continue

        # 找到对应的图片文件
        image_file = None
        for name, filename in char_to_image.items():
            if char_name in name or name in char_name:
                image_file = filename
                break

        if not image_file:
            # 尝试从文件名直接匹配
            simple_name = char_name.replace(" ", "").replace("'", "").replace(",", "").replace('"', "")
            possible_files = [
                f"{simple_name}.png", f"{simple_name}.jpg",
                f"{char_name.replace(' ', '_')}.png", f"{char_name.replace(' ', '_')}.jpg",
                f"{char_name.replace(' ', '')}.png", f"{char_name.replace(' ', '')}.jpg"
            ]

            for possible_file in possible_files:
                if os.path.exists(f"G:/ai编程/100个网站/07 noimnothuman.xyz/code/assets/images/characters/{possible_file}"):
                    image_file = possible_file
                    break

        if not image_file:
            print(f"✗ 未找到 {char_name} 的图片文件")
            continue

        # 构建替换内容
        replacement = f'''<div class="compact-character-item">
                            <img src="assets/images/characters/{image_file}" alt="{char_name}" class="char-image">
                            <span class="char-name">{char_name}</span>
                            <span class="char-trait">\\1</span>
                        </div>'''

        # 执行替换
        new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

        if new_content != content:
            content = new_content
            updated_count += 1
            print(f"✓ 添加了 {char_name} 的图片: {image_file}")
        else:
            print(f"- {char_name} 未找到或已有图片")

    # 保存文件
    with open('G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n总共更新了 {updated_count} 个角色的图片")

    # 统计最终状态
    final_count = content.count('char-image')
    print(f"当前有图片的角色数: {final_count}")

if __name__ == "__main__":
    process_characters_csv()