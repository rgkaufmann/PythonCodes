# Imports in order to set the recursion limit for the Euler method (sys), plot
# The resulting x and y components (plt), and work with trig functions and
# arrays (np and math).
import numpy as np
import math
import matplotlib.pyplot as plt
import sys

# Setting the recursion limit to 4000 to be high enough for the first Euler
# Method to converge.
sys.setrecursionlimit(4000)

# Setting up any needed components, constants, or initial vectors.
INITIALV = 60                                # Initial velocity in m/s
GRAVITY = -9.8                               # Gravitational acceleration m/s^2
DRAG = 0.5                                   # Drag coefficient for a sphere
DENSITY = 1.23                               # Given density of air kg/m^3
SPHERERADIUS = 0.0365                        # Radius of the sphere m
SPHEREMASS = 0.143                           # Mass of the sphere kg
INITIALVZ = INITIALV*math.sin(math.pi/6)     # Initial z velocity m/s
INITIALVX = INITIALV*math.cos(math.pi/6)     # Initial x velocity m/s
FINALSTEP = 2*INITIALVX*INITIALVZ/(-GRAVITY) # Predicted final x distance m
INITIALVECTOR = [INITIALVX, INITIALVZ, 0, 0] # Full initial conditions (m/s, m)
SPHEREAREA = math.pi*SPHERERADIUS**2         # Total surface area of sphere m^2

# EulerMethod takes a separate function that describes a differential equation
# Or system of differential equation and performs a Euler Approximation given
# An initial time prevt, a final time finalt, an initial condition prevy, and
# a step.
def EulerMethod(func, prevt, finalt, prevy, step):
    # The method begins by calculating the Euler approximation for given the
    # Previous y and t.
    nexty = prevy + step*np.array(func(prevy, prevt))
    # This specific function is specified for ballistic equations and thus ends
    # It's calculation when the z component reaches 0. Normally, this if
    # Statement would be left out entirely.
    if nexty[3]<=0:
        return np.array([nexty])
    # This next statement checks if the previous time will still be less than
    # The final time that is given and thus needs another run through the Euler
    # Method. It appends the nexty onto the array and performs another step.
    elif prevt <= finalt+step:
        return np.append(np.array([nexty]),
                         EulerMethod(func, prevt+step, finalt, nexty, step),
                         axis=0)
    # Finally, if the previous time does not pass the above check to be less
    # Than the final time, the given y is returned so it is appened and the
    # Recursion ends.
    else:
        return np.array([nexty])

# The RungeKuttaMethod performs the Runge-Kutta approximation on a given system
# The function requires a differential function, an initial time, a final time,
# An initial vondition prevy, and a step.
# (The Runge-Kutta method is a predictor-corrector approximation of four-stages
# compared to the Improved Euler method or Heun's Method which is a two-stage
# Runge-Kutta method.)
def RungeKuttaMethod(func, prevt, finalt, prevy, step):
    # The method starts by calculating all the values needed to construct the
    # Approximation
    k1 = np.array(func(prevy, prevt))
    k2 = np.array(func(prevy+step*k1/2, prevt+step/2))
    k3 = np.array(func(prevy+step*k2/2, prevt+step/2))
    k4 = np.array(func(prevy+step*k3, prevt+step))
    # And then combines it to form the approximation.
    nexty = prevy+step*(k1+2*k2+2*k3+k4)/6
    # Again, unique to this approximation, it is compared to see if the value
    # Is below zero. If it is, it returns it as the last point.
    if nexty[3]<=0:
        return np.array([nexty])
    # Then the previous time is compared to see if the last time step has been
    # Calculated or if more time steps are necessary. If more time steps are
    # Necessary, the recursion continues and is appended onto the array.
    elif prevt <= finalt+step:
        return np.append(np.array([nexty]),
                         RungeKuttaMethod(func, prevt+step, finalt, nexty,
                                          step),
                         axis=0)
    # If no more time steps are necessary, it produces the last piece and adds
    # It to the back of the array, ending the recursion.
    else:
        return np.array([nexty])

# projectileMotionDifferential takes a vector of the form (xvelocity,
# zvelocity, x, z) and ouputs the vector (xacceleration, zacceleration,
# xvelocity, zvelocity) based on the system of differential equations.
# This equation is specifically for the differential equation that doesn't
# Contain a drag component
def projectileMotionDifferential(vector, time):
    xvelocity = vector[0]
    yvelocity = vector[1]
    return [0, GRAVITY, xvelocity, yvelocity]

# dragMotionDifferential takes a vector of the form (xvelocity, zvelocity, x,
# z) and outputs the vector (xacceleration, zacceleration, xvelocity,
# zvelocity) based on the respective system of differential equations.
# This equation is specifically for the differential equation that involves a
# Drag force on the system.
def dragMotionDifferential(vector, time):
    xvelocity = vector[0]
    zvelocity = vector[1]
    velocity = math.sqrt(xvelocity**2+zvelocity**2)
    return [-1/2*DRAG*DENSITY*SPHEREAREA/SPHEREMASS*velocity*xvelocity,
            GRAVITY-1/2*DRAG*DENSITY*SPHEREAREA/SPHEREMASS*velocity*zvelocity,
            xvelocity, zvelocity]

# projectileMotion creates an array of the values of the z coordinates as a
# Function of the x coordinates using the classical mechanics formulae
def projectileMotion(xval):
    return INITIALVZ/INITIALVX*xval + 1/2*GRAVITY/(INITIALVX**2)*xval**2

