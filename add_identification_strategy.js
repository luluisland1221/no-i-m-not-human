

const fs = require('fs');
const path = require('path');


const characterIdentificationData = {
    'angry-guy': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Aggressive and hostile behavior',
            'Threatening language and body language',
            'Unpredictable mood changes and erratic actions'
        ],
        gameStrategy: [
            'Observe behavioral patterns carefully',
            'Consider potential threats',
            'Handle with caution'
        ]
    },
    'armchair-lawyer-guy': {
        nameCn: '',
        identityType: '×※',
        identityText: 'Confirmed Human (though identity questioned)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Very clean teeth and drooping ears',
            'Confirmed human despite identity questions',
            'Extremely concerned with legal issues'
        ],
        gameStrategy: [
            'Confirmed human identity',
            'Can safely allow entry'
        ]
    },
    'bandana-guy': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity',
        appearanceCondition: 'Random appearance after Day 7',
        identificationFeatures: [
            'Very clean teeth and hand eczema if visitor',
            'Cannot cohabit with "man-in-hoodie"'
        ],
        gameStrategy: [
            'Check teeth and hand features',
            'Clean teeth + eczema indicates visitor'
        ]
    },
    'bar-guy': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Day 2 appearance',
        identificationFeatures: [
            'Kicked out of bar for fighting',
            'Confirmed human'
        ],
        gameStrategy: [
            'Can safely allow entry',
            'Clear human identity'
        ]
    },
    'bearded-guy': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (possibly random)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Moldy armpits when visitor'
        ],
        gameStrategy: [
            'Check armpit features',
            'Mold indicates visitor status'
        ]
    },
    'best-son': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (possibly random)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Bleeding gums when visitor'
        ],
        gameStrategy: [
            'Check gum condition',
            'Bleeding indicates visitor status'
        ]
    },
    'big-momma': {
        nameCn: '',
        identityType: '〇※',
        identityText: 'Confirmed Visitor',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Confirmed visitor',
            'Broken nails, swollen red eyes when visitor',
            'Originally had many children, all taken by FEMA'
        ],
        gameStrategy: [
            'Should help this character',
            'Confirmed visitor identity'
        ]
    },
    'blinded-man': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Guaranteed appearance',
        identificationFeatures: [
            'Sole survivor of wildfire fighting operation, burned by sun',
            'Confirmed human',
            'Eyes swollen and red from smoke',
            'Will give player FEMA notice',
            'Has wife and children at home'
        ],
        gameStrategy: [
            'Confirmed human identity',
            'Can safely allow entry',
            'FEMA notice is important item'
        ]
    },
    'blonde-guy': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (suspected human)',
        appearanceCondition: 'Random appearance after Day 7',
        identificationFeatures: [
            'Shows impulsive behavior'
        ],
        gameStrategy: [
            'Suspected human identity',
            'Observe behavior patterns'
        ]
    },
    'border-patrol-agent': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 9, Day 11',
        identificationFeatures: [
            'Day 11 will "inspect" player',
            'Triggers special ending if player shows abnormal features'
        ],
        gameStrategy: [
            'Key plot character',
            'Pay attention to own status features'
        ]
    },
    'brunette-guy': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (suspected human)',
        appearanceCondition: 'Random appearance after Day 7',
        identificationFeatures: [
            'Shows interest in movies'
        ],
        gameStrategy: [
            'Suspected human identity',
            'Judge with caution'
        ]
    },
    'cabby-man': {
        nameCn: '',
        identityType: '×※',
        identityText: 'Identity Questioned (suspected human)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Swollen red eyes'
        ],
        gameStrategy: [
            'Suspected human identity',
            'Need careful judgment'
        ]
    },
    'cashier-girl': {
        nameCn: '',
        identityType: '〇',
        identityText: 'Confirmed Visitor',
        appearanceCondition: 'Day 2 appearance',
        identificationFeatures: [
            'Fired from supermarket, home occupied',
            'Forced to escape to player\'s home',
            'Fuzzy memory, has anxiety disorder'
        ],
        gameStrategy: [
            'Should help this character',
            'Confirmed visitor identity'
        ]
    },
    'cat-lady': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Visitor',
        appearanceCondition: 'Day 5 appearance',
        identificationFeatures: [
            'Holding a cat, confirmed visitor',
            'Her cat stays at player\'s home, helps find basement',
            'Petting cat increases cat affection',
            'Cannot cohabit with "nun"'
        ],
        gameStrategy: [
            'Must let her enter to advance plot',
            'Cat is important game mechanism character'
        ]
    },
    'cheerful-man': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Shows unusually happy mood',
            'Need to judge identity based on specific features'
        ],
        gameStrategy: [
            'Observe if words and actions match',
            'Pay attention to disguised features'
        ]
    },
    'child': {
        nameCn: '',
        identityType: '-※',
        identityText: 'Suspected random appearance',
        appearanceCondition: 'Suspected random appearance after Day 7',
        identificationFeatures: [
            'Comes to door saying "saw kitchen light on"',
            'Then says "wrong house" and leaves'
        ],
        gameStrategy: [
            'Special plot character',
            'No need to judge identity'
        ]
    },
    'coat-guy': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Will give kombucha in return for beer',
            'Moldy armpits when visitor',
            'Cannot cohabit with "widow"'
        ],
        gameStrategy: [
            'Check armpit features',
            'Mold indicates visitor status',
            'Note conflict with widow'
        ]
    },
    'cozy-man': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 1 guaranteed appearance',
        identificationFeatures: [
            'Neighbor uncle identity',
            'Will explain general game to player',
            'Day 2 his daughter will visit'
        ],
        gameStrategy: [
            'Tutorial character, no need to judge identity',
            'Day 2 his daughter will pick him up'
        ]
    },
    'death-cult-leader': {
        nameCn: '',
        identityType: '-',
        identityText: 'Cannot enter home, but 3 believers will stay',
        appearanceCondition: 'Day 9, Day 11, Day 12',
        identificationFeatures: [
            'Cannot enter home',
            '3 believers will stay at player\'s home',
            'If 3 believers survive to Day 12, triggers special ending'
        ],
        gameStrategy: [
            'Key plot character',
            'Protect believers to trigger special ending'
        ]
    },
    'death-cult-peon': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Day 9 appearance',
        identificationFeatures: [
            'One of the believers appearing on Day 9'
        ],
        gameStrategy: [
            'Clear human identity',
            'Can safely allow entry'
        ]
    },
    'delivery-man': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Appears after ordering from ForRest',
        identificationFeatures: [
            'Appears when player orders items',
            'Delivers in-game store items'
        ],
        gameStrategy: [
            'Store delivery character',
            'No need to judge identity'
        ]
    },
    'disfigured-guy': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (possibly random)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Clean teeth, swollen red eyes, earwax when visitor'
        ],
        gameStrategy: [
            'Check multiple features comprehensively',
            'Judge identity based on feature combination'
        ]
    },
    'egghead-guy': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Cross-eyed male who worships the sun',
            'Red eyes when visitor',
            'Calls FEMA "heretics"'
        ],
        gameStrategy: [
            'Pay attention to eye color',
            'Red eyes indicate visitor status'
        ]
    },
    'factory-guy': {
        nameCn: '',
        identityType: '-',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Day 8 appearance',
        identificationFeatures: [
            'Wearing FEMA protective suit',
            'Photos show black spots',
            'Confirmed human',
            'Admits being FEMA if shot'
        ],
        gameStrategy: [
            'Confirmed human identity',
            'Can test reaction'
        ]
    },
    'fema-agent': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 5 appearance',
        identificationFeatures: [
            'Wearing protective suit and gas mask',
            'Holding gun',
            'Will take away a character under pretext of "inspection"'
        ],
        gameStrategy: [
            'Plot trigger character',
            'Cannot refuse demands'
        ]
    },
    'fetus': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Suspected random appearance',
        identificationFeatures: [
            'Note appears in bedroom after meeting him',
            'Mushrooms appear in basement, can be stored in refrigerator'
        ],
        gameStrategy: [
            'Special item provider',
            'No need to judge identity'
        ]
    },
    'fortune-teller': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Will actively fortune-tell for player',
            'Very neat teeth and swollen red eyes when visitor'
        ],
        gameStrategy: [
            'Check teeth and eye features',
            'Neat teeth + red eyes indicate visitor'
        ]
    },
    'gravedigger': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Gold teeth when visitor',
            'If refused entry, will offer "cat food" as exchange'
        ],
        gameStrategy: [
            'Check dental features',
            'Gold teeth indicate visitor status'
        ]
    },
    'homeless-man': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Hand eczema when visitor'
        ],
        gameStrategy: [
            'Check hand features',
            'Eczema indicates visitor status'
        ]
    },
    'husband-and-wife': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Dislike children, cannot cohabit with "runaway girl"',
            'Smooth armpits when visitor'
        ],
        gameStrategy: [
            'Check armpit features',
            'Smooth indicates visitor status',
            'Note conflict with runaway girl'
        ]
    },
    'immortal-man': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 4, Day 6, Day 10',
        identificationFeatures: [
            'Will say lines guiding player',
            'Will not appear again if "woman with cat" not let in'
        ],
        gameStrategy: [
            'Important plot character',
            'Pay attention to provided guidance'
        ]
    },
    'intruder': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 4, Day 6, Day 10, Day 12',
        identificationFeatures: [
            'Directly causes game over if player alone or claims "alone"',
            'Will stand somewhere on night of Day 3',
            'Will hold soldier\'s head on night of Day 5'
        ],
        gameStrategy: [
            'Absolutely cannot say alone',
            'Dangerous hostile character'
        ]
    },
    'kindergarten-teacher': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Visits carrying husband\'s body',
            'Eyes swollen and red from crying',
            'Confirmed human'
        ],
        gameStrategy: [
            'Can safely allow entry',
            'Confirmed human identity'
        ]
    },
    'little-girl': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Red eyes when visitor',
            'Has an older sister'
        ],
        gameStrategy: [
            'Check eye features',
            'Red eyes indicate visitor status'
        ]
    },
    'miner': {
        nameCn: '',
        identityType: '×※',
        identityText: 'Identity Questioned (suspected human)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Obvious swollen eyes'
        ],
        gameStrategy: [
            'Suspected human identity',
            'Need careful judgment combined with other features'
        ]
    },
    'mushroom-man': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Visitor',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Confirmed visitor',
            'No armpit hair, bugs crawl out of ears',
            'Looking for "purple-haired girl in cloak"',
            'Says "visitors may be reborn from humans"'
        ],
        gameStrategy: [
            'Confirmed visitor identity',
            'Provides important background information'
        ]
    },
    'music-conductor': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (suspected human)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Claims to be former customs officer'
        ],
        gameStrategy: [
            'Suspected human identity',
            'Need careful judgment'
        ]
    },
    'neglectful-mother': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Red hand eczema when visitor',
            'Still has child on Day 2 if human',
            'If child disappears, confirmed visitor',
            'Woman in distress with child'
        ],
        gameStrategy: [
            'Check hand features',
            'Eczema indicates visitor status',
            'Note child situation'
        ]
    },
    'neighbor': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 1 guaranteed appearance',
        identificationFeatures: [
            'Neighbor uncle identity',
            'Will explain general game gameplay to player',
            'Day 2 his daughter will visit'
        ],
        gameStrategy: [
            'Tutorial character, no need to judge identity',
            'Day 2 his daughter will pick him up'
        ]
    },
    'nikita-the-wind-based-intruder': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Random appearance after Day 7',
        identificationFeatures: [
            'Will not enter if "positive guy" in house'
        ],
        gameStrategy: [
            'Character with specific condition restrictions',
            'No need to judge identity'
        ]
    },
    'nun': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (possibly random)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Moldy armpits when visitor',
            'No teeth',
            'Hands injured from contact with "roach poison"'
        ],
        gameStrategy: [
            'Check armpit features',
            'Mold indicates visitor status'
        ]
    },
    'old-lady': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (possibly random)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Swollen red eyes when visitor'
        ],
        gameStrategy: [
            'Observe eye features',
            'Red eyes indicate visitor status'
        ]
    },
    'parentless-teenager': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Night of Day 2',
        identificationFeatures: [
            'Neighbor uncle\'s daughter, confirmed human',
            'Comes to pick up neighbor uncle',
            'Will visit crying on night of Day 5'
        ],
        gameStrategy: [
            'Can safely allow entry',
            'Confirmed human identity'
        ]
    },
    'positive-guy': {
        nameCn: '',
        identityType: '×※',
        identityText: 'Identity Questioned (random in Demo, suspected human in full)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Man wearing "AMOG US" pattern T-shirt',
            'Abnormal nails, eyes and armpits if visitor',
            'Claims to be sports analyst'
        ],
        gameStrategy: [
            'Check nails, eyes and armpit features',
            'Demo requires careful judgment'
        ]
    },
    'protagonist': {
        nameCn: '',
        identityType: '-',
        identityText: 'Player Character',
        appearanceCondition: 'Always present',
        identificationFeatures: [
            'The player character'
        ],
        gameStrategy: [
            'Player character'
        ]
    },
    'raincoat-child': {
        nameCn: '',
        identityType: '-※',
        identityText: 'Suspected random appearance',
        appearanceCondition: 'Suspected random appearance after Day 7',
        identificationFeatures: [
            'Comes to door saying "saw kitchen light on"',
            'Then says "wrong house" and leaves'
        ],
        gameStrategy: [
            'Special plot character',
            'No need to judge identity'
        ]
    },
    'reporter': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Dirty hands when visitor',
            'Black spots on heart when human',
            'Hospital falls into chaos when appears as visitor'
        ],
        gameStrategy: [
            'Check hand and heart features',
            'Judge identity based on features'
        ]
    },
    'seductive-woman': {
        nameCn: '',
        identityType: '×※',
        identityText: 'Identity Questioned (suspected human)',
        appearanceCondition: 'Random appearance after Day 7',
        identificationFeatures: [
            'May know protagonist',
            'Will sleep with protagonist in bedroom if invited'
        ],
        gameStrategy: [
            'Suspected human identity',
            'Need careful judgment'
        ]
    },
    'stand-up-guy': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Swollen red eyes when visitor',
            'Dirty hands when human'
        ],
        gameStrategy: [
            'Check eye and hand features',
            'Judge identity based on features'
        ]
    },
    'stoner': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Random appearance after Day 7',
        identificationFeatures: [
            'Mouth sewn shut'
        ],
        gameStrategy: [
            'Confirmed human identity',
            'Can safely allow entry'
        ]
    },
    'suit-guy': {
        nameCn: '',
        identityType: '×※',
        identityText: 'Confirmed Human (though identity questioned)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Very clean teeth and drooping ears',
            'Confirmed human despite identity questions',
            'Extremely concerned with legal issues'
        ],
        gameStrategy: [
            'Confirmed human identity',
            'Can safely allow entry'
        ]
    },
    'sun-guy': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Cross-eyed male who worships the sun',
            'Red eyes when visitor',
            'Calls FEMA "heretics"'
        ],
        gameStrategy: [
            'Pay attention to eye color',
            'Red eyes indicate visitor status'
        ]
    },
    'surgeon': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Dirty hands when visitor',
            'Black spots on heart when human',
            'Hospital falls into chaos when appears as visitor'
        ],
        gameStrategy: [
            'Check hand and heart features',
            'Judge identity based on features'
        ]
    },
    'sweaty-man': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Will give kombucha in return for beer',
            'Moldy armpits when visitor',
            'Cannot cohabit with "widow"'
        ],
        gameStrategy: [
            'Check armpit features',
            'Mold indicates visitor status',
            'Note conflict with widow'
        ]
    },
    'theorist': {
        nameCn: '',
        identityType: '△',
        identityText: 'Random Identity (Human/Visitor)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Dirty hands when visitor',
            'Black spots on heart when human',
            'Hospital falls into chaos when appears as visitor'
        ],
        gameStrategy: [
            'Check hand and heart features',
            'Judge identity based on features'
        ]
    },
    'the-sisters': {
        nameCn: '',
        identityType: '△',
        identityText: 'Possibly Visitor',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Has a sister with depression'
        ],
        gameStrategy: [
            'Consider relationship with sister',
            'Comprehensive identity judgment'
        ]
    },
    'vigilante': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 9, Day 11',
        identificationFeatures: [
            'Day 11 will "inspect" player',
            'Triggers special ending if player shows abnormal features'
        ],
        gameStrategy: [
            'Key plot character',
            'Pay attention to own status features'
        ]
    },
    'weather-reporter': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Night of Day 2',
        identificationFeatures: [
            'Neighbor uncle\'s daughter, confirmed human',
            'Comes to pick up neighbor uncle',
            'Will visit crying on night of Day 5'
        ],
        gameStrategy: [
            'Can safely allow entry',
            'Confirmed human identity'
        ]
    },
    'widowed-woman': {
        nameCn: '',
        identityType: '×',
        identityText: 'Confirmed Human',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Visits carrying husband\'s body',
            'Eyes swollen and red from crying',
            'Confirmed human'
        ],
        gameStrategy: [
            'Can safely allow entry',
            'Confirmed human identity'
        ]
    },
    'wireface': {
        nameCn: '',
        identityType: '-',
        identityText: 'Special NPC that cannot enter home',
        appearanceCondition: 'Day 4, Day 6, Day 10, Day 12',
        identificationFeatures: [
            'Directly causes game over if player alone or claims "alone"',
            'Will stand somewhere on night of Day 3',
            'Will hold soldier\'s head on night of Day 5'
        ],
        gameStrategy: [
            'Absolutely cannot say alone',
            'Dangerous hostile character'
        ]
    },
    'wounded-man': {
        nameCn: '',
        identityType: '△※',
        identityText: 'Identity Questioned (possibly random)',
        appearanceCondition: 'Random appearance',
        identificationFeatures: [
            'Clean teeth, swollen red eyes, earwax when visitor'
        ],
        gameStrategy: [
            'Check multiple features comprehensively',
            'Judge identity based on feature combination'
        ]
    }
};


