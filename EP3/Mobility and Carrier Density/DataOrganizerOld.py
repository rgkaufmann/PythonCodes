import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf


def parabolicfunc(bfield, coefficient, offset):
    return coefficient * (bfield ** 2.0) + offset


def chisquared(params, bfield, rxy):
    return np.sum((rxy - parabolicfunc(bfield, *params)) ** 2 / 0.1 ** 2)


def initial(data, guess, neg, address):
    fieldguess = np.linspace(min(data[1, :]), max(data[1, :]), 750)
    rguess = parabolicfunc(fieldguess, *guess)

    print('\nShowing plot 1 for ' + address[90:98])
    plt.scatter(data[1, :], data[0, :], marker='.', label="Measured Data")
    plt.plot(fieldguess, rguess, marker="", linestyle="-", linewidth=1, color="g", label="Initial Guess")
    plt.xlabel('B-Field')
    plt.ylabel('Rxx')
    plt.title(address[90:98] + " Rxx Linearity Initial Guess")
    plt.legend(loc='best', numpoints=1)
    plt.show()
    plt.clf()

    return fit(data, guess, neg, address)


def fit(data, guess, neg, address):
    params, cov = cf(parabolicfunc, data[1, :], data[0, :], sigma=0.01 * np.ones(len(data[1, :])),
                     p0=guess, maxfev=10 ** 5)
    chi2 = chisquared(params, data[1, :], data[0, :])
    dof = len(data[1, :]) - len(params)

    cov = cov * dof / chi2
    paramserr = np.sqrt(np.diag(cov))

    fieldfit = np.linspace(min(data[1, :]), max(data[1, :]), len(data[1, :]) * 10)
    rfit = parabolicfunc(fieldfit, *params)

    print('\nShowing plot 2 for ' + address[90:98])
    plt.scatter(data[1, :], data[0, :], marker='.', label="Measured Data")
    plt.plot(fieldfit, rfit, marker="", linestyle="-", linewidth=1, color="r", label="Initial Guess")
    plt.xlabel('B-Field')
    plt.ylabel('Rxx')
    plt.title(address[90:98] + " Rxx Linearity Fitted Guess")
    plt.legend(loc='best', numpoints=1)
    plt.show()
    plt.clf()

    return residual(data, params, neg, address)


def residual(data, params, neg, address):
    residuals = data[0, :] - parabolicfunc(data[1, :], *params)

    plt.title(address[90:98] + " Rxx Linearity Residuals")
    print('\nShowing plot 3 for ' + address[90:98])
    plt.scatter(data[1, :], residuals, marker='.', label="residual (y-y_fit)")
    plt.hlines(0, np.min(data[1, :]), np.max(data[1, :]), lw=2, alpha=0.8)
    plt.xlabel('B-Field')
    plt.ylabel(r'R-R_Fit')
    plt.legend(loc='best', numpoints=1)
    plt.show()
    plt.clf()

    return params


DataHeader = 'C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/'
Data = ['PST194 M1/Bsweep_BH Data.dat',
        'PST195 M1/Bsweep_BH (01) Data.dat',
        'PST196 M1/Bsweep_BH (01) Data.dat',
        'PST197 M1/Bsweep_BH (03) Data.dat']
cutoff = {"PST192": 2.5, "PST191": 3, "PST189": 4, "PST081": 2, "PST042": 6, 'PST037': 4}

for DataIndex in Data:
    DataSet = np.loadtxt(DataHeader + DataIndex)

    RxxData = np.abs(DataSet[:, 3] / DataSet[:, 2] * 998.2)
    RxyData = DataSet[:, 4] / DataSet[:, 2] * 998.2
    BField = DataSet[:, 8]

    plt.title(DataIndex[90:98] + " Rxx Data")
    plt.plot(BField, RxxData)
    plt.xlabel("Rxx (Ohms)")
    plt.ylabel("BField (T)")
    plt.show()

    plt.title(DataIndex[90:98] + " Rxy Data")
    plt.plot(BField, RxyData)
    plt.xlabel("Rxy (Ohms)")
    plt.ylabel("BField (T)")
    plt.show()

    Parameters = initial(np.array([RxxData, BField]), [1, 200], False, DataIndex)
    print(DataIndex[90:98] + " Parameters: ")
    print(Parameters)

    np.savetxt(DataIndex[:-8] + "_Rxx" + DataIndex[-8:], np.array([RxxData, BField]))
