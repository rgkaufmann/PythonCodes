import numpy as np
import Player
import VariousLists as VL


class Firbolg(Player.Player):
    __AbilityImprovementsDex = np.array([0, 1, 0, 0, 0, 2])
    __AbilityImprovementsInt = np.array([0, 0, 0, 1, 0, 2])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        dexorint = input('Would you like to improve Intelligence or Dexterity?')
        while dexorint.capitalize() != "Dex" and dexorint.capitalize() != "Int":
            print('Input not understood.\n')
            dexorint = input('Would you like to improve Intelligence or Dexterity?')
        if dexorint.capitalize() == 'Dex':
            self.improvestats(self.__AbilityImprovementsDex)
        elif dexorint.capitalize() == 'Int':
            self.improvestats(self.__AbilityImprovementsInt)
        self.calcsaves()
        self.calcskills()

        self._Player__Speeds = np.array([30, 0, 0, 0])
        self.addproficienies('Common')
        for newlang in range(2):
            newlanguage = input('You have ' + str(2-newlang) + ' languages you can learn. What language would you like '
                                                               'to know?')
            while (newlanguage.capitalize() not in VL.BasicLanguages) and (newlanguage.capitalize() not in
                                                                           VL.ExoticLanguages):
                print('Input not understood.\n')
                newlanguage = input('You have ' + str(2 - newlang) + ' languages you can learn. What language would you'
                                                                     ' like to know?')
                self.addproficienies(newlanguage)

        self.addabilities('Change Apperance')
        self.addabilities('Unsettling Visage')
        self.addabilities('Divergent Persona')

