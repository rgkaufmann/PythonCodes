import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})


def randomwalk1d(steps):
    firstzero = True
    walk = [0]
    breakpoint = steps
    for count in range(steps):
        x = np.random.rand()
        if x > 0.5:
            walk.append(walk[-1]+1)
        elif x <= 0.5:
            walk.append(walk[-1]-1)
        if walk[-1] == 0 and firstzero:
            breakpoint = count+1
            firstzero = False
    return [walk[-1], breakpoint]


def randomwalk2d(steps):
    firstzero = True
    walk = [(0, 0)]
    breakpoint = steps
    for count in range(steps):
        x = np.random.rand()
        if x > 0.75:
            walk.append([sum(x) for x in zip(walk[-1], (1, 0))])
        elif x > 0.5:
            walk.append([sum(x) for x in zip(walk[-1], (-1, 0))])
        elif x > 0.25:
            walk.append([sum(x) for x in zip(walk[-1], (0, 1))])
        elif x < 0.25:
            walk.append([sum(x) for x in zip(walk[-1], (0, -1))])
        if walk[-1] == [0, 0] and firstzero:
            breakpoint = count+1
            firstzero = False
    return [walk[-1], breakpoint]


def randomwalk3d(steps):
    firstzero = True
    walk = [(0, 0, 0)]
    breakpoint = steps
    for count in range(steps):
        x = 6*np.random.rand()
        if x > 5:
            walk.append([sum(x) for x in zip(walk[-1], (1, 0, 0))])
        elif x > 4:
            walk.append([sum(x) for x in zip(walk[-1], (-1, 0, 0))])
        elif x > 3:
            walk.append([sum(x) for x in zip(walk[-1], (0, 1, 0))])
        elif x > 2:
            walk.append([sum(x) for x in zip(walk[-1], (0, -1, 0))])
        elif x > 1:
            walk.append([sum(x) for x in zip(walk[-1], (0, 0, 1))])
        elif x > 0:
            walk.append([sum(x) for x in zip(walk[-1], (0, 0, -1))])
        if walk[-1] == [0, 0, 0] and firstzero:
            breakpoint = count+1
            firstzero = False
    return [walk[-1], breakpoint]


def independentwalks(numof, steps, dimension):
    walklengths = []
    walkends = []
    if dimension == 1:
        for i in range(numof):
            walk = randomwalk1d(steps)
            walklengths.append(walk[1])
            walkends.append((walk[0])**2)
    elif dimension == 2:
        for i in range(numof):
            walk = randomwalk2d(steps)
            walklengths.append(walk[1])
            walkends.append((walk[0][0])**2+(walk[0][1])**2)
    elif dimension == 3:
        for i in range(numof):
            walk = randomwalk3d(steps)
            walklengths.append(walk[1])
            walkends.append((walk[0][0])**2+(walk[0][1])**2+(walk[0][2])**2)
    mean = np.mean(np.array(walklengths)[np.where(np.array(walklengths) < numsteps)])
    walkinfo = np.array([walklengths, walkends, mean])
    return walkinfo


numsteps = int(1E6)
numofindependent = 100
info1d = independentwalks(numofindependent, numsteps, 1)
info2d = independentwalks(numofindependent, numsteps, 2)
info3d = independentwalks(numofindependent, numsteps, 3)

print len(np.array(info1d[0])[np.where(np.array(info1d[0]) >= numsteps)])
print len(np.array(info2d[0])[np.where(np.array(info2d[0]) >= numsteps)])
print len(np.array(info3d[0])[np.where(np.array(info3d[0]) >= numsteps)])

print info1d[2]
print info2d[2]
print info3d[2]

belowcomplete1d = np.array(info1d[0])[np.where(np.array(info1d[0]) < numsteps)]
belowcomplete2d = np.array(info2d[0])[np.where(np.array(info2d[0]) < numsteps)]
belowcomplete3d = np.array(info3d[0])[np.where(np.array(info3d[0]) < numsteps)]

plt.hist(belowcomplete1d, bins='auto')
plt.title('Histogram of First Zeros in Random Walks in 1 Dimension', fontsize=32)
plt.ylabel('Frequency', fontsize=28)
plt.xlabel('First Zero', fontsize=28)
plt.show()
plt.hist(belowcomplete2d, bins='auto')
plt.title('Histogram of First Zeros in Random Walks in 2 Dimension', fontsize=32)
plt.ylabel('Frequency', fontsize=28)
plt.xlabel('First Zero', fontsize=28)
plt.show()
plt.hist(belowcomplete3d, bins='auto')
plt.title('Histogram of First Zeros in Random Walks in 3 Dimension', fontsize=32)
plt.ylabel('Frequency', fontsize=28)
plt.xlabel('First Zero', fontsize=28)
plt.show()

print np.mean(info1d[1])
print np.mean(info2d[1])
print np.mean(info3d[1])

plt.hist(info1d[1], bins='auto')
plt.title('Histogram of Walk End Lengths After 1e6 Runs in 1 Dimension', fontsize=32)
plt.ylabel('Frequency', fontsize=28)
plt.xlabel('Walk Length', fontsize=28)
plt.show()
plt.hist(info2d[1], bins='auto')
plt.title('Histogram of Walk End Lengths After 1e6 Runs in 2 Dimension', fontsize=32)
plt.ylabel('Frequency', fontsize=28)
plt.xlabel('Walk Length', fontsize=28)
plt.show()
plt.hist(info3d[1], bins='auto')
plt.title('Histogram of Walk End Lengths After 1e6 Runs in 3 Dimension', fontsize=32)
plt.ylabel('Frequency', fontsize=28)
plt.xlabel('Walk Length', fontsize=28)
plt.show()
