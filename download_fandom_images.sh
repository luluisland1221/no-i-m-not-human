#!/bin/bash

# 下载Fandom wiki的endings图片
echo "开始下载Fandom endings图片..."

IMAGE_LINKS_FILE="G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\参考资料\\fandom_endings\\image_links.txt"
SAVE_DIR="G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\参考资料\\fandom_endings\\images"

# 创建保存目录
mkdir -p "$SAVE_DIR"

if [ ! -f "$IMAGE_LINKS_FILE" ]; then
    echo "找不到图片链接文件: $IMAGE_LINKS_FILE"
    echo "请先运行 download_fandom.sh"
    exit 1
fi

# 读取图片链接并下载
echo "正在下载图片..."
cd "$SAVE_DIR"

# 计数器
COUNTER=0
SUCCESS_COUNT=0

while IFS= read -r url; do
    if [ -n "$url" ]; then
        COUNTER=$((COUNTER + 1))

        # 生成文件名
        # 从URL中提取文件名
        filename=$(basename "$url" | cut -d'?' -f1)

        # 如果没有扩展名，添加.jpg
        if [[ "$filename" != *"."* ]]; then
            filename="image_${COUNTER}.jpg"
        fi

        # 清理文件名
        filename=$(echo "$filename" | sed 's/[^a-zA-Z0-9._-]/_/g')

        echo "下载图片 $COUNTER: $filename"

        # 使用curl下载图片
        if curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
           -L -s -o "$filename" "$url"; then

            # 检查文件是否成功下载
            if [ -f "$filename" ] && [ -s "$filename" ]; then
                SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
                echo "  ✓ 下载成功"
            else
                echo "  ✗ 下载失败（文件为空）"
                rm -f "$filename"
            fi
        else
            echo "  ✗ 下载失败"
        fi

        # 添加延迟避免被封
        sleep 1
    fi
done < "$IMAGE_LINKS_FILE"

echo ""
echo "下载完成！"
echo "总图片数: $COUNTER"
echo "成功下载: $SUCCESS_COUNT"
echo "失败: $((COUNTER - SUCCESS_COUNT))"
echo ""
echo "图片保存在: $SAVE_DIR"

# 列出下载的文件
echo ""
echo "下载的文件:"
ls -la "$SAVE_DIR" | grep -E "\.(jpg|jpeg|png|gif|webp)$"