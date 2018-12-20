# PHYS 210 - Project 2 - The Ising Model                    Ryan Kaufmann
# Bonus: Add a second animation showing the individual spins of each electron
# In each of the desired temperatures (0.1K, 2.5K, 100K)
import numpy as np                   # Importing all important function, numpy
import matplotlib.pyplot as plt      # for arrays, plt for plotting, anim for
import matplotlib.animation as anim  # animations, warnings to clear warnings
import warnings                      # and sys to increase recursion limit
import cProfile, pstats, io
import sys

warnings.simplefilter(action='ignore', category=UserWarning)  # Ignores warning
plt.rcParams['animation.ffmpeg_path']='C:/Users/ryank/Downloads/ffmpeg-20171102-d5995c5-win64-static/bin/ffmpeg.exe'
# When using the MovieWriter in the animation saving
plt.rcParams['image.cmap'] = 'Paired'
pr2 = cProfile.Profile()

pr2.enable()
# Declaring all variables used in the program and increases recursion limit
sys.setrecursionlimit(4000)
SigmaSpins = np.random.choice((-1, 1), (50, 50))
Zeros = np.zeros((50, 50))
Temperatures = np.array([0.01, 0.1, 1, 2, 2.5, 3, 4, 5, 10, 100])
SpinDataTemp001 = [SigmaSpins]
SpinDataTemp025 = [SigmaSpins]
SpinDataTemp100 = [SigmaSpins]


# Convergence calculates the electron spin configuration that the original
# configuration reaches after 600000 iterations. It takes an original state
# the current iteration of recusion, and the temperature of the system

def Convergence(sigma, count, temperature):
    for indx in range(500):
        # For loop calculates a random coordinate on the configuration
        # Then calculates the energy difference between the original state
        # And the new state (Derivation at bottom)
        coors = np.random.randint(-1, 49, 2)
        Energydif = (sigma[(coors[0]+1), coors[1]] +
                     sigma[coors[0]-1, coors[1]] +
                     sigma[coors[0], (coors[1]+1)] +
                     sigma[coors[0], coors[1]-1])
        Energydif = -2*sigma[coors[0], coors[1]]*Energydif
        # Finally find whether or not the electron spin should be switched
        # And switches it or not. If the probability needs to be calculated,
        # It is compared to a random number and determined to be switched
        if Energydif >= 0:
            sigma[coors[0], coors[1]] = -1*sigma[coors[0], coors[1]]
        else:
            probability = np.exp(Energydif/temperature)
            if np.random.random() < probability:
                sigma[coors[0], coors[1]] = -1*sigma[coors[0], coors[1]]
    # After 500 iterations, it checks if it has been 1000 iterations since the
    # Last recording of a electron spin. If it has been 1000 iterations, it
    # Records it to be used with the animation segment.
    if temperature == 0.1:
        global SpinDataTemp001
        SpinDataTemp001.append(sigma.tolist())
    elif temperature == 2.5:
        global SpinDataTemp025
        SpinDataTemp025.append(sigma.tolist())
    elif temperature == 100:
        global SpinDataTemp100
        SpinDataTemp100.append(sigma.tolist())
    # Then it decides if it should be through another iteration or returned
    if count >= 1199:
        return sigma
    else:
        return Convergence(sigma, count+1, temperature)


# ConvergenceSet goes through a set of spin configurations and gets the
# Magnetic moment for each using the same temperature. It adds them
# To one array and then returns the complete array
def ConvergenceSet(setsigmaspins, temperature):
    if setsigmaspins.size == SigmaSpins.size:
        return np.sum(Convergence(setsigmaspins[:, :, 0], 0, temperature))
    else:
        return np.append(np.sum(Convergence(setsigmaspins[:, :, 0],
                                            0, temperature)),
                         ConvergenceSet(setsigmaspins[:, :, 1:], temperature))


# TemperatureSet goes through a set of temperatures and gets five magnetic
# Moments for each using each temperature. It then adds them to one
# Array and then returns the complete array.
def TemperatureSet(temperatureset):
    FiveTimesSigmaSpins = np.repeat(SigmaSpins[:, :, np.newaxis], 5, axis=2)
    if temperatureset.size == 1:
        return ConvergenceSet(FiveTimesSigmaSpins,
                              temperatureset[0])[:, np.newaxis]
    else:
        return np.append(ConvergenceSet(FiveTimesSigmaSpins,
                                        temperatureset[0])[:, np.newaxis],
                         TemperatureSet(temperatureset[1:]),
                         axis=1)


# UpdateHeat replaces the data in the heat map with a 'newer' data set
def updateHeat(num, spins):
    Heat.set_data(spins[num])


# UpdateQuiver replaces the data in the vector field with a 'newer' data set
def updateQuiver(num, spins):
    Color = np.arctan2(Zeros, spins[num])
    Quiver.set_UVC(Zeros, spins[num], Color)


# Animate takes in various parameters to construct a figure and form the
# Animation. Then it saves the animation to a file.
def Animate(Temp, File, Type, SpinData):
    fig = plt.figure()
    fig.suptitle('Electron Spins at {}K'.format(Temp))
    if Type == 'Heat':
        global Heat
        Heat = plt.imshow(SigmaSpins, cmap='inferno')
        animation = anim.FuncAnimation(fig, updateHeat, frames=1200,
                                       repeat=False, fargs=(SpinData, ))
        animation.save(File, fps=20)
    elif Type == 'Quiver':
        global Quiver
        Quiver = plt.quiver(Zeros, SigmaSpins, np.arctan2(Zeros, SigmaSpins),
                            pivot='middle')
        animation = anim.FuncAnimation(fig, updateQuiver, frames=1200,
                                       repeat=False, fargs=(SpinData, ))
        animation.save(File, fps=20)


# Gathers data on the convergence configurations given initial spin
MagMoments = TemperatureSet(Temperatures).transpose()
MaxMagMoments = np.amax(np.abs(MagMoments), axis=1)

# Constructs the plot for the magnetic moments versus the temperature
title = 'Magnetic Moment Against Temperature'
title = title + ' As Calculated by the Ising Model'
plt.semilogx(Temperatures, MaxMagMoments)
plt.title(title)
plt.xlabel('Temp (K)')
plt.ylabel('Magnetic Moment')
plt.savefig('Tcurie.pdf')

# Animates each of the required temperatures using both Heat and Quiver funcs
Animate(0.1, 'temp_0.1.mp4', 'Heat', SpinDataTemp001)
Animate(0.1, 'temp_0.1Quiver.mp4', 'Quiver', SpinDataTemp001)
Animate(2.5, 'temp_2.5.mp4', 'Heat', SpinDataTemp025)
Animate(2.5, 'temp_2.5Quiver.mp4', 'Quiver', SpinDataTemp025)
Animate(100, 'temp_100.mp4', 'Heat', SpinDataTemp100)
Animate(100, 'temp_100Quiver.mp4', 'Quiver', SpinDataTemp100)

pr2.disable()
file = open('FullIsingStats.txt', 'w')
s = io.StringIO()
sortby = 'tottime'
ps = pstats.Stats(pr2, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()