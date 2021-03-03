import numpy as np
import Player


class Bugbear(Player.Player):
    __AbilityImprovements = np.array([2, 1, 0, 0, 0, 0])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        self.improvestats(self.__AbilityImprovements)
        self.calcsaves()
        self.calcskills()

        self._Player__Speeds = np.array([30, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Goblin')

        self.addabilities('Darkvision')
        self.addabilities('Long-Limbed')
        self.addabilities('Powerful Build')
        self.addabilities('Surprise Attack')

        self.gainskillproficiency(16)
