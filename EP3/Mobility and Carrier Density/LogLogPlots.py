import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf


def linear(logfield, slope, offset):
    return logfield*slope+offset


def chisquared(params, logfield, rxy):
    return np.sum((rxy - linear(logfield, *params)) ** 2 / 0.01 ** 2)


def initial(data, guess, neg, address):
    logfieldguess = np.linspace(min(data[1, :]), max(data[1, :]), 750)
    logrguess = linear(logfieldguess, *guess)

    plt.scatter(data[1, :], data[0, :], marker='.', label="Measured Data")
    plt.plot(logfieldguess, logrguess, marker="", linestyle="-", linewidth=1, color="g", label="Initial Guess")
    plt.xlabel('Log(B-Field)')
    plt.ylabel('Log(Rxx)')
    if address in [-2., -1., -0.5, 0.5, 1., 2., -10.]:
        plt.title("Power {} Linearity Initial Guess".format(address))
    elif address == 'LogLogThickness':
        plt.title('Log-Log Initial Guess of Slope versus Thickness')
        print('\nSaving plot 1 for Slope vs. Thickness')
    else:
        plt.title(address[90:99] + " Rxx Log-Log Initial Guess")
        print('\nSaving plot 1 for ' + address[90:99])
    plt.legend(loc='best', numpoints=1)

    if neg:
        address1 = address[:90] + "Graphs/" + address[90:99] + "_LogLog_Initial_Neg" + ".png"
    elif address in [-2., -1., -0.5, 0.5, 1., 2., -10.]:
        address1 = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/Graphs/" \
                   "/LogLogs/Thickness/GraphInit{}.png".format(address)
    elif address == 'LogLogThickness':
        address1 = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/Graphs/" \
                   "LogLogThicknessInitial.png"
    else:
        address1 = address[:90] + "Graphs/LogLogs/" + address[90:99] + "_LogLog_Initial_Pos" + ".png"
    plt.savefig(address1)
    plt.clf()

    return fit(data, guess, neg, address)


def fit(data, guess, neg, address):
    params, cov = cf(linear, data[1, :], data[0, :], sigma=0.01 * np.ones(len(data[1, :])), p0=guess, maxfev=10 ** 5)

    logfieldfit = np.linspace(min(data[1, :]), max(data[1, :]), len(data[1, :]) * 10)
    logrfit = linear(logfieldfit, *params)

    plt.scatter(data[1, :], data[0, :], marker='.', label="Measured Data")
    plt.plot(logfieldfit, logrfit, marker="", linestyle="-", linewidth=1, color="r", label="Initial Guess")
    plt.xlabel('Log(B-Field)')
    plt.ylabel('Log(Rxx)')
    if address in [-2., -1., -0.5, 0.5, 1., 2., -10.]:
        plt.title("Power {} Linearity Fitted Guess".format(address))
    elif address == 'LogLogThickness':
        plt.title('Log-Log Fitted Guess of Slope versus Thickness')
        print('\nSaving plot 2 for Slope vs. Thickness')
    else:
        plt.title(address[90:99] + " Rxx Log-Log Fitted Guess")
        print('\nSaving plot 2 for ' + address[90:99])
    plt.legend(loc='best', numpoints=1)

    if neg:
        address1 = address[:90] + "Graphs/" + address[90:99] + "_LogLog_Fitted_Neg" + ".png"
    elif address in [-2., -1., -0.5, 0.5, 1., 2., -10.]:
        address1 = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/Graphs/" \
                   "/LogLogs/Thickness/GraphFit{}.png".format(address)
    elif address == 'LogLogThickness':
        address1 = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/Graphs/" \
                   "LogLogThicknessFitted.png"
    else:
        address1 = address[:90] + "Graphs/LogLogs/" + address[90:99] + "_LogLog_Fitted_Pos" + ".png"
    plt.savefig(address1)
    plt.clf()

    return residual(data, params, neg, address)


