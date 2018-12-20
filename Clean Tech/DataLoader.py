import numpy as np

lats = np.arange(-90, 91, 1) #268
longs = np.arange(-180, 181, 1) #381           #102108 
lats, longs = np.meshgrid(lats, longs)
lats = lats.flatten()
longs = longs.flatten()
types = np.ones(len(lats), dtype=np.int64)
coors = np.concatenate((lats, longs, types))
coors = coors.reshape((3, len(lats))).T

print(coors)

np.savetxt("MapCoors.txt", coors, fmt=('%.4f', '%.4f', '%d'), delimiter=',')