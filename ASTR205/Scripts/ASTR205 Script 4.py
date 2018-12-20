import numpy as np
import matplotlib.pyplot as plt

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "ClusterUBVData.txt"
Data = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "UB-BVIntrinsicColorBasis.txt"
IntrinsicColorData = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "UBVIntrinsicMS.txt"
IntrinsicMSData = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "IsochroneFor3.16e7Years.txt"
Isochrone316e7 = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "IsochroneFor1.00e8Years.txt"
Isochrone1e8 = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "IsochroneFor3.16e8Years.txt"
Isochrone316e8 = np.loadtxt(filename)

plt.gca().invert_yaxis()
plt.title("Initial H-R Diagram of the Given Open Cluster Data Set")
plt.xlabel("B-V (Color)")
plt.ylabel("V (Magnitude)")
plt.scatter(Data[:, 3], Data[:, 2], s=5, c='r', label='Given Data')
plt.legend(loc='best')
plt.show()

binaryFrequency = (33/(105+33))
BFText = "Approximately {:.3f} binary systems in the cluster data set."
print(BFText.format(binaryFrequency))

redshift=0.047
title = "Fitted Open Cluster Data With Redshift {:.3f} Against Intrinsic Color"
title += " Set"
plt.gca().invert_xaxis()
plt.title(title.format(redshift))
plt.xlabel("B-V (Color)")
plt.ylabel("U-B (Color)")
plt.scatter(Data[:, 3]-redshift, Data[:, 4]-0.72*redshift, s=5, c='r',
            label='Redshifted Cluster Data')
plt.scatter(IntrinsicColorData[:, 0], IntrinsicColorData[:, 1], s=5, c='c',
            label='Intrinsic Color Data')
plt.legend(loc='best')
plt.show()

extinction = 3*redshift
print("Extinction is {:.3f}.".format(extinction))

plt.gca().invert_yaxis()
plt.title("H-R Diagram of Given Open Cluster Data Set Adjusted for Redshift")
plt.xlabel("B-V (Color)")
plt.ylabel("V (Magnitude)")
plt.scatter(Data[:, 3]-redshift, Data[:, 2], s=5, c='r',
            label='Redshifted Cluster Data')
plt.legend(loc='best')
plt.show()

distanceModulus = 5.9
title = "Fitted Open Cluster Data with Distance Modulus {:.3f} Against "
title += "Absolute Main Sequence Magnitude Data"
plt.gca().invert_yaxis()
plt.title(title.format(distanceModulus))
plt.xlabel("B-V (Color)")
plt.ylabel("V (Magnitude)")
plt.scatter(Data[:, 3]-redshift, Data[:, 2], s=5, c='r',
            label='Redshifted Cluster Data')
plt.scatter(IntrinsicMSData[:, 1],
            IntrinsicMSData[:, 0]+distanceModulus-extinction,
            s=5, c='g', label='Absolute Main Sequence Magnitude Data')
plt.legend(loc='best')
plt.show()

print("Distance is {:.3f} pc.".format(10*(10**(1/5*(distanceModulus-extinction)))))

plt.gca().invert_yaxis()
plt.title('Multiple Isochrones Against Shifted Given Open Cluster Data Set')
plt.xlabel('B-V (Color)')
plt.ylabel('V (Magnitude)')
plt.scatter(Data[:, 3]-redshift, Data[:, 2]-distanceModulus+extinction,
            s=5, c='r', label='Given Shifted Data Set')
plt.scatter(Isochrone316e7[:, 0]-Isochrone316e7[:, 1], Isochrone316e7[:, 1],
            s=5, c='c', label='3.16e7 Isochrone')
plt.scatter(Isochrone1e8[:, 0]-Isochrone1e8[:, 1], Isochrone1e8[:, 1],
            s=5, c='g', label='1.00e8 Isochrone')
plt.scatter(Isochrone316e8[:, 0]-Isochrone316e8[:, 1], Isochrone316e8[:, 1],
            s=5, c='b', label='3.16e8 Isochrone')
plt.legend(loc='best')
plt.show()

print("Isochrone at 1.00e8 years is best fit for the given cluster data.")

dinosaurs = "1.00e8 years is definitely within the Cretaceous Period during"
dinosaurs += " the lifetime of the dinosaurs."
print(dinosaurs)
dinosaurs = "Dinosaurs would have lived before the formation of the cluster as"
dinosaurs += " well in the Jurassic Period."
print(dinosaurs)