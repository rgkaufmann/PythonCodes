import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit as cf

###############################################################################

def nearFieldRadialFunc(radius, coeff, power, side, offset):
    return coeff*(np.abs(np.abs(radius)-side)**power)+offset

def nearFieldAngularFunc(theta, coeff, freq, phase, offset):
    return coeff*np.sin(freq*theta+phase)+offset

def nearFieldFunc(point, coeff, power, side, freq, phase, offset):
    theta, radius = point
    return nearFieldAngularFunc(theta, nearFieldRadialFunc(radius, coeff,
                                                           power, side, 0),
                                freq, phase, offset)
    
###############################################################################
    
def constantRadiusSetUp(DataSet, Radius):
    WorkedData = np.zeros((len(DataSet), 4))
    WorkedData[:, 0] = np.abs(np.arctan(DataSet[:, 1]/DataSet[:, 0]))
    WorkedData[:, 1] = np.ones(len(DataSet))*Radius
    WorkedData[:, 2] = DataSet[:, 2]
    WorkedData[:, 3] = (np.sqrt(DataSet[:, 0]**2+DataSet[:, 1]**2)-Radius)
    WorkedData[:, 3] *= DataSet[:, 2]/Radius*950
    WorkedData[np.where(WorkedData[:, 2]<=0), 0] += (np.pi/2)
    WorkedData[np.where(DataSet[:, 0]>=0), 0] += np.pi
    return WorkedData

def constantThetaSetUp(DataSet, Theta):
    WorkedData = np.zeros((len(DataSet), 4))
    WorkedData[:, 0] = np.ones(len(DataSet))*Theta
    WorkedData[:, 1] = np.sqrt(DataSet[:, 0]**2+DataSet[:, 1]**2)
    WorkedData[np.where(DataSet[:, 0]<0), 1] *= -1
    WorkedData[:, 2] = DataSet[:, 2]
    WorkedData[:, 3] = (np.abs(np.arctan(DataSet[:, 1]/DataSet[:, 0]))-Theta)
    WorkedData[:, 3] *= DataSet[:, 2]*1500
    if (Theta!=0):
        WorkedData[:, 2] /= Theta
    return WorkedData

def chiSquared(x, y, sigma, params, func):
    return np.sum((y-func(x, *params))**2/sigma**2)

###############################################################################

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField45Positive.txt"
Positive45Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField45Negative.txt"
Negative45Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField90Vertical.txt"
Vertical90Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField00Horizontal.txt"
Horizontal00Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField025Radius.txt"
Radius025Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField050Radius.txt"
Radius050Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField075Radius.txt"
Radius075Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/NearField100Radius.txt"
Radius100Data = np.loadtxt(filename)

###############################################################################

PolarPositive045 = constantThetaSetUp(Positive45Data, np.pi/4)
PolarNegative045 = constantThetaSetUp(Negative45Data, np.pi/4)
PolarVertical090 = constantThetaSetUp(Vertical90Data, np.pi/2)
PolarHorizontal0 = constantThetaSetUp(Horizontal00Data, 0)
PolarRadius025 = constantRadiusSetUp(Radius025Data, 0.25)
PolarRadius050 = constantRadiusSetUp(Radius050Data, 0.5)
PolarRadius075 = constantRadiusSetUp(Radius075Data, 0.75)
PolarRadius100 = constantRadiusSetUp(Radius100Data, 1.0)

FullRadialData = np.vstack((PolarPositive045, PolarNegative045,
                            PolarVertical090, PolarHorizontal0))
FullAngularData = np.vstack((PolarRadius025, PolarRadius050,
                             PolarRadius075, PolarRadius100))
FullData = np.vstack((FullRadialData, FullAngularData))

###############################################################################

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Positive45Data[:, 0], Positive45Data[:, 1],
           Positive45Data[:, 2], c='c')
ax.scatter(Negative45Data[:, 0], Negative45Data[:, 1],
           Negative45Data[:, 2], c='c')
ax.scatter(Vertical90Data[:, 0], Vertical90Data[:, 1],
           Vertical90Data[:, 2], c='c')
ax.scatter(Horizontal00Data[:, 0], Horizontal00Data[:, 1],
           Horizontal00Data[:, 2], c='c')
ax.scatter(Radius025Data[:, 0], Radius025Data[:, 1],
           Radius025Data[:, 2], c='c')
ax.scatter(Radius050Data[:, 0], Radius050Data[:, 1],
           Radius050Data[:, 2], c='c')
ax.scatter(Radius075Data[:, 0], Radius075Data[:, 1],
           Radius075Data[:, 2], c='c')
ax.scatter(Radius100Data[:, 0], Radius100Data[:, 1],
           Radius100Data[:, 2], c='c')
plt.show()

###############################################################################

guess = (0.5, -3, 0.5*np.sqrt(2), 0)
RParams, RCOV = cf(nearFieldRadialFunc, PolarPositive045[:, 1],
                   PolarPositive045[:, 2], p0=guess,
                   sigma=PolarPositive045[:, 3])

rtest1 = np.linspace(-1, -0.78, 100)
rtest2 = np.linspace(-0.72, 0.72, 100)
rtest3 = np.linspace(0.78, 1, 100)
ztest1 = nearFieldRadialFunc(rtest1, *RParams)
ztest2 = nearFieldRadialFunc(rtest2, *RParams)
ztest3 = nearFieldRadialFunc(rtest3, *RParams)

