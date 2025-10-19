/**
 * Precise Chinese content removal script
 * Only removes actual Chinese characters, preserving all English content and HTML structure
 */

const fs = require('fs');
const path = require('path');

// Function to remove only Chinese characters, preserving all else
function removeChineseCharacters(text) {
    // Remove only Chinese characters (Unicode ranges for Chinese)
    // This regex targets only actual Chinese characters, not letters or numbers
    return text.replace(/[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f\U0002b740-\U0002b81f\U0002b820-\U0002ceaf\uf900-\ufaff\u3300-\u33ff\ufe30-\ufe4f]/g, '');
}

// Function to clean a single HTML file
function cleanHTMLFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;

        // Remove only Chinese characters, preserve HTML structure and English text
        content = removeChineseCharacters(content);

        // Remove specific Chinese comments (but keep English comments)
        content = content.replace(/<!--[\s\S]*?[\u4e00-\u9fff][\s\S]*?-->/g, '');
        content = content.replace(/\/\*[\s\S]*?[\u4e00-\u9fff][\s\S]*?\*\//g, '');

        // Clean up excessive whitespace that might result from character removal
        content = content.replace(/\s{2,}/g, ' ');
        content = content.replace(/\n\s*\n/g, '\n');

        // Only write if content actually changed
        if (content !== originalContent) {
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

// Function to clean JavaScript files
function cleanJSFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;

        // Remove Chinese characters from strings but keep the structure
        content = content.replace(/nameCn: '[^']*'/g, "nameCn: ''");

        // Clean Chinese characters from other string values more carefully
        content = content.replace(/'[^']*[\u4e00-\u9fff][^']*'/g, function(match) {
            // Replace Chinese content while preserving English letters and numbers
            return `'${match.replace(/[\u4e00-\u9fff，。！？；：""''（）【】《》、]/g, '').trim()}'`;
        });

        // Remove Chinese comments
        content = content.replace(/\/\/.*[\u4e00-\u9fff].*/g, '');
        content = content.replace(/\/\*[\s\S]*?[\u4e00-\u9fff][\s\S]*?\*\//g, '');

        if (content !== originalContent) {
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

// Main function
function main() {
    console.log('🚀 Starting precise Chinese content removal...\n');

    const charactersDir = path.join(__dirname, 'guide', 'characters');
    const files = fs.readdirSync(charactersDir)
        .filter(file => file.endsWith('.html'));

    console.log(`🧹 Processing ${files.length} HTML files...\n`);

    let htmlCleanedCount = 0;
    let htmlNoChineseCount = 0;

    for (const file of files) {
        const filePath = path.join(charactersDir, file);
        try {
            const wasCleaned = cleanHTMLFile(filePath);
            if (wasCleaned) {
                htmlCleanedCount++;
            } else {
                htmlNoChineseCount++;
            }
        } catch (error) {
            console.error(`Error processing ${file}:`, error.message);
        }
    }

    // Clean the main script file
    console.log('\n🧹 Cleaning script files...');
    const scriptCleaned = cleanJSFile(path.join(__dirname, 'add_identification_strategy.js'));

    console.log('\n📊 Cleanup Summary:');
    console.log(`✅ HTML files cleaned: ${htmlCleanedCount}`);
    console.log(`⚪ HTML files with no Chinese: ${htmlNoChineseCount}`);
    console.log(`📝 Script file cleaned: ${scriptCleaned ? 'Yes' : 'No'}`);

    console.log('\n🎯 Precise Chinese content removal complete!');
}

// Run the script
if (require.main === module) {
    main();
}

module.exports = {
    removeChineseCharacters,
    cleanHTMLFile,
    cleanJSFile
};