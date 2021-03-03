import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

# Name          Tin Content     T\-(Te)     Substrate Temp  Thickness   Comments
# T Series 2    60%             225K?       ---             Varied      Bulk PST
# T Series 1    43.8%           239K        ---             Varied      ---
# P Series      43.8%           239K        Varied          20nm        ---
# PST 441       50%             ---         ---             ---         [100]
# PST 442       50%             ---         ---             ---         [111]
# PST 236       ---             ---         ---             900nm       PST:Cd
# PST 380       48%             ---         ---             20nm        ---

ECHARGE = 1.60217662e-19


def linear(thicklog, slope, offset):
    return slope * thicklog + offset


def thicknessdensity1(thickness, slope, offset):
    return slope * thickness ** 0.14014515 + offset


def thicknessdensity2(thickness, slope, offset):
    return slope * thickness ** 0.69691325 + offset


def thicknessdensity3(thickness, slope, offset):
    return slope * thickness ** 1.44385292 + offset


def thicknessdensity(thickness):
    return 6e13 * thickness ** 0.5


def testfunction(Bfield, pn, thickness, R0):
    resistivity = np.ones(len(Bfield))
    cutoff = ECHARGE * (1e4 * pn) * R0 / 3.0

    resistivity[np.where(np.abs(Bfield) < cutoff)] = (3.0 * 1e-9 * thickness) / \
                                                     (ECHARGE ** 2.0 * R0) * (Bfield[np.where(
                                                         np.abs(Bfield) < cutoff)] ** 2.0) / (1e4 * pn) ** 2.0
    resistivity[np.where(np.abs(Bfield) >= cutoff)] = (1e-9 * thickness / 3.0) * R0

    return resistivity


def function(testthickness):
    testR0 = 202.9131049801961
    testbfield = np.linspace(-150, 150, 5000)

    nchannels = 2 * int(testthickness)
    p = []
    rho = []
    p.append(thicknessdensity(testthickness / float(nchannels)))
    rho.append(testfunction(testbfield, p[0], testthickness / float(nchannels), testR0))
    inversesum = 1.0 / rho[0]
    for index in range(1, nchannels):
        p.append((index + 1.0) * thicknessdensity((index + 1.0) * testthickness / float(nchannels)) - sum(p))
        rho.append(testfunction(testbfield, p[index], testthickness / float(nchannels), testR0))
        inversesum += 1.0 / rho[index]

    rhototal = nchannels / inversesum
    plt.plot(testbfield, rhototal * 3.0 / (testthickness * 1E-9) , label='Thickness: {}nm'.format(int(testthickness)))


ThicknessSeries1 = np.array([60., 40., 20.])        # Tin Content of 43.8%
ThicknessSeries2 = np.array([50., 12.7, 169.])      # Tin Content of 60.0%
ThicknessSeries3 = np.array([66., 16.5])            # Tin Content of 19.0%
CarrierDensitySeries1 = np.array([4.2E+19, 6.5E+19, 1.1E+20])
CarrierDensitySeries2 = np.array([9.7E+19, 1.5E+20, 7.3E+19])
CarrierDensitySeries3 = np.array([3.9E18, 2.432128E18])

CarrierDensitySeries1 = CarrierDensitySeries1 * (ThicknessSeries1 * 1e-7)
CarrierDensitySeries2 = CarrierDensitySeries2 * (ThicknessSeries2 * 1e-7)
CarrierDensitySeries3 = CarrierDensitySeries3 * (ThicknessSeries3 * 1e-7)

params1, cov1 = cf(linear, np.log(ThicknessSeries1), np.log(CarrierDensitySeries1), [1, 40],
                   0.1 * CarrierDensitySeries1)
# plt.scatter(np.log(ThicknessSeries1), np.log(CarrierDensitySeries1))
# plt.plot(np.log(np.linspace(10, 1000)), linear(np.log(np.linspace(10, 1000)), *params1))
# plt.xlabel('Ln(Thickness)')
# plt.ylabel('Ln(Carrier Density)')
# plt.title('Log-Log Plot of Carrier Density versus Thickness for PST189/191/192')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Log-Log Thickness Series 1 CD Fit.png")
# plt.clf()

params2, cov2 = cf(linear, np.log(ThicknessSeries2), np.log(CarrierDensitySeries2),
                   [1, 40], 0.1 * CarrierDensitySeries2)
# plt.scatter(np.log(ThicknessSeries2), np.log(CarrierDensitySeries2))
# plt.plot(np.log(np.linspace(10, 1000)), linear(np.log(np.linspace(10, 1000)), *params2))
# plt.xlabel('Ln(Thickness)')
# plt.ylabel('Ln(Carrier Density)')
# plt.title('Log-Log Plot of Carrier Density versus Thickness for PST037/042/081')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Log-Log Thickness Series 2 CD Fit.png")
# plt.clf()

