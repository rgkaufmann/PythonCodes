import numpy as np
import DiceRoller


class Player:
    __LevelNumbers = {1: 0, 2: 300, 3: 900, 4: 2700, 5: 6500, 6: 14000, 7: 23000, 8: 34000, 9: 48000, 10: 64000,
                      11: 85000, 12: 100000, 13: 120000, 14: 140000, 15: 165000, 16: 195000, 17: 225000,
                      18: 265000, 19: 305000, 20: 355000}

    def __init__(self, name, classoption, alignment, background, exp, backstoryaddress):
        self.__Name = name
        self.__Class = [classoption]
        self.__Alignment = alignment
        self.__Background = background
        self.__EXP = exp
        self.__Level = [0]
        for lvl in range(20):
            if self.__LevelNumbers[lvl + 1] > exp:
                self.__Level = [lvl]
                break
        self.__ProficiencyBonus = int(np.floor((sum(self.__Level) - 1) / 4) + 2)
        self.__AC = 10
        self.__HP = 0
        self.__Proficiencies = []
        self.__Abilities = []
        self.__Equipment = []
        self.__Spells = []
        self.__Stats = DiceRoller.charactercreation()
        self.__SaveProficiencies = np.array([0, 0, 0, 0, 0, 0])
        self.__AbilityProficiencies = np.zeros(18, dtype=np.int8)
        self.__Speeds = np.array([0, 0, 0, 0])
        self.__Money = np.array([0, 0, 0, 0])
        self.__BackStoryAddress = backstoryaddress

    def addabilities(self, newability):
        self.__Abilities.append(newability)

    def addclass(self, newclass):
        self.__Class.append(newclass)

    def addequipment(self, newequipment):
        self.__Equipment.append(newequipment)

    def addexp(self, newexp):
        self.__EXP = self.__EXP + newexp

    def addhp(self, newhp):
        self.__HP = self.__HP + newhp

    def addlevel(self, newlevel):
        self.__Level.append(newlevel)

    def addproficienies(self, newproficiency):
        self.__Proficiencies.append(newproficiency)

    def addspells(self, newspell):
        self.__Spells.append(newspell)

    def calcsaves(self):
        self.__SaveProficiencies = np.floor((self.__Stats - 10 * np.ones(6, dtype=np.int8)) / 2).astype(np.int8)

    def calcskills(self):
        self.__AbilityProficiencies[3] = int(np.floor((self.__Stats[0] - 10) / 2))
        self.__AbilityProficiencies[np.array([0, 15, 16])] = int(np.floor((self.__Stats[1] - 10) / 2))
        self.__AbilityProficiencies[np.array([2, 5, 8, 10, 14])] = int(np.floor((self.__Stats[3] - 10) / 2))
        self.__AbilityProficiencies[np.array([1, 6, 9, 11, 17])] = int(np.floor((self.__Stats[4] - 10) / 2))
        self.__AbilityProficiencies[np.array([4, 7, 12, 13])] = int(np.floor((self.__Stats[5] - 10) / 2))

    def gainskillproficiency(self, skillindex):
        self.__AbilityProficiencies[skillindex] += self.__ProficiencyBonus

    def getabilities(self):
        return self.__Abilities

    def getabilityproficiencies(self):
        return self.__AbilityProficiencies

    def getac(self):
        return self.__AC

    def getalignment(self):
        return self.__Alignment

    def getbackground(self):
        return self.__Background

    def getclass(self):
        return self.__Class

    def getequipment(self):
        return self.__Equipment

    def getexp(self):
        return self.__EXP

    def gethp(self):
        return self.__HP

    def getlevel(self):
        return self.__Level

    def getmoney(self):
        return self.__Money

    def getname(self):
        return self.__Name

    def getproficiencies(self):
        return self.__Proficiencies

    def getproficiencybonus(self):
        return self.__ProficiencyBonus

    def getsaveproficiencies(self):
        return self.__SaveProficiencies

    def getspeeds(self):
        return self.__Speeds

    def getspells(self):
        return self.__Spells

    def getstats(self):
        return self.__Stats

    def improvestats(self, addtostats):
        self.__Stats += addtostats

    def removeabilities(self, oldability):
        self.__Abilities.append(oldability)
