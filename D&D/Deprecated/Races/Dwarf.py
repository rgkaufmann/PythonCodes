import numpy as np
import Player


class Dwarf(Player.Player):
    __AbilityImprovementsD = np.array([1, 0, 2, 0, 0, 0])
    __AbilityImprovementsH = np.array([0, 0, 2, 0, 1, 0])
    __AbilityImprovementsM = np.array([2, 0, 2, 0, 0, 0])
    __InitialTool = ["smith's tools", "brewer's supplies", "mason's tools"]

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress, subrace):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        self._Player__Speeds = np.array([25, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Dwarvish')

        self.addproficienies('Battleaxe')
        self.addproficienies('Handaxe')
        self.addproficienies('Light Hammer')
        self.addproficienies('Warhammer')

        pickedskill = ''
        while pickedskill.lower() not in self.__InitialTool:
            print('From the survivor ability, you gain proficiency in one of the following skills:')
            print(self.__InitialTool)
            pickedskill = input('Which skill would you like to pick? ')

            if pickedskill.lower() == self.__InitialTool[0]:
                self.addproficienies(pickedskill.capitalize())
            elif pickedskill.lower() == self.__InitialTool[1]:
                self.addproficienies(pickedskill.capitalize())
            elif pickedskill.lower() == self.__InitialTool[2]:
                self.addproficienies(pickedskill.capitalize())

        self.addabilities('Darkvision')
        self.addabilities('Dwarven Resilience')

        self.__SubRace = subrace.capitalize()
        if subrace.lower() == 'duergar':
            self.improvestats(self.__AbilityImprovementsD)

            self.removeabilities('Darkvision')
            self.removeabilities('Drawven Resilience')

            self.addabilities('Superior Darkvision')
            self.addabilities('Duergar Resilience')
            self.addabilities('Duergar Magic')
            self.addabilities('Sunlight Sensitivity')

            self.addproficienies('Undercommon')
        elif subrace.lower() == 'hill':
            self.improvestats(self.__AbilityImprovementsH)

            self.addhp(sum(self.getlevel()))
        elif subrace.lower() == 'mountain':
            self.improvestats(self.__AbilityImprovementsM)

            self.addproficienies('Light Armor')
            self.addproficienies('Medium Armor')
        else:
            print("Subrace " + subrace.capitalize() + " not acceptable subrace. Defaulting to Hill.")
            self.__SubRace = "Hill"

            self.improvestats(self.__AbilityImprovementsH)

            self.addhp(sum(self.getlevel()))
        self.calcsaves()
        self.calcskills()

    def getsubrace(self):
        return self.__SubRace
