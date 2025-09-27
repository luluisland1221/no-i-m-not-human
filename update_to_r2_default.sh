#!/bin/bash

# 使用R2默认域名更新图片链接

R2_DOMAIN="https://noimnothuman.d49fda2b529b2cbde6bc93aaf69ca473.r2.dev"

echo "使用R2默认域名更新图片链接..."
echo "R2域名: $R2_DOMAIN"

# 备份当前文件
cp index.html index.html.local
cp guide.html guide.html.local

echo "已备份当前HTML文件"

# 更新index.html中的图片链接
echo "更新index.html..."
sed -i "s|src=\"images\.jpg\"|src=\"$R2_DOMAIN/images.jpg\"|g" index.html
sed -i "s|src=\"assets/images/|src=\"$R2_DOMAIN/assets/images/|g" index.html

# 更新guide.html中的图片链接
echo "更新guide.html..."
sed -i "s|src=\"assets/images/|src=\"$R2_DOMAIN/assets/images/|g" guide.html

echo "图片链接已更新为R2默认域名"
echo ""
echo "现在你可以测试："
echo "- 本地打开 index.html 查看图片是否显示"
echo "- 访问: $R2_DOMAIN/images.jpg"
echo ""
echo "如果自定义域名配置完成后，运行此脚本恢复自定义域名："
echo "sed -i \"s|$R2_DOMAIN|https://images.noimnothuman.xyz|g\" index.html guide.html"