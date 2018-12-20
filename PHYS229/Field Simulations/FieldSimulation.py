import numpy as np
import matplotlib.pyplot as plt

class Particle:
    coulombConstant = 8.988
    
    def __init__(self, xposition, yposition, charge):
        self.xpos = xposition
        self.ypos = yposition
        self.charge = charge
        
    def potential(self, xval, yval):
        distance = np.sqrt((self.xpos-xval)**2+(self.ypos-yval)**2)
        potential = self.coulombConstant*self.charge/distance
        excludeX = np.where(np.abs(np.abs(xval[0, :])-np.abs(self.xpos))<=0.01)
        excludeY = np.where(np.abs(np.abs(yval[:, 0])-np.abs(self.ypos))<=0.01)
        for x in excludeX[0]:
            for y in excludeY[0]:
                potential[x, y]=0
        return potential
    
def HalfCircle(x, r):
    return np.sqrt(r**2-x**2)

P1 = Particle(0.5, 0.5,   1)
P2 = Particle(-0.5, 0.5, -1)
P3 = Particle(0.5, -0.5, -1)
P4 = Particle(-0.5, -0.5, 1)

xCircle1 = np.linspace(-0.25, 0.25, 1000)
xCircle2 = np.linspace(-0.5,  0.5,  1000)
xCircle3 = np.linspace(-0.75, 0.75, 1000)
xCircle4 = np.linspace(-1.0,  1.0,  1000)
xvals = np.linspace(-1, 1, 1000)
yvals = np.linspace(-1, 1, 1000)
xmap, ymap = np.meshgrid(xvals, yvals)

potentialmap = P1.potential(xmap, ymap)
potentialmap += P2.potential(xmap, ymap)
potentialmap += P3.potential(xmap, ymap)
potentialmap += P4.potential(xmap, ymap)

plt.imshow(potentialmap, cmap='seismic', extent=[-1, 1, -1, 1])
#plt.plot(xCircle1,  HalfCircle(xCircle1, 0.25), c='k')
#plt.plot(xCircle1, -HalfCircle(xCircle1, 0.25), c='k')
#plt.plot(xCircle2,  HalfCircle(xCircle2, 0.5),  c='k')
#plt.plot(xCircle2, -HalfCircle(xCircle2, 0.5),  c='k')
#plt.plot(xCircle3,  HalfCircle(xCircle3, 0.75), c='k')
#plt.plot(xCircle3, -HalfCircle(xCircle3, 0.75), c='k')
#plt.plot(xCircle4,  HalfCircle(xCircle4, 1.0),  c='k')
#plt.plot(xCircle4, -HalfCircle(xCircle4, 1.0),  c='k')
#plt.plot(xCircle4,  xCircle4, c='k')
#plt.plot(xCircle4, -xCircle4, c='k')
#plt.plot(xCircle4, np.zeros(xCircle4.shape), c='k')
#plt.plot(np.zeros(xCircle4.shape), xCircle4, c='k')
plt.show()