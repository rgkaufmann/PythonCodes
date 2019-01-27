import numpy as np
from scipy import stats as spicy
import matplotlib.pyplot as plt


def geompmf(k, p):
    return (1-p)**k*p


randoms = np.random.geometric(0.01, 100000)
randoms = randoms[np.where(randoms <= 1000)]
randoms = randoms[np.where(randoms >= 1)]
ranges = np.linspace(1.0, 1000.0, 10000)

plt.hist(randoms, bins=1000)
plt.show()

plt.plot(geompmf(ranges, 0.01))
plt.show()

ranges = np.linspace(0.0, 10.0, 1000)

plt.plot(ranges, np.e**(-1*ranges))
plt.show()
