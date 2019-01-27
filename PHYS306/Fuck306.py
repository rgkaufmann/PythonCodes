import numpy as np
import matplotlib.pyplot as plt


def a(n, w):
    return (2.0)/(np.pi*n)*(1.0)/(np.sqrt(((np.pi)**2.0-w**2.0*n**2.0)**2.0+0.04*n**2.0*w**2.0))


def delta(n, w):
    if n==1 and w==np.pi:
        return np.pi/2
    else:
        return np.arctan((0.2*n)/((w)**2.0-np.pi**2.0*n**2.0))


def sine(n, t, w):
    return a(n, w)*np.sin(n*np.pi*t+delta(n, w))


def C(w):
    return 1-a(1.0, w)*np.sin(delta(1.0, w))-a(2.0, w)*np.sin(delta(2.0, w))-a(3.0, w)*np.sin(delta(3.0, w))-a(4.0, w)*np.sin(delta(4.0, w))


def d(w):
    return 1.0/(np.sqrt(w**2-0.04))*(0.2*C(w)-a(1.0, w)*np.cos(delta(1.0, w))-a(2.0, w)*np.cos(delta(2.0, w))-a(3.0, w)*np.cos(delta(3.0, w))-a(4.0, w)*np.cos(delta(4.0, w)))


def full(t, w):
    exp = np.exp(-0.2*t)*(C(w)*np.cos(np.sqrt(w**2-0.04)*t)+d(w)*np.sin(np.sqrt(w**2-0.04)*t))
    for nval in range(4):
        exp += sine(nval+1.0, t, w)
    return exp


def transcendental(n, w):
    return (2.0)/(np.pi*n)*(1.0)/(np.sqrt(((np.pi)**2.0-np.power(w, 2.0)*n**2.0)**2.0+0.04*n**2.0*np.power(w, 2.0)))


def brachix(theta, r):
    return r*(theta - np.sin(theta))


def brachiy(theta, r):
    return r*(1 - np.cos(theta))

wvals = np.linspace(0, 6, 1000)
sum = 0
for nvalue in range(1000):
    sum += transcendental(nvalue+1, wvals)

thetas = np.linspace(0, 2*np.pi, 1000)

plt.plot(wvals, sum)
plt.title('RMS as a Function of Driving Frequency', fontsize=36)
plt.xlabel('Driving Frequency', fontsize=28)
plt.ylabel('X-Position RMS', fontsize=28)
plt.show()

#plt.plot(brachix(thetas, 0.5), brachiy(thetas, 0.5), label='a=0.5')
#plt.plot(brachix(thetas, 1.0), brachiy(thetas, 1.0), label='a=1.0')
#plt.plot(brachix(thetas, 2.0), brachiy(thetas, 2.0), label='a=2.0')
#plt.title('Various Brachistochrones with Varying a-Values')
#plt.xlabel('X Position')
#plt.xlabel('Y Position')
#plt.legend(loc='best')
#plt.show()