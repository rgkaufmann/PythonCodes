import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf


def linear(field, slope, offset):
    return slope * field + offset


def function(field, slopepar, offsetpar, cutoff):
    resistance = np.zeros(len(field))
    resistance[np.where(np.abs(field) < cutoff)] = slopepar * (field[np.where(np.abs(field) < cutoff)] ** 2) + offsetpar

    maxfield = min(field[np.where(field > cutoff)])
    minfield = max(field[np.where(field < -1 * cutoff)])
    slopelinneg = 2 * slopepar * minfield
    slopelinpos = 2 * slopepar * maxfield
    offsetlinneg = (slopepar * (minfield ** 2) + offsetpar) - slopelinneg * minfield
    offsetlinpos = (slopepar * (maxfield ** 2) + offsetpar) - slopelinpos * maxfield

    resistance[np.where(field > cutoff)] = slopelinpos * field[np.where(field > cutoff)] + offsetlinpos
    resistance[np.where(field < -1 * cutoff)] = slopelinneg * field[np.where(field < -1 * cutoff)] + offsetlinneg
    return resistance


def chisquaredlin(params, field, resid):
    return np.sum((resid - linear(field, *params)) ** 2 / (0.01 * resid) ** 2)


def chisquared(params, field, rxx):
    return np.sum((rxx - function(field, *params)) ** 2 / 0.01 ** 2)


def fit(data, guess, index):
    params, cov = cf(function, data[1, :], data[0, :], sigma=0.01 * np.ones(len(data[1, :])), p0=guess, maxfev=10 ** 5)

    residuals = data[0, :] - function(data[1, :], *params)

    global Params
    Params[index] = list(params[0:2])

    return residuals


def plotting(data1, data2, xtext, ytext, xunits, yunits):
    plt.figure(figsize=(10, 10))
    plt.title("Relationship Between {} and {}".format(xtext, ytext))
    plt.scatter(data1[0:6], data2[0:6], marker='.', color='b', label='Series (236-442)')
    plt.scatter(data1[6:9], data2[6:9], marker='^', color='g', label='Thickness Series 1 (189-192)')
    plt.scatter(data1[9:12], data2[9:12], marker='s', color='r', label='Thickness Series 2 (037-081)')
    plt.scatter(data1[12:], data2[12:], marker='X', color='k', label='Substrate Temp. Series (194-197)')
    for index in range(len(Thicknesses)):
        plt.text(1.01 * data1[index], 1.01 * data2[index], Texts[index])
    plt.xlabel('{} ({})'.format(xtext, xunits))
    plt.ylabel('{} ({})'.format(ytext, yunits))
    plt.legend(loc='best')
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig(DataAddress + 'Graphs/LinearParabolic/Relationships/{}_{}.png'.format(ytext, xtext))
    plt.clf()

    plt.figure(figsize=(10, 10))
    plt.title("Relationship Between {} and {}: Series (236-442)".format(xtext, ytext))
    plt.scatter(data1[0:6], data2[0:6], marker='.', color='b')
    for index in range(6):
        plt.text(data1[index], data2[index], Texts[index])
    plt.xlabel('{} ({})'.format(xtext, xunits))
    plt.ylabel('{} ({})'.format(ytext, yunits))
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig(DataAddress + 'Graphs/LinearParabolic/Relationships/{}_{}_Series.png'.format(ytext, xtext))
    plt.clf()

    plt.figure(figsize=(10, 10))
    plt.title("Relationship Between {} and {}: Thickness Series 1".format(xtext, ytext))
    plt.scatter(data1[6:9], data2[6:9], marker='^', color='g')
    for index in range(6, 9):
        plt.text(data1[index], data2[index], Texts[index])
    plt.xlabel('{} ({})'.format(xtext, xunits))
    plt.ylabel('{} ({})'.format(ytext, yunits))
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig(DataAddress + 'Graphs/LinearParabolic/Relationships/{}_{}_Thickness_Series_1.png'.format(ytext, xtext))
    plt.clf()

    plt.figure(figsize=(10, 10))
    plt.title("Relationship Between {} and {}: Thickness Series 2".format(xtext, ytext))
    plt.scatter(data1[9:12], data2[9:12], marker='s', color='r')
    for index in range(9, 12):
        plt.text(data1[index], data2[index], Texts[index])
    plt.xlabel('{} ({})'.format(xtext, xunits))
    plt.ylabel('{} ({})'.format(ytext, yunits))
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig(DataAddress + 'Graphs/LinearParabolic/Relationships/{}_{}_Thickness_Series_2.png'.format(ytext, xtext))
    plt.clf()

    plt.figure(figsize=(10, 10))
    plt.title("Relationship Between {} and {}: Substrate Temp. Series".format(xtext, ytext))
    plt.scatter(data1[12:], data2[12:], marker='X', color='k')
    for index in range(12, 16):
        plt.text(data1[index], data2[index], Texts[index])
    plt.xlabel('{} ({})'.format(xtext, xunits))
    plt.ylabel('{} ({})'.format(ytext, yunits))
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig(DataAddress + 'Graphs/LinearParabolic/Relationships/{}_{}_Substrate_Temp._Series.png'.format(ytext,
                                                                                                             xtext))
    plt.clf()


