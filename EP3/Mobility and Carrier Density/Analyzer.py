import numpy as np
import DensityClass as Dc
import MobilityClass as Mc
import DataOrganizerNew as Do
import LinearMagnetoResistance as Lmr


dataaddress = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/"
NewData = input("Would you like to analyze new data? ")

if NewData.lower() == "yes" or NewData.lower() == "y":
    DataList = Do.main()
    np.savetxt(dataaddress + "DataList.txt", DataList, fmt="%s")
else:
    try:
        f = open(dataaddress + "DataList.txt", 'r')
        f.close()
        DataList = np.genfromtxt(dataaddress + "DataList.txt", dtype='str', delimiter='\n')
    except IOError:
        DataList = Do.main()
        np.savetxt(dataaddress + "DataList.txt", DataList, fmt="%s")

print(DataList)

electroncharge = 1.60217662e-19
thicknesses = {"PST380": 2e-6, "PST441": 9e-6, "PST442": 9e-6, "PST236": 9e-5}
cutoff = {"PST380": 11, "PST441": 6, "PST442": 6, "PST236": 3}
for Address in DataList:
    Linear = Lmr.Linearity(Address, 1, 0.01)
    RxxData = Mc.Mobility(Address, 1, 1, 0.01, 1.4)
    RxyData = Dc.Density(Address, 1, 0.01)

    XYInitialParams = RxyData.main()
    FinalParams = RxxData.main(XYInitialParams[1])
    LinearityParams = []
    if "Full" in Address or "OutPlane" in Address:
        if "PST236" in Address:
            LinearityParams = Linear.main(cutoff[Address[90:96]], False)
        else:
            LinearityParams = Linear.main(cutoff[Address[90:96]], False)

    print(FinalParams)
    p2d = np.abs(1.0 / (1e4 * electroncharge * FinalParams[1][0]))
    p3d = p2d / thicknesses[Address[90:96]]
    mu = 3.0 / (p2d * electroncharge * FinalParams[0][1])

    print(Address[90:96] + " Data Release:")
    print("2D Carrier Density: {:e}".format(p2d))
    print("3D Carrier Density: {:e}".format(p3d))
    print("Mobility: " + str(mu))
    print(XYInitialParams)
    print(FinalParams[0])
    print(FinalParams[1])
    if "Full" in Address:
        print(LinearityParams[0])
        print(LinearityParams[1])

    input()

    if "OutPlane" in Address:
        f = open(Address[:90] + "Data/" + Address[90:99] + " InPlane Results.txt", 'w')
    else:
        f = open(Address[:90] + "Data/" + Address[90:99] + " Results.txt", 'w')
    f.write(Address[90:96] + " Data Release:\n")
    f.write("2D Carrier Density: {:e}".format(p2d) + "\n")
    f.write("3D Carrier Density: {:e}".format(p3d) + "\n")
    f.write("Mobility: " + str(mu) + "\n")
    f.write("\nInitial Rxy Parameters:\n")
    f.write(np.array2string(XYInitialParams) + "\n")
    f.write("\nRxx Parameters:\n")
    f.write(np.array2string(FinalParams[0]) + "\n")
    f.write("\nAdjusted Rxy Parameters:\n")
    f.write(np.array2string(FinalParams[1]) + "\n")
    if "Full" in Address:
        f.write("\nLinear Rxx Parameters:\n")
        f.write(np.array2string(LinearityParams[0]) + "\n")
        f.write(np.array2string(LinearityParams[1]) + "\n")
    f.close()
