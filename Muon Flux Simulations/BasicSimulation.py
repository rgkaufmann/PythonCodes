import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
MUMASS = 1.883531609E-28                          # kilogram
P0 = 101325                                       # kilogram/(meter*second^2)
T0 = 288.15                                       # kelvin
R = 8.31447                                       # joules/(mol*kelvin)
LAPSE = 0.0065                                    # kelvin/meter
GACC = 9.80665                                    # meters/second^2
AVOGADRO = 6.022E+23                              # 1/mol
Z = 14.28312                                      # unitless
ATOMICMASS = 28.5768                              # unitless
MOLARMASS = 0.0289654                             # kilogram/mol
ECHARGE = -1.60218E-19                            # coulombs
EPSILON0 = 8.85418781E-12                         # farads/meter
EMASS = 9.109383632E-31                           # kilograms
EXCITEPOT = 1.302E-18 * Z                         # joules
SPEEDLIGHT = 2.998E8                              # meters/second
ERADIUS = 6371000                                 # meters
avgheight = 15000                                 # meters
speed = 0.994                                     # unitless
gamma = 1/(np.sqrt(1-speed**2))                   # unitless
histbins = np.arange(0.0, 31.0, 1.0) * 1 / gamma  # unitless
average = 1 / 2.2                                 # 1/microsecond
momentatrials = 1000000                           # unitless


# Functions
def bethefunction(distance, beta, theta):
    height = distance * np.cos(theta)
    gasdensity = ((P0 * MOLARMASS)/(R * T0)) * (1 - (LAPSE * height)/T0)**(((GACC * MOLARMASS)/(R * LAPSE))-1)
    electrondensity = ((AVOGADRO * Z)/(ATOMICMASS * MOLARMASS)) * gasdensity
    coefficient = ((4*np.pi)/(EMASS * SPEEDLIGHT**2 * beta**2)) * ((ECHARGE**2)/(4 * np.pi * EPSILON0))**2
    natlog = (np.log((2 * EMASS * SPEEDLIGHT**2 * beta**2)/(EXCITEPOT * (1-beta**2)))-beta**2)
    return coefficient * electrondensity * natlog


def decay():
    decaypoint = 0
    while True:
        if np.random.poisson(average, 1)[0] > average:
            break
        decaypoint += 1
    return decaypoint


def reldecay():
    decaypoint = 0
    while True:
        if np.random.poisson(average / gamma, 1)[0] > (average / gamma):
            break
        decaypoint += 1
    return decaypoint


def momentadecay(theta, beta):
    decaypoint = 0
    distance = sphericaldistance(theta)
    energy = (MUMASS * SPEEDLIGHT**2)/np.sqrt(1 - beta**2)
    while True:
        if np.random.poisson(average * np.sqrt(1 - beta**2), 1)[0] > average * np.sqrt(1 - beta**2):
            break
        distance -= beta * SPEEDLIGHT * 1e-6
        if distance >= 0:
            energy -= np.abs(quad(bethefunction, distance, distance + (beta * SPEEDLIGHT * 1e-6),
                                  args=(beta, theta))[0])
            if energy <= (MUMASS * SPEEDLIGHT**2):
                energy = 1.001 * (MUMASS * SPEEDLIGHT**2)
            beta = np.sqrt(1 - ((MUMASS * SPEEDLIGHT**2) / energy)**2)
        decaypoint += 1
    return decaypoint, energy, distance


def posnormal(mean, sigma):
    Val = np.random.normal(mean, sigma, 1)
    return Val if Val > 0 else posnormal(mean, sigma)


def posnormalarray(mean, sigma, length):
    ValArray = []
    for index in range(length):
        ValArray.append(posnormal(mean, sigma)[0])
    return np.array(ValArray)


def anglebounds(theta, difference, width):
    return list(np.where(np.array([theta - np.arctan(width / difference), theta + np.arctan(width / difference)]) <= 0,
                         0, np.array([theta - np.arctan(width / difference), theta + np.arctan(width / difference)])))


def sphericaldistance(theta):
    angleC = np.arcsin((ERADIUS * np.sin(np.pi - theta)) / (ERADIUS + avgheight))
    if theta == 0.0:
        return float(avgheight)
    return ((ERADIUS + avgheight) / (np.sin(np.pi - theta))) * np.sin(theta - angleC)