function createIdentificationStrategyHTML(characterData, characterKey) {
    if (!characterData) return '';

    const identityTypeSymbol = {
        '〇': '<span style="color: #00ff88;">●</span> Confirmed Visitor',
        '×': '<span style="color: #ff6b6b;">✕</span> Confirmed Human',
        '△': '<span style="color: #ffaa00;">▲</span> Random Identity',
        '-': '<span style="color: #888;">—</span> Special NPC',
        '○': '<span style="color: #00ff88;">●</span> Confirmed Visitor'
    };

    const identityType = identityTypeSymbol[characterData.identityType.replace('※', '')] || characterData.identityType;
    const hasDoubt = characterData.identityType.includes('※');

    return `
    <!-- Character Identification Strategy Section -->
    <section id="identification-strategy" class="character-section">
        <h2>🎯 Identification Strategy</h2>
        <div class="identification-strategy-content">
            <div class="identity-indicator">
                <h3>Identity Status</h3>
                <div class="identity-badge">
                    <span class="identity-symbol">${identityType}${hasDoubt ? '<span style="color: #ff6b6b; font-size: 0.8em;">※</span>' : ''}</span>
                    <span class="identity-text">${characterData.identityText}</span>
                </div>
            </div>

            <div class="appearance-condition">
                <h3>Appearance Conditions</h3>
                <p><strong>Timing:</strong> ${characterData.appearanceCondition}</p>
            </div>

            <div class="identification-features">
                <h3>Identification Features</h3>
                <ul class="feature-list">
                    ${characterData.identificationFeatures.map(feature => `<li>${feature}</li>`).join('')}
                </ul>
            </div>

            <div class="game-strategy">
                <h3>Game Strategy</h3>
                <ul class="strategy-list">
                    ${characterData.gameStrategy.map(strategy => `<li>${strategy}</li>`).join('')}
                </ul>
            </div>

            <div class=identity-symbols-legend>
                <h3>Identity Symbol Guide</h3>
                <div class=legend-grid>
                    <div class=legend-item>
                        <span class=symbol style=color: #00ff88;>●</span>
                        <span class=symbol-desc>Confirmed Visitor</span>
                    </div>
                    <div class=legend-item>
                        <span class=symbol style=color: #ff6b6b;>✕</span>
                        <span class=symbol-desc>Confirmed Human</span>
                    </div>
                    <div class=legend-item>
                        <span class=symbol style=color: #ffaa00;>▲</span>
                        <span class=symbol-desc>Random Identity</span>
                    </div>
                    <div class=legend-item>
                        <span class=symbol style=color: #888;>—</span>
                        <span class=symbol-desc>Special NPC</span>
                    </div>
                    <div class=legend-item>
                        <span class=symbol style=color: #ff6b6b; font-size: 0.8em;>※</span>
                        <span class=symbol-desc>Identity Uncertain</span>
                    </div>
                </div>
            </div>
        </div>
    </section>`;
}