# plotGraphs is a helper function designed to streamline the process of
# Plotting the data. It first asks if the vertical line designating the final
# Distance of the non-drag equation is needed (boolean Vline). Then asks if the
# Equation that is being plotted is the given drag equation (boolean Drag).
# Finally the data, title, and scatterlabel is passed into the function.
def plotGraphs(Vline, Drag, Data, Title="", scatterlabel=''):
    # If Vline is True then it plots three lines, one at the predicted final x
    # Distance, and two at 1 cm below and above the final x distance.
    if Vline:
        plt.axvline(x=FINALSTEP, c='c')
        plt.axvline(x=FINALSTEP-0.01, c='g')
        plt.axvline(x=FINALSTEP+0.01, c='g')
    # If Drag is True, then it plots the data using a scatter plot and
    # Configures the x limits to be a small amount below 0 and a small amount
    # Above 50. This range is what was approximated by looking at the graph
    # When plotting.
    if Drag:
        plt.scatter(Data[:, 2], Data[:, 3], c='r', s=2.5, label=scatterlabel)
        plt.xlim(0-0.1*120, 1.1*120)
    # If Drag is False, it plots the data using a scatter plot, now making sure
    # That the scatter plot is behind the analytical plot. The analytical plot
    # Is also plotted alongside in front of the given data.
    else:
        plt.scatter(Data[:, 2], Data[:, 3], c='r', s=2.5, label=scatterlabel,
                    zorder=1)
        plt.plot(AnalyticalXValues, AnalyticalSolution,
                 label='Analytiacl Solution', zorder=10)
        plt.xlim(0-0.1*FINALSTEP, 1.1*FINALSTEP)
        plt.legend(loc='best')
    # The rest of the graph is filled out with a title, axis labels, and a line
    # At z=0.
    plt.hlines(0, -100, 1000)
    plt.xlabel('X distance (m)')
    plt.ylabel('Z distance (m)')
    plt.title(Title)
    plt.show()
    
# doEuler is a helper function to help streamline the process of performing
# The Euler Method repeatedly. It calculates the step given a number of points
# And computes the Euler Method and returns all vectors above z=0.
def doEuler(func, points):
    Step = (tMax-tMin)/points
    Euler = EulerMethod(func, tMin, tMax, INITIALVECTOR, Step)
    Euler = Euler[np.where(Euler[:, 3]>0)]
    return Euler

# doRK is a helper function to help streamline the process of performing the
# Runge-Kutta Method repeatedly. It calculates the step given a number of
# Points and computes the Runge-Kutta Method and returns all vectors above z=0.
def doRK(func, points):
    Step = (tMax-tMin)/points
    RK = RungeKuttaMethod(func, tMin, tMax, INITIALVECTOR, Step)
    RK = RK[np.where(RK[:, 3]>0)]
    return RK

# printResults is a helper function designed to streamline the process of
# Printing the results and appending it into a list to be outputted to a txt
# File. It prints the number of points and the last vector of the given data.
def printResults(data, firstprompt):
    Results = ''
    Results += firstprompt.format(len(data))
    Results += '\n'
    Results += "Final X Velocity:  {:.3f}\n".format(data[-1, 0])
    Results += "Final Z Velocity: {:.3f}\n".format(data[-1, 1])
    Results += "Final X Distance:  {:.3f}\n".format(data[-1, 2])
    Results += "Final Z Distance:  {:.3f}\n".format(data[-1, 3])
    Results += '\n'
    print(Results)
    return Results

# The analytical solution is calculated to be used in the plotting. Moreover,
# The starting and ending times are calculated to be used in the Euler and
# Runge-Kutta method.
AnalyticalXValues = np.arange(0, FINALSTEP+0.25, 0.25)
AnalyticalSolution = projectileMotion(AnalyticalXValues)
tMin = 0
tMax = -2*INITIALVZ/GRAVITY

# Each situation is computed (Euler method without drag, Euler method with
# Drag, Runge-Kutta method without drag, and Runge-Kutta method with drag) then
# Plotted with the respective titles and plot types.
EulerVectorNoDrag = doEuler(projectileMotionDifferential, 3271)
plotGraphs(True, False, EulerVectorNoDrag,
           'Euler Approximation of No Drag Ballistic Motion',
           'Euler Approximation')

EulerVectorDrag = doEuler(dragMotionDifferential, 3000)
plotGraphs(False, True, EulerVectorDrag,
           'Euler Approximation of Drag Included Ballistic Motion',
           'Euler Approximation')

RKVectorNoDrag = doRK(projectileMotionDifferential, 13)
plotGraphs(True, False, RKVectorNoDrag,
           'Runge-Kutta Approximation of No Drag Ballistic Motion',
           'Runge-Kutta Approximation')

RKVectorDrag = doRK(dragMotionDifferential, 30)
plotGraphs(False, True, RKVectorDrag,
           'Runge-Kutta Approximation of Drag Included Ballistic Motion',
           'Runge-Kutta Approximation')

# Finally the statistics of each method is printed
Stats = printResults(EulerVectorNoDrag,
                     'Euler Method without Drag Points: {:d}')
Stats += printResults(EulerVectorDrag, 'Euler Method with Drag Points: {:d}')
Stats += printResults(RKVectorNoDrag,
                      'Runge-Kutta Method without Drag Points: {:d}')
Stats += printResults(RKVectorDrag,
                      'Runge-Kutta Method with Drag Points: {:d}')

# And saved to a file.
file = open('Homework II.txt', 'w')
file.write(Stats)
file.close()