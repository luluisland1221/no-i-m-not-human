#!/bin/bash

# 批量上传剩余的角色图片到 R2
cd "G:\ai编程\100个网站\07 noimnothuman.xyz\code\assets\images\characters"

# 获取所有文件并跳过已上传的前100个
files=($(ls | tail -n +101))

total=${#files[@]}
echo "总共需要上传 $total 个文件"

# 分批上传，每批50个文件
for ((i=0; i<total; i+=50)); do
    batch=("${files[@]:$i:50}")
    batch_size=${#batch[@]}

    echo "上传第 $((i/50 + 1)) 批，共 $batch_size 个文件..."

    for file in "${batch[@]}"; do
        if [ -f "$file" ]; then
            echo "正在上传: $file"
            wrangler r2 object put noimnothuman/assets/images/characters/"$file" --file "$file"
            if [ $? -eq 0 ]; then
                echo "✅ $file 上传成功"
            else
                echo "❌ $file 上传失败"
            fi
        fi
    done

    echo "第 $((i/50 + 1)) 批完成"
    echo "----------------------------------------"

    # 添加短暂延迟避免请求过快
    sleep 2
done

echo "所有文件上传完成！"