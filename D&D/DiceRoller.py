import numpy as np


def ndm(n, m):
    return np.random.randint(1, m+1, n)


def charactercreation():
    scores = []
    for i in range(6):
        rolls = ndm(4, 6)
        scores.append(sum(rolls)-min(rolls))
    # print('Your rolls are as follows:')
    # print(scores)

    # stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    # abilities = []
    # num = 0
    # for stat in stats:
    #     while num not in scores:
    #         num = int(input("What would you like to apply to " + stat + '? '))
    #     scores.remove(num)
    #     abilities.append(num)
    #     num = 0

    # return abilities
    return scores
