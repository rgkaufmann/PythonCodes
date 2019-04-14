import numpy as np
import matplotlib.pyplot as plt


def process(steps, n):
    coinvals = np.zeros(n)
    headlists = []
    pairrandoms = n*np.random.rand(steps, 2)
    for indx in range(len(pairrandoms)):
        if pairrandoms[indx][1] < 0.5*n:
            coinvals[int(pairrandoms[indx][0])] = 1
        elif pairrandoms[indx][1] >= 0.5*n:
            coinvals[int(pairrandoms[indx][0])] = 0
        headlists.append(np.sum(coinvals))
    return headlists


heads = np.array(process(20000, 1000))
plt.hist(heads[0:1000], bins='auto')
plt.title('Histogram of Number of Heads Between 0 and 1000 Steps')
plt.xlabel('State (Number of Heads)')
plt.ylabel('Number of Visits')
plt.show()

plt.hist(heads[1000:2000], bins='auto')
plt.title('Histogram of Number of Heads Between 1000 and 2000 Steps')
plt.xlabel('State (Number of Heads)')
plt.ylabel('Number of Visits')
plt.show()

plt.hist(heads[10000:20000], bins='auto')
plt.title('Histogram of Number of Heads Between 10000 and 20000 Steps')
plt.xlabel('State (Number of Heads)')
plt.ylabel('Number of Visits')
plt.show()
