#!/bin/bash

# 自动更新sitemap.txt的脚本
# 扫描所有HTML文件并生成sitemap.txt

BASE_URL="https://noimnothuman.xyz"
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITEMAP_FILE="$CURRENT_DIR/sitemap.txt"

echo "🔄 正在生成sitemap.txt..."

# 查找所有HTML文件，排除node_modules目录
find "$CURRENT_DIR" -name "*.html" -not -path "*/node_modules/*" | sort | while read -r html_file; do
    # 转换为相对路径
    relative_path="${html_file#$CURRENT_DIR/}"

    # 处理根目录的index.html
    if [[ "$relative_path" == "index.html" ]]; then
        url="$BASE_URL/"
    else
        # 转换路径为URL格式，替换反斜杠
        url_path=$(echo "$relative_path" | sed 's/\\/\//g')
        url="$BASE_URL/$url_path"
    fi

    echo "$url"
done > "$SITEMAP_FILE"

# 统计URL数量
URL_COUNT=$(wc -l < "$SITEMAP_FILE")

echo "✅ sitemap.txt已更新，共$URL_COUNT个URL"
echo "🎯 成功生成sitemap.txt，包含$URL_COUNT个页面"