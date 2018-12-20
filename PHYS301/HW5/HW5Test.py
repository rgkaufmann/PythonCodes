import numpy as np
import matplotlib.pyplot as plt

N = 50       ## Number of points where we compute the solution

xVals = np.linspace(-N/2,N/2,N)  ## Locations where we intend to solve the problem
yVals = np.linspace(-N/2,N/2,N)
xMesh, yMesh = np.meshgrid(xVals, yVals)
V = np.zeros((N,N))         ## Place holder for V where all the guesses are zero

## Setting the boundary values
V[:,:] = 0
V[int(N/2),int(N/2)] = 1
Voriginal = V.copy()

C = [500, 1000, 2000, 5000]

## Iterate the soluton and plot each result showing convergence
for convergence in range(len(C)):
    for iterations in range(1,C[convergence]):
        ## Compute the update (notice the end points are left out)
        for i in range(1,N-1):
            for j in range(1,N-1):
                if not (i==25 and j==25):
                    V[i,j]=0.25*(V[i-1,j]+V[i+1,j]+V[i,j+1]+V[i,j-1])
        print('{}, {}'.format(C[convergence], iterations))
        plt.figure(convergence+1)
        plt.plot(V[:,25])
    plt.title('Convergence at {} iterations'.format(C[convergence]))
    plt.figure((convergence+1)*10)
    plt.pcolor(xMesh, yMesh, V)
    plt.title('Convergence at {} iterations'.format(C[convergence]))
    V = Voriginal.copy()
plt.show()