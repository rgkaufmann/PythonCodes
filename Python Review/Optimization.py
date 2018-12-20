import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats, io

def Func(x, y, t):
    return [+4*y+x*t, -4*x-y*t]

xValues = np.linspace(-10, 10, 200)
yValues = np.linspace(-10, 10, 200)
xValues, yValues = np.meshgrid(xValues, yValues)
time = np.arange(0, 100, 1)

xValuesFor = np.copy(xValues)
yValuesFor = np.copy(yValues)
xValuesNpy = np.copy(xValues)
yValuesNpy = np.copy(yValues)

pr = cProfile.Profile()
pr.enable()

for tVal in time:
    for indx1 in range(len(xValuesFor)):
        for indx2 in range(len(xValuesFor)):
            funcVals = Func(xValuesFor[indx1, indx2], yValuesFor[indx1, indx2],
                            tVal)
            xValuesFor[indx1, indx2] += funcVals[0]
            yValuesFor[indx1, indx2] += funcVals[1]
            print('({}, {}) at time = {}'.format(indx1, indx2, tVal))

pr.disable()
file = open('ForLoop.txt', 'w')
s = io.StringIO()
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()

pr.enable()

for tVal in time:
    funcVals = Func(xValuesNpy, yValuesNpy, tVal)
    xValuesNpy += funcVals[0]
    yValuesNpy += funcVals[1]
    print('Time = {}'.format(tVal))
    
pr.disable()
file = open('NumpyUsage.txt', 'w')
s = io.StringIO()
ps = pstats.Stats(pr, stream = s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()

plt.figure(figsize=(10, 20))
plt.subplot(211)
plt.imshow(xValuesFor)
plt.subplot(212)
plt.imshow(xValuesNpy)
plt.show()

plt.figure(figsize=(10, 20))
plt.subplot(211)
plt.imshow(yValuesFor)
plt.subplot(212)
plt.imshow(yValuesNpy)
plt.show()