plt.plot(rtest1, ztest1)
plt.plot(rtest2, ztest2)
plt.plot(rtest3, ztest3)
plt.scatter(PolarPositive045[:, 1], PolarPositive045[:, 2])
plt.show()

chi = chiSquared(PolarPositive045[:, 1], PolarPositive045[:, 2],
                 PolarPositive045[:, 3], RParams, nearFieldRadialFunc)
dof = len(PolarPositive045[:, 1])-len(RParams)
print ("\nGoodness of fit - chi square measure:")
print ("Chi2 = {}, Chi2/dof = {}\n".format(chi, chi/dof))

RCOV = RCOV*dof/chi
paramserr = np.sqrt(np.diag(RCOV))

param_names = ['Coefficient', 'Power', 'Side', 'Offset']

print ("Fit parameters:")
for i in range(len(RParams)):
    print ('{} = {:.3e} +/- {:.3e}'.format(param_names[i], RParams[i],
                                           paramserr[i]))

###############################################################################
    
guess = (50, 2, 0, 0)
AParams, ACOV = cf(nearFieldAngularFunc, PolarRadius025[:, 0],
                   PolarRadius025[:, 2], p0=guess, sigma=PolarRadius025[:, 3])

ttest = np.linspace(0, 2*np.pi, 100)
ztest4 = nearFieldAngularFunc(ttest, *AParams)

plt.plot(ttest, ztest4)
plt.scatter(PolarRadius025[:, 0], PolarRadius025[:, 2])
plt.show()

chi = chiSquared(PolarRadius025[:, 0], PolarRadius025[:, 2],
                 PolarRadius025[:, 3], RParams, nearFieldRadialFunc)
dof = len(PolarRadius025[:, 0])-len(RParams)
print ("\nGoodness of fit - chi square measure:")
print ("Chi2 = {}, Chi2/dof = {}\n".format(chi, chi/dof))

ACOV = ACOV*dof/chi
paramserr = np.sqrt(np.diag(ACOV))

param_names = ['Coefficient', 'Frequency', 'Phase', 'Offset']

print ("Fit parameters:")
for i in range(len(AParams)):
    print ('{} = {:.3e} +/- {:.3e}'.format(param_names[i], AParams[i],
                                           paramserr[i]))

###############################################################################

guess = (5, -0.2, 0.7268, 2, np.pi/2, -0.001)
FParams, FCOV = cf(nearFieldFunc, (FullData[:, 0], FullData[:, 1]),
                   FullData[:, 2], p0=guess, sigma=FullData[:, 3],
                   maxfev=5000)

chi = chiSquared((FullData[:, 0], FullData[:, 1]), FullData[:, 2],
                 FullData[:, 3], FParams, nearFieldFunc)
dof = len(FullData[:, 1])-len(FParams)
print ("\nGoodness of fit - chi square measure:")
print ("Chi2 = {}, Chi2/dof = {}\n".format(chi, chi/dof))

FCOV = FCOV*dof/chi
paramserr = np.sqrt(np.diag(FCOV))

param_names = ['Coefficient', 'Power', 'Side', 'Frequency', 'Phase', 'Offset']

print ("Fit parameters:")
for i in range(len(FParams)):
    print ('{} = {:.3e} +/- {:.3e}'.format(param_names[i], FParams[i],
                                           paramserr[i]))

rtest1 = np.linspace(-1, -0.55, 100)
rtest2 = np.linspace(-0.50, 0, 100)
ttest  = np.linspace(0, 2*np.pi, 100)
rmesh1, tmesh1 = np.meshgrid(rtest1, ttest)
rmesh2, tmesh2 = np.meshgrid(rtest2, ttest)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(rmesh1*np.cos(tmesh1), rmesh1*np.sin(tmesh1),
                nearFieldFunc((tmesh1, rmesh1), *FParams))
ax.plot_surface(rmesh2*np.cos(tmesh2), rmesh2*np.sin(tmesh2),
                nearFieldFunc((tmesh2, rmesh2), *FParams))
ax.scatter(Positive45Data[:, 0], Positive45Data[:, 1],
           Positive45Data[:, 2], c='c')
ax.scatter(Negative45Data[:, 0], Negative45Data[:, 1],
           Negative45Data[:, 2], c='c')
ax.scatter(Vertical90Data[:, 0], Vertical90Data[:, 1],
           Vertical90Data[:, 2], c='c')
ax.scatter(Horizontal00Data[:, 0], Horizontal00Data[:, 1],
           Horizontal00Data[:, 2], c='c')
ax.scatter(Radius025Data[:, 0], Radius025Data[:, 1],
           Radius025Data[:, 2], c='c')
ax.scatter(Radius050Data[:, 0], Radius050Data[:, 1],
           Radius050Data[:, 2], c='c')
ax.scatter(Radius075Data[:, 0], Radius075Data[:, 1],
           Radius075Data[:, 2], c='c')
ax.scatter(Radius100Data[:, 0], Radius100Data[:, 1],
           Radius100Data[:, 2], c='c')
plt.show()