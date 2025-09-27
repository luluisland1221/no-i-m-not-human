# R2 自定义域名配置指南

## 问题诊断
当前网站图片无法显示，因为R2自定义域名 `images.noimnothuman.xyz` 还没有正确配置。

## 解决方案

### 方案1：配置R2自定义域名（推荐）

#### 步骤1：在Cloudflare控制台配置自定义域名
1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com)
2. 选择你的域名 `noimnothuman.xyz`
3. 进入 "R2" 服务
4. 选择存储桶 `noimnothuman`
5. 点击 "设置" -> "自定义域名"
6. 添加自定义域名：`images.noimnothuman.xyz`
7. 按照提示完成DNS配置

#### 步骤2：配置DNS记录
在DNS设置中添加：
```
类型: CNAME
名称: images
内容: 你的R2端点（Cloudflare会提供）
代理状态: 已代理（橙色云）
```

#### 步骤3：验证配置
配置完成后，访问：`https://images.noimnothuman.xyz/images.jpg`
应该能看到图片正常显示。

### 方案2：使用R2默认域名（推荐临时解决方案）

如果自定义域名配置有问题，可以使用R2默认域名：

1. 你的Cloudflare账户ID：`d49fda2b529b2cbde6bc93aaf69ca473`
2. R2默认域名格式：`<bucket-name>.<account-id>.r2.dev`
3. 你的R2默认域名：`noimnothuman.d49fda2b529b2cbde6bc93aaf69ca473.r2.dev`

**立即可用的测试链接：**
- `https://noimnothuman.d49fda2b529b2cbde6bc93aaf69ca473.r2.dev/images.jpg`
- `https://noimnothuman.d49fda2b529b2cbde6bc93aaf69ca473.r2.dev/assets/images/achievements/Breakfast_of_Champions.jpg`

### 方案3：临时使用本地图片

当前已经回退到本地图片路径，网站应该可以正常显示。

## 完成后的操作

当R2自定义域名配置完成后：

1. 重新运行图片路径更新脚本
2. 删除本地的图片文件
3. 提交更改到GitHub

## 验证步骤

配置完成后，测试以下URL是否可访问：
- `https://images.noimnothuman.xyz/images.jpg`
- `https://images.noimnothuman.xyz/assets/images/achievements/Breakfast_of_Champions.jpg`
- `https://images.noimnothuman.xyz/assets/images/characters/DeliveryMan.png`

## 常见问题

1. **自定义域名不生效**：检查DNS配置和Cloudflare代理状态
2. **图片404错误**：确认文件路径在R2中存在
3. **SSL证书问题**：等待Cloudflare自动签发证书（通常需要几分钟到几小时）

## 当前状态

- ✅ R2存储桶已创建并包含291个文件（191MB）
- ✅ 所有图片已上传到R2
- ❌ 自定义域名还未配置
- ✅ 网站暂时使用本地图片路径