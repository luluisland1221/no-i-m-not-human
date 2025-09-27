#!/bin/bash

# 批量上传所有图片到远程R2存储桶
echo "开始上传图片到远程R2存储桶..."

# 上传主要图片
echo "上传主要图片..."
cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code"
if [ -f "images.jpg" ]; then
    wrangler r2 object put noimnothuman/images.jpg --file images.jpg --remote
    echo "✅ images.jpg 上传完成"
fi

# 上传achievements图片
echo "上传achievements图片..."
cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code\assets\images\achievements"
for file in *; do
    if [ -f "$file" ]; then
        echo "上传: $file"
        wrangler r2 object put noimnothuman/assets/images/achievements/"$file" --file "$file" --remote
        echo "✅ $file 上传完成"
    fi
done

# 上传characters图片（分批进行）
echo "上传characters图片..."
cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code\assets\images\characters"

# 获取所有文件
files=(*)
total=${#files[@]}
echo "总共需要上传 $total 个characters图片"

# 分批上传，每批20个文件
for ((i=0; i<total; i+=20)); do
    batch=("${files[@]:$i:20}")
    batch_size=${#batch[@]}

    echo "上传第 $((i/20 + 1)) 批，共 $batch_size 个文件..."

    for file in "${batch[@]}"; do
        if [ -f "$file" ]; then
            echo "正在上传: $file"
            wrangler r2 object put noimnothuman/assets/images/characters/"$file" --file "$file" --remote
            if [ $? -eq 0 ]; then
                echo "✅ $file 上传成功"
            else
                echo "❌ $file 上传失败"
            fi
        fi
    done

    echo "第 $((i/20 + 1)) 批完成"
    echo "----------------------------------------"
    sleep 1  # 短暂延迟避免请求过快
done

echo "所有图片上传完成！"
echo "请在Cloudflare控制台中检查noimnothuman存储桶的内容。"