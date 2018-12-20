from io import StringIO

from typing import BinaryIO

import NBodySystem as System
import sys
import cProfile
import pstats
import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

pr = cProfile.Profile()

pr.enable()

tmin = 0
tmax = 100
dt = 0.01
timeVals = np.arange(tmin-dt, tmax, dt)
numSteps = int((tmax-tmin)/dt)
System1 = System.sysOfObj(dt, 2)
Positions = [System1.getPositions()]
Velocitys = [System1.getVelocities()]

for step in range(numSteps):
    System1.updateObjs()
    Positions.append(System1.getPositions())
    Velocitys.append(System1.getVelocities())

fig = plt.figure(figsize=(8, 8))
axes, line = [], []
Data = [[], [], [], []]
ax = fig.add_subplot(1, 2, 1)
axes.append(ax)
for plotNum in [3, 4, 7, 8]:
    axTemp = fig.add_subplot(2, 4, plotNum)
    axTemp.set_xlim(0, tmax)
    axTemp.set_ylim(-2, 2)
    axes.append(axTemp)
    lnTemp, = axTemp.plot(Data[0], [])
    line.append(lnTemp)
axes[1].set_title('Position of Particle 1')
axes[2].set_title('Position of Particle 2')
axes[3].set_title('Velocity of Particle 1')
axes[4].set_title('Velocity of Particle 2')

for fame in timeVals:  # type: int
    for index in range(4):  # type: int
        if index < 2:
            Data[index].append(Positions[int(np.round(1/dt*fame+1))][0+index])
        elif index > 1:
            Data[index].append(Velocitys[int(np.round(1/dt*fame+1))][-2+index])
        line[index].set_data(timeVals[:int(np.round(1/dt*fame+2))], Data[index])
    print(fame)


def update(frame):
    for indexes in range(4):  # type: int
        if indexes < 2:
            Data[indexes].append(Positions[int(np.round(1/dt*frame+1))][0+indexes])
        elif indexes > 1:
            Data[indexes].append(Velocitys[int(np.round(1/dt*frame+1))][-2+indexes])
        line[indexes].set_data(Data[indexes], timeVals[:int(np.round(1/dt*frame+2))])
    print(frame)
#    scat.set_offsets(np.array([Positions[int(np.round(1/dt*frame))][0], [0, 0]]).T)
    return line,


# ani = anim.FuncAnimation(fig, update, frames=timeVals, blit=True)
plt.show()

pr.disable()
file = open('Test1NBodySimulator.txt', 'w')  # type: BinaryIO
s = io.StringIO()  # type: StringIO
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()
