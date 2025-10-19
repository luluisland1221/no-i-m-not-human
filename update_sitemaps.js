/**
 * Update sitemap files with current character pages and today's date
 */

const fs = require('fs');
const path = require('path');

// Get today's date in YYYY-MM-DD format
function getTodayDate() {
    const today = new Date();
    return today.toISOString().split('T')[0];
}

// Get all character files
function getCharacterFiles() {
    const charactersDir = path.join(__dirname, 'guide', 'characters');
    const files = fs.readdirSync(charactersDir)
        .filter(file => file.endsWith('.html'))
        .sort(); // Sort alphabetically

    return files.map(file => file.replace('.html', ''));
}

// Update sitemap.txt
function updateSitemapTxt() {
    const characterFiles = getCharacterFiles();
    const todayDate = getTodayDate();

    let sitemapContent = `# Main pages
https://noimnothuman.xyz/
https://noimnothuman.xyz/characters.html
https://noimnothuman.xyz/achievements/
https://noimnothuman.xyz/ending/
https://noimnothuman.xyz/guide.html
https://noimnothuman.xyz/download.html
https://noimnothuman.xyz/about.html
https://noimnothuman.xyz/contact.html
https://noimnothuman.xyz/characters/index.html
https://noimnothuman.xyz/privacy-policy.html
https://noimnothuman.xyz/terms-of-service.html

# Character guide pages (${characterFiles.length} total characters)
`;

    // Add all character pages
    characterFiles.forEach(character => {
        sitemapContent += `https://noimnothuman.xyz/guide/characters/${character}.html\n`;
    });

    fs.writeFileSync(path.join(__dirname, 'sitemap.txt'), sitemapContent, 'utf8');
    console.log('✅ Updated sitemap.txt');
}

// Update sitemap.xml
function updateSitemapXml() {
    const characterFiles = getCharacterFiles();
    const todayDate = getTodayDate();

    let xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://noimnothuman.xyz/</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/index.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/guide.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/characters.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/achievements.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/ending.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/download.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/about.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/contact.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/privacy-policy.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://noimnothuman.xyz/terms-of-service.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
`;

    // Add all character pages
    characterFiles.forEach(character => {
        xmlContent += `  <url>
    <loc>https://noimnothuman.xyz/guide/characters/${character}.html</loc>
    <lastmod>${todayDate}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
`;
    });

    xmlContent += '</urlset>';

    fs.writeFileSync(path.join(__dirname, 'sitemap.xml'), xmlContent, 'utf8');
    console.log('✅ Updated sitemap.xml');
}

// Main function
function main() {
    console.log('🗺️ Starting sitemap updates...\n');

    updateSitemapTxt();
    updateSitemapXml();

    const characterFiles = getCharacterFiles();

    console.log(`\n📊 Sitemap Update Summary:`);
    console.log(`📁 Character pages: ${characterFiles.length}`);
    console.log(`📅 Updated date: ${getTodayDate()}`);
    console.log('\n🎯 Sitemap updates complete!');
}

// Run the script
if (require.main === module) {
    main();
}

module.exports = {
    updateSitemapTxt,
    updateSitemapXml,
    getCharacterFiles
};