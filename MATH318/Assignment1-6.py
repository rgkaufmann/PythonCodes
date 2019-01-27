import numpy as np
import matplotlib.pyplot as plt


def birthday(n, days):
    birthdays = np.random.randint(1, days+1, n)
    birthdays.sort()
    for indx in range(n-1):
        if birthdays[indx] == birthdays[indx+1]:
            return True
    return False


def factorial(n, days):
    multiple = 1.0
    for indx in range(n):
        multiple *= (days-indx)
    return multiple


def trueprobability(n, days):
    probability = np.zeros(len(n))
    for indx in range(len(n)):
        probability[indx] = 1.0 - (factorial(n[indx], days) / (np.power(days, n[indx])))
    return probability


earthyear = 365.0
marsyear = 669.0
testprobabilityearth = np.zeros(70)
testprobabilitymars = np.zeros(70)
nvalues = np.arange(1, 71, 1)

for nvalue in nvalues:
    for iteration in range(100000):
        if birthday(nvalue, int(earthyear)):
            testprobabilityearth[nvalue-1] += 1
        if birthday(nvalue, int(marsyear)):
            testprobabilitymars[nvalue-1] += 1
    testprobabilityearth[nvalue-1] /= 100000
    testprobabilitymars[nvalue-1] /= 100000

plt.plot(nvalues, testprobabilityearth, label='Experimental Probability')
plt.plot(nvalues, trueprobability(nvalues, earthyear), label='Expected Probability')
plt.title('Probability of at Least One Repeated Birthday among n People on Earth', fontsize=25)
plt.xlabel('Number of People, n', fontsize=18)
plt.ylabel('Probability', fontsize=18)
plt.legend(loc='best')
plt.show()

plt.plot(nvalues, testprobabilitymars, label='Experimental Probability')
plt.plot(nvalues, trueprobability(nvalues, marsyear), label='Expected Probability')
plt.title('Probability of at Least One Repeated Birthday among n People on Mars', fontsize=25)
plt.xlabel('Number of People, n', fontsize=18)
plt.ylabel('Probability', fontsize=18)
plt.legend(loc='best')
plt.show()
