#!/bin/bash

# 检查并上传缺失的characters图片
echo "开始检查并上传缺失的characters图片..."

cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code\assets\images\characters"

missing_files=()
total_files=0
uploaded_count=0
missing_count=0

echo "检查每个文件是否存在于R2存储桶中..."
echo "============================================"

for file in *; do
    if [ -f "$file" ]; then
        total_files=$((total_files + 1))

        # 检查文件是否存在于R2中
        if wrangler r2 object get noimnothuman/assets/images/characters/"$file" --file /dev/null --remote >/dev/null 2>&1; then
            echo "✅ $file (已存在)"
        else
            echo "❌ $file (缺失，正在上传...)"
            missing_files+=("$file")
            missing_count=$((missing_count + 1))

            # 上传文件
            if wrangler r2 object put noimnothuman/assets/images/characters/"$file" --file "$file" --remote >/dev/null 2>&1; then
                echo "   → 上传成功"
                uploaded_count=$((uploaded_count + 1))
            else
                echo "   → 上传失败！"
            fi
        fi
    fi
done

echo ""
echo "============================================"
echo "检查完成！"
echo "总文件数: $total_files"
echo "缺失文件数: $missing_count"
echo "成功上传: $uploaded_count"
echo ""

if [ $missing_count -gt 0 ]; then
    echo "以下文件之前不存在，现在已经上传："
    for file in "${missing_files[@]}"; do
        echo "  - $file"
    done
else
    echo "所有文件都已存在于R2存储桶中！"
fi