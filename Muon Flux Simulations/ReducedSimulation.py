import numpy as np
import matplotlib.pyplot as plt

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
momentatrials = 500000                            # unitless


# Functions
def bethefunction(distance, beta, theta):
    height = distance * np.cos(theta)
    gasdensity = ((P0 * MOLARMASS)/(R * T0)) * (1 - (LAPSE * height)/T0)**(((GACC * MOLARMASS)/(R * LAPSE))-1)
    electrondensity = ((AVOGADRO * Z)/(ATOMICMASS * MOLARMASS)) * gasdensity
    coefficient = ((4*np.pi)/(EMASS * SPEEDLIGHT**2 * beta**2)) * ((ECHARGE**2)/(4 * np.pi * EPSILON0))**2
    natlog = (np.log((2 * EMASS * SPEEDLIGHT**2 * beta**2)/(EXCITEPOT * (1-beta**2)))-beta**2)
    return coefficient * electrondensity * natlog


def momentadecay(theta, beta):
    decaypoint = 0
    distance = sphericaldistance(theta)
    E = (MUMASS * SPEEDLIGHT**2)/np.sqrt(1 - beta**2)
    while True:
        if np.random.poisson(average * np.sqrt(1 - beta**2), 1)[0] > average * np.sqrt(1 - beta**2):
            break
        deltadistance = beta * SPEEDLIGHT * 1e-6
        if distance - deltadistance >= 0:
            E -= np.abs(bethefunction(distance, beta, theta) * deltadistance)
            if E <= (MUMASS * SPEEDLIGHT**2):
                E = 1.00001 * MUMASS * SPEEDLIGHT**2
            distance -= deltadistance
            beta = np.sqrt(1 - ((MUMASS * SPEEDLIGHT**2) / E)**2)
        else:
            distance -= deltadistance
        decaypoint += 1
    return decaypoint, E, distance


def posnormal(mean, sigma):
    Val = np.random.normal(mean, sigma, 1)
    return Val if Val > 0 else posnormal(mean, sigma)


def posnormalarray(mean, sigma, size):
    ValArray = []
    for ind in range(size):
        ValArray.append(posnormal(mean, sigma)[0])
    return np.array(ValArray)


def anglebounds(theta, difference, width):
    return [theta - np.arctan(width / difference), theta + np.arctan(width / difference)]


def sphericaldistance(theta):
    angleC = np.arcsin((ERADIUS * np.sin(np.pi - theta)) / (ERADIUS + avgheight))
    if theta == 0.0:
        return float(avgheight)
    return ((ERADIUS + avgheight) / (np.sin(np.pi - theta))) * np.sin(theta - angleC)


def secondaryprob(angle, detectorangle, d, w):
    return 1 - ((d * np.tan(np.abs(detectorangle - angle))) / w)


sphericaldistance = np.vectorize(sphericaldistance)
PhiValues = np.linspace(0, np.pi/2, 15)
counts = np.zeros(15)

energies = []
lengths = []
lifetimes = []
momenta = []

AngleSet = np.random.rand(momentatrials) * (np.pi / 2 - anglebounds(0, 0.9, 0.5)[0]) + anglebounds(0, 0.9, 0.5)[0]
DistanceSet = sphericaldistance(AngleSet)
MomentaSet = posnormalarray(1, 0.1, momentatrials) * 5.344E-19
EnergySet = np.sqrt(MomentaSet ** 2 * SPEEDLIGHT ** 2 + MUMASS ** 2 * SPEEDLIGHT ** 4)
BetaSet = np.sqrt(1 - ((MUMASS * SPEEDLIGHT ** 2) / EnergySet) ** 2)

for index in range(len(PhiValues)):
    LowBound, HighBound = anglebounds(PhiValues[index], 0.9, 0.5)
    CountSet = np.where(np.logical_and(AngleSet >= LowBound, AngleSet <= HighBound), 1, 0)
    CountSet = np.where(np.random.rand(len(CountSet)) <= secondaryprob(AngleSet, PhiValues[index], 0.9, 0.5),
                        CountSet, 0)
    for i in range(len(CountSet)):
        if CountSet[i] == 1:
            lifetime, energy, length = momentadecay(AngleSet[i], BetaSet[i])
            energies.append(energy)
            lengths.append(length)
            lifetimes.append(lifetime)
            if length <= 0:
                counts[index] += 1
    print('Angle {} Completed!'.format(PhiValues[index]))

energies = np.array(energies)
momenta = np.sqrt(energies ** 2 - MUMASS ** 2 * SPEEDLIGHT ** 4) / SPEEDLIGHT

plt.errorbar(PhiValues * 180 / np.pi, np.array(counts), yerr=np.sqrt(np.array(counts)), fmt='.')
plt.title('Muon Angle Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Angle [deg]')
plt.savefig('./MomentaTrialsAngles.png')
plt.show()

plt.hist(EnergySet * 6.242E9, bins=np.arange(7, 13, 0.01) * 0.1, density=True, label='Initial')
plt.hist(energies * 6.242E9, bins=np.arange(7, 13, 0.01) * 0.1, density=True, label='Final')
plt.title('Muon Energy Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Energy [GeV]')
plt.savefig("./MomentaTrialsEnergy.png")
plt.show()

plt.hist(MomentaSet, bins=np.arange(4, 6, 0.01) * 1e-19, density=True, label='Initial')
plt.hist(momenta, bins=np.arange(4, 6, 0.01) * 1e-19, density=True, label='Final')
plt.title('Muon Momenta Distribution')
plt.ylabel('Counts [1]')
plt.xlabel('Momentum [m/s]')
plt.savefig("./MomentaTrials.png")
plt.show()
