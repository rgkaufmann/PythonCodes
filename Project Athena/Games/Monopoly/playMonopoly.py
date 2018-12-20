import numpy

###############################################################################

class Player:
    def __init__(self, money, name):
        self.name = name
        self.money = money
        self.properties = []
        self.mortgaged = []
        self.getOutFrees = 0
        
    def getJailFree(self):
        self.getOutFrees += 1
    
    def useJailFree(self):
        if self.getOutFrees == 0:
            return False
        else:
            self.getOutFrees -= 1
            return True
    
    def checkProperty(self, land):
        return land in self.properties and land not in self.mortgaged
    
    def getRent(self, land, otherPlayer):
        if self.checkProperty(land):
            self.money += land.getRent()
            otherPlayer.payRent(land.getRent())
            
    def payRent(self, rent):
        self.money -= rent
    
    def gainMoney(self, advance):
        self.money += advance
        
    def looseMoney(self, debt):
        self.money -= debt
        
    def gainProperty(self, land):
        if land not in self.properties:
            self.properties.append(land)
        
    def sellProperty(self, land, price, otherPlayer):
        if land in self.properties:
            self.properties.remove(land)
            self.money += price
            otherPlayer.gainProperty(land)
            otherPlayer.looseMoney(price)
            
    def mortgageProperty(self, land):
        if self.checkProperty(land):
            self.gainMoney(land.getMortgage)
            self.mortgaged.append(land)
    
    def unmortgageProperty(self, land):
        if land in self.properties and land in self.mortgaged:
            if self.money > land.getMortgage:
                self.looseMoney(land.getMortgage)
                self.mortgaged.remove(land)
                return True
            else:
                return False

###############################################################################

def rollDice():
    return numpy.random.randint(1, 7) + numpy.random.randint(1, 7)

def reorderPlayers(players, first):
    newOrder = dict()
    for order in players.keys():
        if order+first < len(players):
            newOrder.update([(order+1, players[order+first])])
        else:
            newOrder.update([(order+1, players[order+first-len(players)])])
    return newOrder

def pickFirst(players):
    currFirst = -1
    currMax = -1
    for player in players.keys():
        roll = rollDice()
        print(players[player].name + "'s roll: " + str(roll))
        if roll > currMax:
            currMax = roll
            currFirst = player
        elif roll == currMax:
            while True:
                firstRoll = rollDice()
                secondRoll = rollDice()
                print("Tie rolls: " + str(firstRoll) + ", " + str(secondRoll))
                if secondRoll != firstRoll:
                    if secondRoll > firstRoll:
                        currFirst = player
                    break
    newPlayers  = reorderPlayers(players, currFirst)
    return newPlayers
        
###############################################################################

validInput = True
while validInput:
    numPlayers = int(input("How many people are playing Monopoly? "))
    if (numPlayers < 2):
        print("There are too few players.")
    elif (numPlayers > 8):
        print("There are too many players.")
    else:
        break

names = dict()
gameFinished = False

for player in range(numPlayers):
    names.update([(player,
                   Player(1500, input("What is player " + str(player+1) + "'s name? ")))])

names = pickFirst(names)

while not gameFinished:
    for player in names.keys():
        print(str(player) + ": " + names[player].name)
        for player in names.keys():
            print(str(names[player].money))
    gameFinished = True