def residual(data, params, neg, address):
    residuals = data[0, :] - linear(data[1, :], *params)

    if address in [-2., -1., -0.5, 0.5, 1., 2., -10.]:
        plt.title("Power {} Linearity Residuals".format(address))
    elif address == 'LogLogThickness':
        plt.title('Log-Log Residuals of Slope versus Thickness')
        print('\nSaving plot 3 for Slope vs. Thickness')
    else:
        plt.title(address[90:99] + " Rxx Log-Log Residuals")
        print('\nSaving plot 3 for ' + address[90:99])
    plt.scatter(data[1, :], residuals, marker='.', label="residual (y-y_fit)")
    plt.hlines(0, np.min(data[1, :]), np.max(data[1, :]), lw=2, alpha=0.8)
    plt.xlabel('Log(B-Field)')
    plt.ylabel('Log(R)-Log(R)Fit')
    plt.legend(loc='best', numpoints=1)

    if neg:
        address1 = address[:90] + "Graphs/" + address[90:99] + "_LogLog_Residual_Neg" + ".png"
    elif address in [-2., -1., -0.5, 0.5, 1., 2., -10.]:
        address1 = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/Graphs/" \
                   "/LogLogs/Thickness/GraphResid{}.png".format(address)
    elif address == 'LogLogThickness':
        address1 = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/Graphs/" \
                   "LogLogThicknessResids.png"
    else:
        address1 = address[:90] + "Graphs/LogLogs/" + address[90:99] + "_LogLog_Residual_Pos" + ".png"
    plt.savefig(address1)
    plt.clf()

    return params


dataaddress = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/"
DataList = np.genfromtxt(dataaddress + "DataList.txt", dtype='str', delimiter='\n')
YIntercepts = {"PST380 I2": 643.8978692238478, "PST441 G2": 226.06593048689894, "PST441 H3": 202.9131049801961,
               "PST442 G2": 157.79466191022382, "PST442 H2": 322.26661262795716, "PST236 R5": 680.0755508695942,
               "PST192 M1": 246.03900426255757, "PST191 M1": 380.07726768962823, "PST189 M1": 614.3692229525342,
               "PST081 D2": 130.4141990173324, "PST042 D1": 776.0403589246822, "PST037 D1": 30.69315790368633,
               "PST194 M1": 243.6374740926423, "PST195 M1": 240.67907249580892, "PST196 M1": 261.1435187513706,
               "PST197 M1": 238.6561236866221}
cutoff = {"PST380 I2": 9.0, "PST441 G2": 3.9375, "PST441 H3": 4.0, "PST442 G2": 3.8125, "PST442 H2": 3.9921875,
          "PST236 R5": 2.2265625, "PST192 M1": 4.03125, "PST191 M1": 4.5, "PST189 M1": 4.015625, "PST081 D2": 4.5625,
          "PST042 D1": 6.5, "PST037 D1": 3.25, "PST194 M1": 4.25, "PST195 M1": 5.5234375, "PST196 M1": 3.328125,
          "PST197 M1": 4.0}
slopes = []
for Address in DataList:
    if "OutPlane" not in Address:
        RxxData = np.loadtxt(Address[:90] + 'Verified Data/' + Address[90:-8] + "_Rxx" + Address[-8:])
        RxxData[0, :] = RxxData[0, :] - YIntercepts[Address[90:99]]*np.ones(len(RxxData[0, :]))
        LogRxxDataPos = np.log(RxxData[:, np.where(RxxData[1, :] > cutoff[Address[90:99]])][:, 0, :])/np.log(1.1)
        LogRxxDataNeg = np.log(np.abs(RxxData[:, np.where(RxxData[1, :] < -1 * cutoff[Address[90:99]])][:, 0, :]))
        LogRxxDataNeg /= np.log(1.1)

        PosParams = initial(LogRxxDataPos, [1, 5], False, Address)
        NegParams = initial(LogRxxDataNeg, [1, 5], True, Address)

        print(Address[90:96] + ":")
        print(PosParams)
        print(NegParams)

        slopes.append((PosParams[0] + NegParams[0])/2)

        f = open(Address[:90] + "Data/" + Address[90:99] + " LogLog.txt", 'w')
        f.write(Address[90:96] + ":\n")
        f.write("\nLogLog Rxx Parameters:\n")
        f.write(np.array2string(PosParams) + "\n")
        f.write(np.array2string(NegParams) + "\n")
        f.close()

CarrierDensity = [1.168581e+20, 3.558928e+19, 3.602220e+19, 3.512198e+19, 3.257694e+19, 7.778233e+18,
                  4.2E+19, 6.5E+19, 1.1E+20, 9.7E+19, 1.5E+20, 7.3E+19, 3.9E+19, 3.4E+19, 3.7E+19, 4.14E+19]
