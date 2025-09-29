# 网页信息下载工具指南

## 可用的MCP工具

### 1. Web Fetch 工具
- **mcp__web-fetch__fetch_txt**: 获取网页纯文本内容
- **mcp__web-fetch__fetch_html**: 获取网页HTML内容
- **mcp__web-fetch__fetch_markdown**: 获取网页Markdown格式内容
- **mcp__web-fetch__fetch_json**: 获取网页JSON数据

### 2. Web Search 工具
- **mcp__web-search__google_search**: Google搜索
- **mcp__bing-search__bing_search**: Bing搜索
- **mcp__bing-search__fetch_webpage**: 根据搜索结果ID获取网页内容

### 3. Browser Automation 工具
- **mcp__playwright__browser_navigate**: 浏览器导航
- **mcp__playwright__browser_snapshot**: 获取页面快照
- **mcp__playwright__browser_evaluate**: 执行JavaScript
- **mcp__puppeteer__puppeteer_navigate**: Puppeteer导航

### 4. 文件系统工具
- **mcp__filesystem__read_text_file**: 读取文本文件
- **mcp__filesystem__write_file**: 写入文件
- **mcp__filesystem__list_directory**: 列出目录内容

## 已创建的脚本

### 1. Bash脚本 (推荐使用)

#### download_fandom.sh
下载Fandom wiki的endings页面
```bash
bash download_fandom.sh
```

#### download_fandom_images.sh
下载Fandom wiki的endings相关图片
```bash
bash download_fandom_images.sh
```

### 2. Python脚本

#### simple_downloader.py
Python版本的网页下载器
```bash
python simple_downloader.py
```

#### web_downloader.py
功能更完整的Python下载器
```bash
python web_downloader.py
```

## 使用示例

### 1. 使用MCP工具获取网页内容
```python
# 通过Claude Code使用MCP工具
# 1. 获取纯文本内容
mcp__web-fetch__fetch_txt(url="https://no-i-am-not-a-human.fandom.com/wiki/Endings")

# 2. 获取HTML内容
mcp__web-fetch__fetch_html(url="https://no-i-am-not-a-human.fandom.com/wiki/Endings")

# 3. 获取Markdown内容
mcp__web-fetch__fetch_markdown(url="https://no-i-am-not-a-human.fandom.com/wiki/Endings")

# 4. 使用浏览器导航
mcp__playwright__browser_navigate(url="https://no-i-am-not-a-human.fandom.com/wiki/Endings")
```

### 2. 使用搜索功能
```python
# Google搜索
mcp__web-search__google_search(q="No, I'm not a Human game endings", gl="us", hl="en")

# Bing搜索
mcp__bing-search__bing_search(query="No, I'm not a Human endings guide")
```

## 下载结果

### 成功下载的内容
- ✅ Fandom wiki endings页面 (226KB HTML文件)
- ✅ 19张相关图片
- ✅ 完整的图片链接列表

### 文件位置
- 页面HTML: `G:\ai编程\100个网站\07 noimnothuman.xyz\参考资料\fandom_endings\endings_page.html`
- 图片链接: `G:\ai编程\100个网站\07 noimnothuman.xyz\参考资料\fandom_endings\image_links.txt`
- 下载的图片: `G:\ai编程\100个网站\07 noimnothuman.xyz\参考资料\fandom_endings\images\`

## 工具比较

| 工具类型 | 优点 | 缺点 | 适用场景 |
|---------|------|------|----------|
| Bash + curl | 简单可靠，速度快 | 功能有限，需要手动解析 | 快速下载文件 |
| Python脚本 | 功能强大，可扩展 | 需要依赖库 | 复杂的数据提取 |
| MCP工具 | 集成性好，功能丰富 | 有token限制 | 实时交互式操作 |
| Browser工具 | 可处理动态内容 | 速度较慢 | JavaScript渲染页面 |

## 建议

1. **简单下载**: 使用Bash脚本，快速可靠
2. **数据提取**: 使用Python脚本，功能强大
3. **实时操作**: 使用MCP工具，交互式操作
4. **复杂页面**: 使用Browser工具，处理JavaScript

## 注意事项

1. 某些MCP工具可能存在token限制，特别是HTML内容可能超过限制
2. 下载时注意设置适当的User-Agent，避免被拒绝
3. 添加适当的延迟，避免被封IP
4. 尊重网站的robots.txt规则

## 下一步

1. 分析下载的内容，提取endings信息
2. 将图片上传到R2存储桶
3. 更新网站内容
4. 创建更多游戏相关的下载脚本