import numpy as np
import matplotlib.pyplot as plt

def spatial(x, n, a):
    return np.sqrt(2/a)*np.sin(n*np.pi/a*x)

def wavefunction(x, phi, a):
    return 1/np.sqrt(2)*((spatial(x, 1, a)+0j)+np.exp(1j*phi)*spatial(x, 2, a))

def probability(x, phi, a):
    return np.abs(wavefunction(x, phi, a))**2

width=1
xValues=np.linspace(0, 1, 1000)
phiValues = np.linspace(0, np.pi, 5)

for phi in phiValues:
    legendlabel='Phi = {:.3f}'.format(phi)
    plt.plot(xValues, wavefunction(xValues, phi, width).real,
             label=legendlabel)
plt.title('Wavefunction at various values of phi')
plt.ylabel(r'$\Psi(x,0)$')
plt.xlabel('x/a')
plt.legend(loc='best')
plt.xlim(-0.05, 1.45)
plt.ylim(-0.5, 1.8)
plt.show()

for phi in phiValues:
    legendlabel='Phi = {:.3f}'.format(phi)
    plt.plot(xValues, probability(xValues, phi, width), label=legendlabel)
plt.title('Probability function at various values of phi')
plt.ylabel(r'$|\Psi(x,0)|^2$')
plt.xlabel('x/a')
plt.legend(loc='best')
plt.xlim(-0.05, 1.45)
plt.ylim(-0.05, 3.25)
plt.savefig('ProbabilityAtVariousPhi.jpg')
plt.show()