thicknesses = [20., 90., 90., 90., 90., 900., 60., 40., 20., 50., 12.7, 169., 60., 60., 60., 60.]
texts = ['PST380', 'PST441', 'PST441', 'PST442', 'PST442', 'PST236', 'PST192', 'PST191', 'PST189', 'PST081', 'PST042',
         'PST037', 'PST194', 'PST195', 'PST196', 'PST197']
PowerParams = []
for power in [-2., -1., -0.5, 0.5, 1., 2.]:
    PowerParams.append(initial(np.array([slopes, np.power(thicknesses, power)]), [1, 1], False, power))

intercept = (PowerParams[1][1] + PowerParams[2][1])/2.0
print(np.array(slopes) - intercept * np.ones(len(slopes)))

plt.title('Log-Log Plot of Slope versus Thickness')
plt.scatter(np.log(thicknesses)[0: 6], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[0: 6],
            marker='.', color='b', label='Series (236-442)')
plt.scatter(np.log(thicknesses)[6: 9], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[6: 9],
            marker='^', color='g', label='Thickness Series 1 (189-192)')
plt.scatter(np.log(thicknesses)[9: 12], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[9: 12],
            marker='s', color='r', label='Thickness Series 2 (037-081)')
plt.scatter(np.log(thicknesses)[12:], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[12:],
            marker='X', color='k', label='Substrate Temp. Series (194-197)')
for index in range(len(texts)):
    plt.text(1.0001 * np.log(thicknesses)[index],
             1.0001 * np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[index], texts[index])
plt.legend(loc='best')
plt.xlabel('Thickness (nm)')
plt.ylabel('Slope')
plt.show()

plt.title('Log-Log Plot of Slope versus Carrier Density')
plt.scatter(np.log(CarrierDensity)[0: 6], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[0: 6],
            marker='.', color='b', label='Series (236-442)')
plt.scatter(np.log(CarrierDensity)[6: 9], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[6: 9],
            marker='^', color='g', label='Thickness Series 1 (189-192)')
plt.scatter(np.log(CarrierDensity)[9: 12], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[9: 12],
            marker='s', color='r', label='Thickness Series 2 (037-081)')
plt.scatter(np.log(CarrierDensity)[12:], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[12:],
            marker='X', color='k', label='Substrate Temp. Series (194-197)')
for index in range(len(texts)):
    plt.text(1.0001 * np.log(CarrierDensity)[index],
             1.0001 * np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[index], texts[index])
plt.legend(loc='best')
plt.xlabel('Carrier Density (per cm cubed)')
plt.ylabel('Slope')
plt.show()

plt.title('Log-Log Plot of Slope versus Carrier Density')
plt.scatter(CarrierDensity[0: 6], np.array(slopes)[0: 6],
            marker='.', color='b', label='Series (236-442)')
plt.scatter(CarrierDensity[6: 9], np.array(slopes)[6: 9],
            marker='^', color='g', label='Thickness Series 1 (189-192)')
plt.scatter(CarrierDensity[9: 12], np.array(slopes)[9: 12],
            marker='s', color='r', label='Thickness Series 2 (037-081)')
plt.scatter(CarrierDensity[12:], np.array(slopes)[12:],
            marker='X', color='k', label='Substrate Temp. Series (194-197)')
for index in range(len(texts)):
    plt.text(1.0001 * CarrierDensity[index],
             1.0001 * np.array(slopes)[index], texts[index])
plt.legend(loc='best')
plt.xlabel('Carrier Density (per cm cubed)')
plt.ylabel('Slope')
plt.yscale('log')
plt.xscale('log')
plt.show()

plt.title('Log-Log Plot of Slope versus Thickness')
plt.scatter(thicknesses[0: 6], np.array(slopes)[0: 6],
            marker='.', color='b', label='Series (236-442)')
plt.scatter(thicknesses[6: 9], np.array(slopes)[6: 9],
            marker='^', color='g', label='Thickness Series 1 (189-192)')
plt.scatter(thicknesses[9: 12], np.array(slopes)[9: 12],
            marker='s', color='r', label='Thickness Series 2 (037-081)')
plt.scatter(thicknesses[12:], np.array(slopes)[12:],
            marker='X', color='k', label='Substrate Temp. Series (194-197)')
for index in range(len(texts)):
    plt.text(1.0001 * thicknesses[index],
             1.0001 * np.array(slopes)[index], texts[index])
