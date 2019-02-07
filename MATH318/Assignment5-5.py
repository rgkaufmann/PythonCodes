import numpy as np
import matplotlib.pyplot as plt

XVals = np.random.rand(5000)
YVals = np.random.rand(5000)

XValsUse = XVals[np.where(XVals + YVals <= 1)]
YValsUse = YVals[np.where(XVals + YVals <= 1)]

plt.scatter(XValsUse, YValsUse, s=5)
plt.plot(np.array([0, 1, 0, 0]), np.array([0, 0, 1, 0]))
plt.title("Uniform Distribution of X and Y Values Upon a Square", fontsize=48)
plt.xlabel("X Values", fontsize=36)
plt.ylabel("Y Values", fontsize=36)
plt.show()

XVals = np.random.rand(5000)
YVals = []
for value in XVals:
    YVals.append((1-value)*np.random.rand(1))
YVals = np.array(YVals)

plt.scatter(XVals, YVals, s=5)
plt.plot(np.array([0, 1, 0, 0]), np.array([0, 0, 1, 0]))
plt.title("Uniform Distribution of X and Y Values Upon the Remaining Area", fontsize=40)
plt.xlabel("X Values", fontsize=36)
plt.ylabel("Y Values", fontsize=36)
plt.show()
