#!/bin/bash

# 检查缺失的角色图片文件

echo "检查缺失的角色图片文件..."
echo "================================"

# 从guide.html提取所有角色图片引用
cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code"

echo "以下角色图片在R2中缺失："
echo ""

# 检查你提到的特定缺失文件
missing_files=(
    "assets/images/characters/StandUpGuy.jpg"
    "assets/images/characters/SunGuyCloseUp.jpg"
    "assets/images/characters/Swclose.jpg"
    "assets/images/characters/Suitguy1.png"
    "assets/images/characters/SurgeonCloseUp.jpg"
    "assets/images/characters/TheSisters.jpg"
    "assets/images/characters/Stoner-close.png"
    "assets/images/characters/VRcloseup.jpg"
    "assets/images/characters/TheVigilante.png"
    "assets/images/characters/Weather_Man.jpg"
    "assets/images/characters/The_Miner.jpg"
    "assets/images/characters/The_Nun_close_up.jpg"
)

for file in "${missing_files[@]}"; do
    if wrangler r2 object get noimnothuman/"$file" --file /dev/null --remote >/dev/null 2>&1; then
        echo "✅ $file - 存在"
    else
        echo "❌ $file - 缺失"
    fi
done

echo ""
echo "================================"
echo "请检查本地是否包含这些缺失的图片文件"
echo "如果本地有这些文件，我可以帮你上传到R2"