import numpy as np
import matplotlib.pyplot as plt


def uppercircle(xvalues, semimajor):
    return np.sqrt(semimajor**2-np.power(xvalues, 2))


def lowercircle(xvalues, semimajor):
    return -np.sqrt(semimajor**2-np.power(xvalues, 2))


data = np.loadtxt("C:/Users/ryank/Desktop/Github/PythonCodes/ASTR407/Assignment 1/MPCxyz.txt")
xdata, ydata = [], []
normr, normv = [], []

for indx in range(len(data)):
    if np.abs(data[indx][1]) <= 7 and np.abs(data[indx][2]) <= 7:
        xdata.append(data[indx][1])
        ydata.append(data[indx][2])
    normr.append(np.sqrt(data[indx][1] ** 2 + data[indx][2] ** 2 + data[indx][3] ** 2))
    normv.append(np.sqrt(data[indx][4] ** 2 + data[indx][5] ** 2 + data[indx][6] ** 2))

mercuryValues = np.linspace(-0.3871, 0.3871, 1000)
venusValues = np.linspace(-0.7233, 0.7233, 1000)
earthValues = np.linspace(-1.0000, 1.0000, 1000)
marsValues = np.linspace(-1.5237, 1.5237, 1000)
jupiterValues = np.linspace(-5.203, 5.203, 1000)

plt.figure(figsize=(13, 13))
plt.title('Plot of Minor Planets and Planet Orbits within 7 au from the Sun', fontsize=25)
plt.xlabel('X Position', fontsize=18)
plt.ylabel('Y Position', fontsize=18)
plt.scatter(xdata, ydata, s=5, c='b', label='Minor Planets')
plt.plot(mercuryValues, uppercircle(mercuryValues, 0.3871), color='m', label='Mercury Orbit')
plt.plot(mercuryValues, lowercircle(mercuryValues, 0.3871), color='m')
plt.plot(venusValues, uppercircle(venusValues, 0.7233), color='r', label='Venus Orbit')
plt.plot(venusValues, lowercircle(venusValues, 0.7233), color='r')
plt.plot(earthValues, uppercircle(earthValues, 1.0000), color='g', label='Earth Orbit')
plt.plot(earthValues, lowercircle(earthValues, 1.0000), color='g')
plt.plot(marsValues, uppercircle(marsValues, 1.5237), color='k', label='Mercury Orbit')
plt.plot(marsValues, lowercircle(marsValues, 1.5237), color='k')
plt.plot(jupiterValues, uppercircle(jupiterValues, 5.203), color='c', label='Jupiter Orbit')
plt.plot(jupiterValues, lowercircle(jupiterValues, 5.203), color='c')
plt.legend(loc='best')
plt.xlim(-7, 7)
plt.ylim(-7, 7)
plt.show()

normr = np.array(normr)
normv = np.array(normv)

plt.title('Relationship Between Distance from Sun and Velocity for Objects within 7au', fontsize=25)
plt.xlabel('Radius', fontsize=18)
plt.ylabel('Velocity', fontsize=18)
plt.scatter(normr[np.where(normr <= 7)], normv[np.where(normr <= 7)], s=5, c='b')
plt.show()
