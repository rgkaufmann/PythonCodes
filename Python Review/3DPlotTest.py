import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def xfunc(xvals, yvals):
    return (xvals)**3/(xvals**2+yvals**2)

xvalues = np.linspace(-0.0001, 0.0001, 1000)
yvalues = np.linspace(-0.0001, 0.0001, 1000)
xvalues, yvalues = np.meshgrid(xvalues, yvalues)
zvalues = xfunc(xvalues, yvalues)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xvalues, yvalues, zvalues)
plt.show()
