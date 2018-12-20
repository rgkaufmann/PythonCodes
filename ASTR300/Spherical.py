import numpy as np
import matplotlib.pyplot as plt

def integrand(x, alpha):
    return (x**(1-alpha))/(np.sqrt(x**2-1))

xVals = np.linspace(1.1, 100, 1000)

for aVal in [0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 5, 10]:
    plt.figure(int(4*aVal))
    plt.plot(xVals, integrand(xVals, aVal))
plt.show()