sphericaldistance = np.vectorize(sphericaldistance)
momentaarraydecay = np.vectorize(momentadecay)

# Poisson Repitition - No Relativity ###################################################################################
lifetimes = []

for i in range(0, 100000):
    lifetime = decay()
    lifetimes.append(lifetime)

print('Non-Relativistic Poisson Repitition Completed!')

plt.hist(lifetimes, bins=np.arange(int(min(lifetimes)), int(max(lifetimes))+2))
plt.title('Non-Relativistic Muon Lifetimes')
plt.ylabel('Counts [1]')
plt.xlabel('Lifetime [sec]')
plt.yscale('log')
plt.savefig("./NonRelativisticPoisson.png")

# Poisson Repititon - Relativity #######################################################################################
lifetimes = []

for i in range(0, 1000000):
    lifetime = reldecay()
    lifetimes.append(lifetime)

print('Relativistic Poisson Repitition Completed!')

plt.hist(lifetimes, bins=np.arange(int(min(lifetimes)), int(max(lifetimes))+2))
plt.title('Non-Relativistic Muon Lifetimes')
plt.ylabel('Counts [1]')
plt.xlabel('Lifetime [sec]')
plt.yscale('log')
plt.savefig("./RelativisticPoisson.png")

# Path Length ##########################################################################################################
print('Path Length Calculations Completed!')

plt.hist(np.array(lifetimes)*speed*SPEEDLIGHT*1e-6)
plt.title('Muon Path Lengths')
plt.ylabel('Counts [1]')
plt.xlabel('Path Lengths [m]')
plt.yscale('log')
plt.savefig("./PathLength.png")

# Flat Earth Angle Distribution ########################################################################################
angle = np.random.rand(len(lifetimes)) * np.pi/2
pathlength = np.array(lifetimes) * speed * SPEEDLIGHT * 1e-6
detectordistance = avgheight / np.cos(angle)

detectorhits = np.ma.masked_equal(np.where(pathlength >= detectordistance, angle * 360 / (2 * np.pi), -1), -1)

print('Flat Earth Angle Distribution Completed!')

plt.hist(detectorhits, bins=np.arange(0, 91, 1), density=True)
plt.title('Muon Angle Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Angle [deg]')
plt.savefig("./FlatEarthAngles.png")

# Spherical Earth Angle Distribution ###################################################################################
angle = np.random.rand(len(lifetimes)) * np.pi/2
spheredistance = sphericaldistance(angle)

spherehits = np.ma.masked_equal(np.where(pathlength >= spheredistance, angle * 360 / (2 * np.pi), -1), -1)

print('Spherical Earth Angle Distribution Completed!')

plt.hist(spherehits, bins=np.arange(0, 91, 1), density=True)
plt.title('Muon Angle Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Angle [deg]')
plt.savefig("./SphericalEarthAngles.png")

# Momenta and Attenuation ##############################################################################################
AngleSet = np.random.rand(momentatrials) * np.pi/2
DistanceSet = sphericaldistance(AngleSet)
MomentaSet = posnormalarray(4, 25/3, momentatrials) * 5.344E-19
EnergySet = np.sqrt(MomentaSet**2 * SPEEDLIGHT**2 + MUMASS**2 * SPEEDLIGHT**4)
BetaSet = np.sqrt(1 - ((MUMASS * SPEEDLIGHT**2)/EnergySet)**2)

lifetimes, lengths, energies = momentaarraydecay(AngleSet, BetaSet)

print('Momenta Trial Completed!')

lifetimes = np.array(lifetimes)
energies = np.array(energies)
lengths = np.array(lengths)
momenta = (1 / SPEEDLIGHT) * np.sqrt(energies ** 2 - MUMASS ** 2 * SPEEDLIGHT ** 4)

spherehits = np.ma.masked_equal(np.where(lengths >= DistanceSet, AngleSet * 360 / (2 * np.pi), -1), -1)

plt.hist(lifetimes, bins=np.arange(int(min(lifetimes)), int(max(lifetimes))+2))
plt.title('Muon Lifetime Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Lifetime [sec]')
plt.yscale('log')
plt.savefig("./MomentaLifetimes.png")

