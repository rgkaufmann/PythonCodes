import numpy as np
import Player


class Firbolg(Player.Player):
    __AbilityImprovements = np.array([1, 0, 0, 0, 2, 0])

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress):
        Player.Player.__init__(self, name, classoption, alignment, background, exp, backstoryaddress)

        self.improvestats(self.__AbilityImprovements)
        self.calcsaves()
        self.calcskills()

        self._Player__Speeds = np.array([30, 0, 0, 0])
        self.addproficienies('Common')
        self.addproficienies('Elvish')
        self.addproficienies('Giant')

        self.addabilities('Firbolg Magic')
        self.addabilities('Hidden Step')
        self.addabilities('Powerful Build')
        self.addabilities('Speech of Beast and Leaf')
