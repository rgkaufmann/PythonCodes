import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
M = 9.942e30
c = 2.998e8
rs = 2*G*M/c**2

def effectivePotential(r, L):
    return (c**2)/2*(1-rs/r)*(1+L**2/(c**2*r**2))

def energy(r, L):
#    return effectivePotential(r, L)*0.5*L**2
    return 0

def velocitySquare(r, L):
    return energy(r, L)**2-2*effectivePotential(r, L)

def effectivePotentialDerivative(r, L):
    return G*M*r**2-L**2*r+3*G*M/c**2*L**2

rValues = np.linspace(0.00000000001*rs, 5*rs, 1000)
Potential11 = effectivePotential(rValues, c*rs)
DPotential11 = effectivePotentialDerivative(rValues, c*rs)
v11 = velocitySquare(rValues, c*rs)
Potential13 = effectivePotential(rValues, np.sqrt(3)*c*rs)
DPotential13 = effectivePotentialDerivative(rValues, np.sqrt(3)*c*rs)
v13 = velocitySquare(rValues, np.sqrt(3)*c*rs)
Potential14 = effectivePotential(rValues, 4*c*rs)
DPotential14 = effectivePotentialDerivative(rValues, 4*c*rs)
v14 = velocitySquare(rValues, 4*c*rs)
Potential12 = effectivePotential(rValues, 2*c*rs)
DPotential12 = effectivePotentialDerivative(rValues, 2*c*rs)
v12 = velocitySquare(rValues, 2*c*rs)

#print(v12)

fig, ax1 = plt.subplots()
ax1.set_xlabel('Radius in Terms of the Schwarzchild Radius')
ax1.set_ylabel('Effective Potential')
ax1.plot(rValues/rs, Potential11, label=r'L=c*rs')
ax1.plot(rValues/rs, Potential13, label=r'L=\sqrt{3}c*rs')
ax1.plot(rValues/rs, Potential12, label=r'L=2c*rs')
ax1.plot(rValues/rs, Potential14, label=r'L=4c*rs')
ax1.set_ylim(-0.2*1e18, 1.5*1e17)
ax1.hlines(y=0, xmin=0, xmax=5)
ax1.vlines(x=1.5, ymin=-1e33, ymax=1e33)
ax1.vlines(x=3, ymin=-1e33, ymax=1e33)
ax1.set_xlim(0, 5)
fig.legend()
fig.suptitle('Effective Potential of an Object Near a 5 Mass Black Hole as a Function of Radius')

ax2 = ax1.twinx()
ax2.set_ylabel('Velocity Squared')
ax2.plot(rValues/rs, DPotential11)
ax2.plot(rValues/rs, DPotential13)
ax2.plot(rValues/rs, DPotential12)
ax2.plot(rValues/rs, DPotential14)
ax2.set_ylim(-1e18, 1e18)

fig.tight_layout()
plt.show()