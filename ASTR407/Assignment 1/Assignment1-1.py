import numpy as np
import matplotlib.pyplot as plt


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
iteration3 = newtonmethod([[0, 3.0, 100000.0]], 3.0)

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
