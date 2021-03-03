import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

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
momentatrials = 100000                            # unitless


# Functions
def intensityfit(theta, power, coeff):
    return coeff * (np.cos(theta)) ** power


def exponentialfit(moment, coeff, base, offset):
    return coeff * base ** (-1 * moment) + offset


def chi_squared(params, x, y, sigma, func):
    return np.sum(np.power((y-func(x, *params)), 2)/np.power(sigma, 2))


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
    energy = (MUMASS * SPEEDLIGHT**2)/np.sqrt(1 - beta**2)
    while True:
        if np.random.poisson(average * np.sqrt(1 - beta**2), 1)[0] > average * np.sqrt(1 - beta**2):
            break
        deltadistance = beta * SPEEDLIGHT * 1e-6
        if distance - deltadistance >= 0:
            energy -= np.abs(bethefunction(distance, beta, theta) * deltadistance)
            if energy <= (MUMASS * SPEEDLIGHT**2):
                energy = 1.00001 * MUMASS * SPEEDLIGHT**2
            distance -= deltadistance
            beta = np.sqrt(1 - ((MUMASS * SPEEDLIGHT**2) / energy)**2)
        else:
            distance -= deltadistance
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


def secondaryprob(angle, detectorangle, d, w):
    return 1 - ((d * np.tan(np.abs(detectorangle - angle))) / w)


def anglebounds(theta, difference, width):
    return [theta - np.arctan(width / difference), theta + np.arctan(width / difference)]


def sphericaldistance(theta):
    angleC = np.arcsin((ERADIUS * np.sin(np.pi - theta)) / (ERADIUS + avgheight))
    if theta == 0.0:
        return float(avgheight)
    return ((ERADIUS + avgheight) / (np.sin(np.pi - theta))) * np.sin(theta - angleC)


sphericaldistance = np.vectorize(sphericaldistance)
PhiValues = np.linspace(0, np.pi/2, 18)
MomentaValues = np.linspace(0.2, 5, 12)
    PhiTrials = np.linspace(0, np.pi/2, 1000)
    MomentaTrials = np.linspace(0.2, 5.0, 1000)

nps = []
nperrs = []

for jndex in range(len(MomentaValues)):
    counts = np.zeros(len(PhiValues))

    AngleSet = np.random.rand(momentatrials) * (np.pi / 2 - anglebounds(0, 0.9, 0.5)[0]) + anglebounds(0, 0.9, 0.5)[0]
    DistanceSet = sphericaldistance(AngleSet)
    MomentaSet = posnormalarray(MomentaValues[jndex], 0.1, momentatrials) * 5.344E-19
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
                if length <= 0:
                    counts[index] += 1
    print('Momentum {} Completed!'.format(jndex))

    errors = np.where(np.sqrt(counts) == 0, 1, np.sqrt(counts))

    POpt, PCoV = cf(intensityfit, PhiValues, counts, sigma=errors, p0=[3, 1000])
    nps.append(POpt[0])
    nperrs.append(np.sqrt(np.diag(PCoV * (len(PhiValues) - len(POpt)) / chi_squared(POpt, PhiValues, counts,
                                                                                    errors, intensityfit)))[0])

    plt.errorbar(PhiValues, counts, yerr=errors, fmt='.')
    plt.plot(PhiTrials, intensityfit(PhiTrials, *POpt))
    plt.savefig('./Momenta{}Trial.png'.format(jndex))
    plt.show()

nps = np.array(nps)
nperrs = np.array(nperrs)

plt.errorbar(MomentaValues, nps, yerr=nperrs, fmt='.')
plt.savefig('./RyanTrials.png')
plt.show()

POpt, PCoV = cf(exponentialfit, MomentaValues, nps, sigma=nperrs, p0=[1, 3, 0.1])
PErr = np.sqrt(np.diag(PCoV * (len(MomentaValues) - len(POpt)) / chi_squared(POpt, MomentaValues, nps,
                                                                             nperrs, exponentialfit)))

plt.errorbar(MomentaValues, nps, yerr=nperrs, fmt='.')
plt.plot(MomentaTrials, exponentialfit(MomentaTrials, *POpt))
plt.savefig('./RyanTrialsFit.png')
plt.show()

np.savetxt('./RyanResults.txt', [nps, nperrs])
print(nps)
print(nperrs)
print(POpt)
print(PErr)
