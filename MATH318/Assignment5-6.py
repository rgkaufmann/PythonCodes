import numpy as np
import matplotlib.pyplot as plt


def uniform(n, k):
    probability = 0
    if (n == 1):
        if (k <= 0) or (k >= 4):
            return 0
        else:
            return 1.0/3.0
    for value in range(1, 4):
        if float(k-value)/float(n-1) < 1:
            return probability
        elif float(k-value)/float(n-1) > 3:
            probability += 0
        else:
            probability += 1.0/3.0*uniform(int(n-1), int(k-value))
        print str(n)+", "+str(k)+", "+str(value)
        print probability
    return probability


def alluniform(n):
    probabilities = []
    for value in range(1*n, 3*n+1):
        probabilities.append(uniform(n, value))
        print "-----------------"
    return probabilities


S1 = alluniform(1)
plt.bar(np.arange(1, 4), S1)
plt.show()

S2 = alluniform(2)
plt.bar(np.arange(2, 7), S2)
plt.show()

S3 = alluniform(3)
plt.bar(np.arange(3, 10), S3)
plt.show()

S4 = alluniform(4)
plt.bar(np.arange(4, 13), S4)
plt.show()

S5 = alluniform(5)
plt.bar(np.arange(5, 16), S5)
plt.show()

S10 = alluniform(10)
plt.bar(np.arange(10, 31), S10)
plt.show()

S50 = alluniform(50)
plt.bar(np.arange(50, 151), S50)
plt.show()
