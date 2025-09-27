#!/bin/bash

# 修复R2图片链接，使用R2默认域名

echo "修复R2图片链接..."

# 由于自定义域名可能还没有生效，我们先用R2的默认域名
# 但我们需要先获取账户ID来构建正确的URL

# 备份当前文件
cp index.html index.html.cdn
cp guide.html guide.html.cdn

echo "已备份当前HTML文件"
echo "请手动配置以下两项："
echo ""
echo "1. 在Cloudflare控制台为R2存储桶配置自定义域名 images.noimnothuman.xyz"
echo "2. 或者使用R2默认域名（需要账户ID）"
echo ""
echo "临时解决方案："
echo "你可以暂时使用相对路径，让图片从本地加载，直到R2自定义域名配置完成"