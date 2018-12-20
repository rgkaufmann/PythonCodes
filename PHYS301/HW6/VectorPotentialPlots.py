import numpy as np
import matplotlib.pyplot as plt

def vectorPotential(s):
    A = np.zeros(len(s))
    for index in range(len(s)):
        if s[index]<1:
            A[index] = 1-(s[index]**2)
        elif s[index]>1:
            A[index]=2*np.log((s[index])**(-1))
    return A

sVals = np.linspace(0, 10, 10000)
AVals = vectorPotential(sVals)

plt.plot(sVals, AVals)
plt.title('Vector Potential from a Long Wire of Radius R')
plt.xlabel('Radius s in terms of the Radius of the Wire R')
plt.ylabel('Vector Potential in terms of the constant cI')
plt.show()