import numpy as np
import Player


class Aarakocra(Player.Player):
    __AbilityImprovements = np.array([0, 2, 0, 0, 1, 0])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)
        self.improvestats(self.__AbilityImprovements)
        self.calcsaves()
        self.calcskills()

        self._Player__Speeds = np.array([25, 50, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Aarakocra')
        self.addproficienies('Auran')

        self.addabilities('Talons')
