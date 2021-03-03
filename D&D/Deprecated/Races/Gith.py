import numpy as np
import Player


class Gith(Player.Player):
    __AbilityImprovementsY = np.array([2, 0, 0, 1, 0, 0])
    __AbilityImprovementsZ = np.array([0, 0, 0, 1, 2, 0])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress, subrace):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        self._Player__Speeds = np.array([30, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Gith')

        self.__SubRace = subrace.capitalize()
        if subrace.lower() == 'githyanki':
            self.improvestats(self.__AbilityImprovementsY)

            self.addproficienies('Light Armor')
            self.addproficienies('Medium Armor')



            self.addabilities('Githyanki Psionics')
        elif subrace.lower() == 'githzerai':
            self.improvestats(self.__AbilityImprovementsZ)

            self.addabilities('Earth Walk')
            self.addabilities('Merge with Stone')
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
