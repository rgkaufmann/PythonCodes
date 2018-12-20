def pickCharacters(playerNames):
    availableCharacters = {"Ox Bellows": "Ox Bellows\t\t4\t5\t3\t3",
                           "Darrin \"Flash\" Williams": "Darrin \"Flash\" Williams\t6\t3\t3\t3",
                           "Vivian Lopez": "Vivian Lopez\t\t4\t2\t4\t5",
                           "Madame Zostra": "Madame Zostra\t\t3\t4\t4\t4",
                           "Fr. Rhinehardt": "Fr. Rhinehardt\t\t3\t2\t6\t4",
                           "Prof. Longfellow": "Prof. Longfellow\t4\t3\t3\t5",
                           "Jenny LeClerc": "Jenny LeClerc\t\t4\t4\t4\t3",
                           "Heather Granville": "Heather Granville\t4\t3\t3\t5",
                           "Missy Dubourde": "Missy Dubourde\t\t5\t3\t3\t4",
                           "Zoe Ingstrom": "Zoe Ingstrom\t\t4\t3\t5\t3",
                           "Peter Akimoto": "Peter Akimoto\t\t4\t3\t4\t4",
                           "Brandon Jaspers": "Brandon Jaspers\t\t4\t4\t4\t3"}
    tiedCharacters = {"Ox Bellows": "Darrin \"Flash\" Williams",
                      "Darrin \"Flash\" Williams": "Ox Bellows",
                      "Vivian Lopez": "Madame Zostra",
                      "Madame Zostra": "Vivian Lopez",
                      "Fr. Rhinehardt": "Prof. Longfellow",
                      "Prof. Longfellow": "Fr. Rhinehardt",
                      "Jenny LeClerc": "Heather Granville",
                      "Heather Granville": "Jenny LeClerc",
                      "Missy Dubourde": "Zoe Ingstrom",
                      "Zoe Ingstrom": "Missy Dubourde",
                      "Peter Akimoto": "Brandon Jaspers",
                      "Brandon Jaspers": "Peter Akimoto"}
    for player in range(len(playerNames)):
        while True:
            try:
                print(playerNames[player] + ", please pick a character.\n")
                print("Name\t\t\tSpeed\tMight\tSanity\tKnowledge")
                print("---------------------------------------------------------")
                for chars in availableCharacters.keys():
                    print(availableCharacters[chars])
                pickedCharacter = input()
                del availableCharacters[pickedCharacter]
                del availableCharacters[tiedCharacters[pickedCharacter]]
                playerNames[pickedCharacter] = playerNames[player]
                del playerNames[player]
                print()
                break
            except KeyError:
                print("Character not in list of available characters.\n")
    return playerNames

gameFinished = False
validInput = True
while validInput:
    numPlayers = int(input("How many people are playing Betrayal at House on the Hill? "))
    if (numPlayers < 3):
        print("There are too few players.")
    elif (numPlayers > 6):
        print("There are too many players.")
    else:
        break
playerNames = dict()

for player in range(numPlayers):
    playerNames.update([(player, input("What is player " + str(player+1) + "'s name? "))])

print()
playerNames = pickCharacters(playerNames)

while not gameFinished:
    for player in playerNames.keys():
        print(player + "------------" + playerNames[player])
    gameFinished = True