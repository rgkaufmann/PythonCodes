import numpy as np
from scipy.integrate import quad


def waveequation(x, b, c, n):
    return n*np.exp(-c*x**2.0)+n*b*x*np.exp(-c*x**2.0)


def probability(x, b, c, A):
    return np.abs(waveequation(x, b, c, A))**2.0


def wavederivative(x, b, c, n):
    return 2*c*n*np.exp(-c*x**2.0)*(b*x*(2.0*c*x**2.0-3.0)+2.0*c*x**2.0-1.0)


def potential(x):
    return -1.0/2.0*x**2.0+(x/2.0)**4.0


def integrand(x, b, c, A):
    return waveequation(x,b,c,A)*(-1.0/2.0*wavederivative(x, b, c, A)+potential(x)*waveequation(x, b, c, A))


b = 2.0
c = 2.0
prev = 100000000000
(y, abserr) = quad(func=probability, a=-np.inf, b=np.inf, args=(b, c, 1.0))
current = quad(func=integrand, a=-np.inf, b=np.inf, args=(b, c, 1.0/y))
print current[0]
while prev > current[0]:
    b = b + 0.025
    prev = current[0]
    (y, abserr) = quad(func=probability, a=-np.inf, b=np.inf, args=(b, c, 1.0))
    current = quad(func=integrand, a=-np.inf, b=np.inf, args=(b, c, 1.0 / y))
    print current[0]
b = b - 0.025
prev = 10000000000000
while prev > current[0]:
    b = b - 0.025
    prev = current[0]
    (y, abserr) = quad(func=probability, a=-np.inf, b=np.inf, args=(b, c, 1.0))
    current = quad(func=integrand, a=-np.inf, b=np.inf, args=(b, c, 1.0 / y))
    print current[0]
b = b + 0.025
prev = 10000000000000
while prev > current[0]:
    c = c + 0.025
    prev = current[0]
    (y, abserr) = quad(func=probability, a=-np.inf, b=np.inf, args=(b, c, 1.0))
    current = quad(func=integrand, a=-np.inf, b=np.inf, args=(b, c, 1.0 / y))
    print current[0]
c = c - 0.025
prev = 10000000000000
while prev > current[0]:
    c = c - 0.025
    prev = current[0]
    (y, abserr) = quad(func=probability, a=-np.inf, b=np.inf, args=(b, c, 1.0))
    current = quad(func=integrand, a=-np.inf, b=np.inf, args=(b, c, 1.0 / y))
    print current[0]
c = c + 0.025
print b
print c