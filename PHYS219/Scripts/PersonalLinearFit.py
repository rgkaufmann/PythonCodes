# Linear Fit script for square wave integral
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

fname = "/Users/ryank/Desktop/Work/Classes/Python/PHYS219/Final Experiment/"
fname += "DifferentFrequencySquare.csv"

x_unit = "Seconds"
x_name = "Time"
y_unit = "Volts"
y_name = "Output Voltage"

guess = (1e3*1e-7, 0)
###############################################################################
def fit_function(x, RC, offset):
    return 0.05/RC*x+offset

data = np.loadtxt(fname, delimiter=',', comments='#')
x = data[:,0]
y = data[:,1]
y_sigma = 0.03*x+0.021
y_sigma *= 1.2

x_fitfunc = np.linspace(min(x), max(x), 500)

y_guess = fit_function(x_fitfunc, *guess)
plt.errorbar(x, y, yerr=y_sigma, marker='.',
             linestyle='', label='Measured Data', zorder=0)
plt.plot(x_fitfunc, y_guess, marker='', linestyle='-', linewidth=1, color='g',
         label='Initial Guess', zorder=20)
plt.xlabel('{} [{}]'.format(x_name, x_unit))
plt.ylabel('{} [{}]'.format(y_name, y_unit))
plt.title('Initial Guess Fit for Integrator Op Amp with Square Wave')
plt.legend(loc='best', numpoints=1)
print('Displaying Initial Guess Plot')
plt.show()

fit_params, fit_cov = curve_fit(fit_function, x, y, sigma=y_sigma, p0=guess,
                                maxfev=10**5)
###############################################################################
def chi_squared(fit_parameters, x, y, sigma):
    return np.sum((y-fit_function(x, *fit_params))**2/sigma**2)

chi2 = chi_squared(fit_params, x, y, y_sigma)
dof = len(x)-len(fit_params)
print('\nGoodness of Fit: Chi-squared measure')
print('Chi2 = {:.3e}'.format(chi2))
print('Chi2/dof = {:.3e}'.format(chi2/dof))
###############################################################################
fit_cov = fit_cov*dof/chi2
fit_params_error = np.sqrt(np.diag(fit_cov))

params_names = ['RC Time Constant', 'Voffset']
print('\nFit parameters')
for indx in range(len(fit_params)):
    print('{} = {:.3e} +/- {:.3e}'.format(params_names[indx], fit_params[indx],
                                          fit_params_error[indx]))
###############################################################################
y_fitfunc = fit_function(x_fitfunc, *fit_params)

plt.errorbar(x, y, yerr=y_sigma, marker='.', linestyle='',
             label='Measured Data', zorder=0)
plt.plot(x_fitfunc, y_fitfunc, marker='', linestyle='-', linewidth=2,
         color='r', label='Fitted Guess', zorder=20)
plt.xlabel('{} [{}]'.format(x_name, x_unit))
plt.ylabel('{} [{}]'.format(y_name, y_unit))
plt.title('Fitted Guess for Integrator Op Amp with Square Wave')
plt.legend(loc='best', numpoints=1)
print('\nDisplaying Fitted Function Plot')
plt.show()
###############################################################################
y_fit = fit_function(x, *fit_params)
residuals = y-y_fit
normresidual = residuals/y_sigma

hist, bins = np.histogram(normresidual, bins=30)

fig = plt.figure(figsize=(7, 10))

ax1 = fig.add_subplot(211)
ax1.errorbar(x, residuals, yerr=y_sigma, marker='.', linestyle='-',
             label='Residuals (Data-Fit)')
ax1.hlines(0, np.min(x), np.max(x), lw=2, alpha=0.8)
ax1.set_xlabel('{} [{}]'.format(x_name, x_unit))
ax1.set_ylabel('Data-Fit [{}]'.format(y_unit))
ax1.legend(loc='best', numpoints=1)

ax2 = fig.add_subplot(212)
ax2.bar(bins[:-1], hist, width=bins[1]-bins[0])
ax2.set_ylim(0, 1.2*np.max(hist))
ax2.set_xlabel('(Data-Fit)/Sigma')
ax2.set_ylabel('Frequency')

plt.title('Histogram of Normalized Results')

within_error = 100*np.sum((residuals <= y_sigma)&(residuals >= -y_sigma))
within_error /= len(residuals)
print('\nResiduals Info')
print('{:.1f}% of data points agree with the fit'.format(within_error))
ax2.vlines(-1, 0, np.max(hist)*1.3, lw=3, color='r', linestyles='--')
ax2.vlines(1, 0, np.max(hist)*1.3, lw=3, color='r', linestyles='--',
           label='+/- Error')
ax2.text(0, np.max(hist)*1.1,
         '{:.1f}% of data points agree with the fit'.format(within_error),
         horizontalalignment='center', verticalalignment='center')
ax2.legend(loc={0.35, 0.05})

print('\nDisplaying Residuals Plot')
plt.show()