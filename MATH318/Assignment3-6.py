import numpy as np
import math
from scipy import special as spc
import matplotlib.pyplot as plt
from scipy.stats import poisson as psn

def binomial(n, p, towhere):
    probability = 0
    for indx in range(towhere+1):
        probability += spc.binom(n, indx)*p**indx*(1-p)**(n-indx)
    return probability


def poisson(n, p, towhere):
    probability = 0
    for indx in range(towhere+1):
        probability += np.exp(-n*p)*(n*p)**indx/(math.factorial(indx))
    return probability


print binomial(408, 1.0/40.0, 7)
print poisson(408, 1.0/40.0, 7)
kvalues = np.arange(0, 25, 1)

simulation = np.random.binomial(408, 1.0/40.0, 50000)
overbooked = []
flights = 0
for n in range(len(simulation)):
    if simulation[n] < 8:
        flights += 1
    overbooked.append(float(flights)/float(n+1))

plt.hist(simulation, bins="auto", normed=True, label="Simulation")
plt.plot(kvalues, 4.7*psn.pmf(kvalues, 408*1.0/40.0), label="Poisson Approximation")
plt.title('Simulations of Airplane Missed Passengers', fontsize=36)
plt.xlabel("Number of Missed Passengers", fontsize=24)
plt.ylabel('Probability', fontsize=24)
plt.legend(loc="best")
plt.show()

plt.plot(np.arange(1, len(simulation)+1), overbooked)
plt.title("Running Proportion of Overbooked Flights", fontsize=36)
plt.xlabel("Simulation Number", fontsize=24)
plt.ylabel("Proportion", fontsize=24)
plt.show()