import numpy as np
import matplotlib.pyplot as plt

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Field Simulations/Data/FarFieldDistanceDependence.txt"
Data = np.loadtxt(filename)

DataSet = np.zeros(Data.shape)
DataSet[:, 0] = np.sqrt(Data[:, 0]**2+Data[:, 1]**2)
DataSet[:, 1] = Data[:, 2]
DataSet[:, 2] = (np.abs(np.arctan(Data[:, 1]/Data[:, 0]))-np.pi/4)/(np.pi/4)
DataSet[:, 2] *= Data[:, 2]*7.5
sigma = np.abs(np.average(DataSet[:, 2]))

plt.scatter(DataSet[:, 0], np.log(np.abs(DataSet[:, 1])))
plt.show()