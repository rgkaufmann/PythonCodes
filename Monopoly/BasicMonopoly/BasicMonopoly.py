import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats, io

def tileChance(chancenum, tile):
    movetile = [0, 1, 2, 3, 4, 7, 8, 11, 12]
    freecard = [6]
    if chancenum in movetile:
        if chancenum == 0:
            return 0
        elif chancenum == 1:
            return 24
        elif chancenum == 2:
            return 11
        elif chancenum == 3:
            if tile in [22, 36]:
                return 28
            elif tile == 7:
                return 12
        elif chancenum == 4:
            if tile == 7:
                return 15
            elif tile == 22:
                return 25
            elif tile == 36:
                return 5
        elif chancenum == 7:
            return tile-3
        elif chancenum == 8:
            global jail
            jail = True
            return 10
        elif chancenum == 11:
            return 5
        elif chancenum == 12:
            return 39
    elif chancenum in freecard:
        global jailFree
        jailFree = True
        return tile
    else:
        return tile

def tileCommunity(communitynum, tile):
    movetile = [0, 5]
    freetile = [4]
    if communitynum in movetile:
        if communitynum == 0:
            return 0
        elif communitynum == 5:
            global jail
            jail = True
            return 10
    if communitynum in freetile:
        global jailFree
        jailFree = True
        return tile
    else:
        return tile

tilelist = np.array(["Go!", "Mediterranean Avenue", "Community Chest", "Baltic Avenue",
                     "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance",
                     "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Place",
                     "Electric Company", "States Avenue", "Virginia Avenue",
                     "Pennsylvania Railroad", "St. James Place", "Community Chest",
                     "Tennessee Avenue", "New York Avenue", "Free Parking",
                     "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue",
                     "B & O Railroad", "Atlantic Avenue", "Ventnor Avenue",
                     "Water Company", "Marvin Gardens", "Go to Jail", "Pacific Avenue",
                     "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue",
                     "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"])
tilename = np.array(["Go!", "Mediterranean Avenue", "Baltic Avenue",
                     "Oriental Avenue", "Vermont Avenue", "Connecticut Avenue",
                     "St. Charles Place", "States Avenue", "Virginia Avenue",
                     "St. James Place", "Tennessee Avenue", "New York Avenue",
                     "Kentucky Avenue", "Indiana Avenue", "Illinois Avenue",
                     "Atlantic Avenue", "Ventnor Avenue", "Marvin Gardens",
                     "Pacific Avenue", "North Carolina Avenue",
                     "Pennsylvania Avenue", "Park Place", "Broadway",
                     "Reading Railroad", "Pennsylvania Railroad",
                     "B & O Railroad", "Short Line", "Electric Company",
                     "Water Company", "Jail", "Free Parking", "Go to Jail",
                     "Community Chest", "Chance", "Income Tax", "Luxury Tax"])
community = np.array(["Advance to Go", "Bank error in your favor", "Doctor's fee",
                      "Sale of stock", "Get Out of Jail Free", "Go to Jail",
                      "Grand Opera Night", "Holiday Fund matures", "Income tax refund",
                      "It is your birthday", "Life insurance matures", "Pay hospital fees",
                      "Pay school fees", "Receive $25 consultancy fee",
                      "Assessed for street repairs", "Beauty contest"])
chance = np.array(["Advance to Go", "Advance to Illinois Ave.", "Advance to St. Charles Place",
                   "Advance to nearest Utility", "Advance to nearest railroad",
                   "Bank pays dividend", "Get out of Jail Free", "Go back 3 spaces",
                   "Go to Jail", "Make repairs on property", "Pay poor tax",
                   "Take trip on Reading Railroad", "Take a walk on Boardwalk",
                   "Elected Chairman of the Board", "Building loan matures",
                   "Won a crossword competition"])
