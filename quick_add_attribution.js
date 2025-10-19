const fs = require('fs');
const path = require('path');

// 角色映射表
const characterUrls = {
    'armchair-lawyer-guy': 'Armchair_Lawyer_Guy',
    'bandana-guy': 'Bandana_Guy',
    'bar-guy': 'Bar_Guy',
    'bearded-guy': 'Bearded_Guy',
    'best-son': 'Best_Son',
    'big-momma': 'Big_Momma',
    'blinded-man': 'Blinded_Man',
    'blonde-guy': 'Blonde_Guy',
    'border-patrol-agent': 'Border_Patrol_Agent',
    'brunette-guy': 'Brunette_Guy',
    'cabby-man': 'Cabby_Man',
    'cashier-girl': 'Cashier_Girl',
    'cat-lady': 'Cat_Lady',
    'child': 'Child',
    'coat-guy': 'Coat_Guy',
    'cozy-man': 'Cozy_Man',
    'death-cult-peon': 'Death_Cult_Peons',
    'delivery-man': 'Delivery_Man',
    'disfigured-guy': 'Disfigured_Firefighter',
    'egghead-guy': 'Egghead_Guy',
    'factory-guy': 'Factory_Guy',
    'fema-agent': 'FEMA_Agent',
    'fetus': 'Fetus',
    'fortune-teller': 'Fortune_Teller',
    'gravedigger': 'Gravedigger',
    'homeless-man': 'Homeless_Man',
    'husband-and-wife': 'Husband_and_Wife',
    'immortal-man': 'Immortal_Man',
    'intruder': 'Intruder',
    'kindergarten-teacher': 'Kindergarten_Teacher',
    'little-girl': 'Little_Girl',
    'miner': 'Miner',
    'music-conductor': 'Music_Conductor',
    'mushroom-man': 'Mushroom_Eater',
    'neighbor': 'Neighbor',
    'neglectful-mother': 'Deadbeat_Mom',
    'nikita-the-wind-based-intruder': 'Nikita',
    'nun': 'Nun',
    'old-lady': 'Old_Lady',
    'parentless-teenager': 'Parentless_Teenager',
    'positive-guy': 'Positive_Guy',
    'protagonist': 'Protagonist',
    'raincoat-child': 'Raincoat_Child',
    'reporter': 'Reporter',
    'seductive-woman': 'Seductive_Woman',
    'stand-up-guy': 'Stand_Up_Guy',
    'sun-guy': 'Sun_Guy',
    'surgeon': 'Surgeon',
    'sweaty-man': 'Sweaty_Man',
    'theorist': 'Theorist',
    'vigilante': 'Vigilante',
    'weather-reporter': 'Weather_Reporter',
    'widowed-woman': 'Widowed_Woman',
    'wounded-man': 'Wounded_Man'
};

// 显示名称映射
const displayNames = {
    'death': 'Death',
    'death-cult-leader': 'Death Cult Leader',
    'death-cult-peon': 'Death Cult Peon',
    'the-sisters': 'The Sisters',
    'wireface': 'Wireface',
    'neglectful-mother': 'Deadbeat Mom',
    'nikita-the-wind-based-intruder': 'Nikita'
};

function getDisplayName(basename) {
    if (displayNames[basename]) {
        return displayNames[basename];
    }
    return basename.split('-').map(word =>
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
}

function createAttributionHtml(filename) {
    const basename = filename.replace('.html', '');
    const displayName = getDisplayName(basename);

    // 获取Fandom URL
    let fandomUrl;
    if (characterUrls[basename]) {
        fandomUrl = `https://no-i-am-not-a-human.fandom.com/wiki/${characterUrls[basename]}`;
    } else {
        const pascalName = basename.split('-').map(word =>
            word.charAt(0).toUpperCase() + word.slice(1)
        ).join('');
        fandomUrl = `https://no-i-am-not-a-human.fandom.com/wiki/${pascalName}`;
    }

    return `            <!-- Content Attribution -->
            <section class="content-attribution">
                <h3>📚 Content Reference</h3>
                <p>Character information on this page is sourced from the official wiki:</p>
                <div class="attribution-link">
                    <a href="${fandomUrl}" target="_blank" rel="noopener">
                        📖 No, I am not a human Wiki - ${displayName} ↗
                    </a>
                </div>
                <p class="license-info">Content available under <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC-BY-SA</a> unless otherwise noted.</p>
            </section>

`;
}

function addAttributionToFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        const filename = path.basename(filePath);

        // 检查是否已经有内容署名
        if (content.includes('content-attribution')) {
            console.log(`⚠️  ${filename} 已经有内容署名，跳过`);
            return false;
        }

        // 查找插入位置（在Back to Guide Link之前）
        const backToGuideRegex = /(\s*<!-- Back to Guide Link -->\s*<div class="back-to-guide">)/;

        const attributionHtml = createAttributionHtml(filename);

        if (backToGuideRegex.test(content)) {
            const newContent = content.replace(backToGuideRegex, attributionHtml + '$1');

            fs.writeFileSync(filePath, newContent, 'utf8');
            console.log(`✅ 已为 ${filename} 添加内容署名`);
            return true;
        } else {
            console.log(`❌ 无法找到插入位置: ${filename}`);
            return false;
        }

    } catch (error) {
        console.log(`❌ 处理 ${path.basename(filePath)} 时出错: ${error.message}`);
        return false;
    }
}

function main() {
    const charactersDir = 'G:/ai编程/100个网站/07 noimnothuman.xyz/code/guide/characters';

    if (!fs.existsSync(charactersDir)) {
        console.log(`❌ 目录不存在: ${charactersDir}`);
        return;
    }

    const htmlFiles = fs.readdirSync(charactersDir)
        .filter(file => file.endsWith('.html'))
        .sort();

    console.log(`🔍 找到 ${htmlFiles.length} 个角色文件`);
    console.log();

    let successCount = 0;
    let totalCount = htmlFiles.length;

    for (const file of htmlFiles) {
        const filePath = path.join(charactersDir, file);
        if (addAttributionToFile(filePath)) {
            successCount++;
        }
    }

    console.log();
    console.log(`📊 处理完成: ${successCount}/${totalCount} 个文件成功添加内容署名`);
    console.log();
    console.log('🎉 所有角色页面现在都有CC-BY-SA内容署名！');
    console.log('💡 提示:');
    console.log('   - 可以在浏览器中验证效果');
    console.log('   - 现在可以重新申请Google AdSense');
    console.log('   - 建议先测试几个页面确保一切正常');
}

if (require.main === module) {
    main();
}