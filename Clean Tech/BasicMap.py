import numpy as np
import matplotlib.pyplot as plt
import scipy as spicy

class mapPoint:
    def __init__(self, Lat, Long, Type):
        self.coor = (float(Lat), float(Long))
        self.type = Type
        
    def getLat(self):
        return self.coor[0]
    
    def getLong(self):
        return self.coor[1]
    
    def getType(self):
        return self.type
        
class mappable:
    def __init__(self):
        self.mapPlots = []
        self.colors = {'Water': 'b', 'Urban': 'r', 'Natural': 'g', '1': 'k', 'Ice': 'w'}
    
    def loadMap(self, mapData):
        for index in range(len(mapData[:, 0])):
            self.mapPlots.append(mapPoint(*mapData[index, :]))
            print(index)
    
    def plotMap(self):
        for point in self.mapPlots:
            print(str(point.getLong()) + ', ' + str(point.getLat()))
            plt.scatter(point.getLong(), point.getLat(), s=1,
                        c=self.colors.get(point.getType()), marker='s')
        plt.show()
        
file = np.loadtxt("MapCoors.txt", dtype=str, delimiter=',')

BCMap = mappable()
BCMap.loadMap(file)
BCMap.plotMap()