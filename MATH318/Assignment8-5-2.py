import numpy as np


def normal(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-(x ** 2) / 2)


percentages = []
for val in range(100):
    Xvals = np.random.rand(10000)
    Yvals = np.random.rand(10000)
    percent = len(Yvals[np.where(Yvals <= normal(Xvals))])/10000.0
    percentages.append(percent)

percentages = np.array(percentages)
print np.mean(percentages)
print np.var(percentages)
