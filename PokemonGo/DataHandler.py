import numpy as np


class DataHandler:
    dataset = np.array([[]])

    def __init__(self):
        self.dataset = np.array([])

    def loadtxt(self, filename, datatype):
        try:
            self.dataset = np.loadtxt(filename, dtype=datatype, delimiter=',')
        except IOError or ValueError:
            return False
        return True

    def getdata(self):
        return self.dataset

    def adddata(self, newdata):
        if type(newdata) is not list:
            return False
        data = self.dataset.tolist()
        data = list(data)
        for line in newdata:
            print line
            data.append(line)
        self.dataset = np.array(data)
        return True

    def savetxt(self, filename):
        f = open(filename, "w")
        for line in self.dataset:
            for inter in range(len(line)):
                if inter < (len(line)-1):
                    f.write(str(line[inter])+",")
                else:
                    f.write(str(line[inter]))
            f.write("\n")
        f.close()
