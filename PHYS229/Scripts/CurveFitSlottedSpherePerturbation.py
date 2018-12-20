import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

def Periodic(distance, f0, omega, phase, resonance):
    return f0*np.sin(omega*distance+phase)+resonance

def chi_square (params, x, y, sigma):
    if sigma is None:
        sigma = 1.
    return np.sum((y-Periodic(x, *params))**2/sigma**2)

filename = 'C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/Acoustics/Data'
filename += "/AcousticSlottedSphereDataP5.csv"
x_label = 'Theta'
x_units = 'Degrees'
y_label = 'Change in Frequency'
y_units = 'Hz'
Data = np.loadtxt(filename, delimiter=',', comments='#', usecols=(0,1))
Data = Data[(int(len(Data)/2)):, :]

guess = [1.89, np.pi/180, -11.22, 585]
sigma = 0.11

###############################################################################

x_guess = np.linspace(min(Data[:, 0]),max(Data[:, 0]),500)
y_guess = Periodic(x_guess, *guess)

plt.errorbar(Data[:, 0], Data[:, 1], yerr=sigma, marker='.', linestyle='',
             label="measured data")
plt.plot(x_guess, y_guess,marker="", linestyle="-", linewidth=1, color="g",
         label="initial guess")
plt.xlabel('{} [{}]'.format(x_label, x_units))
plt.ylabel('{} [{}]'.format(y_label, y_units))
plt.title(r'Comparison between the data and the intial guess')
plt.legend(loc='best', numpoints=1)
print ('\nDisplaying plot 1')
plt.show()

###############################################################################

params, cov = cf(Periodic, Data[:, 0], Data[:, 1],
                 sigma=sigma*np.ones(len(Data[:, 0])), p0=guess, maxfev=10**5)

chi2 = chi_square(params, Data[:, 0], Data[:, 1], sigma)
dof = len(Data[:, 0]) - len(params)+1
print ("\nGoodness of fit - chi square measure:")
print ("Chi2 = {}, Chi2/dof = {}\n".format(chi2, chi2/dof))

cov = cov*dof/chi2
paramserr = np.sqrt(np.diag(cov))

param_names = ['f0','omega', 'phase','resonance']

print ("Fit parameters:")
for i in range(len(params)):
    print ('{} = {:.3e} +/- {:.3e}'.format(param_names[i], params[i],
                                           paramserr[i]))

###############################################################################

x_fit = np.linspace(min(Data[:, 0]),max(Data[:, 0]),len(Data[:, 0])*10)
y_fit = Periodic(x_fit,*params)

plt.errorbar(Data[:, 0], Data[:, 1], yerr=sigma, marker='.', linestyle='',
             label="measured data")
plt.plot(x_fit, y_fit, marker="", linestyle="-", linewidth=2, color="r",
         label=" fit")
plt.xlabel('{} [{}]'.format(x_label, x_units))
plt.ylabel('{} [{}]'.format(y_label, y_units))
plt.title(r'Relationship between Resonance and Degrees of Perturbation of Slotted Sphere')
plt.legend(loc='best', numpoints=1)
print ('\nDisplaying plot 2')
plt.show()

###############################################################################

y_fit=Periodic(Data[:, 0],*params)
residual = Data[:, 1]-y_fit
hist,bins = np.histogram(residual,bins=30)

fig = plt.figure(figsize=(7,10))
ax1 = fig.add_subplot(211)
ax1.errorbar(Data[:, 0], residual, yerr=sigma, marker='.', linestyle='',
             label="residual (y-y_fit)")
ax1.hlines(0,np.min(Data[:, 0]),np.max(Data[:, 0]),lw=2,alpha=0.8)
ax1.set_xlabel('{} [{}]'.format(x_label,x_units))
ax1.set_ylabel('y-y_fit [{}]'.format(y_units))
ax1.legend(loc='best',numpoints=1)
ax2 = fig.add_subplot(212)
ax2.bar(bins[:-1],hist,width=bins[1]-bins[0])

ax2.set_ylim(0,1.2*np.max(hist))
ax2.set_xlabel('y-y_fit [{}]'.format(y_units))
ax2.set_ylabel('Number of occurences')

if sigma != None:
    within_err=100.*np.sum((residual<=sigma)&(residual>=-sigma))/len(residual)
    print ("\nResidual information:")
    print ('{:.1f}% of data points agree with fit'.format(within_err))
    ax2.vlines(-sigma,0,np.max(hist)*1.3,lw=3,color='r')
    ax2.vlines(+sigma,0,np.max(hist)*1.3,lw=3,color='r',label='+/- error')
    ax2.text(0.0,np.max(hist)*1.1,'{:.1f}% of data'.format(within_err),
             horizontalalignment='center',verticalalignment='center')
    ax2.text(np.min(bins),np.max(hist)*1.1,'{:.1f}% of data'.format(100-within_err),
             horizontalalignment='left',verticalalignment='center')
    ax2.text(np.max(bins),np.max(hist)*1.1,'{:.1f}% of data'.format(100-within_err),
             horizontalalignment='right',verticalalignment='center')
    ax2.legend(loc=(0.35,0.05))
    
print ('\nDisplaying plot 3')
plt.show()