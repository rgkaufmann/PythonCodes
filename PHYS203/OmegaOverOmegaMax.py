import numpy as np
import matplotlib.pyplot as plt

def Omega(x, N):
    return np.exp(-N*x**2/(Beta*(1-Beta)))

def plot(x, N1, N2, N3):
    plt.title("Ratio of Multiplicity at X and the Maximum for Different Number of Oscillators")
    plt.xlabel("x")
    plt.ylabel("Omega/OmegaMax")
    plt.xlim(xmax=0.35, xmin=-0.35)
    plt.ylim(ymin=0)
    plt.plot(x, N1, c='r', label='N = 10 Oscillators')
    plt.plot(x, N2, c='g', label='N = 100 Oscillators')
    plt.plot(x, N3, c='c', label='N = 10000 Oscillators')
    plt.legend(loc='best')
    plt.show()

Beta = 1/3
Xrange = np.linspace(-1/3, 1/3, num=10000)

N10Calc = Omega(Xrange, 10)
N100Calc = Omega(Xrange, 100)
N10000Calc = Omega(Xrange, 10000)

plot(Xrange, N10Calc, N100Calc, N10000Calc)