params3, cov3 = cf(linear, np.log(ThicknessSeries3), np.log(CarrierDensitySeries3),
                   [1, 40], 0.1 * CarrierDensitySeries3)
# plt.scatter(np.log(ThicknessSeries3), np.log(CarrierDensitySeries3))
# plt.plot(np.log(np.linspace(10, 1000)), linear(np.log(np.linspace(10, 1000)), *params3))
# plt.xlabel('Ln(Thickness)')
# plt.ylabel('Ln(Carrier Density)')
# plt.title('Log-Log Plot of Carrier Density versus Thickness for PST113/119')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Log-Log Thickness Series 3 CD Fit.png")
# plt.clf()

plt.scatter(ThicknessSeries3, CarrierDensitySeries3, c='r', label='Thickness Series 3 Data 19.0% Tin')
plt.scatter(ThicknessSeries2, CarrierDensitySeries2, c='b', label='Thickness Series 2 Data 60.0% Tin')
plt.scatter(ThicknessSeries1, CarrierDensitySeries1, c='g', label='Thickness Series 1 Data 43.8% Tin')
plt.plot(np.exp(np.log(np.linspace(10, 200))), np.exp(linear(np.log(np.linspace(10, 200)), *params1)),
         c='g', label='Thickness Series 1 Fit 43.8% Tin')
plt.plot(np.exp(np.log(np.linspace(10, 200))), np.exp(linear(np.log(np.linspace(10, 200)), *params2)),
         c='b', label='Thickness Series 2 Fit 60.0% Tin')
plt.plot(np.exp(np.log(np.linspace(10, 200))), np.exp(linear(np.log(np.linspace(10, 200)), *params3)),
         c='r', label='Thickness Series 3 Fit 19.0% Tin')
plt.xlabel('Thickness (nm)')
plt.ylabel('Carrier Density (per cm^2)')
plt.xscale('log')
plt.yscale('log')
plt.title('Log-Log Plot of Carrier Density versus Thickness')
plt.legend(loc='best')
plt.show()

plt.scatter(ThicknessSeries2, CarrierDensitySeries2, c='b', label='Thickness Series 2 Data 60.0% Tin')
plt.scatter(ThicknessSeries1, CarrierDensitySeries1, c='g', label='Thickness Series 1 Data 43.8% Tin')
plt.plot(np.exp(np.log(np.linspace(10, 200))), np.exp(linear(np.log(np.linspace(10, 200)), *params1)),
         c='g', label='Thickness Series 1 Fit 43.8% Tin')
plt.plot(np.exp(np.log(np.linspace(10, 200))), np.exp(linear(np.log(np.linspace(10, 200)), *params2)),
         c='b', label='Thickness Series 2 Fit 60.0% Tin')
plt.xlabel('Thickness (nm)')
plt.ylabel('Carrier Density (per cm^2)')
plt.xscale('log')
plt.yscale('log')
plt.title('Log-Log Plot of Carrier Density versus Thickness')
plt.legend(loc='best')
plt.show()

# SnParams, SnCoV = cf(linear, [43.8, 60.0, 19.0], [params1[0], params2[0], params3[0]], [0.1, 1.6],
#                      0.1 * np.array([params1[0], params2[0], params3[0]]))

plt.scatter([43.8, 60.0, 19.0], [params1[0], params2[0], params3[0]], label='Data')
# plt.plot(np.linspace(0, 100, 10000), linear(np.linspace(0, 100, 10000), *SnParams), label='Fit')
plt.ylabel('Slope (Unitless)')
plt.xlabel('Sn Content (%)')
plt.title('Plot of Slope versus Tin Content')
plt.show()

print(params1)
print(cov1)
print(params2)
print(cov2)
print(params3)
print(cov3)
# print()
# print(SnParams)
# print(SnCoV)
print()

paramsthick1, covthick1 = cf(thicknessdensity1, ThicknessSeries1, CarrierDensitySeries1, [2e15, 1e20],
                             0.1 * CarrierDensitySeries1)
# plt.scatter(ThicknessSeries1, CarrierDensitySeries1)
# plt.plot(np.linspace(10, 200), thicknessdensity1(np.linspace(10, 200), *paramsthick1))
# plt.xlabel('Thickness')
# plt.ylabel('Carrier Density')
# plt.title('Plot of Carrier Density versus Thickness for PST189/191/192')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Thickness Series 1 CD Fit.png")
# plt.clf()

paramsthick2, covthick2 = cf(thicknessdensity2, ThicknessSeries2, CarrierDensitySeries2, [2e15, 1e20],
                             0.1 * CarrierDensitySeries2)
# plt.scatter(ThicknessSeries2, CarrierDensitySeries2)
# plt.plot(np.linspace(10, 200), thicknessdensity2(np.linspace(10, 200), *paramsthick2))
# plt.xlabel('Thickness')
# plt.ylabel('Carrier Density')
# plt.title('Plot of Carrier Density versus Thickness for PST037/042/081')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Log-Log Thickness Series 2 CD Fit.png")
# plt.clf()

