import numpy as np
import math


class DataHandler:

    def __init__(self):
        self.dataset = np.array([])
        self.file = ''

    def checkdata(self, types):
        if 'BaseStats' in self.file:
            for pokemon in self.dataset:
                print(str(pokemon["Name"])[2:-1])
                if int(math.floor((pokemon["BaseATK"]+15)*(pokemon["BaseDEF"]+15)**0.5*(pokemon["BaseSTM"]+15)**0.5 *
                                  0.790300**2/10)) != pokemon["MaxCP"]:
                    print('Max CP values do not match up! Please reenter data.')
                    input()
                if str(pokemon["Type1"])[2:-1].capitalize() not in types:
                    print('Type 1 does not exist! Please reenter data.')
                    input()
                if str(pokemon["Type2"])[2:-1].capitalize() not in types and str(pokemon[6])[2:-1] != "None":
                    print('Type 2 does not exist! Please reenter data.')
                    input()

    def loadtxt(self, filename, datatype):
        try:
            self.file = filename
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

    def quickpokedex(self, filename):
        f = open(filename, "w")
        for line in self.dataset:
            f.write(str(line[0])[2:-1] + "\n")
        f.close()
