import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from itertools import combinations
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D

npoints = 400
nframe = 10000
xmax, ymax, zmax, xmin, ymin, zmin = 0.5, 0.5, 0.5, 0, 0, 0
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_zlim(zmin, zmax)
tStep = 0.00002
particleRadius = 0.001
particleMass = 2.672*10**(-26)
sizes = np.array([10])
Boltzmann = 1.38064852*10**(-23)

xyz_list = np.random.random((npoints, 3))*0.5
velocity_list = np.append(np.append(-500*np.ones((npoints, 1)),
                                    np.zeros((npoints, 1)), axis=1),
                          np.zeros((npoints, 1)), axis=1)
velocity_list[np.where(xyz_list[:, 0] <= 0.25), 0] *= -1
particle1pos = xyz_list[0, :]
colors = np.ones((npoints, 3))
colors[np.where(xyz_list[:, 0] <= 0.25), :] = np.array([0, 0, 1])
colors[np.where(xyz_list[:, 0] > 0.25), :] = np.array([1, 0, 0])


def MBDistribution(velocity, temperature):
    MBDist = (particleMass*velocity)/(Boltzmann*temperature)
    MBDist *= np.exp(-1/2*particleMass*velocity**2/(Boltzmann*temperature))
    return MBDist


def BDistribution(energy, temperature):
    BDist = 1/(Boltzmann*temperature)
    BDist *= np.exp(-energy/(Boltzmann*temperature))
    return BDist


def Collisions(distances):
    global velocity_list
    select = np.where(np.less_equal(distances, 2*particleRadius))
    if select[0].size:
        distance = distances[select]
        indices = np.asarray(list(combinations(list(range(400)), 2)))
        indices = indices[select]
        pos1 = xyz_list[indices[:, 0], :]
        pos2 = xyz_list[indices[:, 1], :]
        vel1 = velocity_list[indices[:, 0], :]
        vel2 = velocity_list[indices[:, 1], :]
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


def update_point(num):
    global xyz_list, velocity_list, particle1pos, particle2pos, particle3pos

    xOutLims = np.where(np.logical_or(np.greater(xyz_list[:, 0], xmax),
                                      np.less(xyz_list[:, 0], xmin)))
    yOutLims = np.where(np.logical_or(np.greater(xyz_list[:, 1], ymax),
                                      np.less(xyz_list[:, 1], ymin)))
    zOutLims = np.where(np.logical_or(np.greater(xyz_list[:, 2], zmax),
                                      np.less(xyz_list[:, 2], zmin)))
    velocity_list[xOutLims, 0] *= -1
    velocity_list[yOutLims, 1] *= -1
    velocity_list[zOutLims, 2] *= -1

    xCompare = np.asarray(list(combinations(xyz_list[:, 0], 2)))
    yCompare = np.asarray(list(combinations(xyz_list[:, 1], 2)))
    zCompare = np.asarray(list(combinations(xyz_list[:, 2], 2)))
    distCompare = (xCompare[:, 0]-xCompare[:, 1])**2
    distCompare += (yCompare[:, 0]-yCompare[:, 1])**2
    distCompare += (zCompare[:, 0]-zCompare[:, 1])**2
    Collisions(distCompare)

    dx = tStep*velocity_list[:, 0]
    dy = tStep*velocity_list[:, 1]
    dz = tStep*velocity_list[:, 2]
    xyz_list[:, 0] = xyz_list[:, 0]+dx
    xyz_list[:, 1] = xyz_list[:, 1]+dy
    xyz_list[:, 2] = xyz_list[:, 2]+dz

    particle1pos = np.vstack((particle1pos, xyz_list[0, :]))

    for line in particle1lines:
        line[0].set_data(particle1pos[-50:, 0], particle1pos[-50:, 1])
        line[0].set_3d_properties(particle1pos[-50:, 2])
    for image, xyzcombo in zip(images, xyz_list):
        image.set_offsets(xyzcombo[0:2])
        image.set_3d_properties(xyzcombo[2], zdir='z')


particle1lines = [ax.plot([particle1pos[0]], [particle1pos[1]],
                          [particle1pos[2]])]
images = [ax.scatter([xyzcombo[0]], [xyzcombo[1]], [xyzcombo[2]], s=100,
                     zorder=0) for xyzcombo in xyz_list]
for image, indx in zip(images, range(npoints)):
    image.set_color(colors[indx, :])

animation = anim.FuncAnimation(fig, update_point, frames=nframe, interval=1,
                               repeat=False)
plt.show()
#animation.save('collisions.mp4')

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

file = open('collisions.txt', 'w')
file.write('The temperature of the system is approximately {}K'.format(*popt))
file.close()