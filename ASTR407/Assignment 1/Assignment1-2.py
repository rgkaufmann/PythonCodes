import numpy as np
import matplotlib.pyplot as plt


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

print 'Estimation of a(t)     Value of t     Timestep'
for indx in range(len(estimations)):
    print '----------------------------------------------'
    for indx2 in range(len(estimations[indx])):
        print '{:<23}{:<15}{:<8}'.format(*estimations[indx][indx2])