colorcode = np.array(['#CDE6D0', '#975439', '#975439', '#B4E3FA', '#B4E3FA',
                      '#B4E3FA', '#D23B94', '#D23B94', '#D23B94', '#F69424',
                      '#F69424', '#F69424', '#E61B1E', '#E61B1E', '#E61B1E',
                      '#FAF10D', '#FAF10D', '#FAF10D', '#1FB451', '#1FB451',
                      '#1FB451', '#0D6FB3', '#0D6FB3', '#000000', '#000000',
                      '#000000', '#000000', '#D7BAAA', '#D7BAAA', '#CDE6D0',
                      '#CDE6D0', '#CDE6D0', '#8FBC72', '#8FBC72', '#FFBF00',
                      '#FFBF00'])
tilefreq = np.zeros(40, dtype=int)
currenttile = 0
turn = 0
MaxTurn = 100
global jail
jail = False
global jailFree
jailFree = False
double = 1
gamenum = 0
MaxGame = 100000

pr = cProfile.Profile()
pr.enable()

while (gamenum < MaxGame):
    offset = 0
    dicerolls = np.random.randint(1, 7, size=(2, MaxTurn*3))
    chancepicks = np.arange(16)
    np.random.shuffle(chancepicks)
    communitypicks = np.arange(16)
    np.random.shuffle(communitypicks)
    while (turn < MaxTurn):
        if len(chancepicks)==0:
            chancepicks = np.arange(16)
            np.random.shuffle(chancepicks)
        elif len(communitypicks)==0:
            communitypicks = np.arange(16)
            np.random.shuffle(communitypicks)
        if jail:
            if jailFree:
                jail = False
            elif (dicerolls[0][turn + offset] == dicerolls[1][turn + offset]):
                jail = False
            else:
                double += 1
        else:
            double = 1
            diceroll = dicerolls[0][turn + offset] + dicerolls[1][turn + offset]
            currenttile += diceroll
            currenttile = currenttile%40
            if (currenttile == 7 or currenttile == 22 or currenttile==36):
                currenttile = tileChance(chancepicks[0], currenttile)
                chancepicks = np.delete(chancepicks, 0)
            elif (currenttile == 2 or currenttile == 17 or currenttile == 33):
                currenttile = tileCommunity(communitypicks[0], currenttile)
                communitypicks = np.delete(communitypicks, 0)
            if (currenttile == 30):
                currenttile = 10
                jail = True
            tilefreq[currenttile] += 1
            while (dicerolls[0][turn + offset] == dicerolls[1][turn + offset]):
                offset += 1
                diceroll = dicerolls[0][turn + offset] + dicerolls[1][turn + offset]
                currenttile += diceroll
                double += 1
                if (double == 3):
                    currenttile = 10
                    double = 1
                    jail = True
        turn += 1
    print("Game " + str(gamenum+1) + " done!")
    gamenum += 1
    currenttile = 0
    turn = 0
    jail = False
    jailFree = False
    double = 1
    
pr.disable()
file = open('FullMonopolyStats.txt', 'w')
s = io.StringIO()
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()

fixedtilefreq = np.array([tilefreq[0], tilefreq[1], tilefreq[3], tilefreq[6],
                          tilefreq[8], tilefreq[9], tilefreq[11], tilefreq[13],
                          tilefreq[14], tilefreq[16], tilefreq[18], tilefreq[19],
                          tilefreq[21], tilefreq[23], tilefreq[24], tilefreq[26],
                          tilefreq[27], tilefreq[29], tilefreq[31], tilefreq[32],
                          tilefreq[34], tilefreq[37], tilefreq[39], tilefreq[5],
                          tilefreq[15], tilefreq[25], tilefreq[35], tilefreq[12],
                          tilefreq[28], tilefreq[10], tilefreq[20], tilefreq[30],
                          tilefreq[2]+tilefreq[17]+tilefreq[33],
                          tilefreq[7]+tilefreq[22]+tilefreq[36],
                          tilefreq[4], tilefreq[38]])
fixedtilefreq = fixedtilefreq/sum(fixedtilefreq)
xvalues = range(len(tilename))
plt.bar(xvalues, fixedtilefreq, color=colorcode)
plt.xticks(xvalues, tilename, rotation='vertical')
for x, freq in zip(xvalues, fixedtilefreq):
    plt.text(x-0.5, freq+0.001, "{:.3f}".format(freq))
plt.tight_layout()
plt.show()