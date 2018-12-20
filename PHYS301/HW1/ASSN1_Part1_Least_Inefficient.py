import numpy as np
import matplotlib.pyplot as plt

ep0=8.854E-12
Q=1E-6
R=0.1
r=np.arange(0,0.5,0.01)
y=np.zeros(int(0.5/0.01))

for h in range(len(r)):
    for i in r[h:]:
        for j in range(-len(r[np.where(r>=i)]), 1):
            for k in range(1, len(r[np.where(r>=i)]+1)):
                print('{} {} {} {} {}'.format(h, i, j, k, k==-j))
                if k==-j:
                    if i<=0.1:
                        y[j]=Q/(4*np.pi*ep0*0.1)
                    else:
                        y[j]=Q/(4*np.pi*ep0*i)
            
plt.plot(r, y)
plt.title('Potential of a Charged Spherical Shell Over Distance')
plt.xlabel('Distance(m)')
plt.ylabel('Potential(V)')
plt.show()