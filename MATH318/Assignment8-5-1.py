import numpy as np

def normal(x):
    return (1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2)


def In(n):
    return np.mean(normal(np.random.rand(n)))


runs = 100
results = []
for val in range(runs):
    results.append(In(10000))
results = np.array(results)

print np.mean(results)
print np.var(results)