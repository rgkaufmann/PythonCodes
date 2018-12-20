import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy.optimize import curve_fit as optimizer
from scipy.stats import shapiro

warnings.filterwarnings('ignore', category=UserWarning)

def combinedGaussian(X, C1, sigma1, mean1, C2, sigma2, mean2):
    first = (C1/np.sqrt(2*np.pi*sigma1**2))*np.exp(-1/2*((X-mean1)/(2*sigma1))**2)
    second = (C2/np.sqrt(2*np.pi*sigma2**2))*np.exp(-1/2*((X-mean2)/(2*sigma2))**2)
    return first + second

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/ASTR 205 1-2.csv"
Data = np.loadtxt(filename, comments='#')
Xvals = np.arange(-10, 10, 0.05)
alpha = 0.05

n, bins, patch = plt.hist(Data, bins=150, color='c', normed=True)
bin_centers = bins[:-1]+0.5*(bins[1:]-bins[:-1])
plt.title('Histogram of 100,000 Given Random Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

W, pvalue = shapiro(Data)
print('Shapiro-Wilk Normality Test p-value: {:.2e}.'.format(pvalue))
if pvalue<alpha:
    print('Normality test failed, with {:.2e} < {}.'.format(pvalue, alpha))
    print('Data is not Gaussian.')
print()


initial = [5300,1.3,0,1000,1,-4]
plt.hist(Data, bins=150, color='c', zorder=1, normed=True)
plt.plot(bin_centers, combinedGaussian(bin_centers, *initial), 'r--', zorder=10)
plt.title('Histogram with Initial Fit for Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

plt.hist(Data, bins=150, color='c', zorder=1, normed=True)
params, cov = optimizer(combinedGaussian, bin_centers, n, p0=initial)
plt.plot(bin_centers, combinedGaussian(bin_centers, *params), 'r--', zorder=10)
plt.title('Fitted Combined Gaussian for Given Data Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

param_names = ['C1    ', 'sigma1', 'mean1 ', 'C2    ', 'sigma2', 'mean2 ']
print ("Fit parameters:")
for i in range(len(params)):
    if (params[i] < 0):
        print ('{} = {:.3e}'.format(param_names[i], params[i]))
    else:
        print('{} =  {:.3e}'.format(param_names[i], params[i]))