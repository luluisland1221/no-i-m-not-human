#!/bin/bash

# 下载Fandom wiki的endings页面
echo "开始下载Fandom endings页面..."

URL="https://no-i-am-not-a-human.fandom.com/wiki/Endings"
SAVE_DIR="G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\参考资料\\fandom_endings"

# 创建保存目录
mkdir -p "$SAVE_DIR"

# 使用curl下载页面
echo "正在下载页面..."
curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
     -L -s "$URL" > "$SAVE_DIR/endings_page.html"

if [ $? -eq 0 ]; then
    echo "页面下载成功！"
    echo "文件保存在: $SAVE_DIR/endings_page.html"

    # 统计文件大小
    FILE_SIZE=$(wc -c < "$SAVE_DIR/endings_page.html")
    echo "文件大小: $FILE_SIZE 字节"

    # 检查是否包含endings内容
    if grep -q "ending" "$SAVE_DIR/endings_page.html"; then
        echo "文件中包含endings相关内容"
    else
        echo "警告: 文件中可能没有找到endings内容"
    fi

    # 提取所有图片链接
    echo ""
    echo "正在提取图片链接..."
    grep -o 'src="[^"]*static\.wikia\.nocookie\.net[^"]*"' "$SAVE_DIR/endings_page.html" | \
        sed 's/src="//g' | sed 's/"//g' | sort | uniq > "$SAVE_DIR/image_links.txt"

    IMAGE_COUNT=$(wc -l < "$SAVE_DIR/image_links.txt")
    echo "找到 $IMAGE_COUNT 张图片"
    echo "图片链接保存在: $SAVE_DIR/image_links.txt"

    # 显示前5个图片链接
    echo ""
    echo "前5个图片链接:"
    head -5 "$SAVE_DIR/image_links.txt"

else
    echo "下载失败！"
    exit 1
fi

echo ""
echo "下载完成！"