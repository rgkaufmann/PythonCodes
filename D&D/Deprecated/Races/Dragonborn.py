import numpy as np
import Player


class Dragonborn(Player.Player):
    __AbilityImprovements = np.array([2, 0, 0, 0, 0, 1])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress, subrace):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)
        self.improvestats(self.__AbilityImprovements)
        self.calcsaves()
        self.calcskills()

        self.__SubRace = subrace.capitalize()
        if subrace.lower() == 'black':
            self.__DamageType = 'Acid'
            self.__Breath = '5x30 line, Dex'
        elif subrace.lower() == 'blue':
            self.__DamageType = 'Lightning'
            self.__Breath = '5x30 line, Dex'
        elif subrace.lower() == 'brass':
            self.__DamageType = 'Fire'
            self.__Breath = '5x30 line, Dex'
        elif subrace.lower() == 'bronze':
            self.__DamageType = 'Lightning'
            self.__Breath = '5x30 line, Dex'
        elif subrace.lower() == 'copper':
            self.__DamageType = 'Acid'
            self.__Breath = '5x30 line, Dex'
        elif subrace.lower() == 'gold':
            self.__DamageType = 'Fire'
            self.__Breath = '15 cone, Dex'
        elif subrace.lower() == 'green':
            self.__DamageType = 'Poison'
            self.__Breath = '15 cone, Con'
        elif subrace.lower() == 'red':
            self.__DamageType = 'Fire'
            self.__Breath = '15 cone, Dex'
        elif subrace.lower() == 'silver':
            self.__DamageType = 'Cold'
            self.__Breath = '15 cone, Con'
        elif subrace.lower() == 'white':
            self.__DamageType = 'Cold'
            self.__Breath = '15 cone, Con'
        else:
            print("Draconic Ancestry " + subrace.capitalize() + " not acceptable. Defaulting to Brass.")
            self.__SubRace = "Brass"
            self.__DamageType = 'Fire'
            self.__Breath = '5x30 line, Dex'

        self._Player__Speeds = np.array([30, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Draconic')

        self.addabilities('Breath Weapon')
        self.addabilities('Damage Resistance')

    def getsubrace(self):
        return self.__SubRace
