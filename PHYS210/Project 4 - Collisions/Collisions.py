# Physics 210: Collisions Project                               Ryan Kaufmann
# Bonus: Added a trajectory line to the first particle in the xy_list in order
# To make the particle collisions easier to notice
# Importing all necessary libraries, packages, and functions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from itertools import combinations
from scipy.optimize import curve_fit

# Initialize and define all necessary constants and limits for the program to
# Run including frame limits, physical constants, and boudary values
npoints = 400
nframe = 10000
xmax, ymax, xmin, ymin = 1, 1, 0, 0
fig, ax = plt.subplots()
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
tStep = 0.00001
particleRadius = 0.00001
particleMass = 2.672*10**(-26)
sizes = np.array([10])
Boltzmann = 1.38064852*10**(-23)

# Creates each particle's color, initial velocity, and initial position
# (position is random, velocity and color are based on which half the particle
# Begins in: red on right, blue on left)
xy_list = np.random.random((npoints, 2))
velocity_list = np.append(-500*np.ones((npoints, 1)),
                          np.zeros((npoints, 1)), axis=1)
velocity_list[np.where(xy_list[:, 0] <= 0.5), 0] *= -1
particle1pos = xy_list[0, :]
colors = np.ones((npoints, 3))
colors[np.where(xy_list[:, 0] <= 0.5)] = np.array([0, 0, 1])
colors[np.where(xy_list[:, 0] > 0.5)] = np.array([1, 0, 0])


# Template for the Maxwell-Boltzmann Distributions that takes in a temperature
# And velocity for and calculates the distribution of the velocities
# Temperature that is used is fitted for a value
def MBDistribution(velocity, temperature):
    MBDist = (particleMass*velocity)/(Boltzmann*temperature)
    MBDist *= np.exp(-1/2*particleMass*velocity**2/(Boltzmann*temperature))
    return MBDist


# Template for the Boltzmann Distribution that take a velocity and temperature
# And calculates the distribution of the kinetic energies of the particles
def BDistribution(energy, temperature):
    BDist = 1/(Boltzmann*temperature)
    BDist *= np.exp(-energy/(Boltzmann*temperature))
    return BDist


# Finds which particles are currently in a collision and adjusts the speeds of
# The particles according to an equation for elastic collisions
def Collisions(distances):
    global velocity_list
    # Finds the particles that are in a collision
    select = np.where(np.less_equal(distances, 2*particleRadius))
    # Checks if there are any of such particles
    if select[0].size:
        # Gets the distance between the particles, and the velocity and
        # Position of each
        distance = distances[select]
        indices = np.asarray(list(combinations(list(range(400)), 2)))
        indices = indices[select]
        pos1 = xy_list[indices[:, 0], :]
        pos2 = xy_list[indices[:, 1], :]
        vel1 = velocity_list[indices[:, 0], :]
        vel2 = velocity_list[indices[:, 1], :]
        # Goes through each pair of collisions and changes the velocity of both
        # According to the elastic collision equations
        for indx in range(distance.shape[0]):
            posdif1 = pos1[indx, :]-pos2[indx, :]
            posdif2 = pos2[indx, :]-pos1[indx, :]
            veldif1 = vel1[indx, :]-vel2[indx, :]
            veldif2 = vel2[indx, :]-vel1[indx, :]
            newvel1 = -(np.dot(veldif1, posdif1)/distance[indx])*(posdif1)
            newvel1 += vel1[indx, :]
            velocity_list[indices[indx, 0], :] = newvel1
            newvel2 = -(np.dot(veldif2, posdif2)/distance[indx])*(posdif2)
            newvel2 += vel2[indx, :]
            velocity_list[indices[indx, 1], :] = newvel2


# Update function for the animation, calculates the new positions and 
# Velocities of each particles
def update_point(num):
    global xy_list, velocity_list, particle1pos

    # Checking if the particle would go outside of the bounds of the problem
    dx = tStep*velocity_list[:, 0]
    dy = tStep*velocity_list[:, 1]
    xOutLims = np.where(np.logical_or(np.greater(xy_list[:, 0]+dx, xmax),
                                      np.less(xy_list[:, 0]+dx, xmin)))
    yOutLims = np.where(np.logical_or(np.greater(xy_list[:, 1]+dy, ymax),
                                      np.less(xy_list[:, 1]+dy, ymin)))
    # And adjusts the speeds as necessary
    velocity_list[xOutLims, 0] *= -1
    velocity_list[yOutLims, 1] *= -1

    # Creates the necessary distance in a combination to be checked in
    # Collisions function
    xCompare = np.asarray(list(combinations(xy_list[:, 0], 2)))
    yCompare = np.asarray(list(combinations(xy_list[:, 1], 2)))
    distCompare = (xCompare[:, 0]-xCompare[:, 1])**2
    distCompare += (yCompare[:, 0]-yCompare[:, 1])**2
    Collisions(distCompare)

    # Calculates the new position according to the velocity
    dx = tStep*velocity_list[:, 0]
    dy = tStep*velocity_list[:, 1]
    xy_list[:, 0] = xy_list[:, 0]+dx
    xy_list[:, 1] = xy_list[:, 1]+dy

    # Appends particle 1 position onto list of particle 1 positions then graphs
    particle1pos = np.vstack((particle1pos, xy_list[0, :]))
    particle1line.set_data(particle1pos[-50:, 0], particle1pos[-50:, 1])
    im.set_offsets(xy_list)

# Creates initial graphs to be updated in the animation code
particle1line, = ax.plot(particle1pos[0], particle1pos[1], c='g', zorder=100)
im = ax.scatter(xy_list[:, 0], xy_list[:, 1], zorder=0, linewidths=0)
im.set_sizes(sizes)
im.set_facecolor(colors)

# Runs and saves the animation
animation = anim.FuncAnimation(fig, update_point, frames=nframe, interval=1,
                               repeat=False)
plt.show()
#animation.save('collisions.mp4')

# Creates new plots for the histograms that are fitted with scipy's curve fit
# Then saves the plots and shows them
fig, (ax1, ax2) = plt.subplots(2)
n, bins, patch = ax1.hist(np.sqrt(velocity_list[:, 0]**2 +
                                  velocity_list[:, 1]**2),
                          bins=50, normed=True, zorder=0)
bin_centers = bins[:-1]+0.5*(bins[1:]-bins[:-1])
popt, pvoc = curve_fit(MBDistribution, bin_centers, n, p0=[100])
ax1.plot(bin_centers, MBDistribution(bin_centers, *popt), 'r--', zorder=10)
n, bins, patch = ax2.hist(1/2*particleMass*(velocity_list[:, 0]**2 +
                                            velocity_list[:, 1]**2),
                          bins=50, normed=True, zorder=0)
bin_centers = bins[:-1]+0.5*(bins[1:]-bins[:-1])
ax2.plot(bin_centers, BDistribution(bin_centers, *popt), 'r--', zorder=10)
plt.savefig('distributions.pdf')
plt.show()

# Writes the temperature received from the fit to a file
file = open('collisions.txt', 'w')
file.write('The temperature of the system is approximately {}K'.format(*popt))
file.close()