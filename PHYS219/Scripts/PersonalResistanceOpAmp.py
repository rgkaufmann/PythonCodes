import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

fname = "/Users/ryank/Desktop/Work/Classes/Python/PHYS219/Final Experiment/"
fname += "ChangingRC.csv"

x_name = '1/RC'
x_unit = 'Hertz'
y_name = 'Gain Over 1/RC'
y_unit = 'Seconds'
normresidunist = 'Seconds'

guess = (1/(2*np.pi*2000), 60, 0)
###############################################################################
def fit_function(x, gain, fcA0, offset):
    return gain/np.sqrt(1+(x*gain/(fcA0))**2)+offset

def chi_square(fit_parameters, x, y, sigma):
    return np.sum((y-fit_function(x, *fit_parameters))**2/sigma**2)

data = np.loadtxt(fname, delimiter=',', comments='#')

x = data[:, 0]
y = data[:, 1]
y_sigma = data[:, 2]*3.5

xtheory = np.linspace(min(x), max(x), 500)
y_guess = fit_function(xtheory, *guess)

plt.errorbar(x, y, yerr=y_sigma, marker='.', linestyle='', zorder=0,
             label='Measured Data')
plt.plot(xtheory, y_guess, marker='', linestyle='-', linewidth=1, color='g',
         label='Initial Guess', zorder=20)
plt.xscale('log')
plt.xlabel('{} [{}]'.format(x_name, x_unit))
plt.ylabel('{} [{}]'.format(y_name, y_unit))
plt.title('Initial Guess Fit for Op Amp Gain Over 1/RC Versus 1/RC')
plt.legend(loc='best', numpoints=1)
print('Displaying Initial Guess Plot')
plt.show()
###############################################################################
fit_params, fit_cov = curve_fit(fit_function, x, y, sigma=y_sigma, p0=guess,
                                maxfev=10**5)

chi2 = chi_square(fit_params, x, y, y_sigma)
dof = len(x)-len(fit_params)
print('\nGoodness of Fit: Chi-squared measure')
print('Chi2 = {:.3e}'.format(chi2))
print('Chi2/dof = {:.3e}'.format(chi2/dof))
###############################################################################
fit_cov = fit_cov*dof/chi2
fit_params_error = np.sqrt(np.diag(fit_cov))

param_names = ['Gain', 'FcA0', 'V_offset']
print('\nFit Parameters:')
for indx in range(len(fit_params)):
    print('{} = {:.3e} +/- {:.3e}'.format(param_names[indx], fit_params[indx],
                                          fit_params_error[indx]))
###############################################################################
y_fitfunc = fit_function(xtheory, *fit_params)

plt.errorbar(x, y, yerr=y_sigma, marker='.', linestyle='', zorder=0,
             label='Measured Data')
plt.plot(xtheory, y_fitfunc, marker='', linestyle='-', linewidth=2, color='r',
         zorder=20, label='Fitted Function')
plt.xscale('log')
plt.xlabel('{} [{}]'.format(x_name, x_unit))
plt.ylabel('{} [{}]'.format(y_name, y_unit))
plt.title('Fitted Guess for Op Amp Gain Over 1/RC Versus 1/RC')
plt.legend(loc='best', numpoints=1)
print('\nDisplaying Fitted Function Plot')
plt.show()
###############################################################################
y_fit = fit_function(x, *fit_params)
residual = y-y_fit
normresidual = residual/y_sigma

hist, bins = np.histogram(normresidual, bins=30)

fig = plt.figure(figsize=(7,10))

ax1 = fig.add_subplot(211)
ax1.errorbar(x, residual, yerr=y_sigma, marker='.', linestyle='',
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

within_err = 100*np.sum((residual <= y_sigma)&(residual >= -y_sigma))
within_err /= len(residual)
print('\nResidual Information:')
print('{:.1f}% of data points agree within 1 sigma of fit'.format(within_err))
ax2.text(0, np.max(hist)*1.1,
         '{:.1f}% of data points within 1 sigma'.format(within_err),
         horizontalalignment='center', verticalalignment='center')
ax2.vlines(-1, 0, np.max(hist)*1.3, lw=2, color='r', linestyles='--')
ax2.vlines(1, 0, np.max(hist)*1.3, lw=2, color='r', linestyles='--',
           label='+/- one sigma')

print('\nDisplaying Residual Plot')
plt.show()