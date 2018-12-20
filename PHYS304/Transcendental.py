import numpy as np
import matplotlib.pyplot as plt

def tangent(z):
    return np.tan(z)

def transient(z):
    return np.sqrt((8/z)**2-1)

zVals = np.linspace(np.pi, 8, 1000)
tanVals = tangent(zVals)
tranVals = transient(zVals)
zTransients = [4.16483091, 6.83067433]
tanTransients = tangent(zTransients)

plt.plot(zVals, tanVals, label='Tanget')
plt.plot(zVals, tranVals, label='Square Root')
plt.plot(zVals, np.abs(tanVals-tranVals), label='Absolute Value Difference')
plt.scatter(zTransients, tanTransients, label='Numerical Solutions')
plt.ylim(ymin=0, ymax=5)
plt.xlim(np.pi, 8)
plt.legend(loc='best')
plt.title('Graphical Representation of the Transcendental Equation')
plt.xlabel('z Values')
plt.show()

z0 = 4.16483091
z1 = 6.83067433
hbar = 1.0545718e-34
mass = 9.70938356e-31
#a = (8*hbar)/(np.sqrt(2*mass))
a=0.1
kappa0 = np.sqrt(8**2-z0**2)/a
kappa1 = np.sqrt(8**2-z1**2)/a
l0 = z0/a
l1 = z1/a

def HOWavefunction0(x):
#    constant = ((mass)/(5*np.pi*hbar))**(1/4)
    exponential = np.exp(-(mass)/(10*hbar)*x**2)
    return exponential

def HOWavefunction1(x):
    constant = ((mass)/(5*np.pi*hbar))**(1/4)
    constant *= np.sqrt((2*mass)/(5*hbar))
    exponential = np.exp(-(mass)/(10*hbar)*x**2)
    return constant*x*exponential

def FSWWavefunction0Even(x):
    results = np.zeros(x.shape)
    results[np.where(x>a)] = np.exp(-kappa0*x[np.where(x>a)])
    results[np.where(np.logical_and(0<x, x<a))] = np.cos(l0*x[np.where(np.logical_and(0<x, x<a))])
    results[np.where(np.logical_and(0>x, x>-a))] = np.cos(l0*-1*x[np.where(np.logical_and(0>x, x>-a))])
    results[np.where(x<-a)] = np.exp(kappa0*x[np.where(x<-a)])
    return results

def FSWWavefunction0Odd(x):
    results = np.zeros(x.shape)
    results[np.where(x>a)] = np.exp(-kappa0*x[np.where(x>a)])
    results[np.where(np.logical_and(0<x, x<a))] = np.sin(l0*x[np.where(np.logical_and(0<x, x<a))])
    results[np.where(np.logical_and(0>x, x>-a))] = -1*np.sin(l0*-1*x[np.where(np.logical_and(0>x, x>-a))])
    results[np.where(x<-a)] = -1*np.exp(kappa0*x[np.where(x<-a)])
    return results

def FSWWavefunction1Even(x):
    results = np.zeros(x.shape)
    results[np.where(x>a)] = np.exp(-kappa1*x[np.where(x>a)])
    results[np.where(np.logical_and(0<x, x<a))] = np.cos(l1*x[np.where(np.logical_and(0<x, x<a))])
    results[np.where(np.logical_and(0>x, x>-a))] = np.cos(l1*-1*x[np.where(np.logical_and(0>x, x>-a))])
    results[np.where(x<-a)] = np.exp(kappa1*x[np.where(x<-a)])
    return results

def FSWWavefunction1Odd(x):
    results = np.zeros(x.shape)
    results[np.where(x>a)] = np.exp(-kappa1*x[np.where(x>a)])
    results[np.where(np.logical_and(0<x, x<a))] = np.sin(l1*x[np.where(np.logical_and(0<x, x<a))])
    results[np.where(np.logical_and(0>x, x>-a))] = -1*np.sin(l1*-1*x[np.where(np.logical_and(0>x, x>-a))])
    results[np.where(x<-a)] = -1*np.exp(kappa1*x[np.where(x<-a)])
    return results

xValues = np.linspace(-0.1, 0.1, 1000)
HO0 = HOWavefunction0(xValues)
HO1 = HOWavefunction1(xValues)
FSW0E = FSWWavefunction0Even(xValues)
FSW0O = FSWWavefunction0Odd(xValues)
FSW1E = FSWWavefunction1Even(xValues)
FSW1O = FSWWavefunction1Odd(xValues)

plt.plot(xValues, HO0)
plt.plot(xValues, FSW0E)
plt.plot(xValues, FSW0O)
plt.plot(xValues, np.abs(FSW0E+FSW0O))
plt.show()

plt.plot(xValues, HO1)
plt.plot(xValues, FSW1E)
plt.plot(xValues, FSW1O)
plt.plot(xValues, np.abs(FSW1E+FSW1O))
plt.show()