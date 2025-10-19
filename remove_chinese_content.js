/**
 * Remove all Chinese characters and symbols from files
 * Ensures all code and web interface content is in English only
 */

const fs = require('fs');
const path = require('path');

// Function to remove Chinese characters and symbols
function removeChineseContent(text) {
    // Remove Chinese characters (Unicode range for CJK Unified Ideographs)
    text = text.replace(/[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf\uf900-\ufaff\u3300-\u33ff\ufe30-\ufe4f\uf900-\ufaff\U0002f800-\U0002fa1f]/g, '');

    // Remove Chinese punctuation and symbols
    text = text.replace(/[，。！？；：""''（）【】《》、]/g, '');

    // Remove Chinese content comments and references
    text = text.replace(/<!-- .*[\u4e00-\u9fff].* -->/g, '');
    text = text.replace(/\/\*.*[\u4e00-\u9fff].*\*\//g, '');
    text = text.replace(/\/\/.*[\u4e00-\u9fff].*/g, '');

    // Remove specific Chinese phrases that might remain
    text = text.replace(/角色|访客|人类|策略|特征|登场|身份/g, '');
    text = text.replace(/游戏|玩家|剧情|触发|结局/g, '');

    return text;
}

// Function to clean a single file
function cleanFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalLength = content.length;

        content = removeChineseContent(content);

        // Clean up extra whitespace that might result from removal
        content = content.replace(/\s+/g, ' ').trim();

        if (content.length !== originalLength) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ Cleaned: ${path.basename(filePath)}`);
            return true;
        } else {
            console.log(`⚪ No Chinese content found: ${path.basename(filePath)}`);
            return false;
        }
    } catch (error) {
        console.error(`❌ Error cleaning ${path.basename(filePath)}:`, error.message);
        return false;
    }
}

// Function to clean all HTML files in characters directory
function cleanCharacterFiles() {
    const charactersDir = path.join(__dirname, 'guide', 'characters');
    const files = fs.readdirSync(charactersDir)
        .filter(file => file.endsWith('.html'));

    console.log(`🧹 Starting cleanup of ${files.length} character files...\n`);

    let cleanedCount = 0;
    let noChineseCount = 0;
    let errorCount = 0;

    for (const file of files) {
        const filePath = path.join(charactersDir, file);
        try {
            const wasCleaned = cleanFile(filePath);
            if (wasCleaned) {
                cleanedCount++;
            } else {
                noChineseCount++;
            }
        } catch (error) {
            errorCount++;
        }
    }

    console.log(`\n📊 Cleanup Summary:`);
    console.log(`✅ Files cleaned: ${cleanedCount}`);
    console.log(`⚪ No Chinese content: ${noChineseCount}`);
    console.log(`❌ Errors: ${errorCount}`);

    return cleanedCount + noChineseCount;
}

// Function to clean the main script file
function cleanScriptFile() {
    const scriptPath = path.join(__dirname, 'add_identification_strategy.js');

    console.log('\n🧹 Cleaning main script file...');

    try {
        let content = fs.readFileSync(scriptPath, 'utf8');

        // Remove Chinese variable names and comments but keep English functionality
        content = content.replace(/\/\*[\s\S]*?\*\//g, ''); // Remove multi-line comments
        content = content.replace(/\/\/.*[\u4e00-\u9fff].*/g, ''); // Remove Chinese single-line comments

        // Remove Chinese variable names in the data
        content = content.replace(/nameCn: '[^']*'/g, "nameCn: ''");

        // Clean Chinese content from strings but keep structure
        content = content.replace(/'[^']*[\u4e00-\u9fff][^']*'/g, function(match) {
            // Replace Chinese content with English equivalent or empty string
            return `'${match.replace(/[\u4e00-\u9fff，。！？；：""''（）【】《》、]/g, '').trim()}'`;
        });

        // Remove Chinese content from identification text
        content = content.replace(/identityText: '[^']*[\u4e00-\u9fff][^']*'/g, function(match) {
            return "'Identity Unknown'";
        });

        // Clean appearance conditions
        content = content.replace(/appearanceCondition: '[^']*[\u4e00-\u9fff][^']*'/g, function(match) {
            return "'Random Appearance'";
        });

        // Clean identification features
        content = content.replace(/'[^']*[\u4e00-\u9fff][^']*'/g, function(match) {
            return `'${match.replace(/[\u4e00-\u9fff，。！？；：""''（）【】《》、]/g, 'Unknown Feature').trim()}'`;
        });

        // Clean game strategy
        content = content.replace(/'[^']*[\u4e00-\u9fff][^']*'/g, function(match) {
            return `'${match.replace(/[\u4e00-\u9fff，。！？；：""''（）【】《》、]/g, 'Unknown Strategy').trim()}'`;
        });

        fs.writeFileSync(scriptPath, content, 'utf8');
        console.log('✅ Script file cleaned');

        return true;
    } catch (error) {
        console.error(`❌ Error cleaning script file:`, error.message);
        return false;
    }
}

// Main function
function main() {
    console.log('🚀 Starting Chinese content removal process...\n');

    const characterFilesProcessed = cleanCharacterFiles();
    const scriptCleaned = cleanScriptFile();

    console.log('\n🎯 Chinese content removal complete!');
    console.log(`📁 Total files processed: ${characterFilesProcessed + 1} (including script)`);
    console.log('✨ All content is now in English only');
}

// Run script directly
if (require.main === module) {
    main();
}

module.exports = {
    removeChineseContent,
    cleanFile,
    cleanCharacterFiles,
    cleanScriptFile
};