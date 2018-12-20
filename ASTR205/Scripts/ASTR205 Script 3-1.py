import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

def velocityWave(phase, amplitude, frequency, shift, offset):
    return amplitude*np.sin(frequency*phase+shift)+offset

def solveMasses(period, velocity1, velocity2, semimajor1, semimajor2):
    GravCon = 6.674*(10**(-20))
    VelSum = velocity1+velocity2
    SmaSum = semimajor1+semimajor2
    Mass1 = semimajor2*period*86400*(VelSum**3)/(2*np.pi*SmaSum*GravCon)
    Mass2 = period*86400*(VelSum**3)/(2*np.pi*GravCon)-Mass1
    return Mass1, Mass2

def Lorentzian(Day, LMax, Delta, FullEclipse, Loff):
    return LMax/((Delta**2+(Day - FullEclipse)**2)**(1/2))+Loff

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "VBandData.txt"
PhotometricData = np.loadtxt(filename)
filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "VelocityObservations.txt"
VelocityData = np.loadtxt(filename)

###############################################################################

plt.gca().invert_yaxis()
plt.errorbar(PhotometricData[:, 0], PhotometricData[:, 1],
             yerr=PhotometricData[:, 2], marker='.', linestyle='')
plt.title("Straight Plotting of Full Photometric Data Set")
plt.xlabel("Day of Measurement (JD)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

Data2770 = PhotometricData[np.where(PhotometricData[:, 0]<=3000), :][0]
Data2770 = Data2770[np.where(Data2770[:, 0]>=2500), :][0]

plt.gca().invert_yaxis()
plt.errorbar(Data2770[:, 0], Data2770[:, 1], yerr=Data2770[:, 2], marker='.',
             linestyle='')
plt.vlines([2767.7659, 2763.71025], 0, 20, colors='r', linestyles='--')
plt.ylim(17.6, 16.8)
plt.title("Plotting of Photometric Data Close to Julian Day 2765")
plt.xlabel("Day of Measurement (JD)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

period = 2*(2767.7659-2763.71025)
Phase2770 = Data2770[:, 0]/period
Phase2770 = Phase2770%1

plt.gca().invert_yaxis()
plt.errorbar(Phase2770, Data2770[:, 1], yerr=Data2770[:, 2], marker='.',
             linestyle='')
plt.title("Phased Photometric Data Near Julian Day 2765")
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

FullPhase = PhotometricData[:, 0]/period
FullPhase = FullPhase%1

plt.gca().invert_yaxis()
plt.errorbar(FullPhase, PhotometricData[:, 1], yerr=PhotometricData[:, 2],
             marker='.', linestyle='')
plt.title("Fully Phased Set of Binary Star Photometric Data")
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

HalfData = PhotometricData[np.where(FullPhase<=0.5), :][0]
HalfPhase = FullPhase[np.where(FullPhase<=0.5)]

plt.gca().invert_yaxis()
plt.errorbar(HalfPhase, HalfData[:, 1], yerr=HalfData[:, 2], marker='.',
             linestyle='')
plt.title("Half Phased Set of Binary Star Photometric Data (Shallow Eclipse)")
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

initialLorentz = [0.001, 0.002, 0.22, 16.8]
testPhase = np.linspace(0, 0.5, 1000)

plt.gca().invert_yaxis()
plt.errorbar(HalfPhase, HalfData[:, 1], yerr=HalfData[:, 2],
             marker='.', linestyle='')
plt.plot(testPhase, Lorentzian(testPhase, *initialLorentz), c='r',
         linestyle='--')
plt.title("Initial Guess of Lorentzian Fit for Shallow Eclipse Photometrics")
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

LorentzParams, LorentzCOV = cf(Lorentzian, HalfPhase, HalfData[:, 1],
                               sigma=HalfData[:, 2], p0=initialLorentz,
                               maxfev=10**5)

GuessPhases = [0.2098, 0.2225, 0.22425]
Distance1 = -(0.2098-0.224425)*period*86400
Distance2 = -(0.2098-0.2225)*period*86400

plt.gca().invert_yaxis()
plt.errorbar(HalfPhase, HalfData[:, 1], yerr=HalfData[:, 2], marker='.',
             linestyle='')
plt.plot(testPhase, Lorentzian(testPhase, *LorentzParams), c='r',
         linestyle='--')
plt.vlines(GuessPhases, 0, 20, colors='c', linestyle='--')
plt.title("Curve Fit Lorentzian Function for Shallow Eclipse Photometrics")
plt.ylim(17.6, 16.8)
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

plt.gca().invert_yaxis()
plt.errorbar(HalfPhase, HalfData[:, 1], yerr=HalfData[:, 2], marker='.',
             linestyle='')
plt.vlines(GuessPhases, 0, 20, colors='c', linestyle='--')
plt.title("Approximate Phases for First, Second, and Third Contact")
plt.ylim(17.6, 16.8)
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (mag)")
plt.show()

###############################################################################

plt.scatter(VelocityData[:, 3], VelocityData[:, 1], s=5, c='c')
plt.scatter(VelocityData[:, 3], VelocityData[:, 2], s=5, c='r')
plt.title("Fully Phased Set of Given Velocity Data")
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Raidal Velocity of Binary Star System (km/s)")
plt.show()

FirstMax = max(VelocityData[:, 1])
FirstMin = min(VelocityData[:, 1])
SecondMax = max(VelocityData[:, 2])
SecondMin = min(VelocityData[:, 2])
MaxMins = [FirstMax, FirstMin, SecondMax, SecondMin]

plt.scatter(VelocityData[:, 3], VelocityData[:, 1], s=5, c='c')
plt.scatter(VelocityData[:, 3], VelocityData[:, 2], s=5, c='r')
plt.hlines(MaxMins, -0.5, 0.5, colors=['c', 'c', 'r', 'r'])
plt.title("Approximation of Maximum and Minimum Velocities from Data Set")
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (km/s)")
plt.show()

initial = [(FirstMin-FirstMax)/2, 2*np.pi, 0.5, (FirstMin-FirstMax)/2+FirstMin]
FirstParams, FirstCov = cf(velocityWave, VelocityData[:, 3],
                           VelocityData[:, 1], p0=initial, maxfev=10**5)
SecondParams, SecondCov = cf(velocityWave, VelocityData[:, 3],
                             VelocityData[:, 2], p0=initial, maxfev=10**5)

TestX = np.linspace(-0.5,0.5,1000)
FirstTestY = velocityWave(TestX, *FirstParams)
SecondTestY = velocityWave(TestX, *SecondParams)

plt.scatter(VelocityData[:, 3], VelocityData[:, 1], s=5, c='c')
plt.scatter(VelocityData[:, 3], VelocityData[:, 2], s=5, c='r')
plt.title("Curve Fitted Sine Waves to Sinusoidal Velocity Data")
plt.plot(TestX, FirstTestY, c='c')
plt.plot(TestX, SecondTestY, c='r')
plt.xlabel("Phase of Measurement (Phase)")
plt.ylabel("Magnitude of Binary Star System (km/s)")
plt.show()

###############################################################################

PER = period
COMVEL = (SecondParams[3]+FirstParams[3])/2
VELStar1 = abs(FirstParams[0])
VELStar2 = abs(SecondParams[0])
RATIO = VELStar1/VELStar2
SMAStar1 = VELStar1*period*86400/(2*np.pi)
SMAStar2 = VELStar2*period*86400/(2*np.pi)
MASStar1, MASStar2 = solveMasses(PER, VELStar1, VELStar2, SMAStar1, SMAStar2)
RADStar1 = (Distance1*(VELStar1+VELStar2))/2
RADStar2 = (Distance2*(VELStar1+VELStar2))/2

PERString = "The period of the orbit is {:.4f} days."
COMString = "The center of mass velocity is {:.3f} km/s."
VELString = "The maximum radial velocity of star {:d} is {:.3f} km/s."
RATString = "The ratio of {} is {:.6f}."
MASString = "The minimum mass of the star {:d} is {:.3e} kg."
RADString = "The minimum radius of the star {:d} is {:.3e} km."
SMAString = "The minimum semi-major axis of the star{:d} is {:.3e} km."

print(PERString.format(period))
print()
print(COMString.format(COMVEL))
print()
print(VELString.format(1, VELStar1))
print(VELString.format(2, VELStar2))
LargerVelocity = max([VELStar1, VELStar2])
if (abs(VELStar1-VELStar2)<0.1*LargerVelocity):
    print("Stars are on approximate circular orbit.")
print()
print(RATString.format("velocities", RATIO))
print()
print(SMAString.format(1, SMAStar1))
print(SMAString.format(2, SMAStar2))
print()
print(MASString.format(1, MASStar1))
print(MASString.format(2, MASStar2))
print()
print(RADString.format(1, RADStar1))
print(RADString.format(2, RADStar2))