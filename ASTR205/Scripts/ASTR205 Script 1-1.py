import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as optimizer

def Function (X, a, b, c):
    return a*np.exp(X/b)+c

def chi_square (fit_parameters, x, y, sigma):
    if sigma is None:
        sigma = 1
    return np.sum((y-Function(x, *fit_parameters))**2/sigma**2)

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "ASTR 205 1-1.csv"
Data = np.loadtxt(filename, comments='#')
sigma = 1.9

plt.scatter(Data[:, 0], Data[:, 1], c='c', s=1)
plt.title('Initial Plot of the Given Data')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

guess = [1, -1, 1]
fit_params, fit_cov = optimizer(Function, Data[:, 0], Data[:, 1], p0=guess)

chi2 = chi_square(fit_params, Data[:, 0], Data[:, 1], sigma)
dof = len(Data[:, 0]) - len(fit_params)
print ("\nGoodness of fit - chi square measure:")
print ("Chi2/dof = {}\n".format(chi2/dof))

fit_cov = fit_cov*dof/chi2
fit_params_error = np.sqrt(np.diag(fit_cov))
param_names = ['A','B','C']
print ("Fit parameters:")
for i in range(len(fit_params)):
    if (fit_params[i] < 0):
        print ('{} = {:.3e} +/- {:.3e}'.format(param_names[i],
                                              fit_params[i],
                                              fit_params_error[i]))
    else:
        print('{} =  {:.3e} +/- {:.3e}'.format(param_names[i],
                                               fit_params[i],
                                               fit_params_error[i]))

plt.title('Plot of the Given Data with Best-Fit Curve')
plt.scatter(Data[:, 0], Data[:, 1], zorder=1, c='c', label='Data', s=1)
plt.plot(Data[:, 0], Function(Data[:, 0], *fit_params), zorder=10, c='r',
         label='Best-fit')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend(loc = 'best')
plt.show()