plt.hist(spherehits, bins=np.arange(0, 91, 1), density=True)
plt.title('Muon Angle Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Angle [deg]')
plt.savefig("./MomentaAngles.png")

plt.hist(EnergySet * 6.242E9, bins=np.arange(1, 400, 1) * 0.1, density=True, label='Initial')
plt.hist(energies * 6.242E9, bins=np.arange(1, 400, 1) * 0.1, density=True, label='Final')
plt.title('Muon Energy Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Energy [GeV]')
plt.savefig("./MomentaEnergy.png")

plt.hist(MomentaSet, bins=np.arange(0, 200, 1) * 1e-19, density=True, label='Initial')
plt.hist(momenta, bins=np.arange(0, 200, 1) * 1e-19, density=True, label='Final')
plt.title('Muon Momenta Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Momentum [m/s]')
plt.savefig("./Momenta.png")

# Detector Geometry ####################################################################################################
PhiValues = np.linspace(0, 90, 18)
Counts = []

for phi in PhiValues:
    AngleSet = np.random.rand(momentatrials) * np.pi / 2
    LowBound, HighBound = anglebounds(phi, 0.9, 0.5)
    CountSet = np.where(np.logical_and(AngleSet >= LowBound, AngleSet <= HighBound), 1, 0)
    Counts.append(sum(CountSet))
Counts = np.array(Counts)

plt.errorbar(PhiValues * 180 / np.pi, Counts, yerr=np.sqrt(Counts))
plt.title('Detector Geometry Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Angle [deg]')
plt.savefig("./DetecterGeometry.png")

# Combining Everything #################################################################################################
AngleSet = np.random.rand(momentatrials) * np.pi/2
DistanceSet = sphericaldistance(AngleSet)
MomentaSet = posnormalarray(4, 25/3, momentatrials) * 5.344E-19
EnergySet = np.sqrt(MomentaSet**2 * SPEEDLIGHT**2 + MUMASS**2 * SPEEDLIGHT**4)
BetaSet = np.sqrt(1 - ((MUMASS * SPEEDLIGHT**2)/EnergySet)**2)

fulllifetimes = []
fullenergies = []
fulllengths = []
counts = []

for phi in PhiValues:
    LowBound, HighBound = anglebounds(phi, 0.9, 0.5)
    CountSet = np.where(np.logical_and(AngleSet >= LowBound, AngleSet <= HighBound), 1, 0)
    lifetimes, lengths, energies = momentaarraydecay(AngleSet[np.where(CountSet == 1)],
                                                     BetaSet[np.where(CountSet == 1)])
    fulllifetimes = fulllifetimes + lifetimes
    fulllengths = fulllengths + lengths
    fullenergies = fullenergies + energies
    counts.append(sum(CountSet))

print('Detector Geometry with Momenta Trial Completed!')

counts = np.array(Counts)
lifetimes = np.array(lifetimes)
energies = np.array(energies)
lengths = np.array(lengths)
momenta = (1 / SPEEDLIGHT) * np.sqrt(energies ** 2 - MUMASS ** 2 * SPEEDLIGHT ** 4)

spherehits = np.ma.masked_equal(np.where(lengths >= DistanceSet, AngleSet * 360 / (2 * np.pi), -1), -1)

plt.hist(lifetimes, bins=np.arange(int(min(lifetimes)), int(max(lifetimes))+2))
plt.title('Muon Lifetime Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Lifetime [sec]')
plt.yscale('log')
plt.savefig("./MomentaLifetimes.png")

plt.errorbar(PhiValues, counts, yerr=np.sqrt(counts))
plt.title('Muon Angle Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Angle [deg]')
plt.savefig("./MomentaAngles.png")

plt.hist(EnergySet * 6.242E9, bins=np.arange(1, 400, 1) * 0.1, density=True, label='Initial')
plt.hist(energies * 6.242E9, bins=np.arange(1, 400, 1) * 0.1, density=True, label='Final')
plt.title('Muon Energy Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Energy [GeV]')
plt.savefig("./MomentaEnergy.png")

plt.hist(MomentaSet, bins=np.arange(0, 200, 1) * 1e-19, density=True, label='Initial')
plt.hist(momenta, bins=np.arange(0, 200, 1) * 1e-19, density=True, label='Final')
plt.title('Muon Momenta Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Momentum [m/s]')
plt.savefig("./Momenta.png")
