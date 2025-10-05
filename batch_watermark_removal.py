#!/usr/bin/env python3
import os
from PIL import Image, ImageFilter
import numpy as np

def simple_watermark_removal(image_path, output_path):
    """简单的去水印方法 - 适用于角落小水印"""
    try:
        # 打开图片
        img = Image.open(image_path)

        # 转换为RGB模式
        if img.mode != 'RGB':
            img = img.convert('RGB')

        width, height = img.size

        # 创建一个副本用于处理
        result_img = img.copy()

        # 定义四个角落的区域（各占5%）
        corner_size = int(min(width, height) * 0.05)

        corners = [
            (0, 0, corner_size, corner_size),  # 左上
            (width - corner_size, 0, width, corner_size),  # 右上
            (0, height - corner_size, corner_size, height),  # 左下
            (width - corner_size, height - corner_size, width, height)  # 右下
        ]

        # 对每个角落进行模糊处理（简单的去水印方法）
        for x1, y1, x2, y2 in corners:
            corner = result_img.crop((x1, y1, x2, y2))
            # 使用高斯模糊来淡化水印
            blurred_corner = corner.filter(ImageFilter.GaussianBlur(radius=2))
            result_img.paste(blurred_corner, (x1, y1))

        # 检查底部中央（常见水印位置）
        bottom_height = int(height * 0.1)
        bottom_y = height - bottom_height

        if bottom_height > 10:  # 确保有足够的高度
            bottom_region = result_img.crop((0, bottom_y, width, height))
            blurred_bottom = bottom_region.filter(ImageFilter.GaussianBlur(radius=1))
            result_img.paste(blurred_bottom, (0, bottom_y))

        # 保存处理后的图片
        result_img.save(output_path, 'JPEG', quality=95)
        print(f"✓ 已处理: {os.path.basename(image_path)} -> {os.path.basename(output_path)}")

        return True

    except Exception as e:
        print(f"✗ 处理失败 {image_path}: {e}")
        return False

def process_all_images():
    """批量处理所有图片"""
    input_dirs = ['temp_images/characters', 'temp_images/gameplay']
    output_base = 'temp_images/cleaned'

    # 创建输出目录
    os.makedirs(f'{output_base}/characters', exist_ok=True)
    os.makedirs(f'{output_base}/gameplay', exist_ok=True)

    processed_count = 0
    total_count = 0

    for input_dir in input_dirs:
        if os.path.exists(input_dir):
            output_dir = f'{output_base}/{os.path.basename(input_dir)}'

            for filename in os.listdir(input_dir):
                if filename.endswith('.jpg'):
                    total_count += 1
                    input_path = os.path.join(input_dir, filename)
                    output_path = os.path.join(output_dir, filename)

                    if simple_watermark_removal(input_path, output_path):
                        processed_count += 1

    print(f"\n处理完成: {processed_count}/{total_count} 张图片")

    if processed_count > 0:
        print(f"清洁后的图片保存在: {output_base}")
    else:
        print("没有成功处理的图片")

if __name__ == "__main__":
    process_all_images()