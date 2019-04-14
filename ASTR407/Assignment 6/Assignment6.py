import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})

f = 1.0e-7
ve = 1.0
A = 0.3
G = 6.674e-8
R = 8.31e7
s = 5.67e-5
L = 3.85e33
au = 1.496e13
mmw = 28.0
bulk = 3.0
rad = 6.371e8


def scalinglaw(d, rho, r, mu):
    return 4.5e-5*np.sqrt(d)*mu*(rho*r)**2


radii = np.linspace(0.1, 4, 10000)
plt.plot(radii, scalinglaw(1, 1, radii, 1), label="1au")
plt.plot(radii, scalinglaw(9, 1, radii, 1), label="9au")
plt.plot(radii, scalinglaw(35, 1, radii, 1), label='35au')
plt.scatter(1, 1e-3, label='Actual Earth Value')
plt.legend(loc='best')
plt.title('Atmospheric Surface Mass Density as a Function of Planet Radius\nWith Constant Bulk Density and Ratio',
          fontsize=30)
plt.xlabel('Planet Radius in Earth Radii', fontsize=26)
plt.ylabel('Atmospheric Mass Density in g/cc', fontsize=26)
plt.show()
