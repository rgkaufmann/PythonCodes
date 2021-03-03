import numpy as np
import Player


class Genasi(Player.Player):
    __AbilityImprovementsA = np.array([0, 1, 2, 0, 0, 0])
    __AbilityImprovementsE = np.array([1, 0, 2, 0, 0, 0])
    __AbilityImprovementsF = np.array([0, 0, 2, 1, 0, 0])
    __AbilityImprovementsW = np.array([0, 0, 2, 0, 1, 0])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress, subrace):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        self._Player__Speeds = np.array([30, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Primordial')

        self.__SubRace = subrace.capitalize()
        if subrace.lower() == 'air':
            self.improvestats(self.__AbilityImprovementsA)

            self.addabilities('Unending Breath')
            self.addabilities('Mingle with the Wind')
        elif subrace.lower() == 'earth':
            self.improvestats(self.__AbilityImprovementsE)

            self.addabilities('Earth Walk')
            self.addabilities('Merge with Stone')
        elif subrace.lower() == 'fire':
            self.improvestats(self.__AbilityImprovementsF)

            self.addabilities('Darkvision')
            self.addabilities('Fire Resistance')
            self.addabilities('Reach to the Blaze')
        elif subrace.lower() == 'water':
            self.improvestats(self.__AbilityImprovementsW)

            self.addabilities('Amphibious')
            self.addabilities('Acid Resistance')
            self.addabilities('Call to the Wave')

            self._Player__Speeds = np.array([30, 0, 30, 0])
        else:
            print("Subrace " + subrace.capitalize() + " not acceptable subrace. Defaulting to Air.")
            self.__SubRace = "Air"

            self.improvestats(self.__AbilityImprovementsA)

            self.addabilities('Unending Breath')
            self.addabilities('Mingle with the Wind')
        self.calcsaves()
        self.calcskills()

    def getsubrace(self):
        return self.__SubRace
