import numpy as np
import matplotlib.pyplot as plt

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/FarFieldAngleDependence.txt"
Data = np.loadtxt(filename)

DataSet = np.zeros(Data.shape)
DataSet[:, 0] = np.abs(np.arctan(Data[:, 1]/Data[:, 0]))
DataSet[:, 1] = Data[:, 2]
DataSet[:, 2] = (np.sqrt(Data[:, 0]**2+Data[:, 1]**2)-1.5)/1.5
DataSet[:, 2] *= Data[:, 2]*170
DataSet[np.where(DataSet[:, 1]<=0), 0] += (np.pi/2)

plt.scatter(DataSet[:, 0], DataSet[:, 1])
plt.show()