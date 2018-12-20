import numpy as np
import matplotlib.pyplot as plt

def rho(radius):
    return rhoC*(1-radius/RS)

def mass(radius):
    return 4*np.pi*rhoC*((radius**3)/3-(radius**4)/(4*RS))

def temperature(radius):
    return (pressure(radius)*mH*mu)/(k*rho(radius))

def pressure(radius):
    P = PC
    P -= G*np.pi*(rhoC**2)*(2*(radius**2)/3-7*(radius**3)/(9*RS)+(radius**4)/(4*RS**2))
    return P

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "StandardSolarModel.txt"
Data = np.loadtxt(filename)

rhoC = 5639.191
PC = 4.485e14
PCSSM = 2.338e16
TC = 5.772e6
TCSSM = 1.548e7
G = 6.674e-11
k = 1.3807e-23
mu = 1/1.67
mH = 1.67e-27
RS = 6.96e8
MS = 1.989e30

rtest = np.linspace(0, 1, 1000)
mtest = mass(rtest*RS)/MS
ttest = temperature(rtest[:-10]*RS)/TC
ptest = pressure(rtest*RS)/PC

plt.plot(rtest, mtest, c='r', label='Simple Model')
plt.plot(Data[:, 1], Data[:, 0], c='c', label='Standard Solar Model')
plt.legend(loc='best')
plt.title('Comparison of Simple Model and Standard Solar Model When Modelling Mass')
plt.xlabel("Solar Radii")
plt.ylabel("Solar Masses")
plt.show()

plt.plot(rtest[:-10], ttest, c='r', label='Simple Model')
plt.plot(Data[:, 1], Data[:, 2]/TCSSM, c='c', label='Standard Solar Model')
plt.legend(loc='best')
plt.title('Comparison of Simple Model and Standard Solar Model When Modelling Temperature')
plt.xlabel('Solar Radii')
plt.ylabel('Temperature/Central Temperature')
plt.show()

plt.plot(rtest, ptest, c='r', label='Simple Model')
plt.plot(Data[:, 1], (Data[:, 4]*0.1)/PCSSM, c='c', label='Standard Solar Model')
plt.legend(loc='best')
plt.title('Comparison of Simple Model and Standard Solar Model When Modelling Pressure')
plt.xlabel('Solar Radii')
plt.ylabel('Pressure/Central Pressure')
plt.show()