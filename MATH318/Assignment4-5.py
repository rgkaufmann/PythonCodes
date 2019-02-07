import numpy as np
import matplotlib.pyplot as plt

XVals = 2*np.random.rand(10000)-1
YVals = 2*np.random.rand(10000)-1
XValsUse = XVals[np.where(XVals**2+YVals**2<=1)]
YValsUse = YVals[np.where(XVals**2+YVals**2<=1)]

plt.figure(figsize=(13, 13))
plt.scatter(XValsUse, YValsUse)
plt.title('Uniform Distribution of X and Y on a Unit Circle', fontsize=36)
plt.xlabel('X Value', fontsize=28)
plt.ylabel('Y Value', fontsize=28)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()

RVals = np.random.rand(10000)
TVals = 2*np.pi*np.random.rand(10000)

plt.figure(figsize=(13, 13))
plt.scatter(RVals*np.cos(TVals), RVals*np.sin(TVals))
plt.title('Uniform Distribution of R and Theta on a Unit Circle', fontsize=36)
plt.xlabel('X Value', fontsize=28)
plt.ylabel('Y Value', fontsize=28)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()
