import numpy as np
import matplotlib.pyplot as plt
import cmath


def function(f):
    return f**2*(np.abs((np.exp(1j*np.pi/f)+1)/(f**2-1)))**2


fvals = np.linspace(0, 4, 10000)
pvals = function(fvals)

plt.plot(fvals, pvals)
plt.show()