import numpy as np
import matplotlib.pyplot as plt

JupiterPeriod = 11.9                                            # #[yr]
ThirdPeriodsma = np.power((JupiterPeriod*1.0/3.0), 2.0/3.0)     # #[AU]
HalfPeriodsma = np.power((JupiterPeriod*1.0/2.0), 2.0/3.0)      # #[AU]
TwoThirdPeriodsma = np.power((JupiterPeriod*2.0/3.0), 2.0/3.0)  # #[AU]
FifthPeriodsma = np.power((JupiterPeriod*2.0/5.0), 2.0/3.0)     # #[AU]
SeventhPeriodsma = np.power((JupiterPeriod*3.0/7.0), 2.0/3.0)   # #[AU]

data = np.loadtxt('MPCxyz.txt')
rdata = np.zeros(len(data))
vdata = np.zeros(len(data))
for indx in range(len(data)):
    rdata[indx] = np.sqrt((data[indx][1]) ** 2.0 + (data[indx][2]) ** 2.0 + (data[indx][3]) ** 2.0)
    vdata[indx] = np.sqrt((data[indx][4]) ** 2.0 + (data[indx][5]) ** 2.0 + (data[indx][6]) ** 2.0)

semimajors = 1.0/(2.0/rdata-(vdata**2.0)/(4*np.pi**2.0))
semimajorsreduced = semimajors[np.where(semimajors > 2.0)]
semimajorsreduced = semimajorsreduced[np.where(semimajorsreduced < 5.5)]

plt.vlines(ThirdPeriodsma, 0, 200, colors='r', linewidth=3.0, label="One Third of Jupiter's Period", zorder=1)
plt.vlines(HalfPeriodsma, 0, 200, colors='k', linewidth=3.0, label="Half of Jupiter's Period", zorder=2)
plt.vlines(TwoThirdPeriodsma, 0, 200, colors='c', linewidth=3.0, label="Two Thirds of Jupiter's Period", zorder=3)
plt.vlines(FifthPeriodsma, 0, 200, colors='g', linewidth=3.0, label="Two Fifths of Jupiter's Period", zorder=4)
plt.vlines(SeventhPeriodsma, 0, 200, colors='m', linewidth=3.0, label="Three Sevenths of Jupiter's Period", zorder=5)
plt.hist(semimajorsreduced, bins=int((5.5-2.0)/0.01), zorder=100)
plt.title('Histogram of Semi-Major Axes of Minor Planets Between 2.0au and 5.5au', fontsize=30)
plt.xlabel('Semi-major axis, a[AU]', fontsize=24)
plt.ylabel('Number of Planets', fontsize=24)
plt.legend(loc='best')
plt.show()
