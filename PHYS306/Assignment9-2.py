import numpy as np
import matplotlib.pyplot as plt


def potential(theta):
    return (10-8*np.cos(theta))**2/(2*np.sin(theta)**2)+(64)/(2)+np.cos(theta)


xvals = np.linspace(0.00001, np.pi, 100000)

plt.plot(xvals, potential(xvals))
plt.ylim(0, 200)
plt.show()

plt.plot(xvals, potential(xvals))
plt.ylim(0, 200)
plt.title("Effective Potential of a Top")
plt.xlabel("Theta")
plt.ylabel("Potential")
plt.show()

print("{}".format(xvals[np.where(potential(xvals)==min(potential(xvals)))][0]))