import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as spicy

def bestFitPMDeathRate(PMConcentration, Factor):
    return Factor*PMConcentration

def chiSquared(params, x, y, sigma):
    if sigma is None:
        sigma = 1.
    return np.sum((y-bestFitPMDeathRate(x, *params))**2/sigma**2)

dataset = np.loadtxt('death-rate-from-pm25-vs-pm25-concentration-by-country.csv', dtype=str, delimiter=',')
dataset = dataset[np.where(dataset[:, 2]=='2015'), 3:7][0]
dataset = dataset[np.where(dataset[:, 0]!=''), :][0]
dataset = dataset[np.where(dataset[:, 3]!=''), :][0]
print(dataset)

popt, pcov = spicy.curve_fit(bestFitPMDeathRate, dataset[:, 1],
                             dataset[:, 0], p0=2)

#Very High >=0.8
#High >=0.7
#Moderate >=0.55
#Low >=0

examplePMCon = np.arange(0, 125, 1)

chi2 = chiSquared(popt, dataset[:, 1], dataset[:, 0], 1)
dof = len(dataset[:, 1]) - len(popt)
pcov = pcov*dof/chi2
error = np.square(np.diag(pcov))

print("Chi-squared value is: {:.3f}".format(chi2))
print("Chi-squared over degrees of freedom is: {:.3f}".format(chi2/dof))
print("Slope of line is: {:.3e} +/- {:.3e}".format(popt[0], error[0]))

plt.scatter(dataset[:, 1], dataset[:, 0])
plt.plot(examplePMCon, bestFitPMDeathRate(examplePMCon, *popt))
plt.show()