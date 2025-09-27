#!/bin/bash

# 上传缺失的角色图片到R2

echo "上传缺失的角色图片到R2..."
echo "================================"

cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code"

# 缺失文件列表
files_to_upload=(
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
    "assets/images/characters/Comparison_of_the_image_of_a_nun_and_a_character_from_the_video_Christ_the_Saviour_Ensemble_and_Mother_Earth_Our_icons.png"
)

uploaded_count=0
failed_count=0

for file in "${files_to_upload[@]}"; do
    if [ -f "$file" ]; then
        echo "上传: $file"
        if wrangler r2 object put noimnothuman/"$file" --file "$file" --remote >/dev/null 2>&1; then
            echo "✅ 成功"
            ((uploaded_count++))
        else
            echo "❌ 失败"
            ((failed_count++))
        fi
    else
        echo "❌ 文件不存在: $file"
        ((failed_count++))
    fi
done

echo ""
echo "================================"
echo "上传完成:"
echo "✅ 成功: $uploaded_count 个文件"
echo "❌ 失败: $failed_count 个文件"
echo ""
echo "注意: The_Nun_close_up.jpg 可能需要使用 Comparison_of_the_image_of_a_nun...png 文件"