function createChineseSourceAttribution() {
    return `
    <!--  -->
    <section class=content-attribution chinese-source>
        <h3>📖 </h3>
        <p></p>
        <div class=attribution-link>
            <a href=https:
                🎮  -   ↗
            </a>
        </div>
        <p class=translation-note></p>
    </section>`;
}

// Get character file list
function getCharacterFiles() {
    const charactersDir = path.join(__dirname,'guide', 'characters');
    const files = fs.readdirSync(charactersDir)
        .filter(file => file.endsWith('.html'))
        .map(file => file.replace('.html', ''));
    return files;
}

// Update single character page
function updateCharacterPage(characterKey) {
    const filePath = path.join(__dirname, 'guide', 'characters', `${characterKey}.html`);

    if (!fs.existsSync(filePath)) {
        console.log(`File not found: ${filePath}`);
        return false;
    }

    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const characterData = characterIdentificationData[characterKey];

        if (!characterData) {
            console.log(`No character data found: ${characterKey}`);
            return false;
        }

        // Find insertion point - after existing Identification Section
        const identificationSectionEnd = '</section>';
        const identificationSectionIndex = content.lastIndexOf(identificationSectionEnd);

        if (identificationSectionIndex === -1) {
            console.log(`Identification Section not found: ${characterKey}`);
            return false;
        }

        // Insert identification strategy section
        const insertPosition = identificationSectionIndex + identificationSectionEnd.length;
        const strategyHTML = createIdentificationStrategyHTML(characterData, characterKey);

        content = content.slice(0, insertPosition) + strategyHTML + content.slice(insertPosition);

  // Write to file
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Updated: ${characterKey}.html`);
        return true;

    } catch (error) {
        console.error(`❌ Failed to update ${characterKey}:`, error.message);
        return false;
    }
}

// Main function
function main() {
    console.log('🎮 Starting integration of character identification strategies...\n');

    const characterFiles = getCharacterFiles();
    console.log(`Found ${characterFiles.length} character files\n`);

    let successCount = 0;
    let failCount = 0;

    for (const characterKey of characterFiles) {
        if (updateCharacterPage(characterKey)) {
            successCount++;
        } else {
            failCount++;
        }
    }

    console.log(`\n✅ Successfully updated: ${successCount} files`);
    console.log(`❌ Failed: ${failCount} files`);
    console.log('\n🎯 Character identification strategy integration complete!');
}

// Run script directly
if (require.main === module) {
    main();
}

module.exports = {
    characterIdentificationData,
    createIdentificationStrategyHTML,
    createChineseSourceAttribution,
    updateCharacterPage
};