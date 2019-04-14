import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


def wavefunction1(b):
    return (b*(1.0+np.exp(-4.0*b)*(8.0*b-1)))/(4.0*np.exp(-4.0*b)*(np.exp(4.0*b)+1.0))


def wavefunction2(b):
    return (64.0*b**2.0-32.0*b-3.0)/(32.0*b**2.0*np.exp(-4.0*b)*(np.exp(4.0*b)+1.0))


def full(b):
    return wavefunction1(b)+wavefunction2(b)


xvals = np.linspace(0.5, 20, 500)
plt.plot(xvals, full(xvals))
plt.show()

#minimum = minimize(full, x0=np.array([1.1, 2.5]), bounds=((1, None), (None, None)))
#print minimum