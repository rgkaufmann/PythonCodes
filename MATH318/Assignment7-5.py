import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})


def randomwalk(steps, breaking):
    walk = [0]
    count = 0
    while count < steps:
        x = np.random.rand()
        if x > 0.5:
            walk.append(walk[-1]+1)
        else:
            walk.append(walk[-1]-1)
        if walk[-1] == 0 and breaking:
            break
        count += 1
    return walk


def independentrw(numof, steps, breaking):
    walklengths = []
    counter = 0
    while counter < numof:
        walk = randomwalk(steps, breaking)
        walklengths.append(len(walk)-1)
        print walklengths[-1]
        counter += 1
    return walklengths


def loglog(data, max):
    greater = []
    counter = 0
    while counter < max:
        greater.append((len(data[np.where(data>counter)]))/(1E3))
        counter += 1
    return greater


numsteps = 1E6
stepvals = np.arange(0, numsteps, 1)
walkvalues = randomwalk(numsteps, False)

plt.plot(stepvals, walkvalues[1:])
plt.title("Random Walk on the Integers With Equal\nIncreasing and Decreasing Probabilities", fontsize=36)
plt.xlabel("Step Number n", fontsize=28)
plt.ylabel("Simulated Value of Sn", fontsize=28)
plt.xlim(0, numsteps)
plt.show()

numofindependent = 1000
lengths = np.array(independentrw(numofindependent, numsteps, True))
notreturn = lengths[np.where(lengths == 1e6)]
print len(notreturn)

plt.hist(lengths, bins=400)
plt.title("Histogram of Steps to Return to 0 in a Random Walk", fontsize=36)
plt.xlabel("Step of First Return", fontsize=28)
plt.ylabel("Number of Occurances", fontsize=28)
plt.show()

biggerthan = loglog(lengths, numsteps)
plt.loglog(stepvals, biggerthan)
plt.title("Log-Log Plot of Values of T Greater than the Step", fontsize=36)
plt.xlabel("Step Number k", fontsize=28)
plt.ylabel("Number of T Greater than k", fontsize=28)
plt.ylim(0, 1.1)
plt.show()
