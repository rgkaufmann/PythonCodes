import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as ode

#Set up our equations that output our differential equations
#Make sure to keep track of what each part of your input vector is
def NewtonsSecond(vector, time, k, m):   #[xVel, yVel, zVel, xPos, yPos, zPos]
    xvel = vector[0]
    yvel = vector[1]
    zvel = vector[2]
    xpos = vector[3]
    ypos = vector[4]
    zpos = vector[5]
    #Returns vectors of form [xAcc, yAcc, zAcc, xVel, yVel, zVel]
    return [-k/m*xpos, -k/m*ypos, -k/m*zpos, xvel, yvel, zvel]

#Intakes a vector of [Density, Mass, Pressure]
def NeutronStar(vector, time, c, G):
    density = vector[0]
    mass = vector[1]
    #Returns vectors of form [dD/dr, dM/dr, dP/dr]
    return [0, 4*np.pi*time**2*density/(c*2), -G*mass*density/(time*c)**2]

#Intakes a vector of [xVel, yVel, xPos, yPos]
def Ballistics(Vector, Time):
    xvelocity = Vector[0]
    yvelocity = Vector[1]
    #Returns vectors of form [xAcc, yAcc, xVel, yVel]
    return [-drag/mass*xvelocity, -GRAVITY-drag/mass*yvelocity,
            xvelocity, yvelocity]

# Define all constants used in the above functions
drag = 25*np.random.rand()      #None
mass = 100*np.random.rand()     #kg
k = 25*np.random.rand()         #N/m
c = 10*np.random.rand()         #None
G = 6.674e-11                   #N*m^2/kg^2
GRAVITY = 9.8                   #m/s^2

#Define our time array and any initial values
t = np.linspace(1, 5, 200)
NewtonInitials = [10, 10, 10, 10, 10, 10]*np.random.rand(6) #m/s and m
NeutronInitials = [10e10, 0, 5]*np.random.rand(3)           #kg/m^3, kg, Pa
BallisticsInitials = [10, 10, 0, 0]*np.random.rand(4)       #m/s and m

#Compute the numerical solutions to the ODEs using odeint
solNewton = ode(NewtonsSecond, NewtonInitials, t, args=(k, mass))
solNeutron = ode(NeutronStar, NeutronInitials, t, args=(c, G))
solBallistics = ode(Ballistics, BallisticsInitials, t)

#Graph all solutions
plt.title("Solving Newton's Second Law in Three Dimensions\nSolution for velocity as a function of time")
plt.plot(t, solNewton[:, 0], label='X Velocity')
plt.plot(t, solNewton[:, 1], label='Y Velocity')
plt.plot(t, solNewton[:, 2], label='Z Velocity')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (meters/second)')
plt.legend(loc='best')
plt.show()

plt.title("Solving Newton's Second Law in Three Dimensions\nSolution for position as a function of time")
plt.plot(t, solNewton[:, 3], label='X Position')
plt.plot(t, solNewton[:, 4], label='Y Position')
plt.plot(t, solNewton[:, 5], label='Z Position')
plt.xlabel('Time (seconds)')
plt.ylabel('Position (meters)')
plt.legend(loc='best')
plt.show()

plt.title('Density Inside a Neutron Star as a Function of Radius', y=1.04)
plt.plot(t, solNeutron[:, 0])
plt.xlabel('Radius (meters)')
plt.ylabel('Density (kilograms per meters cubed)')
plt.show()

plt.title('Mass Inside a Neutron Star as a Function of Radius', y=1.04)
plt.plot(t, solNeutron[:, 1])
plt.xlabel('Radius (meters)')
plt.ylabel('Mass (kilograms)')
plt.show()

plt.title('Pressure Inside a Neutron Star as a Function of Radius', y=1.04)
plt.plot(t, solNeutron[:, 2])
plt.xlabel('Radius (meters)')
plt.ylabel('Pressure (pascals)')
plt.show()

plt.title('Solving a Drag Conscious Ballistics Equation for Velocities as a Function of Time')
plt.plot(t, solBallistics[:, 0], label='X Velocity')
plt.plot(t, solBallistics[:, 1], label='Y Velocity')
plt.legend(loc='best')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (meters/second)')
plt.show()

plt.title('Solving a Drag Conscious Ballistics Equation for a Given Trajectory')
plt.plot(solBallistics[:, 2], solBallistics[:, 3])
plt.xlabel('X-Position (meters)')
plt.ylabel('Y-Position (meters)')
plt.show()