#!/bin/bash

# 使用自定义域名更新图片链接

CUSTOM_DOMAIN="https://images.noimnothuman.xyz"

echo "使用自定义域名更新图片链接..."
echo "自定义域名: $CUSTOM_DOMAIN"

# 备份当前文件
cp index.html index.html.r2-default
cp guide.html guide.html.r2-default

echo "已备份当前HTML文件"

# 更新index.html中的图片链接
echo "更新index.html..."
sed -i "s|https://noimnothuman\.d49fda2b529b2cbde6bc93aaf69ca473\.r2\.dev|$CUSTOM_DOMAIN|g" index.html

# 更新guide.html中的图片链接
echo "更新guide.html..."
sed -i "s|https://noimnothuman\.d49fda2b529b2cbde6bc93aaf69ca473\.r2\.dev|$CUSTOM_DOMAIN|g" guide.html

echo "图片链接已更新为自定义域名"
echo ""
echo "更新后的图片URL示例："
echo "- $CUSTOM_DOMAIN/images.jpg"
echo "- $CUSTOM_DOMAIN/assets/images/characters/DeliveryMan.png"
echo "- $CUSTOM_DOMAIN/assets/images/achievements/Breakfast_of_Champions.jpg"
echo ""
echo "请先测试自定义域名是否可以访问："
echo "curl -I $CUSTOM_DOMAIN/images.jpg"