HBAR = 1.055E-34
ECHARGE = 1.60217662e-19

DataAddress = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/"
DataList = np.genfromtxt(DataAddress + "DataList.txt", dtype='str', delimiter='\n')
Guesses = {'PST037 D1': [1., 30.6978808, 4.0],
           'PST042 D1': [1., 775.336895, 6.0],
           'PST081 D2': [1., 130.319061, 5.0],
           'PST189 M1': [1., 614.301094, 4.0],
           'PST191 M1': [1., 379.982672, 5.0],
           'PST192 M1': [1., 246.040756, 5.0],
           'PST194 M1': [1., 244.238951, 3.0],
           'PST195 M1': [1., 240.953776, 5.0],
           'PST196 M1': [1., 262.213455, 2.0],
           'PST197 M1': [1., 239.230760, 3.0],
           'PST236 R5': [1., 678.360833, 1.5],
           'PST441 G2': [1., 225.468076, 3.0],
           'PST441 H3': [1., 202.160719, 3.0],
           'PST442 G2': [1., 157.563429, 3.0],
           'PST442 H2': [1., 321.498163, 3.0],
           'PST380 I2': [1., 644.241571, 9.0]}
Params = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
          [1, 1], [1, 1], [1, 1]]
ParamsIndex = 0
CriticalBField = []
Intercept = []
Thicknesses = [20., 90., 90., 90., 90., 900., 60., 40., 20., 50., 12.7, 169., 60., 60., 60., 60.]
CarrierDensity = [1.168581e+20, 3.558928e+19, 3.602220e+19, 3.512198e+19, 3.257694e+19, 7.778233e+18,
                  4.2E+19, 6.5E+19, 1.1E+20, 9.7E+19, 1.5E+20, 7.3E+19, 3.9E+19, 3.4E+19, 3.7E+19, 4.14E+19]
Texts = ['PST380', 'PST441', 'PST441', 'PST442', 'PST442', 'PST236', 'PST192', 'PST191', 'PST189', 'PST081', 'PST042',
         'PST037', 'PST194', 'PST195', 'PST196', 'PST197']

