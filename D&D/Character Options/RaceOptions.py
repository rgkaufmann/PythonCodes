import numpy as np

Races = np.array(['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling',
                  'Dragonborn', 'Dwarf', 'Elf', 'Firbolg', 'Genasi', 'Gith',
                  'Gnome', 'Goblin', 'Goliath', 'Half-Elf', 'Halfling',
                  'Half-Orc', 'Hobgoblin', 'Human', 'Kalashtar', 'Kenku',
                  'Kobold', 'Lizardfolk', 'Loxodon', 'Minotaur', 'Orc',
                  'Shifter', 'Simic Hybrid', 'Tabaxi', 'Tiefling', 'Tortle',
                  'Triton', 'Vedalken', 'Viashino', 'Warforged', 
                  'Yuan-ti Pureblood'])
Variants = np.array([False, True, False, False, False, False, True, True,
                     False, True, True, True, False, False, True, True,
                     True, False, True, False, False, False, False, False,
                     False, False, True, False, False, True, False, False,
                     False, False, True, False])
Monster = np.array([False, False, True, False, False, False, False, False,
                    False, False, True, False, True, False, False, False,
                    False, True, False, False, False, True, False, False,
                    True, True, False, True, False, False, False, False, False,
                    True, False, True])

AasimarVariants=np.array(['Protector', 'Scourge', 'Fallen'])
DwarfVariants=np.array(['Hill', 'Mountain', 'House Kundarak'])
ElfVariants=np.array(['Avariel', 'Dark', 'Eladrin', 'Grugach', 'High', 'Sea',
                      'Shadar-kai', 'Wood', 'Bishtahar/Tirahar', 'Vadahar',
                      'Tajuru', 'Joraga', 'Mul Daya'])
GenasiVariants=np.array(['Air', 'Earth', 'Fire', 'Water'])
GithVariants=np.array(['Githyanki', 'Githzerai'])
GnomeVariants=np.array(['Deep', 'Forest', 'Rock'])
HalfElfVariants=np.array(['Versatile', 'Keen', 'Wood', 'High', 'Drow',
                          'Aquatic'])
HalflingVariants=np.array(['Ghostwise', 'Lightfoot', 'Stout'])
HalfOrcVariants=np.array(['Traditional', 'Mark of Finding'])
HumanVariants=np.array(['Traditional', 'Variant', 'Gavony', 'Kessig',
                        'Nephalia', 'Stensia'])
ShifterVariants=np.array(['Beasthide', 'Longtooth', 'Swiftstride', 'Wildhunt'])
TieflingVariants=np.array(['Abyssal', 'Baalzebul', 'Dispater', 'Fierna',
                           'Glasya', 'Levistus', 'Mammon', 'Mephistopheles',
                           'Feral', 'Zariel'])
WarforgedVariants=np.array(['Envoy', 'Juggernaut', 'Skirmisher'])

VariantDict={'Aasimar':AasimarVariants, 'Dwarf':DwarfVariants,
             'Elf':ElfVariants, 'Genasi':GenasiVariants, 'Gith':GithVariants,
             'Gnome':GnomeVariants, 'Half-Elf':HalfElfVariants,
             'Halfling':HalflingVariants, 'Half-Orc':HalfOrcVariants,
             'Human':HumanVariants, 'Shifter':ShifterVariants,
             'Tiefling':TieflingVariants, 'Warforged':WarforgedVariants}

def ChooseRace():
    global Races
    global Variants
    global Monster
    prompt = "That answer doesn't make sense. Please answer again. "
    
    monsterCampaign = str(input("Are you playing a monstrous campaign? "))
    while monsterCampaign.lower() not in ['no', 'yes']:
        monsterCampaign = str(input(prompt))
    
    if monsterCampaign.lower()=='no':
        Races=Races[np.where(np.invert(Monster))]
        Variants=Variants[np.where(np.invert(Monster))]
        Monster=Monster[np.where(np.invert(Monster))]
    elif monsterCampaign.lower()=='yes':
        Races=Races[np.where(Monster)]
        Variants=Variants[np.where(Monster)]
        Monster=Monster[np.where(Monster)]

    print('\nThe following are the valid races for your campaign:')
    print('Race Option\t\tVariation?')
    print('----------------------------------')
    for index in range(len(Races)):
        tabular = Races[index]
        tabular += '\t'*int(3-np.floor(len(tabular)/8))
        print(tabular+str(Variants[index]))

    random = str(input('Would you like a random race? '))
    while random.lower() not in ['no', 'yes']:
        random = str(input(prompt))
    
    if random.lower()=='yes':
        pickRace = int(len(Races)*np.random.rand())
        if Variants[pickRace]:
            pickVariant = int(len(VariantDict[Races[pickRace]])*np.random.rand())
            Race = VariantDict[Races[pickRace]][pickVariant]+' '+Races[pickRace]
        else:
            Race = Races[pickRace]
    elif random.lower()=='no':
        Race = str(input('What race would you like to play? Please match the case. '))
        while Race not in Races:
            Race = str(input(prompt))
        if Variants[np.where(Races==Race)]:
            print('The following are the valid subraces for a {}.'.format(Race))
            print('Variant')
            print('--------------------------')
            for variation in VariantDict[Race]:
                print(variation)
            Variant = str(input('What variant would you like to play? Please match the case. '))
            while Variant not in VariantDict[Race]:
                Variant = str(input(prompt))
            Race = Variant+' '+Race
            
    return Race