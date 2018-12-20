import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.optimize import curve_fit as cf

def temperatureFunc (temperature):
    return 1/((293**4+temperature**4))

def cumulativeTimeFunc(temperature, emissivity):
    y = -temperatureFunc(temperature)
    C = 9.899e-12
    return integrate.trapz(y, temperature)/(C*emissivity)

###############################################################################

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Cooling Process/Data/DataSet1.txt"
times1   = np.loadtxt(filename, usecols=0)*60
smooth1  = np.loadtxt(filename, usecols=2)+273
lacquer1 = np.loadtxt(filename, usecols=3)+273
rough1   = np.loadtxt(filename, usecols=1)+273
uncert1  = np.loadtxt(filename, usecols=4)

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Cooling Process/Data/DataSet2.txt"
times2   = np.loadtxt(filename, usecols=0)*60
smooth2  = np.loadtxt(filename, usecols=1)+273
lacquer2 = np.loadtxt(filename, usecols=2)+273
rough2   = np.loadtxt(filename, usecols=3)+273
uncert2  = np.loadtxt(filename, usecols=4)

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Cooling Process/Data/SamDataSet.txt"
times3   = np.loadtxt(filename, usecols=0)*60
smooth3  = np.loadtxt(filename, usecols=1)+273
lacquer3 = np.loadtxt(filename, usecols=2)+273
rough3   = np.loadtxt(filename, usecols=3)+273
uncert3  = np.loadtxt(filename, usecols=4)

###############################################################################

print(max(smooth2))
print(min(smooth2))
testTemps = np.linspace(max(smooth2), min(smooth2), 10000)

#fitParams, fitCOV = cf(cumulativeTimeFunc, smooth2, times2, sigma=uncert2, p0=(0.01), maxfev=10**5)

plt.scatter(times2, smooth2, c='g', label='Smooth')
plt.plot(cumulativeTimeFunc(testTemps, 1), testTemps)
plt.show()