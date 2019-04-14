import numpy as np
import matplotlib.pyplot as plt


def convolution(array, n):
    if n > 1:
        return np.convolve(array, convolution(array, n-1))
    elif n == 1:
        return array


for sval in [1, 2, 3, 4, 5, 10, 50]:
    S = convolution([1.0/3.0, 1.0/3.0, 1.0/3.0], sval)
    plt.bar(np.arange(1*sval, 3*sval+1), S)
    plt.title("Addition of {:d} Uniform Random Variables".format(sval), fontsize=40)
    plt.xlabel("Outcome of Random Variable", fontsize=32)
    plt.ylabel("Probability of Outcome", fontsize=32)
    plt.show()

for tval in [1, 2, 3, 4, 5, 10, 50]:
    T = convolution([1.0/15.0, 1.0/15.0, 11.0/15.0, 1.0/15.0, 1.0/15.0], tval)
    plt.bar(np.arange(0*tval, 4*tval+1), T)
    plt.title("Addition of {:d} Random Variables Y".format(tval), fontsize=40)
    plt.xlabel("Outcome of Random Variable", fontsize=32)
    plt.ylabel("Probability of Outcome", fontsize=32)
    plt.show()
