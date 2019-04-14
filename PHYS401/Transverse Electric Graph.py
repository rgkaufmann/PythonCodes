import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def magneticz(modem, moden, lena, lenb, xvals, yvals):
    return np.cos(modem*np.pi*xvals/lena)*np.cos(moden*np.pi*yvals/lenb)


xvalues = np.linspace(0, 2.4, 1000)
yvalues = np.linspace(0, 3.6, 1000)
xvalues, yvalues = np.meshgrid(xvalues, yvalues)

fig = plt.figure()
fig.suptitle("Flux Pattern of the Z-Component of the Magnetic Field", fontsize=36)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xvalues, yvalues, magneticz(2, 0, 2.4, 3.6, xvalues, yvalues))
ax.set_xlabel("X Distance in Centimeters", fontsize=18)
ax.set_ylabel('Y Distance in Centimeters', fontsize=18)
ax.set_zlabel("Magnitude of Magnetic Field", fontsize=18)
plt.show()

plt.pcolormesh(xvalues, yvalues, magneticz(2, 0, 2.4, 3.6, xvalues, yvalues))
plt.title("Flux Pattern of the Z-Component of the Magnetic Field", fontsize=36)
plt.xlabel("X Distance in Centimeters", fontsize=18)
plt.ylabel('Y Distance in Centimeters', fontsize=18)
cbar = plt.colorbar()
cbar.ax.set_ylabel("Magnitude of Magnetic Field", fontsize=18)
plt.show()

plt.pcolormesh(xvalues, yvalues, np.abs(magneticz(2, 0, 2.4, 3.6, xvalues, yvalues)))
plt.title("Flux Pattern of the Absolute Value\nof the Z-Component of the Magnetic Field", fontsize=36)
plt.xlabel("X Distance in Centimeters", fontsize=18)
plt.ylabel('Y Distance in Centimeters', fontsize=18)
cbar = plt.colorbar()
cbar.ax.set_ylabel("Magnitude of Magnetic Field", fontsize=18)
plt.show()
