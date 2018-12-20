import numpy as np

Classes = np.array(['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                    'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock',
                    'Wizard'])
Archetypes = np.array([6, 6, 18, 6, 11, 8, 6, 6, 7, 10, 9, 15])
PrimalPaths = np.array(['Path of the Ancestral Guardian',
                        'Path of the Battlerager', 'Path of the Berserker',
                        'Path of the Storm Herald',
                        'Path of the Totem Warrior', 'Path of the Zealot'])
Colleges = np.array(['College of Glamour', 'College of Lore',
                     'College of Satire', 'College of Swords',
                     'COllege of Valor', 'College of Whispers'])
DivineDomains = np.array(['Arcana Domain', 'Ambition Domain', 'City Domain',
                          'Death Domain', 'Forge Domain', 'Grave Domain',
                          'Knowledge Domain', 'Life Domain', 'Light Domain',
                          'Nature Domain', 'Order Domain', 'Protection Domain',
                          'Solidarity Domain', 'Strength Domain',
                          'Tempest Domain', 'Trickery Domain', 'War Domain',
                          'Zeal Domain'])
DruidCircles = np.array(['Circle of Dreams', 'Circle of the Land',
                         'Circle of the Moon', 'Circle of the Shepherd',
                         'Circle of Spores', 'Circle of Twilight'])
MartialArchetypes = np.array(['Arcane Archer', 'Battle Master', 'Brute',
                              'Cavalier', 'Champion', 'Eldritch Knight',
                              'Monster Hunter', 'Purple Dragon Knight',
                              'Samurai', 'Scout', 'Sharpshooter'])
MonasticTraditions = np.array(['Way of the Drunken master',
                               'Way of the Four Elements', 'Way of the Kensei',
                               'Way of the Long Death', 'Way of the Open Hand',
                               'Way of the Shadow', 'Way of the Sun Soul',
                               'Way of Tranquility'])
SacredOaths = np.array(['Oath of the Ancients', 'Oath of Conquest',
                        'Oath of the Crown', 'Oath of Devotion',
                        'Oath of Redemption', 'Oath of Vengeance'])
RangerArchetypes = np.array(['Beast Master', 'Gloom Stalker', 'Horizon Walker',
                             'Hunter', 'Monster Slayer', 'Primeval Guardian'])
RoguishArchetypes = np.array(['Arcane Trickster', 'Assassin', 'Inquisitive',
                              'Mastermind', 'Scout', 'Swashbuckler', 'Thief'])
SorcerousOrigin = np.array(['Divine Soul', 'Draconic Bloodline', 'Giant Soul',
                            'Phoenix Sorcery', 'Pyromancer', 'Sea Sorcery',
                            'Shadow Magic', 'Stone Sorcery', 'Storm Sorcery',
                            'Wild Magic'])
OtherworldlyPatron = np.array(['The Archfey', 'The Celestial', 'The Fiend',
                               'The Ghost in the Machine', 'The Great Old One',
                               'The Hexblade', 'The Raven Queen', 'The Seeker',
                               'The Undying'])
ArcaneTraditions = np.array(['Artificer', 'Bladesinging', 'Lore Mastery',
                             'School of Abjuration', 'School of Conjuration',
                             'School of Divination', 'School of Enchantment',
                             'School of Evocation', 'School of Illusion',
                             'School of Invention', 'School of Necromancy',
                             'School of Transmutation', 'Technomancy',
                             'Theurgy', 'War Magic'])
ClassOptionsDict = {'Barbarian':PrimalPaths, 'Bard':Colleges,
                    'Cleric':DivineDomains, 'Druid':DruidCircles,
                    'Fighter':MartialArchetypes, 'Monk':MonasticTraditions,
                    'Paladin':SacredOaths, 'Ranger':RangerArchetypes,
                    'Rogue':RoguishArchetypes, 'Sorcerer':SorcerousOrigin,
                    'Warlock':OtherworldlyPatron, 'Wizard':ArcaneTraditions}

def ChooseClass():
    global Classes
    global Archetypes
    prompt = "That answer doesn't make sense. Please answer again. "

    print('\nThe following are the valid classes for your campaign:')
    print('Class\t\t\tSubclasses')
    print('----------------------------------')
    for index in range(len(Classes)):
        tabular = Classes[index]
        tabular += '\t'*int(3-np.floor(len(tabular)/8))
        print(tabular+str(Archetypes[index]))

    random = str(input('Would you like a random class? '))
    while random.lower() not in ['no', 'yes']:
        random = str(input(prompt))
    
    if random.lower()=='yes':
        pickClass = int(len(Classes)*np.random.rand())
        pickOption = int(len(ClassOptionsDict[Classes[pickClass]])*np.random.rand())
        Class = ClassOptionsDict[Classes[pickClass]][pickOption]+' '+Classes[pickClass]
    elif random.lower()=='no':
        Class = str(input('What class would you like to play? Please match the case. '))
        while Class not in Classes:
            Class = str(input(prompt))
        print('The following are the valid subclasses for {}s.'.format(Class))
        print('Subclass')
        print('-----------------------------')
        for option in ClassOptionsDict[Class]:
            print(option)
        Option = str(input('What archetype would you like to play? Please match the case. '))
        while Option not in ClassOptionsDict[Class]:
            Option = str(input(prompt))
        Class = Option+' '+Class
            
    return Class