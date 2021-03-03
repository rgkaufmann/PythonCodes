import numpy as np
import matplotlib.pyplot as plt
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    warnings.warn("deprecated", DeprecationWarning)

gooddatalist = []


def loader(sample, direction, number):
    dataaddress = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/"

    if direction.lower() == "up":
        dataaddress += "{}/BSweep_-1to14T_Spininjection(0{}).dat".format(sample, number)
    elif direction.lower() == "down":
        dataaddress += "{}/BSweep_14to-1T_Spininjection(0{}).dat".format(sample, number)
    elif direction.lower() == 'full':
        dataaddress += "{}/BSweep_-14to14T_Spininjection(0{}).dat".format(sample, number)
    else:
        dataaddress += "{}/OutPlane_-14to14T_Spininjection(0{}).dat".format(sample, number)

    refsensitivity, xxsensitivity, xysensitivity = 1, 1, 1
    f = open(dataaddress, 'r')
    datareached = False
    data = []
    headers = ""
    for line in f:
        if "sensitivities" in line and not datareached:
            colonone = line.find(":", 40)
            colontwo = line.rfind(":")
            refsensitivity = float(line[42:colonone])
            xxsensitivity = float(line[colonone+1:colontwo])
            try:
                xysensitivity = float(line[colontwo+1:])
            except ValueError:
                xysensitivity = float(line[colontwo:-1])
        elif "---------" not in line and not datareached:
            pass
        elif datareached:
            if "Temperature" in line:
                headers = line
            elif line == "\n":
                pass
            else:
                data.append(line)
        else:
            datareached = True

    f.close()
    try:
        f = open(dataaddress[:-8] + "_Data_Only" + direction + dataaddress[-8:], 'r')
        f.close()
        return [headers, refsensitivity, xxsensitivity, xysensitivity, dataaddress, data, 1]
    except IOError:
        return [headers, refsensitivity, xxsensitivity, xysensitivity, dataaddress, data, 0]


def sorter(sensitivities, dataaddress, data, direction, needloading):
    newdataaddress = dataaddress[:-8] + "_Data_Only_" + direction + dataaddress[-8:]

    if needloading == 0:
        f = open(newdataaddress, "w")
        for i in range(len(data)):
            f.write(data[i])
        f.close()

    data = np.loadtxt(newdataaddress)
    if data.size:
        try:
            plt.plot(data[:, 0], data[:, 3])
            plt.show()
            gooddata = input('Is this the data that should be analyzed? ')
            if gooddata.lower() == 'yes' or gooddata.lower() == 'y':
                global gooddatalist
                gooddatalist.append(newdataaddress)
                rxxcreation(sensitivities, data, newdataaddress)
                rxyprelimcreation(sensitivities, data, newdataaddress)
        except IndexError:
            pass


def rxxcreation(sensitivities, data, dataaddress):
    refresist = 996.51
    rxx = (sensitivities[1]*data[:, 4]*refresist)/(sensitivities[0]*data[:, 3])
    rxxdata = np.append(np.array([rxx]), np.array([data[:, 0]]), axis=0)

    rxxaddress = dataaddress[:-8] + "_Rxx" + dataaddress[-8:]
    # noinspection PyTypeChecker
    np.savetxt(rxxaddress, rxxdata)


def rxyprelimcreation(sensitivities, data, dataaddress):
    refresist = 996.51
    rxy = (sensitivities[2]*data[:, 2]*refresist)/(sensitivities[0]*data[:, 3])
    rxydata = np.append(np.array([rxy]), np.array([data[:, 0]]), axis=0)

    rxyaddress = dataaddress[:-8] + "_Rxy" + dataaddress[-8:]
    # noinspection PyTypeChecker
    np.savetxt(rxyaddress, rxydata)


def main():
    samples = ['PST380 I2', "PST441 G2", 'PST441 H3', 'PST442 G2', 'PST442 H2', 'PST236 R5', 'PST037d1', 'PST042D1',
               'PST081D2', 'PST189M1', 'PST191M1', 'PST192M1']
    directions = ['Up', 'Down', "Full", 'OutPlane']
    for samplenumber in samples:
        for direct in directions:
            for takenumber in range(99):
                try:
                    data = loader(samplenumber, direct, takenumber+1)
                    sorter(data[1:4], data[4], data[5], direct, data[6])
                except IOError:
                    break
                except ValueError:
                    pass
    return gooddatalist
