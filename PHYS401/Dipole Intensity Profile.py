import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})


def intense(t):
    return 1-0.5*(np.sin(t))**2


t = np.linspace(0, np.pi, 100000)
plt.plot(t, intense(t))
plt.xlabel("Theta", fontsize=24)
plt.ylabel("Intensity", fontsize=24)
plt.ylim(0,1.1)
plt.title("Intensity as a Function of Polar Angle", fontsize=30)
plt.show()
