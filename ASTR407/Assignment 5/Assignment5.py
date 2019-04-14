import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})


def polarmoi(k, f):
    return (1.0+(k-1.0)*f**5.0)/(1.0+(k-1.0)*f**3.0)*(2.0/5.0)


kvals = [0.9, 1.5, 2.0]
fvals = np.linspace(0.0, 1.0, 10000)
for kval in kvals:
    plt.plot(fvals, polarmoi(kval, fvals), label="k = {}".format(kval))
plt.hlines(0.375, 0, 1, colors='r', label='Ceres Polar Moment of Inertia')
plt.hlines(0.385, 0, 1, colors='r', label='Ceres Upper Limit')
plt.hlines(0.365, 0, 1, colors='r', label='Ceres Lower Limit')
plt.title("Polar Moment of Inertia as a Function of\nCore Radius Fraction for Various k", fontsize=36)
plt.xlabel("Fraction of Total Radius R", fontsize=28)
plt.ylabel("Polar Moment of Inertia", fontsize=28)
plt.legend(loc='best')
plt.xlim(0.0, 1.0)
plt.ylim(0.3, 0.41)
plt.show()