# 批量修正所有角色页面中的Bandana Guy错误
# 阶段1：紧急名称修正

$charactersDir = "guide\characters"

# 角色名称映射
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
    'death-cult-peon.html' = 'Death Cult Peon'
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

function Fix-CharacterFile {
    param(
        [string]$FilePath,
        [string]$CharacterName
    )

    try {
        $content = Get-Content -Path $FilePath -Raw -Encoding UTF8
        $originalContent = $content

        # 主要替换模式
        $replacements = @{
            'The Bandana Guy is a visitor' = "The $CharacterName is a character"
            'His bandana accessory gives him a distinctive look' = 'Their distinctive features give them a unique appearance'
            'His bandana accessory' = 'Their distinctive features'
            'His bandana' = 'Their appearance'
            'he presents himself' = 'they present'
            'he appears' = 'they appear'
            'his casual' = 'their approach'
            'his relaxed' = 'their demeanor'
            'his distinctive' = 'their unique'
            'his approachable' = 'their manner'
            'the Bandana Guy' = "the $CharacterName"
            'Bandana Guy' = $CharacterName
        }

        # 执行替换
        foreach ($pattern in $replacements.Keys) {
            $content = $content -replace [regex]::Escape($pattern), $replacements[$pattern]
        }

        # 修复性别相关的代词
        if ($CharacterName -match 'Girl|Woman|Lady|Mom|Sister|Teacher|Nun|Daughter|Mother') {
            $content = $content -replace 'they present', 'she presents'
            $content = $content -replace 'they appear', 'she appears'
            $content = $content -replace 'their', 'her'
            $content = $content -replace 'them', 'her'
        }

        # 只有内容发生变化时才写入文件
        if ($content -ne $originalContent) {
            Set-Content -Path $FilePath -Value $content -Encoding UTF8
            return $true
        }
        return $false
    }
    catch {
        Write-Host "❌ 修复失败: $FilePath - $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

Write-Host "🚨 阶段1：紧急名称修正开始..." -ForegroundColor Cyan

$fixedCount = 0
$totalFiles = 0

foreach ($htmlFile in Get-ChildItem -Path $charactersDir -Filter "*.html") {
    $totalFiles++

    if ($characterMapping.ContainsKey($htmlFile.Name)) {
        $characterName = $characterMapping[$htmlFile.Name]

        # 跳过bandana-guy.html，这是正确的Bandana Guy页面
        if ($htmlFile.Name -eq 'bandana-guy.html') {
            Write-Host "⚪ 跳过: $($htmlFile.Name) (这是正确的Bandana Guy页面)" -ForegroundColor Yellow
            continue
        }

        if (Fix-CharacterFile -FilePath $htmlFile.FullName -CharacterName $characterName) {
            $fixedCount++
            Write-Host "✅ 修正完成: $($htmlFile.Name) -> $characterName" -ForegroundColor Green
        } else {
            Write-Host "⚪ 无需修正: $($htmlFile.Name)" -ForegroundColor Gray
        }
    }
}

Write-Host "`n📊 阶段1修正结果:" -ForegroundColor Cyan
Write-Host "   总文件数: $totalFiles"
Write-Host "   成功修正: $fixedCount"
Write-Host "   无需修正/跳过: $($totalFiles - $fixedCount)"

if ($fixedCount -gt 0) {
    Write-Host "`n🎯 阶段1完成！已修正$fixedCount个文件的Bandana Guy错误。" -ForegroundColor Green
    Write-Host "🔄 准备进入阶段2：基本信息完善" -ForegroundColor Cyan
} else {
    Write-Host "`n✅ 未发现需要修正的Bandana Guy错误。" -ForegroundColor Green
}