RACES = ['Aarakocra',
         'Aasimar',
         'Bugbear',
         'Centaur',
         'Changeling',
         'Dragonborn',
         'Dwarf',
         'Elf',
         'Firbolg',
         'Genasi',
         'Gith',
         'Gnome',
         'Goblin',
         'Goliath',
         'Half-Elf',
         'Half-Orc',
         'Halfling',
         'Hobgoblin',
         'Human',
         'Kalashtar',
         'Kenku',
         'Kobold',
         'Lizardfolk',
         'Loxodon',
         'Minotaur',
         'Orc',
         'Shifter',
         'Simic Hybrid',
         'Tabaxi',
         'Tiefling',
         'Triton',
         'Vedalken',
         'Verdan',
         'Warforged',
         'Yuan-ti Pureblood']

MONSTERRACES = ['Bugbear',
                'Goblin',
                'Hobgoblin',
                'Kobold',
                'Orc',
                'Yuan-ti Pureblood']

SUBRACES = {'Aarakocra':         [],
            'Aasimar':           ['Fallen', 'Protector', 'Scourge'],
            'Bugbear':           [],
            'Centaur':           [],
            'Changeling':        [],
            'Dragonborn':        [],
            'Dwarf':             ['Duergar', 'Hill', 'Mark of Warding', 'Mountain'],
            'Elf':               ['Drow', 'Eladrin', 'High', 'Mark of Shadow', 'Sea', 'Shadar-kai', 'Wood'],
            'Firbolg':           [],
            'Genasi':            ['Air', 'Earth', 'Fire', 'Water'],
            'Gith':              ['Githyanki', 'Githzerai'],
            'Gnome':             ['Deep', 'Forest', 'Mark of Scribing', 'Rock'],
            'Goblin':            [],
            'Goliath':           [],
            'Half-Elf':          ['Original', 'Aquatic Elf Descent', 'Drow Descent', 'Mark of Detection', 'Mark of Storm', 'Moon/Sun Elf Descent', 'Wood Elf Descent'],
            'Half-Orc':          ['Original', 'Mark of Finding'],
            'Halfling':          ['Ghostwise', 'Lightfoot', 'Mark of Healing', 'Mark of Hospitality', 'Stout'],
            'Hobgoblin':         [],
            'Human':             ['Original', 'Mark of Finding', 'Mark of Handling', 'Mark of Making', 'Mark of Passage', 'Mark of Setinel', 'Variant'],
            'Kalashtar':         [],
            'Kenku':             [],
            'Kobold':            [],
            'Lizardfolk':        [],
            'Loxodon':           [],
            'Minotaur':          [],
            'Orc':               [],
            'Shifter':           ['Beasthide', 'Longtooth', 'Swiftstride', 'Wildhunt'],
            'Simic Hybrid':      [],
            'Tabaxi':            [],
            'Tiefling':          ['Original', 'Asmodeus', 'Baalzebul', 'Dispater', 'Fierna', 'Glasya', 'Levistus', 'Mammon', 'Mephistopheles', 'Variant', 'Zariel'],
            'Triton':            [],
            'Vedalken':          [],
            'Verdan':            [],
            'Warforged':         [],
            'Yuan-ti Pureblood': []}

# Stats, Speed, Age, Size, Language, Proficiencies, Skills, Abilities

CLASSES = ['Artificer',
           'Barbarian',
           'Bard',
           'Cleric',
           'Druid',
           'Fighter',
           'Monk',
           'Mystic',
           'Paladin',
           'Ranger',
           'Rogue',
           'Sorcerer',
           'Warlock',
           'Wizard']

HALFCASTER = ['Artificer',
              'Paladin',
              'Ranger']

FULLCASTER = ['Bard',
              'Cleric',
              'Druid',
              'Sorcerer',
              'Warlock',
              'Wizard']

