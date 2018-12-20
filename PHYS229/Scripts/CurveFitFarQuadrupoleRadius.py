import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

def farRadiusFunc(radius, coeff, power, offset):
    return coeff*(radius**power)*np.sin(2.001772*3*np.pi/4-0.002958)+offset

def chiSquared(x, y, sigma, params):
    return np.sum((y-farRadiusFunc(x, *params))**2/sigma**2)

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/FarFieldDistanceDependence.txt"
Data = np.loadtxt(filename)

DataSet = np.zeros(Data.shape)
DataSet[:, 0] = np.sqrt(Data[:, 0]**2+Data[:, 1]**2)
DataSet[:, 1] = Data[:, 2]
DataSet[:, 2] = (np.abs(np.arctan(Data[:, 1]/Data[:, 0]))-np.pi/4)/(np.pi/4)
DataSet[:, 2] *= Data[:, 2]*7.5
sigma = np.abs(np.average(DataSet[:, 2]))

###############################################################################

guess = [-1, -1, 0]
xtest = np.linspace(min(DataSet[:, 0]), max(DataSet[:, 0]), num=1000)

plt.errorbar(DataSet[:, 0], DataSet[:, 1], yerr=DataSet[:, 2], linestyle='',
             marker='.')
plt.title("Initial Plot of the Quadrupole Distance Dependence Far Field")
plt.xlabel("Radius (meters)")
plt.ylabel("Potential (Volts)")
plt.plot(xtest, farRadiusFunc(xtest, *guess))
plt.show()

###############################################################################

Fitparams, Fitcov = cf(farRadiusFunc, DataSet[:, 0], DataSet[:, 1], p0=guess,
                       sigma=DataSet[:, 2])
ytest = farRadiusFunc(xtest, *Fitparams)

plt.errorbar(DataSet[:, 0], DataSet[:, 1], yerr=DataSet[:, 2], linestyle='',
             marker='.')
plt.plot(xtest, ytest)
plt.title("Fitted Plot of the Quadrupole Distance Dependence Far Field")
plt.xlabel("Radius (meters)")
plt.ylabel("Potential (Volts)")
plt.show()

chi = chiSquared(DataSet[:, 0], DataSet[:, 1], DataSet[:, 2], Fitparams)
dof = len(DataSet[:, 0])-len(Fitparams)
print ("\nGoodness of fit - chi square measure:")
print ("Chi2 = {}, Chi2/dof = {}\n".format(chi, chi/dof))

Fitcov = Fitcov*dof/chi
paramserr = np.sqrt(np.diag(Fitcov))

param_names = ['Coefficient', 'Power', 'Offset']

print ("Fit parameters:")
for i in range(len(Fitparams)):
    print ('{} = {:.5e} +/- {:.3e}'.format(param_names[i], Fitparams[i],
                                           paramserr[i]))
    
###############################################################################

y_fit=farRadiusFunc(DataSet[:, 0], *Fitparams)
residual = DataSet[:, 1]-y_fit
hist,bins = np.histogram(residual,bins=30)


fig = plt.figure(figsize=(7,10))
fig.suptitle("Residuals of the Quadrupole Distance Dependence Far Field")
ax1 = fig.add_subplot(211)
ax1.errorbar(Data[:, 0], residual, yerr=DataSet[:, 2], marker='.', linestyle='',
             label="residual (y-y_fit)")
ax1.hlines(0,np.min(Data[:, 0]),np.max(Data[:, 0]),lw=2,alpha=0.8)
ax1.set_ylabel("Residuals")
ax1.set_xlabel("Radius (meters)")
ax2 = fig.add_subplot(212)
ax2.bar(bins[:-1],hist,width=bins[1]-bins[0])
ax2.set_ylim(0,1.2*np.max(hist))
ax2.set_xlabel("Residuals")
ax2.set_ylabel("Frequency")
within_err=100.*np.sum((residual<=sigma)&(residual>=-sigma))/len(residual)
print ("\nResidual information:")
print ('{:.1f}% of data points agree with fit'.format(within_err))
ax2.vlines(-sigma,0,np.max(hist)*1.3,lw=3,color='r')
ax2.vlines(+sigma,0,np.max(hist)*1.3,lw=3,color='r',label='+/- error')
plt.show()