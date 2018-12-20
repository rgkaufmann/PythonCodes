import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

###############################################################################

#Function in the form f(x)=a where a is constant
def Constant(x, Amp):
    return Amp*np.ones(len(x))

#Function in the form f(x)=a*x+b, where a, b are constant
def Linear(x, Amp, Cons):
    return Amp*x+Cons

#Function in the form f(x)=a*(x+b)^p+c where a, b, c, p are constant
def Power(x, Amp, Shift, Cons, Power):
    return Amp*(x+Shift)**Power+Cons

#Function in the form f(x)=a*ln(x+b)+c where a, b, c are constant
def Logarithm(x, Amp, Shift, Cons):
    return Amp*np.log(x+Shift)+Cons

#Function in the form f(x)=a*d^(x+b)+c where a, b, c, d are constant
def Exponential(x, Amp, Base, Shift, Cons):
    return Amp*Base**(x+Shift)+Cons

#Function in the form f(x)=a*sin(x+b)+c where a, b, c are constant
def Sine(x, Amp, Shift, Cons):
    return Amp*np.sin(x+Shift)+Cons

###############################################################################
    
#Function used to create noise in the data set
def Noise(data):
    return data*(0.75*np.ones(len(data))+np.random.rand(len(data))/2)

###############################################################################

zeroPointStart = 9*np.random.rand()

xrange = np.linspace(-10, 10, num=1000)
constantData = Noise(Constant(xrange, 9*np.random.rand()))
linearData = Noise(Linear(xrange, 10*np.random.rand()-5,
                          18*np.random.rand()-9))
squareData = Noise(Power(xrange, 10*np.random.rand()-5, 18*np.random.rand()-9,
                         200*np.random.rand()-100, 2))
cubeData = Noise(Power(xrange, 10*np.random.rand()-5, 18*np.random.rand()-9,
                       2000*np.random.rand()-1000, 3))
squarerootData = Noise(Power(xrange[np.where(xrange>-zeroPointStart)],
                             10*np.random.rand()-5, zeroPointStart,
                             10*np.random.rand()-5, 1/2))
cuberootData = Noise(Power(xrange[np.where(xrange>-zeroPointStart)],
                           10*np.random.rand()-5, zeroPointStart,
                           10*np.random.rand()-5, 1/3))
reciprocalData = Noise(Power(xrange[np.where(xrange!=-zeroPointStart)], 
                              10*np.random.rand()-5, zeroPointStart,
                              10*np.random.rand()-5, -1))
logarithmData = Noise(Logarithm(xrange[np.where(xrange>-zeroPointStart)],
                          10*np.random.rand()-5, zeroPointStart,
                          10*np.random.rand()-5))
base2expData = Noise(Exponential(xrange, 10*np.random.rand()-5, 2,
                                 10*np.random.rand()-5,
                                 2000*np.random.rand()-1000))
baseeexpData = Noise(Exponential(xrange, 10*np.random.rand()-5, np.exp(1),
                                 18*np.random.rand()-9,
                                 20000*np.random.rand()-10000))
sineData = Noise(Sine(xrange, 10*np.random.rand()-5,
                      4*np.pi*np.random.rand()-2*np.pi, np.random.rand()))

###############################################################################

plt.plot(xrange, constantData)
plt.title('Constant')
plt.ylim((-10, 10))
plt.show()

plt.plot(xrange, linearData)
plt.title('Linear')
plt.show()

plt.plot(xrange, squareData)
plt.title('Square')
plt.show()

plt.plot(xrange, cubeData)
plt.title('Cube')
plt.show()

plt.plot(xrange[np.where(xrange>-zeroPointStart)], squarerootData)
plt.title('Square Root')
plt.show()

plt.plot(xrange[np.where(xrange>-zeroPointStart)], cuberootData)
plt.title('Cube Root')
plt.show()

plt.plot(xrange[np.where(xrange!=-zeroPointStart)], reciprocalData)
plt.title('Reciprocal')
plt.show()