SUBCLASSES = {'Artificer': ['Alchemist', 'Artillerist', 'Battle Smith'],
              'Barbarian': ['Ancestral Guardian', 'Battlerager', 'Beast', 'Berserker', 'Storm Herald', 'Totem Warrior', 'Wild Soul', 'Zealot'],
              'Bard':      ['Eloquence', 'Glamour', 'Lore', 'Satire', 'Swords', 'Valor', 'Whispers'],
              'Cleric':    ['Ambition', 'Arcana', 'Beauty', 'City', 'Darkness', 'Death', 'Destruction', 'Forge', 'Grave', 'Knowledge', 'Life', 'Light', 'Nature', 'Order', 'Preotection', 'Solidarity', 'Strength', 'Tempest', 'Trickery', 'Twilight', 'War', 'Zeal'],
              'Druid':     ['Dreams', 'Land', 'Moon', 'SHepherd', 'Spores', 'Twilight', 'Wildfire'],
              'Fighter':   ['Arcane Archer', 'Battle Master', 'Brute', 'Cavalier', 'Champion', 'Eldritch Knight', 'Samurai', 'Scout', 'Sharpshooter', 'Slayer', 'Warlord', 'Weapon Master'],
              'Monk':      ['Astral Self', 'Drunken Master', 'Four Elements', 'Kensei', 'Long Death', 'Mercy', 'Open Hand', 'Shadow', 'Soul Knife', 'Sun Soul', 'Tranquility'],
              'Mystic':    ['Avatar', 'Awakened', 'Immortal', 'Nomad', 'Soul Knife', 'Wu Jen'],
              'Paladin':   ['Ancients', 'Conquest', 'Crown', 'Devotion', 'Heroism', 'Oathbreaker', 'Redemption', 'Treachery', 'Vengeance', 'Watchers'],
              'Ranger':    ['Beast Master', 'Gloom Stalker', 'Horizon Walker', 'Hunter', 'Monster Slayer', 'Primeval Guardian', 'Swarmkeeper'],
              'Rogue':     ['Acrobat', 'Arcane Trickster', 'Assassin', 'Inquisitive', 'Mastermind', 'Revived', 'Scout', 'Soul Knife', 'Swashbuckler', 'Thief'],
              'Sorcerer':  ['Aberrant Mind', 'Divine Soul', 'Draconic', 'Giant Soul', 'Phoenix', 'Pyromancer', 'Sea', 'Shadow', 'Stone', 'Storm', 'Wild'],
              'Warlock':   ['Archfey', 'Celestial', 'Fiend', 'Ghost in the Machine', 'Great Old One', 'Hexblade', 'Kraken', 'Lolth', 'Lurker in the Deep', 'Noble Genie', 'Raven Queen', 'Seeker', 'Undying'],
              'Wizard':    ['Abjuration', 'Artificer', 'Bladesinging', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Invention', 'Lore Mastery', 'Necromancy', 'Onomancy', 'Psionics', 'Technomancy', 'Theurgy', 'Transmutation', 'War Magic']}

ALIGNMENTS = ['Lawful Good',
              'Lawful Neutral',
              'Lawful Evil',
              'Neutral Good',
              'True Neutral',
              'Neutral Evil',
              'Chaotic Good',
              'Chaotic Neutral',
              'Chaotic Evil']

STANDARDALIGNMENTS = {'Aarakocra':         ['green', 'orange', 'red',
                                            'green', 'orange', 'red',
                                            'green', 'orange', 'red'],
                      'Aasimar':           ['green', 'red', 'orange',
                                            'green', 'red', 'orange',
                                            'green', 'red', 'orange'],
                      'Bugbear':           ['red',    'red',    'red',
                                            'red',    'red',    'orange',
                                            'orange', 'orange', 'green'],
                      'Centaur':           ['red',   'orange', 'red',
                                            'green', 'green',  'green',
                                            'red',   'orange', 'red'],
                      'Changeling':        ['red',   'red',   'red',
                                            'red',   'green', 'red',
                                            'green', 'green', 'green'],
                      'Dragonborn':        ['green',  'orange', 'red',
                                            'orange', 'red',    'orange',
                                            'red',    'orange', 'green'],
                      'Dwarf':             ['green',  'green', 'orange',
                                            'orange', 'red',   'red',
                                            'red',    'red',   'red'],
                      'Elf':               ['red',    'red',    'red',
                                            'orange', 'orange', 'red',
                                            'green',  'green',  'green'],
                      'Firbolg':           ['orange', 'red',    'red',
                                            'green',  'orange', 'red',
                                            'red',    'red',    'red'],
                      'Genasi':            ['red',    'orange', 'red',
                                            'orange', 'green',  'orange',
                                            'red',    'orange', 'red'],
                      'Gith':              ['red', 'green',  'green',
                                            'red', 'orange', 'orange',
                                            'red', 'red',    'red'],
                      'Gnome':             ['orange', 'red',   'red',
                                            'green',  'green', 'green',
                                            'orange', 'red',   'red'],
                      'Goblin':            ['red',    'red',    'red',
                                            'orange', 'orange', 'green',
                                            'red',    'red',    'red'],
                      'Goliath':           ['orange', 'green',  'orange',
                                            'red',    'orange', 'red',
                                            'red',    'red',    'red'],
                      'Half-Elf':          ['red',   'red',    'red',
                                            'red',   'orange', 'red',
                                            'green', 'green',  'green'],
                      'Half-Orc':          ['red',   'red',   'red',
                                            'red',   'red',   'orange',
                                            'green', 'green', 'green'],
                      'Halfling':          ['green',  'orange', 'red',
                                            'orange', 'red',    'red',
                                            'orange', 'red',    'red',],
                      'Hobgoblin':         ['orange', 'orange', 'green',
                                            'red',    'red',    'orange',
                                            'red',    'red',    'red'],
                      'Human':             ['green', 'green', 'green',
                                            'green', 'green', 'green',
                                            'green', 'green', 'green'],
                      'Kalashtar':         ['green',  'orange', 'orange',
                                            'orange', 'red',    'red',
                                            'red',    'red',    'red'],
                      'Kenku':             ['red',    'red',    'red',
                                            'red',    'orange', 'red',
                                            'orange', 'green',  'orange'],
                      'Kobold':            ['red', 'orange', 'green',
                                            'red', 'orange', 'orange',
                                            'red', 'red',    'red'],
                      'Lizardfolk':        ['red',    'orange', 'red',
                                            'orange', 'green',  'orange',
                                            'red',    'orange', 'red'],
                      'Loxodon':           ['green',  'orange', 'orange',
                                            'orange', 'red',    'red',
                                            'red',    'red',    'red'],
                      'Minotaur':          ['orange', 'green', 'red',
                                            'red',    'red',   'red',
                                            'red',    'green', 'orange'],
                      'Orc':               ['red',    'red',    'red',
                                            'red',    'red',    'orange',
                                            'orange', 'orange', 'green'],
                      'Shifter':           ['red',    'red',    'red',
                                            'orange', 'green',  'orange',
                                            'red',    'orange', 'red'],
                      'Simic Hybrid':      ['red',    'orange', 'red',
                                            'orange', 'green',  'orange',
                                            'red',    'orange', 'red'],
                      'Tabaxi':            ['red',    'red',    'red',
                                            'orange', 'red',    'red',
                                            'green',  'orange', 'orange'],
                      'Tiefling':          ['red'     'red',   'red',
                                            'orange', 'red',   'orange',
                                            'orange', 'green', 'green'],
                      'Triton':            ['green',  'orange', 'orange',
                                            'orange', 'red',    'red',
                                            'red',    'red',    'red'],
                      'Vedalken':          ['green',  'orange', 'orange',
                                            'orange', 'red',    'red',
                                            'red',    'red',    'red'],
                      'Verdan':            ['orange', 'red',    'red',
                                            'green',  'orange', 'red',
                                            'orange', 'red',    'red'],
                      'Warforged':         ['orange', 'green',  'orange',
                                            'red',    'orange', 'red',
                                            'red',    'red',    'red'],
                      'Yuan-ti Pureblood': ['red',    'red',    'red',
                                            'orange', 'orange', 'green',
                                            'red',    'red',    'red']}

EXPLEVELS = [0,
             300,
             900,
             2700,
             6500,
             14000,
             23000,
             34000,
             48000,
             64000,
             85000,
             100000,
             120000,
             140000,
             165000,
             195000,
             225000,
             265000,
             305000,
             355000]
