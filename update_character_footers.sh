#!/bin/bash

# 批量更新角色指南页面footer的脚本

cd "G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide/characters"

# 需要更新的文件列表（排除angry-guy.html，因为它已经是正确的格式）
files=(
    "armchair-lawyer-guy.html"
    "bandana-guy.html"
    "bar-guy.html"
    "bearded-guy.html"
    "best-son.html"
    "big-momma.html"
    "blinded-man.html"
    "blonde-guy.html"
    "border-patrol-agent.html"
    "brunette-guy.html"
    "cabby-man.html"
    "cashier-girl.html"
    "cat-lady.html"
    "cheerful-man.html"
    "child.html"
    "coat-guy.html"
    "cozy-man.html"
    "death.html"
    "death-cult-leader.html"
    "death-cult-peon.html"
    "delivery-man.html"
    "disfigured-guy.html"
    "egghead-guy.html"
    "factory-guy.html"
    "fema-agent.html"
    "fetus.html"
    "fortune-teller.html"
    "gravedigger.html"
    "homeless-man.html"
    "husband-and-wife.html"
    "immortal-man.html"
    "intruder.html"
    "kindergarten-teacher.html"
    "little-girl.html"
    "miner.html"
    "mushroom-man.html"
    "music-conductor.html"
    "neglectful-mother.html"
    "neighbor.html"
    "nikita-the-wind-based-intruder.html"
    "nun.html"
    "old-lady.html"
    "parentless-teenager.html"
    "positive-guy.html"
    "protagonist.html"
    "raincoat-child.html"
    "reporter.html"
    "seductive-woman.html"
    "stand-up-guy.html"
    "stoner.html"
    "suit-guy.html"
    "sun-guy.html"
    "surgeon.html"
    "sweaty-man.html"
    "theorist.html"
    "the-sisters.html"
    "vigilante.html"
    "weather-reporter.html"
    "widowed-woman.html"
    "wireface.html"
    "wounded-man.html"
)

# 新的footer结构
new_footer='<div class="footer-section">
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

# 旧的footer结构（需要被替换的部分）
old_footer_pattern='<div class="footer-section">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../../guide.html">Game Guide</a></li>
                    <li><a href="../../guide.html#characters">Characters</a></li>
                    <li><a href="../download.html">Download</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Resources</h4>
                <ul>
                    <li><a href="../../guide.html#achievements">Achievements</a></li>
                    <li><a href="../../guide.html#character-scripts">Character Scripts</a></li>
                    <li><a href="../../guide.html#edible-items">Edible Items</a></li>
                    <li><a href="../community.html">Community</a></li>
                </ul>'

echo "开始批量更新角色指南页面footer..."

# 统计更新数量
updated_count=0
total_count=${#files[@]}

# 循环更新每个文件
for file in "${files[@]}"; do
    if [[ -f "$file" ]]; then
        echo "正在更新: $file ($((updated_count + 1))/$total_count)"

        # 使用sed替换footer结构
        sed -i 's|<div class="footer-section">\
                <h4>Quick Links</h4>\
                <ul>\
                    <li><a href="../index.html">Home</a></li>\
                    <li><a href="../../guide.html">Game Guide</a></li>\
                    <li><a href="../../guide.html#characters">Characters</a></li>\
                    <li><a href="../download.html">Download</a></li>\
                </ul>\
            </div>\
            <div class="footer-section">\
                <h4>Resources</h4>\
                <ul>\
                    <li><a href="../../guide.html#achievements">Achievements</a></li>\
                    <li><a href="../../guide.html#character-scripts">Character Scripts</a></li>\
                    <li><a href="../../guide.html#edible-items">Edible Items</a></li>\
                    <li><a href="../community.html">Community</a></li>\
                </ul>|<div class="footer-section">\
                <h4>Quick Links</h4>\
                <ul>\
                    <li><a href="../index.html">Home</a></li>\
                    <li><a href="../characters.html">Characters</a></li>\
                    <li><a href="../achievements.html">Achievements</a></li>\
                    <li><a href="../ending.html">Endings</a></li>\
                    <li><a href="../download.html">Download</a></li>\
                </ul>\
            </div>\
            <div class="footer-section">\
                <h4>Game Content</h4>\
                <ul>\
                    <li><a href="../characters.html">Character Identification Guide</a></li>\
                    <li><a href="../achievements.html">Complete Achievement List</a></li>\
                    <li><a href="../ending.html">All Game Endings</a></li>\
                    <li><a href="https://store.steampowered.com/app/3180070/No_Im_not_a_Human/" target="_blank">Steam Store</a></li>\
                </ul>|g' "$file"

        ((updated_count++))
        echo "✓ 已完成: $file"
    else
        echo "⚠ 文件不存在: $file"
    fi
done

echo ""
echo "批量更新完成！"
echo "更新文件数: $updated_count/$total_count"
echo "所有角色指南页面的footer已标准化为新的导航结构。"