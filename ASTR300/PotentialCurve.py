import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

font = {'size':16}

matplotlib.rc('font', **font)

fig = plt.figure()
ax = Axes3D(fig)

def xPos(t):
    return 2*np.cos(t)

def xVel(t):
    return -2*np.sin(t)

def yPos(t):
    return np.cos(np.pi*t/2)

def yVel(t):
    return -np.pi/2*np.sin(np.pi*t/2)

tValues = np.arange(-10, 10.1, 0.1)
xValues = xPos(tValues)
yValues = yPos(tValues)

ax.plot(xValues, yValues, tValues, 'o')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Time')
ax.set_title('Path of a Star in a Galaxy Defined By a Given Potential')
plt.show()

plt.scatter(xValues[:100], yValues[:100], c=tValues[:100], cmap=plt.cm.coolwarm)
plt.xlabel('X Position')
plt.ylabel('Y Position')
#plt.set_zlabel('Time')
plt.title('Path of a Star in a Galaxy Defined By a Given Potential')
CB = plt.colorbar()
CB.set_label('Time')
plt.show()

xVelocity = xVel(tValues)
yVelocity = yVel(tValues)
zAngular = xValues*yVelocity-yValues*xVelocity

plt.plot(tValues, zAngular)
plt.xlabel('Time (t)')
plt.ylabel('Angular Momentum (Lz)')
plt.title('Angular Momentum in the z-direction of a Star Defined By a Given Potential')
plt.hlines(0, -10, 10)
plt.xlim(-10, 10)
plt.show()

#for angle in range(0, 360*20):
#    ax.view_init(30, angle)
#    plt.draw()
#    plt.pause(.001)

