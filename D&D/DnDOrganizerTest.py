#import Tkinter as tk
import numpy as np
import sys
sys.path.append('/Users/ryank/Desktop/Work/Classes/Coding Projects/D&D/Character Options')
import RaceOptions as RO
import ClassOptions as CO

def RollStats():
    stats = np.ones(6)
    for index in range(len(stats)):
        rolls = np.random.randint(1, 7, 4)
        rolls = np.delete(rolls, np.where(rolls==min(rolls))[0][0])
        stats[index] = sum(rolls)
    return stats

def ApplyRacialBonus(stats, race):
    try:
        filename = '/Users/ryank/Desktop/Work/Classes/Coding Projects/D&D/Race Files/'
        filename += race
        filename += '.txt'
        file = open(filename, 'r')
        FullFile = file.readlines()
        chooseStat = 'none'
        for indx in range(6):
            if FullFile[3+indx][-3]==',':
                addition = int(FullFile[3+indx][-2])
            else:
                addition = float(FullFile[3+indx][-4:-1])
            if addition==0.5 and chooseStat=='none':
                chooseStat = list(stats.keys())[indx]
            elif addition==0.5:
                prompt = 'Choose to put 1 in {} or {}. '
                statUpgrade = str(input(prompt.format(chooseStat, list(stats.keys())[indx]))).upper()
                stats[statUpgrade] += 1
            else:
                stats[list(stats.keys())[indx]] += addition
        return stats
    except FileNotFoundError:
        return stats
    
def AssignStats(stats):
    statList = ['str', 'dex', 'con', 'int', 'wis']
    newStats = {}
    for statType in statList:
        print('Avaliable Numbers: '+str(stats))
        prompt = 'What number would you like to put in the {} place? '
        statNum = int(input(prompt.format(statType.upper())))
        while statNum not in stats:
            statNum = int(input('That is not an avaliable number.'))
        stats = np.delete(stats, np.where(stats==statNum)[0][0])
        newStats[statType.upper()] = statNum
    newStats['CHA'] = int(stats[0])
    return newStats

Race = RO.ChooseRace()
Class = CO.ChooseClass()
CharacterStats = RollStats()

print()
print(Race+', '+Class)

CharacterStats = ApplyRacialBonus(AssignStats(CharacterStats), Race)

print(CharacterStats)