plt.plot(xrange[np.where(xrange>-zeroPointStart)], logarithmData)
plt.title('Logarithm')
plt.show()

plt.plot(xrange, base2expData)
plt.title('Base 2 Exponential')
plt.show()

plt.plot(xrange, baseeexpData)
plt.title('Base e Exponential')
plt.show()

plt.plot(xrange, sineData)
plt.title('Sine')
plt.show()

###############################################################################

poptCon, pcovCon = cf(Constant, xrange, constantData, p0=[5])
plt.scatter(xrange, constantData)
plt.plot(xrange, Constant(xrange, *poptCon), c='r')
plt.ylim((-10, 10))
plt.show()

poptLin, pcovLin = cf(Linear, xrange, linearData, p0=[5, 2])
plt.scatter(xrange, linearData)
plt.plot(xrange, Linear(xrange, *poptLin), c='r')
plt.show()

#poptSqu, pcovSqu = cf(Power, xrange, squareData, p0=[5, 2, 100, 2], maxfev=10000)
#plt.scatter(xrange, squareData)
#plt.plot(xrange, Power(xrange, *poptSqu), c='r')
#plt.show()

#poptCub, pcovCub = cf(Power, xrange, cubeData, p0=[5, 2, 1000, 3], maxfev=10000)
#plt.scatter(xrange, cubeData)
#plt.plot(xrange, Power(xrange, *poptCub), c='r')
#plt.show()

#poptRoo, pcovRoo = cf(Power, xrange[np.where(xrange>-zeroPointStart)], squarerootData, p0=[2, 5, 2, 1/2], maxfev=10000)
#plt.scatter(xrange[np.where(xrange>-zeroPointStart)], squarerootData)
#plt.plot(xrange[np.where(xrange>-zeroPointStart)], Power(xrange[np.where(xrange>-zeroPointStart)], *poptRoo), c='r')
#plt.show()

#poptCro, pcovCro = cf(Power, xrange[np.where(xrange>-zeroPointStart)], cuberootData, p0=[2, 5, 2, 1/3], maxfev=10000)
#plt.scatter(xrange[np.where(xrange>-zeroPointStart)], cuberootData)
#plt.plot(xrange[np.where(xrange>-zeroPointStart)], Power(xrange[np.where(xrange>-zeroPointStart)], *poptCro), c='r')
#plt.show()

#poptRec, pcovRec = cf(Power, xrange[np.where(xrange!=-zeroPointStart)], reciprocalData, p0=[2, 5, 2, -1], maxfev=10000)
#plt.scatter(xrange[np.where(xrange!=-zeroPointStart)], reciprocalData)
#plt.plot(xrange[np.where(xrange!=-zeroPointStart)], Power(xrange[np.where(xrange!=-zeroPointStart)], *poptRec), c='r')
#plt.show()

#poptLog, pcovLog = cf(Logarithm, xrange[np.where(xrange>-zeroPointStart)], logarithmData, p0=[2, 5, 2], maxfev=10000)
#plt.scatter(xrange[np.where(xrange>-zeroPointStart)], logarithmData)
#plt.plot(xrange[np.where(xrange>-zeroPointStart)], Logarithm(xrange[np.where(xrange>-zeroPointStart)], *poptLog), c='r')
#plt.show()

poptEx2, pcovEx2 = cf(Exponential, xrange, base2expData, p0=[2, 2, 2, 500], maxfev=10000)
plt.scatter(xrange, base2expData)
plt.plot(xrange, Exponential(xrange, *poptEx2), c='r')
plt.show()

poptExe, pcovExe = cf(Exponential, xrange, baseeexpData, p0=[2, np.exp(1), 2, 500], maxfev=10000)
plt.scatter(xrange, baseeexpData)
plt.plot(xrange, Exponential(xrange, *poptExe), c='r')
plt.show()

poptSin, pcovSin = cf(Sine, xrange, sineData, p0=[2, np.pi/2, 0.5], maxfev=10000)
plt.scatter(xrange, sineData)
plt.plot(xrange, Sine(xrange, *poptSin), c='r')
plt.show()