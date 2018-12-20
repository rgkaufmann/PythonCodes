import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import cProfile, pstats, io

pr = cProfile.Profile()
pr.enable()

def update(frame):
    global grid
    gridCopy = np.copy(grid)
    size = grid.shape
    for rowIndx in range(size[0]):
        for colIndx in range(size[1]):
            totalOn = grid[(rowIndx-1)%size[0], (colIndx-1)%size[1]]
            totalOn += grid[(rowIndx-1)%size[0], colIndx]
            totalOn += grid[(rowIndx-1)%size[0], (colIndx+1)%size[1]]
            totalOn += grid[rowIndx, (colIndx-1)%size[1]]
            totalOn += grid[rowIndx, (colIndx+1)%size[1]]
            totalOn += grid[(rowIndx+1)%size[0], (colIndx-1)%size[1]]
            totalOn += grid[(rowIndx+1)%size[0], colIndx]
            totalOn += grid[(rowIndx+1)%size[0], (colIndx+1)%size[1]]
            
            if (grid[rowIndx, colIndx] == 1):
                if totalOn < 2 or totalOn > 3:
                    gridCopy[rowIndx, colIndx] = 0
            else:
                if totalOn == 3:
                    gridCopy[rowIndx, colIndx] = 1
                    
    mat.set_array(gridCopy*255)
    grid = gridCopy
    return [mat]
        
N = 400
grid = np.random.choice([1, 0], N*N, p=[0.2, 0.8]).reshape(N, N)

fig, ax = plt.subplots()
mat = ax.imshow(grid*255, animated=True)
animate = ani.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()

pr.disable()
file = open('Conway.txt', 'w')
s = io.StringIO()
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()