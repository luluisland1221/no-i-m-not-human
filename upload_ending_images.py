#!/usr/bin/env python3
"""
上传结局图片到R2存储桶的脚本
"""

import os
import sys
from pathlib import Path
import subprocess

def upload_ending_images():
    """上传结局图片到R2"""

    # R2配置
    r2_bucket = "noimnothuman-images"
    r2_path = "endings/"

    # 本地图片目录
    current_dir = Path(__file__).parent
    images_dir = current_dir / "ending_images"

    if not images_dir.exists():
        print("❌ ending_images 目录不存在")
        return False

    print("📤 上传结局图片到R2存储桶...")
    print(f"🪣 存储桶: {r2_bucket}")
    print(f"📂 路径: {r2_path}")

    # 获取所有图片文件
    image_files = list(images_dir.glob("*.png")) + list(images_dir.glob("*.jpg"))

    if not image_files:
        print("❌ 没有找到图片文件")
        return False

    success_count = 0
    total_count = len(image_files)

    for image_file in image_files:
        print(f"\n📸 上传: {image_file.name}")

        # 构建R2路径
        r2_full_path = f"{r2_path}{image_file.name}"

        # 执行wrangler命令
        cmd = [
            "wrangler", "r2", "object", "put",
            f"{r2_bucket}/{r2_full_path}",
            "--file", str(image_file)
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ 上传成功: {image_file.name}")
            success_count += 1
        except subprocess.CalledProcessError as e:
            print(f"❌ 上传失败: {image_file.name}")
            print(f"错误: {e.stderr}")
        except FileNotFoundError:
            print("❌ wrangler命令未找到，请确保已安装Wrangler")
            return False

    print(f"\n📊 上传完成: {success_count}/{total_count}")

    if success_count > 0:
        print("\n🌐 R2图片链接格式:")
        for i in range(1, 11):
            print(f"https://images.noimnothuman.xyz/{r2_path}ending_{i}.png")

    return success_count > 0

def main():
    """主函数"""
    print("🎮 No, I'm not a Human - R2图片上传工具")
    print("=" * 50)

    if upload_ending_images():
        print("\n✅ 图片上传完成！")
        print("现在可以创建 ending.html 页面了")
    else:
        print("\n❌ 图片上传失败")
        sys.exit(1)

if __name__ == "__main__":
    main()