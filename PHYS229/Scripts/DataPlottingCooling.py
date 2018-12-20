import numpy as np
import matplotlib.pyplot as plt

def convection(t, Tc):
    return np.power(1/(C*t-1/(np.power(Tc-293, 1/4))), 4)+293

C = -0.00005761

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Cooling Process/Data/DataSet1.txt"
times1   = np.loadtxt(filename, usecols=0)*60
smooth1  = np.loadtxt(filename, usecols=2)+273
lacquer1 = np.loadtxt(filename, usecols=3)+273
rough1   = np.loadtxt(filename, usecols=1)+273
uncert1  = np.loadtxt(filename, usecols=4)

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Cooling Process/Data/DataSet2.txt"
times2   = np.loadtxt(filename, usecols=0)*60
smooth2  = np.loadtxt(filename, usecols=1)+273
lacquer2 = np.loadtxt(filename, usecols=2)+273
rough2   = np.loadtxt(filename, usecols=3)+273
uncert2  = np.loadtxt(filename, usecols=4)

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/PHYS229/"
filename += "Cooling Process/Data/SamDataSet.txt"
times3   = np.loadtxt(filename, usecols=0)*60
smooth3  = np.loadtxt(filename, usecols=1)+273
lacquer3 = np.loadtxt(filename, usecols=2)+273
rough3   = np.loadtxt(filename, usecols=3)+273
uncert3  = np.loadtxt(filename, usecols=4)

plt.scatter(times1, smooth1, c='r')
plt.title('Temperature as a function of time for a cooling smooth aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times2, smooth2, c='r')
plt.title('Temperature as a function of time for a cooling smooth aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times3, smooth3, c='r')
plt.title('Temperature as a function of time for a cooling smooth aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times1, lacquer1, c='r')
plt.title('Temperature as a function of time for a cooling lacquered aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times2, lacquer2, c='r')
plt.title('Temperature as a function of time for a cooling lacquered aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times3, lacquer3, c='r')
plt.title('Temperature as a function of time for a cooling lacquered aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times1, rough1, c='r')
plt.title('Temperature as a function of time for a cooling rough aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times2, rough2, c='r')
plt.title('Temperature as a function of time for a cooling rough aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

plt.scatter(times3, rough3, c='r')
plt.title('Temperature as a function of time for a cooling rough aluminum rod')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

testTimes = np.linspace(min(times1), max(times1), 100)

plt.scatter(times1, smooth1, c='r', label='Smooth')
plt.scatter(times1, lacquer1, c='g', label='Lacquered')
plt.scatter(times1, rough1, c='c', label='Rough')
plt.plot(testTimes, convection(testTimes, 363), c='m', label='Convection')
plt.title('Temperature as a function of time for a cooling rod compared to a convection equation')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.legend(loc='best')
plt.show()

testTimes = np.linspace(min(times2), max(times2), 100)

plt.scatter(times2, smooth2, c='r', label='Smooth')
plt.scatter(times2, lacquer2, c='g', label='Lacquered')
plt.scatter(times2, rough2, c='c', label='Rough')
plt.plot(testTimes, convection(testTimes, 363), c='m', label='Convection')
plt.title('Temperature as a function of time for a cooling rod compared to a convection equation')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.legend(loc='best')
plt.show()

testTimes = np.linspace(min(times3), max(times3), 100)

plt.scatter(times3, smooth3, c='r', label='Smooth')
plt.scatter(times3, lacquer3, c='g', label='Lacquered')
plt.scatter(times3, rough3, c='c', label='Rough')
plt.plot(testTimes, convection(testTimes, 363), c='m', label='Convection')
plt.title('Temperature as a function of time for a cooling rod compared to a convection equation')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.legend(loc='best')
plt.show()