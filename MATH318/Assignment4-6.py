import numpy as np
import matplotlib.pyplot as plt

NormalValues = np.random.normal(0, 1, 10000)
RunningAverage = []
CurrentAverage = 0
for indx in range(len(NormalValues)):
    CurrentAverage = (CurrentAverage*(indx)+NormalValues[indx])/(indx+1)
    RunningAverage.append(CurrentAverage)

plt.plot(range(1, len(NormalValues)+1), RunningAverage)
plt.title('Running Average of Normal Distribution', fontsize=42)
plt.xlabel('Iteration', fontsize=28)
plt.ylabel('Average', fontsize=28)
plt.show()

ExponentialValues = np.random.exponential(1.0/2.0, 10000)
RunningAverage = []
CurrentAverage = 0
for indx in range(len(ExponentialValues)):
    CurrentAverage = (CurrentAverage*(indx)+ExponentialValues[indx])/(indx+1)
    RunningAverage.append(CurrentAverage)

plt.plot(range(1, len(ExponentialValues)+1), RunningAverage)
plt.title('Running Average of Exponential Distribution', fontsize=42)
plt.xlabel('Iteration', fontsize=28)
plt.ylabel('Average', fontsize=28)
plt.show()

CauchyValues = np.random.standard_cauchy(10000)
RunningAverage = []
CurrentAverage = 0
for indx in range(len(CauchyValues)):
    CurrentAverage = (CurrentAverage*(indx)+CauchyValues[indx])/(indx+1)
    RunningAverage.append(CurrentAverage)

plt.plot(range(1, len(CauchyValues)+1), RunningAverage)
plt.title('Running Average of Cauchy Distribution', fontsize=42)
plt.xlabel('Iteration', fontsize=28)
plt.ylabel('Average', fontsize=28)
plt.show()
