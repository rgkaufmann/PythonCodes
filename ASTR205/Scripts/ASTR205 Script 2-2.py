import numpy as np
import matplotlib.pyplot as plt

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "HST47TucPhotometrics.txt"
Data = np.loadtxt(filename)

V_BData = np.empty((len(Data[:, 0]), 2))
V_BData[:, 0] = Data[:, 0]
V_BData[:, 1] = Data[:, 0] - Data[:, 1]

plt.gca().invert_yaxis()
plt.title('Color-Magnitude Diagram of Area around 47-Tucanae')
plt.xlabel('V-I')
plt.ylabel('V magnitude')
plt.scatter(V_BData[:, 1], V_BData[:, 0], s=0.01, marker='.', color='c')
plt.show()

plt.title('Proper Motion Diagram of Area around 47-Tucanae')
plt.xlabel('Proper motion in X')
plt.ylabel('Proper motion in Y')
plt.scatter(Data[:, 3], Data[:, 2], s=0.01, marker='.', color='r')
plt.show()

V_BData47Tuc = V_BData[(np.where(Data[:, 2]**2+Data[:, 3]**2<=0.3**2)), :][0]
Tuc47Data = Data[(np.where(Data[:, 2]**2+Data[:, 3]**2<=0.3**2)), :][0]

SmallMagellanicData = Data[(np.where((Data[:, 2]+0.6)**2+(Data[:,  3]+0.2)**2<=0.25**2)), :][0]
V_BDataSmallMagellanic = V_BData[(np.where((Data[:, 2]+0.6)**2+(Data[:,  3]+0.2)**2<=0.25**2)), :][0]

OtherData = Data[np.where(np.logical_not(np.logical_or(((Data[:, 2]+0.6)**2+(Data[:,  3]+0.2)**2<=0.25**2), Data[:, 2]**2+Data[:, 3]**2<=0.1))), :][0]
V_BDataOther = V_BData[np.where(np.logical_not(np.logical_or(((Data[:, 2]+0.6)**2+(Data[:,  3]+0.2)**2<=0.25**2), Data[:, 2]**2+Data[:, 3]**2<=0.1))), :][0]

plt.gca().invert_yaxis()
plt.title('Isolated Color-Magnitude Diagram of Only 47-Tucanae')
plt.xlabel('V-I')
plt.ylabel('V magnitude')
plt.scatter(V_BData47Tuc[:, 1], V_BData47Tuc[:, 0], s=0.01, marker='.',
            color='c')
plt.show()

plt.gca().invert_yaxis()
plt.title('Color-Magnitude Diagram of Different Bodies from Given Data')
plt.xlabel('V-I')
plt.ylabel('V magnitude')
plt.scatter(V_BDataOther[:, 1], V_BDataOther[:, 0], s=0.01, marker='.',
            color='c', label='Other')
plt.scatter(V_BData47Tuc[:, 1], V_BData47Tuc[:, 0], s=0.01, marker='.',
            color='r', label='47-Tucanae')
plt.scatter(V_BDataSmallMagellanic[:, 1], V_BDataSmallMagellanic[:, 0], s=0.01,
            marker='.', color='m', label='Small Magellanic Cloud')
plt.legend(numpoints=1, markerscale=100, loc='best')
plt.show()

plt.title('Proper Motion Digram of Different Bodies from Given Data')
plt.xlabel('Proper motion in X')
plt.ylabel('Proper motion in Y')
plt.scatter(OtherData[:, 3], OtherData[:, 2], s=0.01, marker='.', color='c',
            label='Other')
plt.scatter(Tuc47Data[:, 3], Tuc47Data[:, 2], s=0.01, marker='.', color='r',
            label='47-Tucanae')
plt.scatter(SmallMagellanicData[:, 3], SmallMagellanicData[:, 2], s=0.01,
            marker='.', color='m', label='Small Magellanic Cloud')
plt.legend(numpoints=1, markerscale=100, loc='best')
plt.show()

plt.gca().invert_yaxis()
plt.title('Adjusted Color-Magnitude Diagram of 47-Tucanae and the Small Magellanic Cloud')
plt.xlabel('V-I')
plt.ylabel('V magnitude')
plt.scatter(V_BData47Tuc[:, 1], V_BData47Tuc[:, 0], s=0.01, marker='.',
            color='r', label='47-Tucanae')
plt.scatter(V_BDataSmallMagellanic[:, 1]+0.1, V_BDataSmallMagellanic[:, 0]-5.8, s=0.01,
            marker='.', color='m', label='Small Magellanic Cloud')
plt.legend(numpoints=1, markerscale=100, loc='best')
plt.show()