for Address in DataList:
    if "OutPlane" not in Address:
        adjustment = 1.0
        RxxData = np.loadtxt(Address[:90] + 'Verified Data/' + Address[90:-8] + "_Rxx" + Address[-8:])
        for iteration in range(20):
            Params[ParamsIndex][0:] = Guesses[Address[90:99]][0:2]

            Guesses123 = np.array([Guesses[Address[90:99]], Guesses[Address[90:99]], Guesses[Address[90:99]]])
            Guesses123[1][2] += adjustment
            Guesses123[2][2] -= adjustment
            residuals1 = fit(RxxData, Guesses123[0], ParamsIndex)
            residuals2 = fit(RxxData, Guesses123[1], ParamsIndex)
            residuals3 = fit(RxxData, Guesses123[2], ParamsIndex)

            params1, cov1 = cf(linear, RxxData[1, :][np.where(np.abs(RxxData[1, :]) > 1)],
                               residuals1[np.where(np.abs(RxxData[1, :]) > 1)], [1, 1],
                               0.01 * residuals1[np.where(np.abs(RxxData[1, :]) > 1)])
            params2, cov2 = cf(linear, RxxData[1, :][np.where(np.abs(RxxData[1, :]) > 1)],
                               residuals2[np.where(np.abs(RxxData[1, :]) > 1)], [1, 1],
                               0.01 * residuals2[np.where(np.abs(RxxData[1, :]) > 1)])
            params3, cov3 = cf(linear, RxxData[1, :][np.where(np.abs(RxxData[1, :]) > 1)],
                               residuals3[np.where(np.abs(RxxData[1, :]) > 1)], [1, 1],
                               0.01 * residuals3[np.where(np.abs(RxxData[1, :]) > 1)])

            chi1 = chisquaredlin(params1, RxxData[1, :], residuals1)
            chi2 = chisquaredlin(params2, RxxData[1, :], residuals2)
            chi3 = chisquaredlin(params3, RxxData[1, :], residuals3)

            Guesses[Address[90:99]][0:2] = Params[ParamsIndex]
            Guesses[Address[90:99]][2] = Guesses123[[chi1, chi2, chi3].index(min([chi1, chi2, chi3]))][2]

            adjustment /= 2

        fieldfit = np.linspace(min(RxxData[1, :]), max(RxxData[1, :]), len(RxxData[1, :]) * 10)
        plt.scatter(RxxData[1, :], RxxData[0, :], marker='.', label="Measured Data")
        plt.plot(fieldfit, function(fieldfit, *Guesses[Address[90:99]]), marker="", linestyle="-", linewidth=1,
                 color="r", label="Initial Guess")
        plt.xlabel('B-Field')
        plt.ylabel('Rxx')
        plt.title(Address[90:99] + " Rxx Fitted Guess")
        print('\nSaving plot 2 for ' + Address[90:99])
        plt.legend(loc='best', numpoints=1)
        address = Address[:90] + "Graphs/LinearParabolic/" + Address[90:99] + "_Fitted_Pos" + ".png"
        plt.savefig(address)
        plt.clf()

        plt.title(Address[90:99] + " Rxx Residuals")
        print('\nSaving plot 3 for ' + Address[90:99])
        plt.scatter(RxxData[1, :], RxxData[0, :] - function(RxxData[1, :], *Guesses[Address[90:99]]), marker='.',
                    label="residual (y-y_fit)")
        plt.hlines(0, np.min(RxxData[1, :]), np.max(RxxData[1, :]), lw=2, alpha=0.8)
        plt.xlabel('B-Field')
        plt.ylabel(r'R-R_{Fit}')
        plt.legend(loc='best', numpoints=1)

        address = Address[:90] + "Graphs/LinearParabolic/" + Address[90:99] + "_Residual_Pos" + ".png"
        plt.savefig(address)
        plt.clf()

        print(Address[90:96] + ":")
        print(Guesses[Address[90:99]])

        f = open(Address[:90] + "Data/" + Address[90:99] + " LinearParabolic.txt", 'w')
        f.write(Address[90:96] + ":\n")
        f.write("\nRxx Parameters:\n")
        f.write('\tSlopeLinPos\tOffsetLinPos\tSlopeLinNeg\tOffsetLinNeg\tSlopePar\tOffsetPar\tCutoff\n')
        f.write(str(Guesses[Address[90:99]]) + "\n")
        f.close()

        CriticalBField.append(Guesses[Address[90:99]][2])
        Intercept.append(Guesses[Address[90:99]][1])
        ParamsIndex += 1

MagneticLengths = np.sqrt(HBAR/(ECHARGE*np.array(CriticalBField)))*1E9
plotting(Thicknesses, CriticalBField, 'Thickness', 'Critical B-Field', 'nm', 'T')
plotting(Thicknesses, MagneticLengths, 'Thickness', 'Magnetic Length', 'nm', 'nm')
plotting(CarrierDensity, CriticalBField, 'Carrier Density', 'Critical B-Field', 'per cm cubed', 'T')
plotting(CarrierDensity, MagneticLengths, 'Carrier Density', 'Magnetic Length', 'per cm cubed', 'nm')
