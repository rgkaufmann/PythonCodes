import numpy as np
import matplotlib.pyplot as plt

inclination = 2.44996247*np.pi/180              # # radians
perihelion = 42.37733279                        # # AU
aphelion = 46.88190499                          # # AU
semimajorau = 44.62961889                       # # AU
semimajorkm = 6676495970                        # # AU
periodyr = 298.1600                             # # Years
perioddy = 108901.3326                          # # Days
periheliondate = 2473447.5403                   # # Julian Days
argumentperihelion = 181.14813924539*np.pi/180  # # radians
ascendingnode = 159.04395317345*np.pi/180       # # radians
meananomaly = 310.91947579009*np.pi/180         # # radians
eccentricity = (aphelion/semimajorau)-1         # # radians
meanmotion = 2*np.pi/perioddy                   # # radians per day
April272019 = 2458600.500000                    # # Julian Days
Jan12019 = 2458484.731250                       # # Julian Days
meananom = meananomaly+meanmotion*(Jan12019-April272019)

def keplers(mean, eccentric):
    return eccentric-eccentricity*np.sin(eccentric)-mean


def keplersderivative(eccentric):
    return 1-eccentricity*np.cos(eccentric)


def newtonmethod(interactions, testinitial):
    while interactions[-1][2] > 1.0e-20:
        newtest = testinitial - keplers(meananom,
                  testinitial) / keplersderivative(testinitial)
        interactions.append([interactions[-1][0] + 1,
                             newtest, np.abs(newtest - testinitial)])
        testinitial = newtest
    return interactions


eccentricanomaly = newtonmethod([[0, meananom, 1000.0]], meananom)[-1][1]
xprime = semimajorau*(np.cos(eccentricanomaly)-eccentricity)
yprime = semimajorau*np.sqrt(1-eccentricity**2.0)*np.sin(eccentricanomaly)

print eccentricity
print meananom
print eccentricanomaly
print "{:.25f}".format(xprime)
print "{:.25f}".format(yprime)

xecliptic = (np.cos(argumentperihelion)*np.cos(ascendingnode)-
             np.sin(argumentperihelion)*np.sin(ascendingnode)*
             np.cos(inclination))*xprime+\
            (-np.sin(argumentperihelion)*np.cos(ascendingnode)-
             np.cos(argumentperihelion)*np.sin(ascendingnode)*
             np.cos(inclination))*yprime
yecliptic = (np.cos(argumentperihelion)*np.sin(ascendingnode)+
             np.sin(argumentperihelion)*np.cos(ascendingnode)*
             np.cos(inclination))*xprime+\
            (-np.sin(argumentperihelion)*np.sin(ascendingnode)+
             np.cos(argumentperihelion)*np.cos(ascendingnode)*
             np.cos(inclination))*yprime
zecliptic = (np.sin(argumentperihelion)*np.sin(inclination))*xprime+\
            (np.cos(argumentperihelion)*np.sin(inclination))*yprime

print xecliptic
print yecliptic
print zecliptic
print "{:.25f}".format(np.sqrt(xecliptic**2.0+yecliptic**2.0+zecliptic**2.0))
print "{:.25f}".format(np.sqrt(xprime**2.0+yprime**2.0))

costrueanom = (np.cos(eccentricanomaly)-eccentricity)/\
              (1-eccentricity*np.cos(eccentricanomaly))
radiuspolar = (semimajorau*(1-eccentricity**2.0))/(1+eccentricity*costrueanom)
print costrueanom
print "{:.25f}".format(radiuspolar)