plt.legend(loc='best')
plt.xlabel('Thickness (nm)')
plt.ylabel('Slope')
plt.yscale('log')
plt.xscale('log')
plt.show()

SlopeThicknessParams1 = initial(np.array([np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[6: 9],
                                         np.log(thicknesses)[6: 9]]), [1, 1], False, 'LogLogThickness')
plt.title('Log-Log Plot of Slope versus Thickness')
plt.scatter(np.log(thicknesses)[6: 9], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[6: 9],
            marker='^', color='g', label='Thickness Series 1 (189-192)')
plt.plot(np.linspace(np.log(20), np.log(60), 500),
         linear(np.linspace(np.log(20), np.log(60), 500), *SlopeThicknessParams1), color='g')
for index in range(6, 9, 1):
    plt.text(1.0001 * np.log(thicknesses)[index],
             1.0001 * np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[index], texts[index])
plt.xlabel('Thickness (nm)')
plt.ylabel('Slope')
plt.show()


SlopeThicknessParams2 = initial(np.array([np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[9: 12],
                                         np.log(thicknesses)[9: 12]]), [1, 1], False, 'LogLogThickness')
plt.title('Log-Log Plot of Slope versus Thickness')
plt.scatter(np.log(thicknesses)[9: 12], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[9: 12],
            marker='s', color='r', label='Thickness Series 2 (037-081)')
plt.plot(np.linspace(np.log(10), np.log(175), 500),
         linear(np.linspace(np.log(10), np.log(175), 500), *SlopeThicknessParams2), color='r')
for index in range(9, 12, 1):
    plt.text(1.0001 * np.log(thicknesses)[index],
             1.0001 * np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[index], texts[index])
plt.xlabel('Thickness (nm)')
plt.ylabel('Slope')
plt.show()

SlopeDensityParams1 = initial(np.array([np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[12:],
                                       np.log(CarrierDensity)[12:]]), [1, 1], False, 'LogLogThickness')
plt.title('Log-Log Plot of Slope versus Carrier Density')
plt.scatter(np.log(CarrierDensity)[12:], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[12:],
            marker='X', color='k', label='Substrate Temp. Series (194-197)')
plt.plot(np.linspace(np.log(3.2e19), np.log(4.2e19), 500),
         linear(np.linspace(np.log(3.2e19), np.log(4.2e19), 500), *SlopeDensityParams1), color='k')
for index in range(12, 16, 1):
    plt.text(1.0001 * np.log(CarrierDensity)[index],
             1.0001 * np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[index], texts[index])
plt.xlabel('Carrier Density (nm)')
plt.ylabel('Slope')
plt.show()

SlopeThicknessParams = initial(np.array([np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes)))),
                                         np.log(thicknesses)]), [1, 1], False, 'LogLogThickness')
print(SlopeThicknessParams)
plt.title('Log-Log Plot of Slope versus Thickness')
plt.scatter(np.log(thicknesses)[0: 6], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[0: 6],
            marker='.', color='b', label='Series (236-442)')
plt.scatter(np.log(thicknesses)[6: 9], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[6: 9],
            marker='^', color='g', label='Thickness Series 1 (189-192)')
plt.scatter(np.log(thicknesses)[9: 12], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[9: 12],
            marker='s', color='r', label='Thickness Series 2 (037-081)')
plt.scatter(np.log(thicknesses)[12:], np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[12:],
            marker='X', color='k', label='Substrate Temp. Series (194-197)')
plt.plot(np.linspace(np.log(20), np.log(60), 500),
         linear(np.linspace(np.log(20), np.log(60), 500), *SlopeThicknessParams1), color='g',
         label='Thickness Series 1 Fit')
plt.plot(np.linspace(np.log(10), np.log(175), 500),
         linear(np.linspace(np.log(10), np.log(175), 500), *SlopeThicknessParams2), color='r',
         label='Thickness Series 2 Fit')
plt.plot(np.linspace(np.log(10), np.log(900), 500),
         linear(np.linspace(np.log(10), np.log(900), 500), *SlopeThicknessParams), color='c',
         label='Total Fit')
for index in range(len(texts)):
    plt.text(1.0001 * np.log(thicknesses)[index],
             1.0001 * np.log(np.abs(np.array(slopes) - intercept * np.ones(len(slopes))))[index], texts[index])
plt.legend(loc='best')
plt.xlabel('Thickness (nm)')
plt.ylabel('Slope')
plt.show()
