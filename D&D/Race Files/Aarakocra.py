import sys
sys.path.append('/Users/ryank/Desktop/Work/Classes/Coding Projects/D&D/Character Options')
import ClassOptions as CO

class Aarakocra:
    race = 'Aarakocra'
    classes = {}
    stats = []
    statIncrease = [0, 2, 0, 0, 1, 0]
    travelSpeed = [25, 50, 0, 0, 0]
    languages = ['Common', 'Aarakocra', 'Auran']
    proficiencies = []
    resistances = []
    
    def __init__(self, playerClass='', level=0):
        if not playerClass=='':
            self.classes[playerClass] = level
    
    def addClass(self, newClass='', level=1):
        if newClass in CO.Classes:
            if newClass not in self.classes.keys():
                self.classes[newClass] = level
                return True
            elif newClass in self.classes.key():
                self.classes[newClass] += level
                return True
        else:
            return False
        
    def addLanguage(self, newLanguage):
        if newLanguage not in self.languages:
            self.languages.append(newLanguage)
            return True
        else:
            return False
        
    def addResistance(self, newResistance):
        if newResistance not in self.resistances:
            self.resistances.append(newResistance)
            return True
        else:
            return False

    def applyRacialBonus(self, stats):
        if len(stats)==6:
            self.stats = stats + self.statIncrease
            return True
        else:
            return False
    
    def getClasses(self):
        return self.classes
    
    def getLanguages(self):
        return self.languages
    
    def getProficiencies(self):
        return self.proficiencies
    
    def getRace(self):
        return self.race
        
    def getResistances(self):
        return self.resistances
    
    def getStatIncrease(self):
        return self.statIncrease
    
    def getStats(self):
        return self.stats
    
    def setClasses(self, classes):
        if type(classes) is dict:
            self.classes = classes
            return True
        else:
            return False
    
    def setLanguages(self, languages):
        if type(languages) is list:
            self.languages = languages
            return True
        else:
            return False
    
    def setProficiencies(self, proficiencies):
        if type(proficiencies) is list:
            self.proficiencies = proficiencies
            return True
        else:
            return False
        
    def setResistances(self, resistances):
        if type(resistances) is list:
            self.resistances = resistances
            return True
        else:
            return False
        
    def setStats(self, stats):
        if type(stats) is list and len(stats)==6:
            self.stats = stats
            return True
        else:
            return False
        
print(type([0, 2, 3]) is list)
print(type({'cat':5, 'dog':6}) is dict)