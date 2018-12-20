import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/ryank/Desktop/Work/Classes/Coding Projects/Monopoly/IntermediateMonopolyPython')
import Token as token

def chanceRoll(chanceNum, tile):
    movetile = [0, 1, 2, 3, 4, 7, 8, 11, 12]
    freecard = [6]
    if chanceNum in movetile:
        if chanceNum == 0:
            return 0
        elif chanceNum == 1:
            return 24
        elif chanceNum == 2:
            return 11
        elif chanceNum == 3:
            if tile in [22, 36]:
                return 28
            elif tile == 7:
                return 12
        elif chanceNum == 4:
            if tile == 7:
                return 15
            elif tile == 22:
                return 25
            elif tile == 36:
                return 5
        elif chanceNum == 7:
            return tile-3
        elif chanceNum == 8:
            global jail
            jail = True
            return 10
        elif chanceNum == 11:
            return 5
        elif chanceNum == 12:
            return 39
    elif chanceNum in freecard:
        global jailFree
        jailFree = True
        return tile
    else:
        return tile

def communityRoll(communityNum, tile):
    movetile = [0, 5]
    freetile = [4]
    if communityNum in movetile:
        if communityNum == 0:
            return 0
        elif communityNum == 5:
            global jail
            jail = True
            return 10
    if communityNum in freetile:
        global jailFree
        jailFree = True
        return tile
    else:
        return tile