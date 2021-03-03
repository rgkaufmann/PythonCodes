import numpy as np
import Player


class Aasimar(Player.Player):
    __AbilityImprovementsFallen = np.array([1, 0, 0, 0, 0, 2])
    __AbilityImprovementsProtector = np.array([0, 0, 0, 0, 1, 2])
    __AbilityImprovementsScourge = np.array([0, 0, 1, 0, 0, 2])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress, subrace):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        self.addabilities('Darkvision')
        self.addabilities('Celestial Resistance')
        self.addabilities('Healing Hands')
        self.addabilities('Light Bearer')

        self.__SubRace = subrace
        if subrace.lower() == 'fallen':
            self.improvestats(self.__AbilityImprovementsFallen)
            self.addabilities('Necrotic Shroud')
        elif subrace.lower() == 'protector':
            self.improvestats(self.__AbilityImprovementsProtector)
            self.addabilities('Radiant Soul')
        elif subrace.lower() == 'scourge':
            self.improvestats(self.__AbilityImprovementsScourge)
            self.addabilities('Radiant Consumption')
        else:
            print("Subrace " + subrace + " not acceptable subrace. Defaulting to base.")
            self.__SubRace = "Default"

            self.improvestats(self.__AbilityImprovementsProtector)
            self.removeabilities('Healing Hands')
            self.removeabilities('Light Bearer')
            self.addabilities('Celestial Legacy')
        self.calcsaves()
        self.calcskills()

        self._Player__Speeds = np.array([30, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Celestial')

    def getsubrace(self):
        return self.__SubRace
