import numpy as np
import matplotlib.pyplot as plt


def func(r):
    return 2608.0*((r-10.0)**3.0)/(r**3.0)


rvals = np.linspace(10, 100, 10000)
tvals = func(rvals)
plt.plot(rvals, tvals)
plt.hlines(1200, 10, 100)
plt.text(12, 1220, r"$\Delta$T=1200K")
plt.xlim(10, 100)
plt.ylim(0)
plt.title("Variation of Temperature Difference with Respect to Object Radius")
plt.xlabel("Radius in kilometers")
plt.ylabel("Temperature Change in Kelvin Difference")
plt.show()

print [rvals[np.where(tvals >= 1200)][0], tvals[np.where(tvals >= 1200)][0]]
print [rvals[np.where(tvals <= 1200)][-1], tvals[np.where(tvals <= 1200)][-1]]
