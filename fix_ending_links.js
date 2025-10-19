/**
 * Fix inconsistent ending links throughout the website
 * Unify all links to point to ending.html instead of ending/ directory
 */

const fs = require('fs');
const path = require('path');

// Function to fix ending links in a single file
function fixEndingLinks(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;

        // Replace directory-style links with file links
        content = content.replace(/href="\.\/ending\//g, 'href="./ending.html"');
        content = content.replace(/href='\.\.\/ending\//g, 'href="../ending.html"');
        content = content.replace(/href="\.\.\/\.\.\/ending\//g, 'href="../../ending.html"');
        content = content.replace(/href='\.\.\/\.\.\/ending\//g, 'href="../../ending.html"');

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

// Function to get all HTML files
function getAllHtmlFiles(dir) {
    const files = [];

    function traverse(currentDir) {
        const items = fs.readdirSync(currentDir);

        for (const item of items) {
            const fullPath = path.join(currentDir, item);
            const stat = fs.statSync(fullPath);

            if (stat.isDirectory()) {
                traverse(fullPath);
            } else if (item.endsWith('.html')) {
                files.push(fullPath);
            }
        }
    }

    traverse(dir);
    return files;
}

// Main function
function main() {
    console.log('🔧 Starting ending links fix...\n');

    const projectDir = __dirname;
    const htmlFiles = getAllHtmlFiles(projectDir);

    console.log(`Found ${htmlFiles.length} HTML files\n`);

    let fixedCount = 0;
    let noChangeCount = 0;
    let errorCount = 0;

    for (const file of htmlFiles) {
        // Skip the ending files themselves
        if (file.includes('ending.html') || file.includes('ending/')) {
            continue;
        }

        try {
            const wasFixed = fixEndingLinks(file);
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

// Run the script
if (require.main === module) {
    main();
}

module.exports = {
    fixEndingLinks,
    getAllHtmlFiles
};