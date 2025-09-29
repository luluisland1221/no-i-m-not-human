#!/usr/bin/env python3
"""
综合网页信息下载脚本
支持多种下载方式和MCP工具集成
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
from urllib.parse import urljoin, urlparse
import re
from typing import Dict, List, Optional, Tuple
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WebDownloader:
    def __init__(self, base_dir: str = "downloaded_content"):
        self.base_dir = base_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

        # 创建基础目录
        os.makedirs(base_dir, exist_ok=True)
        os.makedirs(os.path.join(base_dir, 'images'), exist_ok=True)
        os.makedirs(os.path.join(base_dir, 'text'), exist_ok=True)
        os.makedirs(os.path.join(base_dir, 'json'), exist_ok=True)

    def download_page(self, url: str, method: str = 'requests') -> Dict:
        """
        下载网页内容，支持多种方法
        """
        try:
            if method == 'requests':
                return self._download_with_requests(url)
            else:
                logger.warning(f"不支持的下载方法: {method}")
                return {}
        except Exception as e:
            logger.error(f"下载失败 {url}: {e}")
            return {}

    def _download_with_requests(self, url: str) -> Dict:
        """使用requests下载网页"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # 提取基本信息
            title = soup.find('title')
            title_text = title.get_text().strip() if title else '无标题'

            # 提取主要内容
            content = self._extract_main_content(soup)

            # 提取所有链接
            links = self._extract_links(soup, url)

            # 提取图片
            images = self._extract_images(soup, url)

            result = {
                'url': url,
                'title': title_text,
                'content': content,
                'links': links,
                'images': images,
                'html': str(soup),
                'download_time': time.strftime('%Y-%m-%d %H:%M:%S')
            }

            return result

        except Exception as e:
            logger.error(f"requests下载失败: {e}")
            return {}

    def _extract_main_content(self, soup: BeautifulSoup) -> str:
        """提取网页主要内容"""
        # 尝试找到主要内容区域
        content_selectors = [
            'article',
            'main',
            '.content',
            '#content',
            '.post-content',
            '.entry-content',
            '.mw-parser-output',  # MediaWiki
            'div[role="main"]'
        ]

        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if not main_content:
            main_content = soup.find('body')

        if main_content:
            # 移除不需要的元素
            for element in main_content.find_all(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                element.decompose()

            return main_content.get_text(strip=True)

        return ''

    def _extract_links(self, soup: BeautifulSoup, base_url: str) -> List[Dict]:
        """提取所有链接"""
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)

            # 只提取同域链接
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                links.append({
                    'text': link.get_text().strip(),
                    'url': full_url
                })

        return links[:50]  # 限制链接数量

    def _extract_images(self, soup: BeautifulSoup, base_url: str) -> List[Dict]:
        """提取图片信息"""
        images = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                full_url = urljoin(base_url, src)
                images.append({
                    'src': full_url,
                    'alt': img.get('alt', ''),
                    'title': img.get('title', '')
                })

        return images[:20]  # 限制图片数量

    def download_images(self, images: List[Dict], save_dir: str = None) -> List[str]:
        """下载图片到本地"""
        if save_dir is None:
            save_dir = os.path.join(self.base_dir, 'images')

        downloaded_files = []

        for i, img_info in enumerate(images):
            try:
                src = img_info['src']
                if not src or not src.startswith('http'):
                    continue

                # 生成文件名
                filename = f"image_{i+1}_{os.path.basename(urlparse(src).path)}"
                if not filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    filename += '.jpg'

                filepath = os.path.join(save_dir, filename)

                # 下载图片
                response = self.session.get(src, timeout=30)
                response.raise_for_status()

                with open(filepath, 'wb') as f:
                    f.write(response.content)

                downloaded_files.append(filepath)
                logger.info(f"下载图片: {filename}")

                # 添加延迟避免被封
                time.sleep(1)

            except Exception as e:
                logger.error(f"下载图片失败 {src}: {e}")

        return downloaded_files

    def save_content(self, data: Dict, url: str) -> str:
        """保存内容到文件"""
        try:
            # 生成安全的文件名
            parsed_url = urlparse(url)
            safe_name = re.sub(r'[^\w\s-]', '', parsed_url.netloc + parsed_url.path)
            safe_name = re.sub(r'[-\s]+', '-', safe_name).strip('-')

            base_filename = safe_name or 'page'

            # 保存为JSON
            json_file = os.path.join(self.base_dir, 'json', f"{base_filename}.json")
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            # 保存纯文本
            txt_file = os.path.join(self.base_dir, 'text', f"{base_filename}.txt")
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(f"标题: {data.get('title', '')}\n")
                f.write(f"URL: {data.get('url', '')}\n")
                f.write(f"下载时间: {data.get('download_time', '')}\n")
                f.write("="*50 + "\n\n")
                f.write(data.get('content', ''))

            # 保存HTML
            html_file = os.path.join(self.base_dir, f"{base_filename}.html")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(data.get('html', ''))

            logger.info(f"内容已保存: {base_filename}")
            return json_file

        except Exception as e:
            logger.error(f"保存内容失败: {e}")
            return ""

    def process_fandom_endings(self) -> Dict:
        """专门处理Fandom wiki的endings页面"""
        url = "https://no-i-am-not-a-human.fandom.com/wiki/Endings"

        logger.info(f"开始处理Fandom endings页面: {url}")

        # 下载页面
        data = self.download_page(url)

        if not data:
            logger.error("无法下载页面")
            return {}

        # 专门解析endings信息
        endings_data = self._parse_fandom_endings(data['html'])

        # 下载图片
        if endings_data.get('images'):
            downloaded_images = self.download_images(endings_data['images'])
            endings_data['downloaded_images'] = downloaded_images

        # 保存内容
        saved_file = self.save_content(endings_data, url)

        return {
            'endings_data': endings_data,
            'saved_file': saved_file,
            'url': url
        }

    def _parse_fandom_endings(self, html_content: str) -> Dict:
        """专门解析Fandom endings页面的结构"""
        soup = BeautifulSoup(html_content, 'html.parser')

        endings = []

        # 查找所有endings表格
        tables = soup.find_all('table')

        for table in tables:
            # 检查是否是endings表格
            if any(keyword in table.get_text().lower() for keyword in ['ending', 'requirements', 'text']):
                rows = table.find_all('tr')

                for row in rows[1:]:  # 跳过表头
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 3:
                        ending_info = {
                            'number': cells[0].get_text().strip(),
                            'title': '',
                            'photo': '',
                            'text': cells[1].get_text().strip(),
                            'requirements': cells[2].get_text().strip()
                        }

                        # 尝试提取图片
                        img = cells[0].find('img')
                        if img:
                            ending_info['photo'] = img.get('src', '')
                            ending_info['title'] = img.get('alt', '')

                        endings.append(ending_info)

        # 提取所有图片
        images = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and 'static.wikia.nocookie.net' in src:
                images.append({
                    'src': src,
                    'alt': img.get('alt', ''),
                    'title': img.get('title', '')
                })

        return {
            'endings': endings,
            'images': images,
            'total_endings': len(endings),
            'parse_time': time.strftime('%Y-%m-%d %H:%M:%S')
        }

    def create_summary_report(self, results: Dict) -> str:
        """创建下载总结报告"""
        report = []
        report.append("="*60)
        report.append("网页下载总结报告")
        report.append("="*60)
        report.append(f"目标URL: {results.get('url', '')}")
        report.append(f"处理时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

        endings_data = results.get('endings_data', {})
        report.append(f"发现endings数量: {endings_data.get('total_endings', 0)}")
        report.append(f"发现图片数量: {len(endings_data.get('images', []))}")
        report.append(f"成功下载图片: {len(endings_data.get('downloaded_images', []))}")

        # 详细endings信息
        report.append("\n发现的Endings:")
        for i, ending in enumerate(endings_data.get('endings', [])[:5], 1):
            report.append(f"{i}. {ending.get('title', '无标题')}")
            report.append(f"   要求: {ending.get('requirements', '未知')[:100]}...")

        if len(endings_data.get('endings', [])) > 5:
            report.append(f"   ... 还有 {len(endings_data.get('endings', [])) - 5} 个endings")

        report.append("\n保存的文件:")
        report.append(f"- JSON数据: {results.get('saved_file', '')}")

        report_text = "\n".join(report)

        # 保存报告
        report_file = os.path.join(self.base_dir, 'download_report.txt')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_text)

        return report_text

def main():
    """主函数"""
    print("开始下载网页信息...")

    # 创建下载器
    downloader = WebDownloader("G:\\ai编程\\100个网站\\07 noimnothuman.xyz\\参考资料\\fandom_endings")

    # 处理Fandom endings页面
    results = downloader.process_fandom_endings()

    if results:
        # 生成报告
        report = downloader.create_summary_report(results)
        print("\n" + report)

        print(f"\n下载完成！文件保存在: {downloader.base_dir}")
    else:
        print("下载失败！")

if __name__ == "__main__":
    main()