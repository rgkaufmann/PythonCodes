import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

MP = 938.2592
MN = 939.5527

Z = [2, 8, 12, 20, 26, 40, 50, 59, 68, 79, 82, 92]
N = [2, 8, 14, 20, 26, 50, 74, 76, 94, 118, 126, 143]
B = [28.3, 127.6, 216.7, 342.0, 447.7, 783.9, 1050.0,
     1124.4, 1320.7, 1559.4, 1636.4, 1783.9]

Z = np.array(Z)
N = np.array(N)
B = np.array(B)
A = Z + N


def Pairings (A, Z, ap):
    if (A % 2) == 0 and (Z % 2) == 0:
        return ap / (A ** (1 / 2))
    elif (A % 2) == 0 and (Z % 2) == 1:
        return  -1 * ap / (A ** (1 / 2))
    else:
        return 0


PairVectorize = np.vectorize(Pairings)

def LDM(X, av, au, ac, aa, ap):
    Z, A = X
    vol = av * A
    sur = au * (A ** (2 / 3))
    col = ac * Z * (Z - 1) / (A ** (1 / 3))
    asy = aa * ((A - 2 * Z) ** 2) / A
    pai = PairVectorize(A, Z, ap)
    return vol - sur - col - asy + pai


def Z0(A, aa, ac):
    x2 = (MN - MP) + 4 * aa + ac * (A ** (-1 / 3))
    x3 = 2 * ac * (A ** (-1 / 3)) + 8 * aa / A
    return np.round(x2 / x3)


XVals = np.vstack((Z.ravel(), A.ravel()))
p0 = [16.0, 18.0, 0.7, 23.0, 12.0]
popt, pcov = cf(LDM, XVals, B.ravel(), p0)

print(popt)

Atest = np.linspace(1, 250, 250)
Ztest = np.linspace(1, 250, 250)
Atest, Ztest = np.meshgrid(Atest, Ztest)
Btest = LDM((Ztest, Atest), *popt)
Bln = np.log(Btest)

fig = plt.figure()
im = plt.imshow(Bln, origin='lower')
fig.colorbar(im)
plt.show()

Atest = np.linspace(20, 240, 221)
Btest = LDM((Z0(Atest, popt[3], popt[2]), Atest), *popt)

plt.plot(Atest, Btest/Atest)
plt.title('Binding Energy per Nucleon at $Z_0$ from the Liquid Drop Model')
plt.xlabel('Total Nucleons $A$ (1)')
plt.ylabel('Binding Energy per Nucleon (MeV)')
plt.show()
