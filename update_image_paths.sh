#!/bin/bash

# 批量更新HTML文件中的图片路径为R2 CDN地址

echo "开始更新HTML文件中的图片路径..."

# 定义新的CDN基础URL
CDN_BASE="https://images.noimnothuman.xyz"

# 更新index.html
echo "更新 index.html..."
sed -i "s|src=\"images\.jpg\"|src=\"$CDN_BASE/images.jpg\"|g" index.html
sed -i "s|src=\"assets/images/|src=\"$CDN_BASE/assets/images/|g" index.html

# 更新guide.html
echo "更新 guide.html..."
sed -i "s|src=\"assets/images/|src=\"$CDN_BASE/assets/images/|g" guide.html

echo "图片路径更新完成！"
echo "新的图片地址格式: https://images.noimnothuman.xyz/assets/images/..."