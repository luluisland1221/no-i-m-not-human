# PowerShell script to batch update character guide footers

# 设置工作目录
Set-Location "G:\ai编程\100个网站\07 noimnothuman.xyz\code\guide\characters"

# 需要更新的文件列表（排除已经完成的文件）
$completedFiles = @("angry-guy.html", "armchair-lawyer-guy.html", "bandana-guy.html", "bar-guy.html", "bearded-guy.html")
$allFiles = Get-ChildItem -Filter "*.html" | Select-Object -ExpandProperty Name
$filesToUpdate = $allFiles | Where-Object { $_ -notin $completedFiles }

Write-Host "开始更新 $($filesToUpdate.Count) 个角色指南页面..." -ForegroundColor Green

$updatedCount = 0
$totalCount = $filesToUpdate.Count

foreach ($file in $filesToUpdate) {
    $updatedCount++
    Write-Host "[$updatedCount/$totalCount] 正在更新: $file" -ForegroundColor Yellow

    try {
        # 读取文件内容
        $content = Get-Content -Path $file -Raw -Encoding UTF8

        # 定义替换模式
        $oldPattern = '(?s)<div class="footer-section">\s*<h4>Quick Links</h4>.*?<li><a href="\.\.\/community\.html">Community</a></li>\s*</ul>\s*</div>'

        $newContent = '<div class="footer-section">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../characters.html">Characters</a></li>
                    <li><a href="../achievements.html">Achievements</a></li>
                    <li><a href="../ending.html">Endings</a></li>
                    <li><a href="../download.html">Download</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Game Content</h4>
                <ul>
                    <li><a href="../characters.html">Character Identification Guide</a></li>
                    <li><a href="../achievements.html">Complete Achievement List</a></li>
                    <li><a href="../ending.html">All Game Endings</a></li>
                    <li><a href="https://store.steampowered.com/app/3180070/No_Im_not_a_Human/" target="_blank">Steam Store</a></li>
                </ul>
            </div>'

        # 检查是否需要更新
        if ($content -match "Resources") {
            # 执行替换
            $content = $content -replace $oldPattern, $newContent

            # 写回文件
            Set-Content -Path $file -Value $content -Encoding UTF8
            Write-Host "✓ 已更新: $file" -ForegroundColor Green
        } else {
            Write-Host "- 跳过: $file (已经是正确格式)" -ForegroundColor Gray
        }

    } catch {
        Write-Host "✗ 错误处理文件 $file : $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "`n批量更新完成!" -ForegroundColor Cyan
Write-Host "已处理的文件数: $updatedCount/$totalCount" -ForegroundColor Cyan