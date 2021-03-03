########################################################################################################################
# PART ZERO: Import Statements
########################################################################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
from os import walk, remove
import cProfile
import pstats
import io

########################################################################################################################
# Set up profiler
########################################################################################################################

setfigsize = (7, 7)
Profiler = cProfile.Profile()

########################################################################################################################
# PART ONE: Data Loading and Sorting
# Enable profiler for part 1
# Load all data in two categories, all .dat files and raw data files
########################################################################################################################

Profiler.enable()

MyPath = 'C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/Verified Data/'
DatFiles = []
for (DirPath, DirNames, FileNames) in walk(MyPath):
    DatFiles.extend([(DirPath + '/' + File) for File in FileNames if '.dat' in File])
OriginalFiles = [File for File in DatFiles if 'Rx' not in File]

########################################################################################################################
# Deletes Test.dat if it exists
########################################################################################################################

if 'Test.dat' in OriginalFiles[0]:
    remove(OriginalFiles[0])
    OriginalFiles = OriginalFiles[1:]

########################################################################################################################
# Recreates .dat files to have Rxx and Ryy data
########################################################################################################################

for FileName in OriginalFiles:
    # Opens given file and searches for the beginning of data and copies it
    File = open(FileName, 'r')
    DataReached = False
    Data = []
    refsensitivity, xxsensitivity, xysensitivity = 0, 0, 0
    for Line in File:
        if "sensitivities" in Line and not DataReached:
            colonone = Line.find(":", 40)
            colontwo = Line.rfind(":")
            refsensitivity = float(Line[42:colonone])
            xxsensitivity = float(Line[colonone + 1:colontwo])
            try:
                xysensitivity = float(Line[colontwo + 1:])
            except ValueError:
                xysensitivity = float(Line[colontwo:-1])
        elif "---------" not in Line and not DataReached:
            continue
        elif DataReached:
            if "Temperature" in Line or 'Zeit' in Line:
                headers = Line
            elif Line == "\n":
                continue
            else:
                Data.append(Line)
        else:
            DataReached = True
    File.close()

    # Creates temporary file with just all raw data
    File = open(MyPath + 'Test.dat', "w")
    for i in range(1, len(Data)):
        File.write(Data[i])
    File.close()

    # Configures Rxx, Rxy, and BField Data
    DataSet = np.loadtxt(MyPath + 'Test.dat')
    if '191' in FileName or '192' in FileName:
        RxxData = np.abs(DataSet[:, 4] / DataSet[:, 2] * 998.2)
        RxyData = DataSet[:, 3] / DataSet[:, 2] * 998.2
        RxxError = np.abs(RxxData) * np.sqrt((0.01 * DataSet[:, 4] / DataSet[:, 4]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        RxyError = np.abs(RxyData) * np.sqrt((0.01 * DataSet[:, 3] / DataSet[:, 3]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        BField = DataSet[:, -3]
    elif '081' in FileName:
        RxxData = np.abs(DataSet[:, 3] / DataSet[:, 2] * 47.2)
        RxyData = DataSet[:, 4] / DataSet[:, 2] * 47.2
        RxxError = np.abs(RxxData) * np.sqrt((0.01 * DataSet[:, 3] / DataSet[:, 3]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        RxyError = np.abs(RxyData) * np.sqrt((0.01 * DataSet[:, 4] / DataSet[:, 4]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        BField = DataSet[:, -3]
    elif '380' in FileName:
        RxxData = np.abs(DataSet[:, 4] / DataSet[:, 3] * 4958.2 * xxsensitivity/refsensitivity)
        RxyData = DataSet[:, 2] / DataSet[:, 3] * 4958.2 * xysensitivity/refsensitivity
        RxxError = np.abs(RxxData) * np.sqrt((0.01 * DataSet[:, 4] / DataSet[:, 4]) ** 2 + (0.01 * DataSet[:, 3] /
                                                                                            DataSet[:, 3]) ** 2)
        RxyError = np.abs(RxyData) * np.sqrt((0.01 * DataSet[:, 3] / DataSet[:, 3]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        BField = DataSet[:, 0]
    elif '236' in FileName or '441' in FileName or '442' in FileName:
        RxxData = np.abs(DataSet[:, 4] / DataSet[:, 3] * 996.51 * xxsensitivity/refsensitivity)
        RxyData = DataSet[:, 2] / DataSet[:, 3] * 996.51 * xysensitivity/refsensitivity
        RxxError = np.abs(RxxData) * np.sqrt((0.01 * DataSet[:, 4] / DataSet[:, 4]) ** 2 + (0.01 * DataSet[:, 3] /
                                                                                            DataSet[:, 3]) ** 2)
        RxyError = np.abs(RxyData) * np.sqrt((0.01 * DataSet[:, 3] / DataSet[:, 3]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        BField = DataSet[:, 0]
    else:
        RxxData = np.abs(DataSet[:, 3] / DataSet[:, 2] * 998.2)
        RxyData = DataSet[:, 4] / DataSet[:, 2] * 998.2
        RxxError = np.abs(RxxData) * np.sqrt((0.01 * DataSet[:, 3] / DataSet[:, 3]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        RxyError = np.abs(RxyData) * np.sqrt((0.01 * DataSet[:, 4] / DataSet[:, 4]) ** 2 + (0.01 * DataSet[:, 2] /
                                                                                            DataSet[:, 2]) ** 2)
        BField = DataSet[:, -3]

    # Saves the Rxx and Rxy data in distinct folders and removes temporary file
    # noinspection PyTypeChecker
    np.savetxt(FileName[:-4] + " Rxx Data.dat", np.array([BField, RxxData, RxxError]))
    # noinspection PyTypeChecker
    np.savetxt(FileName[:-4] + " Rxy Data.dat", np.array([BField, RxyData, RxyError]))
    remove(MyPath + 'Test.dat')
    print(FileName + ' has been completed!')
print()

########################################################################################################################
# Finish and record profiling for part 1
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part One Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()

########################################################################################################################
# PART TWO: First Order Rxy Linear Fit
# Create functions dictating curve fitting and residual plotting as well as a linear fit and chi-squared equations
########################################################################################################################


def tolinear(xvalues, slope, offset):
    # Linear equation in form y = m * x + b
    return slope * xvalues + offset


def chisquared(params, xdata, ydata, function, sigma):
    # Standard chi-squared equation given residuals and error
    return np.sum((ydata - function(xdata, *params)) ** 2 / sigma ** 2)


def fittings(xdata, ydata, xtype, ytype, function, initialguess, sigma, title, dataaddress, save=True, showchi2=True):
    # Begin by curve-fitting the data using given initial guess and errors
    params, cov = cf(function, xdata, ydata, initialguess, sigma=sigma, maxfev=5000)

    # Calculate the chi-squared, degrees of freedom, and parameter errors of the given fit
    if showchi2:
        chi2 = chisquared(params, xdata, ydata, function, sigma)
        dof = len(xdata) - len(params)
        print('Chi-Squared of sample: {}'.format(chi2))
        print('Chi-Squared over degrees of freedom of sample: {}'.format(chi2/dof))
    error = np.sqrt(np.diag(cov))

    # Calculate a data set using the parameters given from the curve-fitting
    xfit = np.linspace(min(xdata), max(xdata), 1000)
    yfit = function(xfit, *params)

    # Plot the data given the title, labels, and such along with the fit
    # Save the plot in the same folder as the data
    if save:
        plt.figure(figsize=setfigsize , dpi=750)
        plt.errorbar(xdata, ydata, yerr=sigma, ls='', marker='.', c='b', label='Measured Parameters')
        plt.plot(xfit, yfit, c='r', label='Fitted Parameters')
        plt.title(title)
        plt.xlabel(xtype)
        plt.ylabel(ytype)
        plt.legend(loc='best')
        plt.savefig(dataaddress[:(dataaddress.rfind('/') + 1)] + dataaddress[(dataaddress.find(' ', 113) + 1):-9] +
                    ' Fit ErrorBar.png')
        plt.close('all')
        plt.clf()
        plt.cla()

        plt.figure(figsize=setfigsize, dpi=750)
        plt.scatter(xdata, ydata, c='b', label='Measured Parameters')
        plt.plot(xfit, yfit, c='r', label='Fitted Parameters')
        plt.title(title)
        plt.xlabel(xtype)
        plt.ylabel(ytype)
        plt.legend(loc='best')
        plt.savefig(dataaddress[:(dataaddress.rfind('/') + 1)] + dataaddress[(dataaddress.find(' ', 113) + 1):-9] +
                    ' Fit Scatter.png')
        plt.close('all')
        plt.clf()
        plt.cla()

    return [params, error]


def residuals(xdata, ydata, xtype, function, params, title, dataaddress, save=True):
    # Calculate the residuals of the fitted parameters
    resids = ydata - function(xdata, *params)

    # Plot the residuals given the title, labels, and such
    # Save the plot in the same folder as the data
    if save:
        plt.figure(figsize=setfigsize, dpi=750)
        plt.scatter(xdata, resids, marker='.', label='Residuals')
        plt.hlines(0, np.min(xdata), np.max(xdata), lw=2, alpha=0.8)
        plt.title(title)
        plt.xlabel(xtype)
        plt.ylabel('Residuals')
        plt.legend(loc='best')
        plt.savefig(dataaddress[:(dataaddress.rfind('/') + 1)] + dataaddress[(dataaddress.find(' ', 113) + 1):-9] +
                    ' Resids.png')
        plt.close('all')
        plt.clf()
        plt.cla()

    return resids


########################################################################################################################
# Enable profiler for part 2
# Apply the fittings and residuals functions to each raw Rxy data sets
########################################################################################################################

Profiler = cProfile.Profile()
Profiler.enable()

XYParamList, XYErrorList = [], []
for FileName in OriginalFiles:
    # Receive the data of the file
    FileName = FileName[:-4] + " Rxy Data.dat"
    RxyData = np.loadtxt(FileName)

    # Apply the curve-fits and residuals for each data set
    NextParams, NextErr = fittings(RxyData[0, :], RxyData[1, :], 'Magnetic Field (T)', 'Resistance (Ohms)', tolinear,
                                   [0.001, 200.], RxyData[2, :], 'Fitted Hall Resistance of Sample ' +
                                   FileName[104:113], FileName)
    residuals(RxyData[0, :], RxyData[1, :], 'Magnetic Field (T)', tolinear, NextParams,
              'Residuals of Hall Resistance of Sample ' + FileName[104:113], FileName)

    # Record each of the parameters and error measurements
    XYParamList.append(NextParams)
    XYErrorList.append(NextErr)

    print('First order approximation of ' + FileName[104:113] + ' Rxy is complete!\n')
XYParamList, XYErrorList = np.array(XYParamList), np.array(XYErrorList)
print()

########################################################################################################################
# Finish and record profiling for part 2
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part Two Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()

########################################################################################################################
# PART THREE: First Order Rxx Parabolic Fit and Second Order Rxy Linear Fit
# Create functions dictating Parabolic Fits
########################################################################################################################


def toparabolic(xvalues, coefficient, offset):
    # Parabolic equation in form y = m * x ^ 2 + b
    return coefficient * xvalues ** 2 + offset


########################################################################################################################
# Enable profiler for part 3
# Apply the parabolic fittings and residuals to each raw Rxx data sets
########################################################################################################################

Profiler = cProfile.Profile()
Profiler.enable()

XXParamList, XXErrorList = [], []
for FileName in OriginalFiles:
    # Receive the data of the file
    FileName = FileName[:-4] + " Rxx Data.dat"
    RxxData = np.loadtxt(FileName)

    # Apply the curve-fits and residuals for each data set
    NextParams, NextErr = fittings(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', 'Resistance (Ohms)', toparabolic,
                                   [0.001, 200.], RxxData[2, :], 'Fitted Longitudinal Resistance of Sample ' +
                                   FileName[104:113], FileName)
    residuals(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', toparabolic, NextParams,
              'Residuals of Longitudinal Resistance of Sample ' + FileName[104:113], FileName)

    # Record each of the parameters and error measurements
    XXParamList.append(NextParams)
    XXErrorList.append(NextErr)

    print('First order approximation of ' + FileName[104:113] + ' Rxx is complete!\n')
XXParamList, XXErrorList = np.array(XXParamList), np.array(XXErrorList)
print()

########################################################################################################################
# Rework Rxy and perform second order approximation of linear curve fit
########################################################################################################################

for Index in range(len(OriginalFiles)):
    # Receive the data of the files
    OriginalName = OriginalFiles[Index]
    FileName = OriginalName[:-4] + " Rxx Data.dat"
    RxxData = np.loadtxt(FileName)
    FileName = OriginalName[:-4] + " Rxy Data.dat"
    RxyData = np.loadtxt(FileName)

    # Calculation of correction and new error values
    Correction = (XYParamList[Index][1] / XXParamList[Index][1]) * RxxData[1, :]
    CorrectionError = (RxxData[2, :] ** 2) / (RxxData[1, :] ** 2)
    CorrectionError += (XYErrorList[Index][1] ** 2) / (XYParamList[Index][1] ** 2)
    CorrectionError += (XXErrorList[Index][1] ** 2) / (XXParamList[Index][1] ** 2)
    RxyPrime = RxyData[1, :] - Correction
    SigmaPrime = np.sqrt(RxyData[2, :] ** 2 + Correction ** 2 * CorrectionError)

    # Apply the curve-fits and residuals for each data set
    NextParams, NextErr = fittings(RxyData[0, :], RxyPrime, 'Magnetic Field (T)', 'Resistance (Ohms)', tolinear,
                                   [0.001, 200.], SigmaPrime, 'Fitted Hall Resistance of Sample ' +
                                   FileName[104:113], FileName)
    residuals(RxyData[0, :], RxyPrime, 'Magnetic Field (T)', tolinear, NextParams,
              'Residuals of Hall Resistance of Sample ' + FileName[104:113], FileName)

    # Record each of the parameters and error measurements
    XYParamList[Index] = NextParams
    XYErrorList[Index] = NextErr

    print('Second order approximation of ' + FileName[104:113] + ' Rxy is complete!\n')
print()

########################################################################################################################
# Finish and record profiling for part 3
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part Three Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()

########################################################################################################################
# PART FOUR: Second Order Rxx Parabolic Fit and Third Order Rxy Linear Fit
# Create functions dictating piece-wise linear and parabolic behavior, mimicking linear magneto-resistance
########################################################################################################################


def topiecewise(xvalues, slope, offset, cutoff):
    # Create y-values array and calculate all parabolic parts of piece-wise
    yvalues = np.zeros(len(xvalues))
    yvalues[np.where(np.abs(xvalues) < cutoff)] = slope * (xvalues[np.where(np.abs(xvalues) < cutoff)] ** 2) + offset

    # Calculate the minimum and maximum value of given x-values for parabolic portions
    maxxval = min(xvalues[np.where(xvalues > cutoff)])
    minxval = max(xvalues[np.where(xvalues < -1 * cutoff)])

    # Calculate the linear coefficients and offsets to create smooth function
    slopelinneg = 2 * slope * minxval
    slopelinpos = 2 * slope * maxxval
    offsetlinneg = (slope * (minxval ** 2) + offset) - slopelinneg * minxval
    offsetlinpos = (slope * (maxxval ** 2) + offset) - slopelinpos * maxxval

    # Calculate and return the remaining y-values
    yvalues[np.where(xvalues > cutoff)] = slopelinpos * xvalues[np.where(xvalues > cutoff)] + offsetlinpos
    yvalues[np.where(xvalues < -1 * cutoff)] = slopelinneg * xvalues[np.where(xvalues < -1 * cutoff)] + offsetlinneg
    return yvalues


########################################################################################################################
# Enable profiler for part 4
# Calculate the best cutoff from various initial guesses for each file
########################################################################################################################

Profiler = cProfile.Profile()
Profiler.enable()

Cutoffs = {'PST037 D1': 3.5, 'PST042 D1': 3.5, 'PST081 D2': 3.5, 'PST189 M1': 3.5, 'PST113 D1': 3.5, 'PST119 D1': 3.5,
           'PST191 M1': 3.5, 'PST192 M1': 3.5, 'PST194 M1': 3.5, 'PST195 M1': 3.5, 'PST196 M1': 3.5, 'PST197 M1': 3.5,
           'PST236 R5': 3.5, 'PST441 G2': 3.5, 'PST441 H3': 3.5, 'PST442 G2': 3.5, 'PST442 H2': 3.5, 'PST380 I2': 9.0}
Adjustment = 1.0
for Index in range(len(OriginalFiles)):
    FileName = OriginalFiles[Index]
    # This correction can only be applied to out of plane measurements
    if 'InPlane' not in FileName:
        # Loading data and initializing adjustment value
        Adjustment = 1.0
        FileName = FileName[:-4] + " Rxx Data.dat"
        RxxData = np.loadtxt(FileName)

        # Repeatedly adjust cutoff over 40 iterations
        for Iteration in range(40):
            # Create three cutoffs at +/-1 and +0 from the original guess
            GuessCutoffs = np.array([1, 1, 1]) * Cutoffs[FileName[104:113]]
            GuessCutoffs[0] += Adjustment
            GuessCutoffs[2] -= Adjustment

            # Create arrays to store parameters, errors, and residuals
            CutoffParameters = [0, 0, 0]
            CutoffErrors = [0, 0, 0]
            CutoffResiduals = [0, 0, 0]

            # Fit each of the cutoff guesses and record each errors and parameters
            CutoffParameters[0], CutoffErrors[0] = fittings(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)',
                                                            'Resistance (Ohms)', topiecewise,
                                                            [XXParamList[Index][0], XXParamList[Index][1],
                                                             GuessCutoffs[0]], RxxData[2, :],
                                                            'Test Fitted Longitudinal Resistance', FileName, save=False,
                                                            showchi2=False)
            CutoffParameters[1], CutoffErrors[1] = fittings(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)',
                                                            'Resistance (Ohms)', topiecewise,
                                                            [XXParamList[Index][0], XXParamList[Index][1],
                                                             GuessCutoffs[1]], RxxData[2, :],
                                                            'Test Fitted Longitudinal Resistance', FileName, save=False,
                                                            showchi2=False)
            CutoffParameters[2], CutoffErrors[2] = fittings(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)',
                                                            'Resistance (Ohms)', topiecewise,
                                                            [XXParamList[Index][0], XXParamList[Index][1],
                                                             GuessCutoffs[2]], RxxData[2, :],
                                                            'Test Fitted Longitudinal Resistance', FileName, save=False,
                                                            showchi2=False)

            # Calculate the residuals of each of the cutoffs
            CutoffResiduals[0] = residuals(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', topiecewise,
                                           CutoffParameters[0], 'Test Residuals of Longitudinal Resistance', FileName,
                                           save=False)
            CutoffResiduals[1] = residuals(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', topiecewise,
                                           CutoffParameters[1], 'Test Residuals of Longitudinal Resistance', FileName,
                                           save=False)
            CutoffResiduals[2] = residuals(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', topiecewise,
                                           CutoffParameters[2], 'Test Residuals of Longitudinal Resistance', FileName,
                                           save=False)

            # Curve-fit each of the residuals to a linear model
            ResidParams = [0, 0, 0]
            ResidErr = [0, 0, 0]
            ResidParams[0], ResidErr[0] = fittings(RxxData[0, :], CutoffResiduals[0], 'Magnetic Field (T)', 'Residuals',
                                                   tolinear, [0.01, 200], 0.01 * CutoffResiduals[0],
                                                   'Test Fitted Residuals', FileName, save=False, showchi2=False)
            ResidParams[1], ResidErr[1] = fittings(RxxData[0, :], CutoffResiduals[1], 'Magnetic Field (T)', 'Residuals',
                                                   tolinear, [0.01, 200], 0.01 * CutoffResiduals[1],
                                                   'Test Fitted Residuals', FileName, save=False, showchi2=False)
            ResidParams[2], ResidErr[2] = fittings(RxxData[0, :], CutoffResiduals[2], 'Magnetic Field (T)', 'Residuals',
                                                   tolinear, [0.01, 200], 0.01 * CutoffResiduals[2],
                                                   'Test Fitted Residuals', FileName, save=False, showchi2=False)

            # Calculate chi-squared by analyzing the parameters of the residuals
            ResidsChiSquare = [0, 0, 0]
            ResidsChiSquare[0] = chisquared(ResidParams[0], RxxData[0, :], CutoffResiduals[0], tolinear,
                                            0.01 * CutoffResiduals[0])
            ResidsChiSquare[1] = chisquared(ResidParams[1], RxxData[0, :], CutoffResiduals[1], tolinear,
                                            0.01 * CutoffResiduals[1])
            ResidsChiSquare[2] = chisquared(ResidParams[2], RxxData[0, :], CutoffResiduals[2], tolinear,
                                            0.01 * CutoffResiduals[2])

            # Replace old parameters with new optimal paramters and reduce the adjustment size
            XXParamList[Index] = CutoffParameters[list(ResidsChiSquare).index(min(ResidsChiSquare))][0:2]
            Cutoffs[FileName[104:113]] = GuessCutoffs[list(ResidsChiSquare).index(min(ResidsChiSquare))]
            Adjustment /= 2

        # Plot the best fit parameters and residuals
        fittings(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', 'Resistance (Ohms)', topiecewise,
                 [XXParamList[Index][0], XXParamList[Index][1], Cutoffs[FileName[104:113]]], RxxData[2, :],
                 'Fitted Longitudinal Resistance of Sample ' + FileName[104:113], FileName)
        LastResiduals = residuals(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', topiecewise,
                                  [XXParamList[Index][0], XXParamList[Index][1], Cutoffs[FileName[104:113]]],
                                  'Residuals of Longitudinal Resistance of Sample ' + FileName[104:113], FileName)

        print(FileName[104:113] + ' Cutoff Value:\t{}'.format(Cutoffs[FileName[104:113]]))

        if 'PST113 D1' in FileName and 'Annealed 4K SmallHB' not in FileName:
            Cutoffs[FileName[104:113]] = 3.5
    print('Second order approximation of ' + FileName[104:113] + ' Rxx is complete!\n')
print()

########################################################################################################################
# Rework Rxy and perform third order approximation of linear curve fit
########################################################################################################################

for Index in range(len(OriginalFiles)):
    # Receive the data of the files
    OriginalName = OriginalFiles[Index]
    FileName = OriginalName[:-4] + " Rxx Data.dat"
    RxxData = np.loadtxt(FileName)
    FileName = OriginalName[:-4] + " Rxy Data.dat"
    RxyData = np.loadtxt(FileName)

    # Calculation of correction and new error values
    Correction = (XYParamList[Index][1] / XXParamList[Index][1]) * RxxData[1, :]
    CorrectionError = (RxxData[2, :] ** 2) / (RxxData[1, :] ** 2)
    CorrectionError += (XYErrorList[Index][1] ** 2) / (XYParamList[Index][1] ** 2)
    CorrectionError += (XXErrorList[Index][1] ** 2) / (XXParamList[Index][1] ** 2)
    RxyPrime = RxyData[1, :] - Correction
    SigmaPrime = np.sqrt(RxyData[2, :] ** 2 + Correction ** 2 * CorrectionError)

    # Apply the curve-fits and residuals for each data set
    NextParams, NextErr = fittings(RxyData[0, :], RxyPrime, 'Magnetic Field (T)', 'Resistance (Ohms)', tolinear,
                                   [0.001, 200.], SigmaPrime, 'Fitted Hall Resistance of Sample ' + FileName[104:113],
                                   FileName)
    residuals(RxyData[0, :], RxyPrime, 'Magnetic Field (T)', tolinear, NextParams,
              'Residuals of Hall Resistance of Sample ' + FileName[104:113], FileName)

    # Record each of the parameters and error measurements
    XYParamList[Index] = NextParams
    XYErrorList[Index] = NextErr

    print('Third order approximation of ' + FileName[104:113] + ' Rxy is complete!\n')
print()

########################################################################################################################
# Finish and record profiling for part 4
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part Four Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()

########################################################################################################################
# PART FIVE: Calculations of carrier density and mobility
# Enable profiler for part 5
# Initialize all necessary lists for data
# Initialize all constants
########################################################################################################################

Profiler = cProfile.Profile()
Profiler.enable()

Thicknesses = {'PST037 D1': 1.69e-5, 'PST042 D1': 1.27e-6, 'PST081 D2': 5e-6, 'PST113 D1': 6.6e-6, 'PST119 D1': 1.65e-6,
               'PST189 M1': 2.e-6, 'PST191 M1': 4.e-6, 'PST192 M1': 6.e-6, 'PST194 M1': 6.e-6, 'PST195 M1': 6.e-6,
               'PST196 M1': 6.e-6, 'PST197 M1': 6.e-6, 'PST236 R5': 9.e-5, 'PST441 G2': 9.e-6, 'PST441 H3': 9.e-6,
               'PST442 G2': 9.e-6, 'PST442 H2': 9.e-6, 'PST380 I2': 2.e-6}
D2CarrierDensity = []
D2CDError = []
D3CarrierDensity = []
D3CDError = []
Mobility = []
MobilityError = []

ElectronCharge = 1.60217662e-19

########################################################################################################################
# Calculate each of the 2D and 3D carrier density and mobility for each sample
########################################################################################################################

for Index in range(len(OriginalFiles)):
    FileName = OriginalFiles[Index]

    if 'InPlane' not in FileName:
        D2CarrierDensity.append(np.abs(1.0 / (1e4 * ElectronCharge * XYParamList[Index][0])))
        D2CDError.append(np.abs(D2CarrierDensity[len(D2CDError)] * -1 * XYErrorList[Index][0] / XYParamList[Index][0]))

        D3CarrierDensity.append(D2CarrierDensity[len(D3CDError)] / Thicknesses[FileName[104:113]])
        D3CDError.append(np.abs(D2CDError[len(D3CDError)] / Thicknesses[FileName[104:113]]))

        Mobility.append(3.0 / (D2CarrierDensity[len(Mobility)] * ElectronCharge * XXParamList[Index][1]))
        MobilityError.append(np.abs(-1 * Mobility[len(MobilityError)] *
                                    np.sqrt((D2CDError[len(MobilityError)] / D2CarrierDensity[len(MobilityError)]) ** 2
                                            + (XXErrorList[Index][1] / XXParamList[Index][1]) ** 2)))

    print('Calculation for carrier density and mobility of ' + FileName[104:113] + ' is complete!')
print()

########################################################################################################################
# Finish and record profiling for part 5
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part Five Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()

########################################################################################################################
# PART SIX: Creation of Carrier Density and Resistivity vs Thickness Relationships
# Enable profiler for part 6
########################################################################################################################

Profiler = cProfile.Profile()
Profiler.enable()

########################################################################################################################
# Initialize all required data lists
########################################################################################################################

Carrier19Sn = []
Carrier19Err = []
Mobility19Sn = []
Mobility19Err = []
RhoXX19Sn = []
RhoXX19Err = []
Thickness19Sn = []
Carrier43Sn = []
Carrier43Err = []
RhoXX43Sn = []
RhoXX43Err = []
Mobility43Sn = []
Mobility43Err = []
Thickness43Sn = []
Carrier60Sn = []
Carrier60Err = []
RhoXX60Sn = []
RhoXX60Err = []
Mobility60Sn = []
Mobility60Err = []
Thickness60Sn = []

########################################################################################################################
# Recover all carrier densities (2D), errors, and thicknesses needed to plot
########################################################################################################################

InPlaneOffset = 0
for Index in range(len(OriginalFiles)):
    FileName = OriginalFiles[Index]
    if 'PST037' in FileName or 'PST042' in FileName or 'PST081' in FileName:
        Carrier60Sn.append(D2CarrierDensity[Index - InPlaneOffset])
        Carrier60Err.append(D2CDError[Index - InPlaneOffset])
        RhoXX60Sn.append(XXParamList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        RhoXX60Err.append(XXErrorList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        Mobility60Sn.append(Mobility[Index - InPlaneOffset])
        Mobility60Err.append(MobilityError[Index - InPlaneOffset])
        Thickness60Sn.append(Thicknesses[FileName[104:113]])
    elif 'PST113' in FileName and 'LargeHB' in FileName and 'Annealed' not in FileName:
        Carrier19Sn.append(D2CarrierDensity[Index - InPlaneOffset])
        Carrier19Err.append(D2CDError[Index - InPlaneOffset])
        RhoXX19Sn.append(XXParamList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        RhoXX19Err.append(XXErrorList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        Mobility19Sn.append(Mobility[Index - InPlaneOffset])
        Mobility19Err.append(MobilityError[Index - InPlaneOffset])
        Thickness19Sn.append(Thicknesses[FileName[104:113]])
    elif 'PST119' in FileName:
        Carrier19Sn.append(D2CarrierDensity[Index - InPlaneOffset])
        Carrier19Err.append(D2CDError[Index - InPlaneOffset])
        RhoXX19Sn.append(XXParamList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        RhoXX19Err.append(XXErrorList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        Mobility19Sn.append(Mobility[Index - InPlaneOffset])
        Mobility19Err.append(MobilityError[Index - InPlaneOffset])
        Thickness19Sn.append(Thicknesses[FileName[104:113]])
    elif 'PST189' in FileName or 'PST191' in FileName or 'PST192' in FileName:
        Carrier43Sn.append(D2CarrierDensity[Index - InPlaneOffset])
        Carrier43Err.append(D2CDError[Index - InPlaneOffset])
        RhoXX43Sn.append(XXParamList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        RhoXX43Err.append(XXErrorList[Index - InPlaneOffset][1] * Thicknesses[FileName[104:113]] / (3 * 100))
        Mobility43Sn.append(Mobility[Index - InPlaneOffset])
        Mobility43Err.append(MobilityError[Index - InPlaneOffset])
        Thickness43Sn.append(Thicknesses[FileName[104:113]])
    elif 'InPlane' in FileName:
        InPlaneOffset += 1

########################################################################################################################
# Plot all carrier densities and resistivities with respect to thickness
########################################################################################################################

CDSlopes = []
CDSlopeErr = []
RhoXXSlopes = []
RhoXXSlopeErr = []
CDs = [Carrier19Sn, Carrier43Sn, Carrier60Sn]
CDErr = [Carrier19Err, Carrier43Err, Carrier60Err]
RhoXXs = [RhoXX19Sn, RhoXX43Sn, RhoXX60Sn]
RhoXXErr = [RhoXX19Err, RhoXX43Err, RhoXX60Err]
Thick = [Thickness19Sn, Thickness43Sn, Thickness60Sn]
TinContent = [19, 43.8, 60]
for Index in range(3):
    # Fit and plotting of carrier density data
    Parameters, CovarianceCD = cf(tolinear, np.log(Thick[Index]), np.log(CDs[Index]), [2000, 1],
                                  sigma=np.abs(np.array(CDErr[Index]) / np.array(CDs[Index])), maxfev=5000)

    CDSlopes.append(Parameters[0])
    CDSlopeErr.append(np.sqrt(np.diag(CovarianceCD))[0])
    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    CDFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.figure(figsize=setfigsize, dpi=750)
    plt.plot(ThickFit, CDFit, c='r', label='Thickness Fit')
    plt.errorbar(Thick[Index], np.array(CDs[Index]), np.array(CDErr[Index]), ls='', marker='.', c='b',
                 label='Thickness Data')
    plt.title('{}% Tin Content 2D Carrier Density vs Thickness'.format(TinContent[Index]))
    plt.xlabel('Thickness (cm)')
    plt.ylabel('Carrier Density (per cm^2)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='best')
    plt.savefig(MyPath + 'Model Graphs/{}Sn 2D Carrier Density.png'.format(TinContent[Index]))
    plt.close('all')
    plt.clf()
    plt.cla()

    # Fit and plotting of resistivity data
    Parameters, CovarianceRho = cf(tolinear, np.log(Thick[Index]), np.log(RhoXXs[Index]), [2000, 1],
                                   sigma=np.abs(np.array(RhoXXErr[Index]) / np.array(RhoXXs[Index])), maxfev=5000)

    RhoXXSlopes.append(Parameters[0])
    RhoXXSlopeErr.append(np.sqrt(np.diag(CovarianceRho))[0])
    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    RhoXXFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.figure(figsize=setfigsize, dpi=750)
    plt.plot(ThickFit, RhoXXFit, c='r', label='Thickness Fit')
    plt.errorbar(Thick[Index], RhoXXs[Index], RhoXXErr[Index], ls='', marker='.', c='b', label='Thickness Data')
    plt.title('{}% Tin Content RhoXX vs Thickness'.format(TinContent[Index]))
    plt.xlabel('Thickness (cm)')
    plt.ylabel('Resistivity (Ohm-meters)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='best')
    plt.savefig(MyPath + 'Model Graphs/{}Sn RhoXX.png'.format(TinContent[Index]))
    plt.close('all')
    plt.clf()
    plt.cla()

########################################################################################################################
# Plot all carrier densities with respect to thickness on a single graph and all the slopes vs tin content
########################################################################################################################

Colors = ['r', 'b', 'g']
plt.figure(figsize=setfigsize, dpi=750)
for Index in range(3):
    # Fit and plotting of carrier density data
    Parameters, Covariance = cf(tolinear, np.log(Thick[Index]), np.log(CDs[Index]), [2000, 1],
                                sigma=np.abs(np.array(CDErr[Index]) / np.array(CDs[Index])), maxfev=5000)

    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    CDFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.plot(ThickFit, CDFit, c=Colors[Index], label='{}% Tin Thickness Fit'.format(TinContent[Index]))
    plt.errorbar(Thick[Index], np.array(CDs[Index]), np.array(CDErr[Index]), ls='', marker='.', c=Colors[Index],
                 label='{}% Tin Thickness Data'.format(TinContent[Index]))
plt.title('2D Carrier Density vs Thickness for Three Series')
plt.xlabel('Thickness (cm)')
plt.ylabel('Carrier Density (per cm^2)')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All 2D CDs vs Thickness.png')
plt.close('all')
plt.clf()
plt.cla()

plt.figure(figsize=setfigsize, dpi=750)
for Index in range(3):
    # Fit and plotting of carrier density data
    Parameters, CovarianceRho = cf(tolinear, np.log(Thick[Index]), np.log(RhoXXs[Index]), [2000, 1],
                                   sigma=np.abs(np.array(RhoXXErr[Index]) / np.array(RhoXXs[Index])), maxfev=5000)

    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    RhoXXFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.plot(ThickFit, RhoXXFit, c=Colors[Index], label='{}% Tin Thickness Fit'.format(TinContent[Index]))
    plt.errorbar(Thick[Index], RhoXXs[Index], RhoXXErr[Index], ls='', marker='.', c=Colors[Index],
                 label='{}% Tin Thickness Data'.format(TinContent[Index]))
plt.title('Rhoxx vs Thickness for Three Series')
plt.xlabel('Thickness (cm)')
plt.ylabel('Rhoxx (Ohm-meters)')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All RhoXXs vs Thickness.png')
plt.close('all')
plt.clf()
plt.cla()

plt.figure(figsize=setfigsize, dpi=750)
plt.errorbar(TinContent, CDSlopes, CDSlopeErr, ls='', marker='.', c='b', label='Thickness Data')
plt.title('2D Carrier Density vs Thickness Log-Log Slope vs Tin Content')
plt.xlabel('Tin Content (%)')
plt.ylabel('Slope (unitless)')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All 2D CD Slopes.png')
plt.close('all')
plt.clf()
plt.cla()

plt.figure(figsize=setfigsize, dpi=750)
plt.errorbar(TinContent, RhoXXSlopes, RhoXXSlopeErr, ls='', marker='.', c='b', label='Thickness Data')
plt.title('Rhoxx vs Thickness Log-Log Slope vs Tin Content')
plt.xlabel('Tin Content (%)')
plt.ylabel('Slope (unitless)')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All RhoXX Slopes.png')
plt.close('all')
plt.clf()
plt.cla()

########################################################################################################################
# Repeat for 3D Carrier Density and Mobility
########################################################################################################################

CDSlopes = []
CDSlopeErr = []
MobilitySlopes = []
MobilitySlopeErr = []
CDs = [Carrier19Sn, Carrier43Sn, Carrier60Sn]
CDErr = [Carrier19Err, Carrier43Err, Carrier60Err]
Mobilities = [Mobility19Sn, Mobility43Sn, Mobility60Sn]
MobilityErr = [Mobility19Err, Mobility43Err, Mobility60Err]
Thick = [Thickness19Sn, Thickness43Sn, Thickness60Sn]
TinContent = [19, 43.8, 60]
for Index in range(3):
    # Fit and plotting of carrier density data
    Parameters, CovarianceCD = cf(tolinear, np.log(Thick[Index]), np.log(CDs[Index]), [2000, 1],
                                  sigma=np.abs(np.array(CDErr[Index]) / np.array(CDs[Index])), maxfev=5000)

    CDSlopes.append(Parameters[0])
    CDSlopeErr.append(np.sqrt(np.diag(CovarianceCD))[0])
    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    CDFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.figure(figsize=setfigsize, dpi=750)
    plt.plot(ThickFit, CDFit / ThickFit, c='r', label='Thickness Fit')
    plt.errorbar(Thick[Index], np.array(CDs[Index]) / np.array(Thick[Index]),
                 np.array(CDErr[Index]) / np.array(Thick[Index]), ls='', marker='.', c='b', label='Thickness Data')
    plt.title('{}% Tin Content 3D Carrier Density vs Thickness'.format(TinContent[Index]))
    plt.xlabel('Thickness (cm)')
    plt.ylabel('Carrier Density (per cm^3)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='best')
    plt.savefig(MyPath + 'Model Graphs/{}Sn 3D Carrier Density.png'.format(TinContent[Index]))
    plt.close('all')
    plt.clf()
    plt.cla()

    # Fit and plotting of resistivity data
    Parameters, CovarianceMu = cf(tolinear, np.log(Thick[Index]), np.log(Mobilities[Index]), [2000, 1],
                                  sigma=np.abs(np.array(MobilityErr[Index]) / np.array(MobilityErr[Index])),
                                  maxfev=5000)

    MobilitySlopes.append(Parameters[0])
    MobilitySlopeErr.append(np.sqrt(np.diag(CovarianceMu))[0])
    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    MobilityFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.figure(figsize=setfigsize, dpi=750)
    plt.plot(ThickFit, MobilityFit, c='r', label='Thickness Fit')
    plt.errorbar(Thick[Index], Mobilities[Index], MobilityErr[Index], ls='', marker='.', c='b', label='Thickness Data')
    plt.title('{}% Tin Content Mobility vs Thickness'.format(TinContent[Index]))
    plt.xlabel('Thickness (cm)')
    plt.ylabel('Mobility (cm^2/Vs)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='best')
    plt.savefig(MyPath + 'Model Graphs/{}Sn Mobility.png'.format(TinContent[Index]))
    plt.close('all')
    plt.clf()
    plt.cla()

Colors = ['r', 'b', 'g']
plt.figure(figsize=setfigsize, dpi=750)
for Index in range(3):
    # Fit and plotting of carrier density data
    Parameters, Covariance = cf(tolinear, np.log(Thick[Index]), np.log(CDs[Index]), [2000, 1],
                                sigma=np.abs(np.array(CDErr[Index]) / np.array(CDs[Index])), maxfev=5000)

    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    CDFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.plot(ThickFit, CDFit / ThickFit, c=Colors[Index], label='{}% Tin Thickness Fit'.format(TinContent[Index]))
    plt.errorbar(Thick[Index], np.array(CDs[Index]) / np.array(Thick[Index]),
                 np.array(CDErr[Index]) / np.array(Thick[Index]), ls='', marker='.', c=Colors[Index],
                 label='{}% Tin Thickness Data'.format(TinContent[Index]))
plt.title('3D Carrier Density vs Thickness for Three Series')
plt.xlabel('Thickness (cm)')
plt.ylabel('3D Carrier Density (per cm^3)')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All 3D CDs vs Thickness.png')
plt.close('all')
plt.clf()
plt.cla()

plt.figure(figsize=setfigsize, dpi=750)
for Index in range(3):
    # Fit and plotting of carrier density data
    Parameters, CovarianceMu = cf(tolinear, np.log(Thick[Index]),  np.log(Mobilities[Index]), [2000, 1],
                                  sigma=np.abs(np.array(MobilityErr[Index]) / np.array(MobilityErr[Index])),
                                  maxfev=5000)

    ThickFit = np.linspace(0.9 * min(Thick[Index]), 1.1 * max(Thick[Index]), 5000)
    MobilityFit = np.exp(tolinear(np.log(ThickFit), *Parameters))

    plt.plot(ThickFit, MobilityFit, c=Colors[Index], label='{}% Tin Thickness Fit'.format(TinContent[Index]))
    plt.errorbar(Thick[Index], Mobilities[Index], MobilityErr[Index], ls='', marker='.', c=Colors[Index],
                 label='{}% Tin Thickness Data'.format(TinContent[Index]))
plt.title('Mobility vs Thickness for Three Series')
plt.xlabel('Thickness (cm)')
plt.ylabel('Mobility (cm^2/Vs)')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All Mobilities vs Thickness.png')
plt.close('all')
plt.clf()
plt.cla()

plt.figure(figsize=setfigsize, dpi=750)
plt.errorbar(TinContent, np.array(CDSlopes) - np.ones(len(CDSlopes)), CDSlopeErr, ls='', marker='.', c='b',
             label='Thickness Data')
plt.title('3D Carrier Density vs Thickness Log-Log Slope vs Tin Content')
plt.xlabel('Tin Content (%)')
plt.ylabel('Slope (unitless)')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All 3D CD Slopes.png')
plt.close('all')
plt.clf()
plt.cla()

plt.figure(figsize=setfigsize, dpi=750)
plt.errorbar(TinContent, MobilitySlopes, MobilitySlopeErr, ls='', marker='.', c='b', label='Thickness Data')
plt.title('Mobility vs Thickness Log-Log Slope vs Tin Content')
plt.xlabel('Tin Content (%)')
plt.ylabel('Slope (unitless)')
plt.legend(loc='best')
plt.savefig(MyPath + 'Model Graphs/All Mobility Slopes.png')
plt.close('all')
plt.clf()
plt.cla()

########################################################################################################################
# Finish and record profiling for part 6
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part Six Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()

########################################################################################################################
# PART SEVEN: Saving the data
# Enable profiler for part 7
########################################################################################################################

Profiler = cProfile.Profile()
Profiler.enable()

########################################################################################################################
# Save all received and created data in individual files in each folder
########################################################################################################################

RecordedCD = {'PST037 D1': 7.3E+19, 'PST042 D1': 1.5E+20, 'PST081 D2': 9.7E+19, 'PST113 D1': 3.9E+18,
              'PST119 D1': 2.0E+19, 'PST189 M1': 1.1E+20, 'PST191 M1': 6.5E+19, 'PST192 M1': 4.2E+19,
              'PST194 M1': 3.5E+19, 'PST195 M1': 3.2E+19, 'PST196 M1': 3.2E+19, 'PST197 M1': 3.7E+19,
              'PST236 R5': 7.3e+18, 'PST380 I2': 1.168581e+20, 'PST441 G2': 3.558928e+19, 'PST441 H3': 3.602220e+19,
              'PST442 G2': 3.512198e+19, 'PST442 H2': 3.257694e+19}
RecordedMobility = {'PST037 D1': 500, 'PST042 D1': 130, 'PST081 D2': 300, 'PST113 D1': 733, 'PST119 D1': 258,
                    'PST189 M1': 141, 'PST191 M1': 191, 'PST192 M1': 300, 'PST194 M1': 365, 'PST195 M1': 414,
                    'PST196 M1': 378, 'PST197 M1': 352, 'PST236 R5': 92, 'PST380 I2': 1.168581e+20,
                    'PST441 G2': 3.558928e+19, 'PST441 H3': 3.602220e+19, 'PST442 G2': 3.512198e+19,
                    'PST442 H2': 3.257694e+19}
InPlaneOffset = 0
for Index in range(len(OriginalFiles)):
    FileName = OriginalFiles[Index]

    DataFile = open(FileName[:-4] + ' Data Release.txt', 'w')
    DataFile.write(FileName[104:113] + ' Data Release:\n\n')
    DataFile.write('Final Fitting Parameters:\n')
    DataFile.write('Rxx Linear-Parabolic Slope:\t\t{} +/- {}\tOhms/T^2\n'.format(XXParamList[Index][0],
                                                                                 XXErrorList[Index][0]))
    DataFile.write('Rxx Linear-Parabolic Offset:\t\t{} +/- {}\tOhms\n'.format(XXParamList[Index][1],
                                                                              XXErrorList[Index][1]))
    DataFile.write('Rxx Linear-Parabolic Critical B-Field:\t{} +/- {}\tT\n'.format(Cutoffs[FileName[104:113]],
                                                                                   Adjustment))
    DataFile.write('Rxy Linear Slope:\t\t{} +/- {}\tOhms/T\n'.format(XYParamList[Index][0], XYErrorList[Index][0]))
    DataFile.write('Rxy Linear Offset:\t\t{} +/- {}\tOhms'.format(XYParamList[Index][1], XYErrorList[Index][1]))
    if 'InPlane' in FileName:
        InPlaneOffset += 1
    else:
        DataFile.write('\n\nCarrier Density and Mobility:\n')
        DataFile.write('2-D Carrier Density:\t{:e} +/- {:e}\t1/cm^2\n'.format(D2CarrierDensity[Index - InPlaneOffset],
                                                                              D2CDError[Index - InPlaneOffset]))
        DataFile.write('3-D Carrier Density:\t{:e} +/- {:e}\t1/cm^3\n'.format(D3CarrierDensity[Index - InPlaneOffset],
                                                                              D3CDError[Index - InPlaneOffset]))
        DataFile.write('Mobility:\t\t{:e} +/- {:e}\tcm^2/(V*s)'.format(Mobility[Index - InPlaneOffset],
                                                                       MobilityError[Index - InPlaneOffset]))

        DataFile.write('\n\nRecorded Data:\n')
        DataFile.write('3-D Carrier Density:\t{:e}\t1/cm^3\n'.format(RecordedCD[FileName[104:113]]))
        DataFile.write('Mobility:\t\t{:e}\tcm^2/(V*s)'.format(RecordedMobility[FileName[104:113]]))

        DataFile.write('\n\nData Discrepancy:\n')
        DataFile.write('3-D Carrier Density:\t{:e}\t1/cm^3\n'.format(D3CarrierDensity[Index - InPlaneOffset] -
                                                                     RecordedCD[FileName[104:113]]))
        DataFile.write('3-D Carrier Density:\t{:e}\tSigmas\n'.format((D3CarrierDensity[Index - InPlaneOffset] -
                                                                      RecordedCD[FileName[104:113]]) /
                                                                     D3CDError[Index - InPlaneOffset]))
        DataFile.write('Mobility:\t\t{:e}\tcm^2/(V*s)'.format(Mobility[Index - InPlaneOffset] -
                                                              RecordedMobility[FileName[104:113]]))
        DataFile.write('Mobility:\t\t{:e}\tSigmas'.format((Mobility[Index - InPlaneOffset] -
                                                           RecordedMobility[FileName[104:113]]) /
                                                          MobilityError[Index - InPlaneOffset]))
    DataFile.close()

########################################################################################################################
# Finish and record profiling for part 7
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part Seven Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()

########################################################################################################################
# PART EIGHT: Fitting the Parish/Littlewood Model
# Enable profiler for part 8
########################################################################################################################

Profiler = cProfile.Profile()
Profiler.enable()

########################################################################################################################
# Creating the function for the model
########################################################################################################################


def ParishLittlewoodModel(magneticfield, rhostar, mustar):
    return rhostar * (np.sqrt(1 + (mustar * magneticfield) ** 2) - 1 + 1/3)


def fittings(xdata, ydata, xtype, ytype, function, initialguess, sigma, title, dataaddress, save=True, showchi2=True):
    # Begin by curve-fitting the data using given initial guess and errors
    params, cov = cf(function, xdata, ydata, initialguess, sigma=sigma, maxfev=5000)

    # Calculate the chi-squared, degrees of freedom, and parameter errors of the given fit
    if showchi2:
        chi2 = chisquared(params, xdata, ydata, function, sigma)
        dof = len(xdata) - len(params)
        print('Chi-Squared of sample: {}'.format(chi2))
        print('Chi-Squared over degrees of freedom of sample: {}'.format(chi2/dof))
    error = np.sqrt(np.diag(cov))

    # Calculate a data set using the parameters given from the curve-fitting
    xfit = np.linspace(min(xdata), max(xdata), 1000)
    yfit = function(xfit, *params)

    # Plot the data given the title, labels, and such along with the fit
    # Save the plot in the same folder as the data
    if save:
        plt.figure(figsize=setfigsize, dpi=750)
        plt.scatter(xdata, ydata, c='b', label='Measured Parameters')
        plt.plot(xfit, yfit, c='r', label='Fitted Parameters')
        plt.title(title)
        plt.xlabel(xtype)
        plt.ylabel(ytype)
        plt.legend(loc='best')
        plt.savefig(dataaddress[:(dataaddress.rfind('/') + 1)] + dataaddress[(dataaddress.find(' ', 113) + 1):-9] +
                    ' Parish-Littlewood.png')
        plt.close('all')
        plt.clf()
        plt.cla()

    return [params, error]


def residuals(xdata, ydata, xtype, function, params, title, dataaddress, save=True):
    # Calculate the residuals of the fitted parameters
    resids = ydata - function(xdata, *params)

    # Plot the residuals given the title, labels, and such
    # Save the plot in the same folder as the data
    if save:
        plt.figure(figsize=setfigsize, dpi=750)
        plt.scatter(xdata, resids, marker='.', label='Residuals')
        plt.hlines(0, np.min(xdata), np.max(xdata), lw=2, alpha=0.8)
        plt.title(title)
        plt.xlabel(xtype)
        plt.ylabel('Residuals')
        plt.legend(loc='best')
        plt.savefig(dataaddress[:(dataaddress.rfind('/') + 1)] + dataaddress[(dataaddress.find(' ', 113) + 1):-9] +
                    ' Parish-Littlewood Resids.png')
        plt.close('all')
        plt.clf()
        plt.cla()

    return resids


########################################################################################################################
# Apply the model for the data sets
# Fitting the model for the data sets
########################################################################################################################

InPlaneOffset = 0
for Index in range(len(OriginalFiles)):
    # Receive the data of the file
    FileName = OriginalFiles[Index - InPlaneOffset][:-4] + " Rxx Data.dat"
    RxxData = np.loadtxt(FileName)

    if 'InPlane' in FileName:
        InPlaneOffset += 1
    else:
        # Calculate effective resistivity and mobility
        RhoStar = 2.0 * (XXParamList[Index - InPlaneOffset][1] * Thicknesses[OriginalFiles[Index - InPlaneOffset][104:113]]
                         / (3 * 100)) / (np.pi * Thicknesses[OriginalFiles[Index - InPlaneOffset][104:113]]) * 0.35
        MuStar = np.pi * Mobility[Index - InPlaneOffset] / (2 * 0.35)
        MagneticField = np.linspace(1.1 * min(RxxData[0, :]), 1.1 * max(RxxData[0, :]))

        # Plotting the Parish-Littlewood Model
        plt.figure(figsize=setfigsize, dpi=750)
        plt.errorbar(RxxData[0, :], RxxData[1, :], RxxData[2, :], ls='', marker='.', c='b', label='Data')
        plt.plot(MagneticField, ParishLittlewoodModel(MagneticField, RhoStar, MuStar), marker='.', label='Fit')
        plt.title('Initial Parish-Littlewood Model of ' + FileName[104:113])
        plt.xlabel('B-Field (T)')
        plt.ylabel('Resistance (Ohms)')
        plt.legend(loc='best')
        plt.savefig(FileName[:(FileName.rfind('/') + 1)] + FileName[(FileName.find(' ', 113) + 1):-9] +
                    ' Parish-Littlewood Initial.png')
        plt.close('all')
        plt.clf()
        plt.cla()

        # Apply the curve-fits and residuals for each data set
        NextParams, NextErr = fittings(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', 'Resistance (Ohms)',
                                       ParishLittlewoodModel, [RhoStar, MuStar], RxxData[2, :],
                                       'Parish-Littlewood Model of ' + FileName[104:113], FileName)
        residuals(RxxData[0, :], RxxData[1, :], 'Magnetic Field (T)', ParishLittlewoodModel, NextParams,
                  'Residuals of Parish-Littlewood Model of ' + FileName[104:113], FileName)


########################################################################################################################
# Finish and record profiling for part 8
########################################################################################################################

Profiler.disable()
File = open(MyPath + 'Part Eight Stats.txt', 'w')
S = io.StringIO()
SortBy = 'tottime'
PStat = pstats.Stats(Profiler, stream=S).sort_stats(SortBy)
PStat.print_stats()
File.write(S.getvalue())
File.close()