paramsthick3, covthick3 = cf(thicknessdensity3, ThicknessSeries3, CarrierDensitySeries3, [2e15, 1e20],
                             0.1 * CarrierDensitySeries3)
# plt.scatter(ThicknessSeries3, CarrierDensitySeries3)
# plt.plot(np.linspace(10, 200), thicknessdensity3(np.linspace(10, 200), *paramsthick3))
# plt.xlabel('Thickness')
# plt.ylabel('Carrier Density')
# plt.title('Plot of Carrier Density versus Thickness for PST113/119')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Log-Log Thickness Series 3 CD Fit.png")
# plt.clf()

plt.scatter(ThicknessSeries3, CarrierDensitySeries3, c='r', label='Thickness Series 3 Data 19.0% Tin')
plt.scatter(ThicknessSeries2, CarrierDensitySeries2, c='b', label='Thickness Series 2 Data 60.0% Tin')
plt.scatter(ThicknessSeries1, CarrierDensitySeries1, c='g', label='Thickness Series 1 Data 43.8% Tin')
plt.plot(np.linspace(10, 200), thicknessdensity1(np.linspace(10, 200), *paramsthick1),
         c='g', label='Thickness Series 1 Fit 43.8% Tin')
plt.plot(np.linspace(10, 200), thicknessdensity2(np.linspace(10, 200), *paramsthick2),
         c='b', label='Thickness Series 2 Fit 60.0% Tin')
plt.plot(np.linspace(10, 200), thicknessdensity3(np.linspace(10, 200), *paramsthick3),
         c='r', label='Thickness Series 3 Fit 19.0% Tin')
plt.xlabel('Thickness')
plt.ylabel('Carrier Density')
plt.title('Plot of Carrier Density versus Thickness')
plt.legend(loc='best')
plt.show()

print(paramsthick1)
print(covthick1)
print(paramsthick2)
print(covthick2)
print(paramsthick3)
print(covthick3)
print()

# RxxDataT1N1 = np.loadtxt('C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/'
#                          'Verified Data/PST192 M1/BsweepBH (01) _RxxData.dat')
# RxxDataT1N2 = np.loadtxt('C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/'
#                          'Verified Data/PST191 M1/Bsweep_SH (01) _RxxData.dat')
# RxxDataT1N3 = np.loadtxt('C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/'
#                          'Verified Data/PST189 M1/B_sweep_BH_R1_12_1_R2_12_10_R3_10_3 (01) _RxxData.dat')
# RxxDataT2N1 = np.loadtxt('C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/'
#                          'Verified Data/PST081 D2/I_8_B_R1_5_2_R2_6_5_Bsweep_HBbig (01) _RxxData.dat')
# RxxDataT2N2 = np.loadtxt('C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/'
#                          'Verified Data/PST042 D1/I_D_4_R1_6_8_R2_6_5_R3_5_3_bsweep_small (01) _RxxData.dat')
# RxxDataT2N3 = np.loadtxt('C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/'
#                          'Verified Data/PST037 D1/I_9_2_R1_B_12_R2_11_12_Bsweep_big (01) _RxxData.dat')

# plt.scatter([60., 40., 20.], [246.03900426255757, 380.07726768962823, 614.3692229525342])
# plt.title('Plot of Resistance versus Carrier Density')
# plt.xlabel('Thickness (nm)')
# plt.ylabel('Rxx (Ohms)')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Thickness Series 1 Resist Data.png")
# plt.clf()
#
# plt.scatter([50., 12.7, 169.], [130.4141990173324, 776.0403589246822, 30.69315790368633])
# plt.title('Plot of Resistance versus Carrier Density')
# plt.xlabel('Thickness (nm)')
# plt.ylabel('Rxx (Ohms)')
# plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/New Graphs/Thickness Series 2 Resist Data.png")
# plt.clf()

plt.scatter([60., 40., 20.], [246.03900426255757, 380.07726768962823, 614.3692229525342],
            c='g', label='Thickness Series 1 Data')
plt.scatter([50., 12.7, 169.], [130.4141990173324, 776.0403589246822, 30.69315790368633],
            c='b', label='Thickness Series 2 Data')
plt.title('Plot of Resistance versus Carrier Density')
plt.xlabel('Thickness (nm)')
plt.ylabel('Rxx (Ohms)')
plt.legend(loc='best')
plt.show()

for thickness in np.arange(100., 1001., 100):
    function(thickness)
plt.title('Linear Magneto-resistance Dependence on Channel Number')
plt.xlabel('Magnetic Field (T)')
plt.ylabel('Delta Rxx (Ohms)')
plt.legend(loc='best')
plt.show()
