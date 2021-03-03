import matplotlib.pyplot as plt
import numpy as np


Materials = [r'Cd_3As_2', r'YPdBi', r'NbP', 'PbTe/SnTe Heterostructs', 'PbTe/SnTe Heterostructs', r'TlBiSSe', 'TaAs',
             'PST 236', 'PST 441', 'PST 442', 'Epitaxial Graphene']
LMRPercentIncrease = [3100, 350, 850000, 2150, 3, 10000, 5400, 12, 20, 28]
Mobilities = [64000, 7800, 5000000, 30000, 45, 14000, 500000, 40, 270, 376]
LMRUnextrapolated = [350, 850000, 5400]
LMRExtrapolated = [700, 1322222, 8400]
MobilitiesExtrapolated = [7800, 5000000, 500000]
LMRDisorder = [55]
MobilitiesDisorder = [3500]

plt.scatter(Mobilities, LMRPercentIncrease, c='b', marker='o')
plt.scatter(MobilitiesDisorder, LMRDisorder, c='r', marker='o')
plt.scatter(MobilitiesExtrapolated, LMRExtrapolated, c='k', marker='X')
plt.vlines(MobilitiesExtrapolated, LMRUnextrapolated, LMRExtrapolated, linestyles='--')
for indx in range(len(LMRPercentIncrease)):
    plt.text(1.1*Mobilities[indx], 1.1*LMRPercentIncrease[indx], Materials[indx])
plt.text(1.1*MobilitiesDisorder[0], 1.1*LMRDisorder[0], Materials[-1])
plt.xlabel(r'Mobilities of Materials (cm^2/Vs)')
plt.ylabel(r'Percent Increase of Resistance')
plt.title('Percent Increase as a Function of Mobility')
plt.yscale('log')
plt.xscale('log')
plt.show()

Materials = [r'Cd_3As_2', 'PST 236', 'PST 441', 'PST 441', 'PST 380', 'Bismuth Nanoribbons',
             'Bismuth Nanoribbons', 'TaAs', 'PbTe/SnTe\nHeterostructs']
CriticalBField = [0.35, 1.5, 4, 4, 11, 2, 1, 0.5] # , 0.001
Thickness = [20000, 900, 90, 90, 10, 100, 25, 100000] # , 1000000
CBFieldRanges = [2, 4]
Thicknesses = [25, 10]

plt.figure(figsize=(15, 15))
plt.scatter(Thickness, CriticalBField, c='b', marker='o')
plt.vlines(Thicknesses, [0, CBFieldRanges[1]], [CBFieldRanges[0], 10], colors='r', linestyles='--')
plt.scatter([1000000, 16], [0.001, 1], c='k', marker='X')
plt.vlines(1000000, 1.1*0.001, 0.1, colors='w', linestyles='--')
plt.text(300000, 1.1*0.001, 'Silver Chalcogenides')
plt.text(1.1*16, 1.1, 'Epitaxial Graphene')
for indx in range(len(CBFieldRanges)):
    plt.text(1.1*Thicknesses[indx], 1.1*CBFieldRanges[indx], Materials[-1])
for indx in range(len(CriticalBField)):
    if Materials[indx] == 'Bismuth Nanoribbons':
        plt.text(1.1 * Thickness[indx], 0.8 * CriticalBField[indx], Materials[indx])
    else:
        plt.text(1.1*Thickness[indx], 1.1*CriticalBField[indx], Materials[indx])
plt.xlabel(r'Thickness of Materials (nm)')
plt.ylabel(r'Critical Magnetic Field (T)')
plt.title('Critical Magnetic Field as a Function of Thickness')
plt.yscale('log')
plt.xscale('log')
plt.show()

hbar = 1.055E-34
echarge = 1.602E-19
maglengths = np.sqrt(hbar/(echarge*np.array(CriticalBField)))*1E9
disorders = [0.001, 1]
disordermaglentghs = np.sqrt(hbar/(echarge*np.array(disorders)))*1E9

plt.figure(figsize=(15, 15))
plt.scatter(Thickness, maglengths, c='b', marker='o')
plt.scatter([1000000, 16], disordermaglentghs, c='k', marker='X')
plt.text(300000, 1.1*disordermaglentghs[0], 'Silver Chalcogenides')
plt.text(1.1*16, 0.8*disordermaglentghs[1], 'Epitaxial Graphene')
for indx in range(len(maglengths)):
    plt.text(1.1*Thickness[indx], 1.1*maglengths[indx], Materials[indx])
plt.xlabel(r'Thickness of Materials (nm)')
plt.ylabel(r'Magnetic Length (nm)')
plt.title('Magnetic Length as a Function of Thickness')
plt.yscale('log')
plt.xscale('log')
plt.show()

Materials = ['Cd3As2', 'TlBiSSe', 'Epitaxial Graphene', 'TaAs', 'PST\n441', 'PST 236', 'PST 442']
CriticalBField = [0.35, 0.1, 1, 0.5, 4, 1.5, 4]
Mobility = [65000, 14000, 3500, 500000, 270, 40, 376]

plt.figure(figsize=(15, 15))
plt.scatter(Mobility, CriticalBField, c='b', marker='o')
for indx in range(len(CriticalBField)):
    plt.text(1.1*Mobility[indx], 1.1*CriticalBField[indx], Materials[indx])
plt.xlabel(r'Mobilities of Materials (cm^2/Vs)')
plt.ylabel(r'Critical Magnetic Field (T)')
plt.title('Critical Magnetic Field as a Function of Mobility')
plt.yscale('log')
plt.xscale('log')
plt.show()

Materials = ['Cd3As2', 'TlBiSSe', 'InSb', 'TaAs', 'Silver Chalcogenide', 'Silver Chalcogenide',
             'PST 236', 'PST 441', 'PST442']
CriticalBField = [0.35, 0.1, 0.7, 0.5, 0.001, 0.001, 1.5, 4, 4]
Density = [5E16, 3.8E17, 5E17, 2.65E17, 2.5E17, 9E17, 7.8E18, 3.6E19, 3.3E19]

plt.figure(figsize=(15, 15))
plt.scatter(Density, CriticalBField, c='b', marker='o')
plt.vlines(1E17, 0, 5, colors='w')
for indx in range(len(CriticalBField)):
    plt.text(1.1*Density[indx], 1.1*CriticalBField[indx], Materials[indx])
plt.xlabel(r'Density of Materials (cm^-3)')
plt.ylabel(r'Critical Magnetic Field (T)')
plt.title('Critical Magnetic Field as a Function of Density')
plt.yscale('log')
plt.xscale('log')
plt.show()
