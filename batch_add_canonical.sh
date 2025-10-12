#!/bin/bash

# 设置路径
CHARACTERS_DIR="G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide/characters"

echo "开始为所有角色页面添加canonical URL..."

count=0
success=0

# 遍历所有HTML文件
for file in "$CHARACTERS_DIR"/*.html; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        count=$((count + 1))

        echo "处理: $filename"

        # 检查是否已经有canonical URL
        if grep -q 'rel="canonical"' "$file"; then
            echo "  ✅ 已有canonical URL，跳过"
            success=$((success + 1))
            continue
        fi

        # 添加canonical URL
        canonical_url="https://noimnothuman.xyz/guide/characters/$filename"

        # 在第7行后插入canonical URL
        sed -i "7a\\    <link rel=\"canonical\" href=\"$canonical_url\">" "$file"

        # 验证是否添加成功
        if grep -q 'rel="canonical"' "$file"; then
            echo "  ✅ 成功添加canonical URL"
            success=$((success + 1))
        else
            echo "  ❌ 添加失败"
        fi
    fi
done

echo ""
echo "📊 处理完成:"
echo "   总文件数: $count"
echo "   成功处理: $success"
echo "   失败数量: $((count - success))"