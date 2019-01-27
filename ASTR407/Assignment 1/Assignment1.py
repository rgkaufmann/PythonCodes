import numpy as np
import matplotlib.pyplot as plt

########################################################################################################################
#                                                Question 1
########################################################################################################################


def f(x):
    return np.power(x, 3.0)-11*x+13


def derivative(x):
    return 3*np.power(x, 2.0)-11


def newtonmethod(interactions, testinitial):
    while interactions[-1][2] > 1.0e-9:
        newtest = testinitial - f(testinitial) / derivative(testinitial)
        interactions.append([interactions[-1][0] + 1, newtest, np.abs(newtest - testinitial)])
        testinitial = newtest
    return interactions


iteration2 = newtonmethod([[0, 2.0, 100000.0]], 2.0)
print
iteration3 = newtonmethod([[0, 3.0, 100000.0]], 3.0)

print
print 'Iteration     Current Estimate X     Difference with last iteration'
for indx in range(len(iteration2)):
    print '{:<14}{:<23}{:<30}'.format(*iteration2[indx])
print
print 'Iteration     Current Estimate X     Difference with last iteration'
for indx in range(len(iteration3)):
    print '{:<14}{:<23}{:<30}'.format(*iteration3[indx])

values = np.linspace(1, 4, 1000)
plt.plot(values, f(values))
plt.hlines(0, 1, 4)
plt.xlabel('x Values', fontsize=18)
plt.ylabel('f(x) Values', fontsize=18)
plt.title('Graph of given function f(x) between x=1 and x=4', fontsize=25)
plt.show()

########################################################################################################################
#                                                Question 2
########################################################################################################################


def afunc(t):
    return (16.0*t+16.0)**(1.0/4.0)


def aderivative(a):
    return 4.0*a**(-3.0)


def euler(maximum, dt, initial):
    points = [[initial, 0, dt]]
    for t in np.arange(dt, maximum+dt, dt):
        points.append([points[-1][0]+dt*aderivative(points[-1][0]), t, dt])
    return points


fifteen = afunc(15.0)
print
print fifteen

tvalues = np.linspace(0, 15, 1000)
plt.plot(tvalues, afunc(tvalues))
plt.title('Analytic Solution of Differential Equation Between t=0 and t=15', fontsize=25)
plt.xlabel('t Values', fontsize=18)
plt.ylabel('x Values', fontsize=18)
plt.show()

timestep = 1.0
estimations = [euler(15, timestep, 2)]
while np.abs(estimations[-1][-1][0]-fifteen) > 0.01*fifteen:
    timestep = timestep/2.0
    estimations.append(euler(15, timestep, 2))

print
print 'Estimation of a(t)     Value of t     Timestep'
for indx in range(len(estimations)):
    print '----------------------------------------------'
    for indx2 in range(len(estimations[indx])):
        print '{:<23}{:<15}{:<8}'.format(*estimations[indx][indx2])

########################################################################################################################
#                                                Question 3
########################################################################################################################


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
