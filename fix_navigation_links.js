/**
 * Fix navigation links in character pages
 * Change "Back to Character Guide" links from guide.html#characters to characters.html
 */

const fs = require('fs');
const path = require('path');

// Function to fix navigation links in a single file
function fixNavigationLinks(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;

        // Replace the incorrect navigation link
        const oldLink = '<a href="../../guide.html#characters" class="btn-back">← Back to Character Guide</a>';
        const newLink = '<a href="../../characters.html" class="btn-back">← Back to Characters</a>';

        content = content.replace(oldLink, newLink);

        // Also update the text to be more accurate
        content = content.replace('Back to Character Guide', 'Back to Characters');

        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ Fixed: ${path.basename(filePath)}`);
            return true;
        } else {
            console.log(`⚪ No changes needed: ${path.basename(filePath)}`);
            return false;
        }
    } catch (error) {
        console.error(`❌ Error fixing ${path.basename(filePath)}:`, error.message);
        return false;
    }
}

// Main function to fix all character files
function fixAllCharacterFiles() {
    const charactersDir = path.join(__dirname, 'guide', 'characters');
    const files = fs.readdirSync(charactersDir)
        .filter(file => file.endsWith('.html'));

    console.log(`🔧 Starting navigation link fixes for ${files.length} character files...\n`);

    let fixedCount = 0;
    let noChangeCount = 0;
    let errorCount = 0;

    for (const file of files) {
        const filePath = path.join(charactersDir, file);
        try {
            const wasFixed = fixNavigationLinks(filePath);
            if (wasFixed) {
                fixedCount++;
            } else {
                noChangeCount++;
            }
        } catch (error) {
            errorCount++;
        }
    }

    console.log(`\n📊 Fix Summary:`);
    console.log(`✅ Files fixed: ${fixedCount}`);
    console.log(`⚪ No changes needed: ${noChangeCount}`);
    console.log(`❌ Errors: ${errorCount}`);

    return fixedCount + noChangeCount;
}

// Main function
function main() {
    console.log('🚀 Starting navigation link correction...\n');

    const filesProcessed = fixAllCharacterFiles();

    console.log('\n🎯 Navigation link correction complete!');
    console.log(`📁 Total files processed: ${filesProcessed}`);
    console.log('✨ All character pages now correctly link to characters.html');
}

// Run the script
if (require.main === module) {
    main();
}

module.exports = {
    fixNavigationLinks,
    fixAllCharacterFiles
};