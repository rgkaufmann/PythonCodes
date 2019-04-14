import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

TIDAL = 0.29                      # Unitless tidal love number
OBLATE = 12.0                     # Unitless oblateness constant
GRAV = 6.674e-20                  # G in km^3/(kg*s^2)
TMASS = 5.9721986e24+7.3459e22    # Earth's mass in kg
EMRAD = 6371.008                  # Semi-major axis of Moon in km
MMASS = 7.3459e22                 # Moon's mass in kg
STOGYR = 3.154e16                 # Convert inverse seconds to inverse Gyr
B = (3*(TIDAL/OBLATE))*(np.sqrt(GRAV/TMASS)*(EMRAD**5*MMASS))*STOGYR            # B in km^(13/2)/Gyr


def differential(distance):
    return B*(distance**(-11.0/2.0))        # km/Gyr


def timeindependenteulermethod(initialconditions, step, finaldistance):
    numericalanalysis = [initialconditions]                # Initial conditions in [Step Number, Current Distance, Time]
    while numericalanalysis[-1][1] > finaldistance:
        nextdistance = numericalanalysis[-1][1] - step*differential(numericalanalysis[-1][1])
        numericalanalysis.append([numericalanalysis[-1][0] + 1, nextdistance, (numericalanalysis[-1][2]) - step])
    return numericalanalysis


timestep = 0.1
final = 2.5*EMRAD
initials = [0, 60.0*EMRAD, 0]
approx = timeindependenteulermethod(initials, timestep, final)

while np.abs(approx[-1][2]+1.6) > 0.05:
    timestep = timestep/2
    approx = timeindependenteulermethod(initials, timestep, final)
print approx[-2]

title = "Numerical Approximation of the Reduction of\nthe Moon's Semi-Major Axis With Step Size of {}Gyr"
approx = np.transpose(approx)
plt.plot(approx[2, :], approx[1, :])
plt.title(title.format(timestep), fontsize=36)
plt.xlabel("Time From Present in Gigayears", fontsize=24)
plt.ylabel("Moon Semi-Major Axis in kilometers", fontsize=24)
plt.vlines(-1.5, 0, 61.0*EMRAD)
plt.hlines(40.0*EMRAD, -1.7, 0)
plt.xlim(xmin=-1.7, xmax=0)
plt.ylim(ymin=0, ymax=61.0*EMRAD)
plt.show()


def qvariation(time, power):
    return 12.0*(1-time)**power


def bconstant(time, power):
    return (3*(TIDAL/qvariation(time, power)))*(np.sqrt(GRAV/TMASS)*(EMRAD**5*MMASS))*STOGYR


def seconddifferential(distance, time, power):
    return bconstant(time, power)*(distance**(-11.0/2.0))


def timedependenteulermethod(initialconditions, step, finaltime, power):
    numericalanalysis = [initialconditions]                # Initial conditions in [Step Number, Current Distance, Time]
    while numericalanalysis[-1][2] > -finaltime:
        nextdistance = numericalanalysis[-1][1] - step*seconddifferential(numericalanalysis[-1][1],
                                                                          numericalanalysis[-1][2],
                                                                          power)
        numericalanalysis.append([numericalanalysis[-1][0] + 1, nextdistance, (numericalanalysis[-1][2]) - step])
    return numericalanalysis


final = 4.4
powerZ = 1.0
adjustment = 1.0
counter = 0
constqapprox = approx
approx = timedependenteulermethod(initials, timestep, final, powerZ)
while (np.abs(approx[-1][1]-2.5*EMRAD) > 0.025*EMRAD) or np.isnan(approx[-1][1]):
    adjustment /= 2
    if ((approx[-1][1]-2.5*EMRAD) < 0) or np.isnan(approx[-1][1]):
        powerZ += adjustment
    else:
        powerZ -= adjustment
    approx = timedependenteulermethod(initials, timestep, final, powerZ)
    print powerZ
print approx[-2]

title = "Numerical Approximation of the Reduction of the Moon's Semi-Major\nAxis With Step Size of {}Gyr"
title += " and Oblateness Power {}"
approx = np.transpose(approx)
plt.plot(approx[2, :], approx[1, :], label='Time Dependent Q Value')
plt.plot(constqapprox[2, :], constqapprox[1, :], label='Constant Q Value')
plt.vlines(-4.4, 0, 61.0*EMRAD)
plt.title(title.format(timestep, powerZ), fontsize=36)
plt.xlabel("Time From Present in Gigayears", fontsize=24)
plt.ylabel("Moon Semi-Major Axis in kilometers", fontsize=24)
plt.ylim(ymin=0, ymax=61.0*EMRAD)
plt.legend(loc='best')
plt.show()

print(qvariation(-4.4, powerZ))
