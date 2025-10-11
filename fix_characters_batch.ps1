# 角色页面基本信息批量修复脚本
# 修复所有角色页面中错误的"Bandana Guy"信息

$characterMapping = @{
    'angry-guy.html' = 'Angry Guy'
    'armchair-lawyer-guy.html' = 'Armchair Lawyer Guy'
    'bar-guy.html' = 'Bar Guy'
    'bearded-guy.html' = 'Bearded Guy'
    'best-son.html' = 'Best Son'
    'big-momma.html' = 'Big Momma'
    'blinded-man.html' = 'Blinded Man'
    'blonde-guy.html' = 'Blonde Guy'
    'border-patrol-agent.html' = 'Border Patrol Agent'
    'brunette-guy.html' = 'Brunette Guy'
    'cabby-man.html' = 'Cabby Man'
    'cashier-girl.html' = 'Cashier Girl'
    'cat-lady.html' = 'Cat Lady'
    'cheerful-man.html' = 'Cheerful Man'
    'child.html' = 'Child'
    'coat-guy.html' = 'Coat Guy'
    'cozy-man.html' = 'Cozy Man'
    'death.html' = 'Death'
    'death-cult-leader.html' = 'Death Cult Leader'
    'death-cult-peon.html' = 'Death Cult Peons'
    'delivery-man.html' = 'Delivery Man'
    'delivery-man-backup.html' = 'Delivery Man Backup'
    'disfigured-guy.html' = 'Disfigured Guy'
    'egghead-guy.html' = 'Egghead Guy'
    'factory-guy.html' = 'Factory Guy'
    'fema-agent.html' = 'FEMA Agent'
    'fetus.html' = 'Fetus'
    'fortune-teller.html' = 'Fortune Teller'
    'gravedigger.html' = 'Gravedigger'
    'homeless-man.html' = 'Homeless Man'
    'husband-and-wife.html' = 'Husband and Wife'
    'immortal-man.html' = 'Immortal Man'
    'intruder.html' = 'Intruder'
    'kindergarten-teacher.html' = 'Kindergarten Teacher'
    'little-girl.html' = 'Little Girl'
    'miner.html' = 'Miner'
    'mushroom-man.html' = 'Mushroom Man'
    'music-conductor.html' = 'Music Conductor'
    'neglectful-mother.html' = 'Neglectful Mother'
    'neighbor.html' = 'Neighbor'
    'nikita-the-wind-based-intruder.html' = 'Nikita the Wind'
    'nun.html' = 'Nun'
    'old-lady.html' = 'Old Lady'
    'parentless-teenager.html' = 'Parentless Teenager'
    'positive-guy.html' = 'Positive Guy'
    'protagonist.html' = 'Protagonist'
    'raincoat-child.html' = 'Raincoat Child'
    'reporter.html' = 'Reporter'
    'seductive-woman.html' = 'Seductive Woman'
    'stand-up-guy.html' = 'Stand Up Guy'
    'stoner.html' = 'Stoner'
    'suit-guy.html' = 'Suit Guy'
    'sun-guy.html' = 'Sun Guy'
    'surgeon.html' = 'Surgeon'
    'sweaty-man.html' = 'Sweaty Man'
    'theorist.html' = 'Theorist'
    'the-sisters.html' = 'The Sisters'
    'vigilante.html' = 'Vigilante'
    'weather-reporter.html' = 'Weather Reporter'
    'widowed-woman.html' = 'Widowed Woman'
    'wireface.html' = 'Wireface'
    'wounded-man.html' = 'Wounded Man'
}

function Fix-CharacterPage {
    param(
        [string]$FilePath,
        [string]$CorrectName
    )

    try {
        $content = Get-Content -Path $FilePath -Raw -Encoding UTF8
        $originalContent = $content

        # 修复基本信息中的角色名称
        $content = $content -replace '(<span class="info-label">Name:</span>\s*<span class="info-value">).+?(</span>)', "`${1}$CorrectName`$2"

        # 修复页面标题（如果包含错误的Bandana Guy）
        if ($content -match "Bandana Guy") {
            # 确定冠词
            if ($CorrectName -match '^[AEIOUaeiou]') {
                $article = "An"
            } else {
                $article = "The"
            }

            # 修复主要描述
            $content = $content -replace 'The Bandana Guy is a visitor', "$article $CorrectName is a character"
            $content = $content -replace 'The Bandana Guy appears to be', "$CorrectName appears to be"

            # 修复特征描述
            if ($CorrectName -ne "Bandana Guy") {
                $content = $content -replace 'bandana accessory gives him a distinctive look', 'distinctive appearance makes them memorable'
                $content = $content -replace 'His bandana could suggest', 'Their background could involve'
            }
        }

        # 只有内容发生变化时才写入文件
        if ($content -ne $originalContent) {
            Set-Content -Path $FilePath -Value $content -Encoding UTF8
            Write-Host "✅ 修复完成: $FilePath -> $CorrectName" -ForegroundColor Green
            return $true
        } else {
            Write-Host "⚪ 无需修复: $FilePath" -ForegroundColor Yellow
            return $false
        }
    }
    catch {
        Write-Host "❌ 修复失败: $FilePath - $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# 主执行逻辑
Write-Host "🔧 开始修复角色页面基本信息..." -ForegroundColor Cyan

$fixedCount = 0
$totalCount = 0
$charactersDir = "guide\characters"

if (-not (Test-Path $charactersDir)) {
    Write-Host "❌ 目录不存在: $charactersDir" -ForegroundColor Red
    exit 1
}

foreach ($htmlFile in Get-ChildItem -Path $charactersDir -Filter "*.html") {
    if ($characterMapping.ContainsKey($htmlFile.Name)) {
        $totalCount++
        $correctName = $characterMapping[$htmlFile.Name]

        if (Fix-CharacterPage -FilePath $htmlFile.FullName -CorrectName $correctName) {
            $fixedCount++
        }
    } else {
        Write-Host "⚠️  未找到映射: $($htmlFile.Name)" -ForegroundColor Magenta
    }
}

Write-Host "`n📊 修复完成:" -ForegroundColor Cyan
Write-Host "   总文件数: $totalCount"
Write-Host "   已修复: $fixedCount"
Write-Host "   无需修复: $($totalCount - $fixedCount)"