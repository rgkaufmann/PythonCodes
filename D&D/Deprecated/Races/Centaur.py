import numpy as np
import Player


class Centaur(Player.Player):
    __AbilityImprovements = np.array([2, 0, 0, 0, 1, 0])
    __InitialSkill = ['animal handling', 'medicine', 'nature', 'survival']

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        self.improvestats(self.__AbilityImprovements)
        self.calcsaves()
        self.calcskills()

        self._Player__Speeds = np.array([40, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Sylvan')

        self.addabilities('Fey')
        self.addabilities('Charge')
        self.addabilities('Hooves')
        self.addabilities('Equine Build')

        pickedskill = ''
        while pickedskill.lower() not in self.__InitialSkill:
            print('From the survivor ability, you gain proficiency in one of the following skills:')
            print(self.__InitialSkill)
            pickedskill = input('Which skill would you like to pick? ')

            if pickedskill.lower() == self.__InitialSkill[0]:
                self.gainskillproficiency(1)
            elif pickedskill.lower() == self.__InitialSkill[1]:
                self.gainskillproficiency(9)
            elif pickedskill.lower() == self.__InitialSkill[2]:
                self.gainskillproficiency(10)
            elif pickedskill.lower() == self.__InitialSkill[3]:
                self.gainskillproficiency(17)
