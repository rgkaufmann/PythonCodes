# Physical Differential Equations - Ryan Kaufmann
# BONUS: Inclued three other numerical approximation method (Euler,
# Improved Euler, and Runge-Kutta) and added them to the plot. Allowed
# User input to the program, lettnig them change the constants and in
# Some cases the time period looked at. Made the maximum time in the
# Problems analytically defined using the lambert-W function. Added
# Three more physical systems that can be observed and compared to the
# Analytical solution, including Motion through Viscous Liquids,
# Damped Harmonic Oscillations, and Forced Undamped Harmonic Oscillations
# Finally added an option to enter custom constant coefficient system of
# Equations and have their numerical approximation displayed on a graph
import numpy as np                  # Importing necessary functions:
import matplotlib.pyplot as plt     # numpy for arrays, pyplot for plotting
from scipy.integrate import odeint  # odeint for differential equations
from scipy.special import lambertw  # lambertw for maximum time


# Calculates the Euler Method Approximation of a given function
# Requires a funciton name, initial time, final time, initial y, and step size
def EulerMethod(func, prevt, finalt, prevy, step):
    nexty = prevy + step*np.array(func(prevy, prevt))  # Euler Approximation
    if np.any(np.greater(nexty, 10^4)):
        return np.array([nexty])
    elif prevt <= finalt+step:  # Checks if the time is next to last
        return np.append(np.array([nexty]),
                         EulerMethod(func, prevt+step,
                                     finalt, nexty, step),
                         axis=0)  # Appends the next step to back of array
    else:
        return np.array([nexty])  # Returns an array of the value if time is
# the last time that is given (finalt)


# Calculates the Improved Euler Method Approximation of a given function
# Requires a function name, initial time, final time, initial y, and step size
def ImprovedEulerMethod(func, prevt, finalt, prevy, step):
    m1 = np.array(func(prevy, prevt))  # First component of approximation
    m2 = np.array(func(prevy+step*m1, prevt+step))  # Second component
    nexty = prevy+step*(m1+m2)/2  # Computes full approximation
    if np.any(np.greater(nexty, 10^4)):
        return np.array([nexty])
    elif prevt <= finalt+step:
        return np.append(np.array([nexty]),
                         ImprovedEulerMethod(func, prevt+step,
                                             finalt, nexty, step),
                         axis=0)
    else:
        return np.array([nexty])
# Ends with similar method to before of checking the time value and appending
# The next value onto the back of the array.


# Calculates The Runge-Kutta Method Approximation of a given function
# Requires a function name, initial time, final time, initial y, and step size
def RungeKuttaMethod(func, prevt, finalt, prevy, step):
    k1 = np.array(func(prevy, prevt))
    k2 = np.array(func(prevy+step*k1/2, prevt+step/2))
    k3 = np.array(func(prevy+step*k2/2, prevt+step/2))
    k4 = np.array(func(prevy+step*k3, prevt+step))
    nexty = prevy+step*(k1+2*k2+2*k3+k4)/6
# Extremely similar method to Improved Euler of calculating individual parts
# And then combining them into one approximate value of y
    if np.any(np.greater(nexty, 10^4)):
        return np.array([nexty])    
    elif prevt <= finalt+step:
        return np.append(np.array([nexty]),
                         RungeKuttaMethod(func, prevt+step,
                                          finalt, nexty, step),
                         axis=0)
    else:
        return np.array([nexty])
# Then again checks time value and appends next value onto back of the array


# Takes in several values and constructs the basics of the plot structure
# Making the title and labels and limiting the graph
def plotSetUp(xMax, title, xlbl, ylbl, limity=True):
    plt.title(title)
    plt.xlim(0-0.1*xMax, 1.1*xMax)
    if limity:               # Limits the y and x values so that graph doesn't
        plt.ylim(ymin=0)     # Get dwarfed, Attempts to show entire graph.
    plt.hlines(0, -10, 100)  # Gives 0 line necessary for many plots
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid()
    plt.legend()


# Takes in various parts of plot and plots all of the graphs using the number
# Of graphs it needs to plot (based on the physical system), the analytical
# Solutions, and the array of approximations. Also requires anything to set up
# the plot using the above function
def plotGraphs(plotNumber, FirstAnalytical, SecondAnalytical,
               odeint, Euler, ImprovedEuler, RungeKutta, Time,
               xMax, Title1, xLabel1, yLabel1,
               Title2='', xLabel2='', yLabel2=''):
    if plotNumber == 1:  # For Ballistic and Viscous Motion
        plt.scatter(odeint[:, 2], odeint[:, 3], c='b',  # All plots
                    label='odeint Approximation')
        plt.scatter(Euler[:, 2], Euler[:, 3], c='g',
                    label='Euler Method Approximation')
        plt.scatter(ImprovedEuler[:, 2], ImprovedEuler[:, 3], c='m',
                    label='Improved Euler Method Approximation')
        plt.scatter(RungeKutta[:, 2], RungeKutta[:, 3], c='k',
                    label='Runge-Kutta Method Approximation')
        plt.plot(FirstAnalytical(Time), SecondAnalytical(Time), c='r',
                 label='Analytical Solution')
        plotSetUp(xMax, Title1, xLabel1, yLabel1)  # Plot setup
        plt.show()      # Shows Plot
    elif plotNumber == 2:  # For Oscillations
        plt.scatter(Time, odeint[:, 1], c='b', label='odeint Approximation')
        plt.scatter(Time, Euler[:len(Time), 1], c='g',
                    label='Euler Method Approximation')
        plt.scatter(Time, ImprovedEuler[:len(Time), 1], c='m',
                    label='Improved Euler Method Approximation')
        plt.scatter(Time, RungeKutta[:len(Time), 1], c='k',
                    label='Runge-Kutta Method Approximation')
        plt.plot(Time, FirstAnalytical(Time), c='r',
                 label='Analytical Solution')
        plotSetUp(xMax, Title1, xLabel1, yLabel1, False)
        plt.show()
        plt.scatter(Time, odeint[:, 0], c='b',
                    label='odeint Approximation')
        plt.scatter(Time, Euler[:len(Time), 0], c='g',
                    label='Euler Method Approximation')
        plt.scatter(Time, ImprovedEuler[:len(Time), 0], c='m',
                    label='Improved Euler Method Approximation')
        plt.scatter(Time, RungeKutta[:len(Time), 0], c='k',
                    label='Runge-Kutta Method Approximation')
        plt.plot(Time, SecondAnalytical(Time), c='r',
                 label='Analytical Solution')
        plotSetUp(xMax, Title2, xLabel2, yLabel2, False)
        plt.show()
# Does similar procedure but now does two plots, one for velocity and the other
# For position


# Plots the numerical solutions to a Custom system of differential equations
# This function only requires the analytical solution arrays and time.
def plotCustom(odeint, Euler, ImprovedEuler, RungeKutta, Time):
    title = 'Approximate Solutions for Equation {}'
    for equationNumber in range(len(CustomVector)):
        plt.scatter(Time, odeint[:len(Time), equationNumber], c='b',
                    label='odeint Approximation')
        plt.scatter(Time, Euler[:len(Time), equationNumber], c='g',
                    label='Euler Method Approximation')
        plt.scatter(Time, ImprovedEuler[:len(Time), equationNumber], c='m',
                    label='Improved Euler Methd Approximation')
        plt.scatter(Time, RungeKutta[:len(Time), equationNumber], c='r',
                    label='Runge-Kutta MethodApproximation')
        plotSetUp(Time[-1],
                  title.format(equationNumber+1),
                  'Time', '', False)
        plt.show()
# Using a for loop, plots all solutions with respect to time, units unknown
# Uses similar approach to the oscillation equations.


# Prompts for the constants used in the differential equations. All constants
# Declared globally
def promptConstants(SystemPrompt):
    prompt = 'Would you like to look at a preset set of initial conditions? '
    prompt = prompt+'(Yes/No) '
    if SystemPrompt == promptBallistic:  # Presets are only limited to
        preset = input(prompt)           # Ballistic Motion
        if preset.lower() == 'yes':
            promptPresets()
    else:                             # If not a preset, calls prompt function
        print('Please enter values greater than 0')
        SystemPrompt()


# Asks for any constant that is needed in the Ballistic motion equations
def promptBallistic():
    promptX = 'What is the initial x-direction velocity in m/s? '
    promptY = 'What is the initial y-direction velocity in m/s? '
    promptGrav = 'What is the gravitational acceleration in m/s^2? '
    global DRAG         # In kilograms per second
    global MASS         # In kilograms
    global GRAVITY      # In meters per seconds squared
    global INITIALVX    # In meters
    global INITIALVY    # In meters
    try:
        DRAG = float(input('What is the drag coefficient in kg/s? '))
        MASS = float(input('What is the mass of the object in kg? '))
        GRAVITY = float(input(promptGrav))
        INITIALVX = float(input(promptX))
        INITIALVY = float(input(promptY))
    except ValueError:
        print('Values are not numbers, please try again.')
        promptBallistic()
# Checks if values entered are legal


# Asks for any constant that is needed in the Viscosity motion equations
def promptViscosity():
    promptRadius = 'What is the radius of the ball that is falling in m? '
    promptViscous = 'What is the dynamic viscosity of the liquid in kg/(s*m)? '
    promptDensity = 'What is the density of the liquid in kg/m^3? '
    promptMass = 'What is the mass of the ball that is falling in kg? '
    promptX = 'What is the initial x-direction velocity in m/s? '
    promptY = 'What is the initial y-direction velocity in m/s? '
    promptGrav = 'What is the gravitational acceleration in m/s^2? '
    global RADIUS           # In meters
    global VISCOSITY        # In kilograms per second-meters
    global DENSITYLIQUID    # In kilograms per meters cubed
    global MASSBALL         # In kilograms
    global GRAVITY          # In meters per seconds squared
    global INITIALVX        # In meters
    global INITIALVY        # In meters
    try:
        RADIUS = float(input(promptRadius))
        VISCOSITY = float(input(promptViscous))
        DENSITYLIQUID = float(input(promptDensity))
        MASSBALL = float(input(promptMass))
        GRAVITY = float(input(promptGrav))
        INITIALVX = float(input(promptX))
        INITIALVY = float(input(promptY))
    except ValueError:
        print('Values are not numbers, please try again.')
        promptViscosity()
# Checks if values entered are legal


# Asks for any constant that is neded in the Damped oscillations equations
def promptDamped():
    promptViscous = 'What is the dynamic viscosity of the fluid in kg/(s*m)? '
    promptSpring = 'What is the spring constant of the spring in kg/s^2? '
    promptX = 'What is the initial displacement of the ball in m? '
    global RADIUS           # In meters
    global VISCOSITY        # In kilograms per second-meters
    global MASS             # In kilograms
    global SPRINGCONSTANT   # In kilograms per seconds squared
    global INITIALX         # In meters
    try:
        RADIUS = float(input('What is the radius of the ball in m? '))
        VISCOSITY = float(input(promptViscous))
        MASS = float(input('What is the mass of the ball in kg? '))
        SPRINGCONSTANT = float(input(promptSpring))
        INITIALX = float(input(promptX))
    except ValueError:
        print('Values are not numbers, please try again.')
        promptDamped()
# Checks if values entered are legal


# Asks for any constant that is needed in Forced Undamped oscillation equations
def promptForcedUndamped():
    promptSpring = 'What is the spring constant of the spring in kg/s^2? '
    promptFrequency = 'What is the frequency that the force is acting'
    promptFrequency = promptFrequency + " on the system in rads/s? "
    promptForce = 'What is the magnitude of the external force in kg*m/s^2? '
    promptX = 'What is the initial position of the ball in m? '
    global FORCE            # In kilogram-meters per seconds squared
    global FREQUENCY        # In radians per second
    global MASS             # In kilograms
    global SPRINGCONSTANT   # In kilograms per seconds squared
    global INITIALX         # In meters
    try:
        FORCE = float(input(promptForce))
        FREQUENCY = float(input(promptFrequency))
        MASS = float(input('What is the mass of the ball in kg? '))
        SPRINGCONSTANT = float(input(promptSpring))
        INITIALX = float(input(promptX))
    except ValueError:
        print('Values are not numbers, please try again.')
        promptForcedUndamped()
# Checks if values entered are legal


# Asks for the initial conditions and differential matrix for a custom equation
def promptCustom():
    matrixPrompt = 'What is the coefficient of equation {} for the '
    matrixPrompt = matrixPrompt + 'derivative of equation {}? '
    vectorPrompt = 'What is the initial condition for equation {}? '
    global CustomMatrix
    global CustomVector
    try:
        SIZE = int(input('How many equations are there? '))
        CustomMatrix = np.matrix(np.zeros((SIZE, SIZE)))
        CustomVector = np.zeros(SIZE)
        for indxrow in range(SIZE):
            for indxcol in range(SIZE):
                matrixPrompt2 = matrixPrompt.format(indxcol, indxrow)
                CustomMatrix[indxrow, indxcol] = float(input(matrixPrompt2))
            vectorPrompt2 = vectorPrompt.format(indxrow)
            CustomVector[indxrow] = float(input(vectorPrompt2))
        CustomMatrix = CustomMatrix.transpose()
    except ValueError:
        print('Values are not numbers, please try again.')
        promptCustom()
# Checks if values entered are legal


# If preset was selected, asks for which preset and loads the given set of
# Constants to be used in the ballistic motion equation
def promptPresets():
    presetPrompt = 'What preset would you like to load? (Enter List to see the'
    presetPrompt = presetPrompt + ' list of presets or Cancel to exit) '
    PRESETS = np.genfromtxt("Presets.txt", dtype=np.str, delimiter=';')
    preset = input(presetPrompt)
    if preset.lower() == 'cancel':  # Exits program if cancel entered
        return None
    elif preset.lower() == 'list':  # Displays presets if list entered
        for indx in range(len(PRESETS)):
            print(PRESETS[indx])
        print()
        promptPresets()
    elif preset.lower() in map(lambda x: x.lower(), PRESETS):
        # Searches for presets in the folder and applies the constants
        filename = 'Presets/'
        filename = filename + preset[0:preset.index(' ')]
        filename = filename + preset[preset.rfind(' ')+1:] + '.txt'
        Constants = np.loadtxt(filename)
        global DRAG         # In kilograms per second
        global MASS         # In kilograms
        global GRAVITY      # In meters per seconds squared
        global INITIALVX    # In meters
        global INITIALVY    # In meters
        DRAG = Constants[0]
        MASS = Constants[2]
        GRAVITY = Constants[1]
        INITIALVX = Constants[3]
        INITIALVY = Constants[4]
    else:           # If preset isn't found, then the prompt asks again
        print('Preset not found.\n')
        promptPresets()


# Identifies and runs the given system of equations to be observed
def lookupSystem(SystemName):
    if SystemName.lower() == BUILTINSYSTEMS[0].lower():
        BallisticEquation()
    elif SystemName.lower() == BUILTINSYSTEMS[1].lower():
        ViscosityEquation()
    elif SystemName.lower() == BUILTINSYSTEMS[2].lower():
        DampedEquation()
    elif SystemName.lower() == BUILTINSYSTEMS[3].lower():
        ForcedUndampedEquation()
    elif SystemName.lower() == BUILTINSYSTEMS[4].lower():
        CustomEquation()


# The differential system of equation for the ballistic motion equation
# Returns a vector of X-Velocity, Y-Velocity, X-Position, and Y-Position
# To be used in odeint, Euler, ImprovedEuler, and RungeKutta
def differentialBallistics(Vector, Time):
    xvelocity = Vector[0]
    yvelocity = Vector[1]
    return [-DRAG/MASS*xvelocity, -GRAVITY-DRAG/MASS*yvelocity,
            xvelocity, yvelocity]


# The differential system of equation for the viscous motion equation
# Returns a vector of X-Velocity, Y-Velocity, X-Position, and Y-Position
# To be used in odeint, Euler, ImprovedEuler, and RungeKutta
def differentialViscosity(Vector, Time):
    xvelocity = Vector[0]
    yvelocity = Vector[1]
    return [-6*np.pi*VISCOSITY*RADIUS*xvelocity/MASSBALL,
            (-MASSLIQUID*GRAVITY-6*np.pi*VISCOSITY*RADIUS*yvelocity)/MASSBALL,
            xvelocity, yvelocity]


# The differential system of equation for the damped oscillation equation
# Returns a vector of velocity, and position
# To be used in odeint, Euler, ImprovedEuler, and RungeKutta
def differentialDamped(Vector, Time):
    velocity = Vector[0]
    position = Vector[1]
    return [-POSITIONCOEFFICIENT*position-VELOCITYCOEFFICIENT*velocity,
            velocity]


# The differential system of equation for the forced undamped equation
# Returns a vector of velocity, and position
# To be used in odeint, Euler, ImprovedEuler, and RungeKutta
def differentialForcedUndamped(Vector, Time):
    velocity = Vector[0]
    position = Vector[1]
    return [FORCE/MASS*np.cos(FREQUENCY*Time)-SPRINGCONSTANT/MASS*position,
            velocity]


# The differential system of equation for custom equations
# Returns a vector multiplies by the custom matrix (Vector and Matrix are
# Inversed to return correct order) Used in odeint, Euler, Improved, RK
def differentialCustom(Vector, Time):
    return np.array(Vector*CustomMatrix)[0]


# The analytical solution to X position of ballistic motion
def xBallistic(time):
    return (INITIALVX*MASS/DRAG)*(1-np.exp(-(DRAG*time)/MASS))


# The analytical solution to Y position of ballistic motion
def yBallistic(time):
    ySolution = (MASS/DRAG)*(INITIALVY+(MASS*GRAVITY)/DRAG)
    ySolution = ySolution*(1-np.exp(-(DRAG*time)/MASS))
    ySolution = ySolution-(MASS*GRAVITY)/DRAG*time
    return ySolution


# The analytical solution to X position of viscous motion
def xViscosity(time):
    xSolution = (INITIALVX*MASSBALL/(6*np.pi*VISCOSITY*RADIUS))
    xSolution = xSolution*(1-np.exp(-(6*np.pi*VISCOSITY*RADIUS*time)/MASSBALL))
    return xSolution


# The analytical solution to Y position of viscous motion
def yViscosity(time):
    ySolution = MASSBALL/(6*np.pi*VISCOSITY*RADIUS)
    ySolution *= (INITIALVY+MASSLIQUID*GRAVITY/(6*np.pi*VISCOSITY*RADIUS))
    ySolution *= (1-np.exp(-(6*np.pi*VISCOSITY*RADIUS*time)/MASSBALL))
    ySolution -= (MASSLIQUID*GRAVITY/(6*np.pi*VISCOSITY*RADIUS))*time
    return ySolution+10


# The analytical solution to the position of damped oscillation
def DampedPosition(time):
    PosSolution1 = INITIALX*np.exp(-VELOCITYCOEFFICIENT/2*time)
    PosSolution1 *= np.cos(np.sqrt(np.abs(SOLUTIONCOEFFICIENT))*time)
    PosSolution2 = INITIALX*VELOCITYCOEFFICIENT
    PosSolution2 /= (2*np.sqrt(SOLUTIONCOEFFICIENT))
    PosSolution2 *= np.exp(-VELOCITYCOEFFICIENT/2*time)
    PosSolution2 *= np.sin(np.sqrt(np.abs(SOLUTIONCOEFFICIENT))*time)
    return PosSolution1 + PosSolution2


# The analytical solution to the velocity of damped oscillation
def DampedVelocity(time):
    PosSolution = -(VELOCITYCOEFFICIENT**2*INITIALX)
    PosSolution -= 4*INITIALX*np.abs(SOLUTIONCOEFFICIENT)
    PosSolution /= (4*np.sqrt(np.abs(SOLUTIONCOEFFICIENT)))
    PosSolution *= np.exp(-VELOCITYCOEFFICIENT/2*time)
    PosSolution *= np.sin(np.sqrt(np.abs(SOLUTIONCOEFFICIENT))*time)
    return PosSolution


# The analytical solution to the position of forced undamped oscillation
def ForcedUndampedPosition(time):
    PosSolution1 = (INITIALX-(FORCE/MASS)/((SPRINGCONSTANT/MASS)-FREQUENCY**2))
    PosSolution1 *= np.cos(np.sqrt(SPRINGCONSTANT/MASS)*time)
    PosSolution2 = (FORCE/MASS)/((SPRINGCONSTANT/MASS)-FREQUENCY**2)
    PosSolution2 *= np.cos(FREQUENCY*time)
    return PosSolution1+PosSolution2


# The analytical solution to the velocity of forced undamped oscillation
def ForcedUndampedVelocity(time):
    Solution1 = -(INITIALX-(FORCE/MASS)/((SPRINGCONSTANT/MASS)-FREQUENCY**2))
    Solution1 *= SPRINGCONSTANT/MASS*np.sin(np.sqrt(SPRINGCONSTANT/MASS)*time)
    Solution2 = (FORCE/MASS)/((SPRINGCONSTANT/MASS)-FREQUENCY**2)
    Solution2 *= FREQUENCY*np.sin(FREQUENCY*time)
    return Solution1-Solution2


# This function processes the ballistic equation and its numerical solutions
# The parameter is passed to check if the current constants is the example
# Problem
def BallisticEquation(first=False):
    # First the constants are initialized and assigned values, using the prompt
    global TimeSpan
    global odeintVector
    if not first:
        promptConstants(promptBallistic)
    INITIALVECTOR = [INITIALVX, INITIALVY, 0, 0]

    # Then the time span is set based on the analytical solution of the
    # Ballistic motion problem. Then applied to the minimum time and number
    # of points, we make the step size and the timespan
    Wparam = np.exp(-(DRAG*INITIALVY)/(GRAVITY*MASS)-1)
    Wparam *= (-(DRAG*INITIALVY)/(GRAVITY*MASS)-1)
    AnalyticalTimeMax = GRAVITY*MASS
    AnalyticalTimeMax *= lambertw(Wparam)
    AnalyticalTimeMax += DRAG*INITIALVY+GRAVITY*MASS
    tMax = (AnalyticalTimeMax/(DRAG*GRAVITY)).real  # In Seconds
    tMin = 0                                        # In Seconds
    Points = 250
    Step = (tMax-tMin)/Points
    TimeSpan = np.arange(tMin, tMax, Step)

    # Finally we calculate our numerical solution values, using odeint, Euler
    # Method, Improved Euler Method, and Runge Kutta and then we plot our
    # Solutions using our plotgraphs function above.
    odeintVector = odeint(differentialBallistics,
                          INITIALVECTOR, TimeSpan)
    EulerVector = EulerMethod(differentialBallistics,
                              tMin, tMax, INITIALVECTOR, Step)
    ImprovedEulerVector = ImprovedEulerMethod(differentialBallistics,
                                              tMin, tMax, INITIALVECTOR, Step)
    RungeKuttaVector = RungeKuttaMethod(differentialBallistics,
                                        tMin, tMax, INITIALVECTOR, Step)
    plotGraphs(1, xBallistic, yBallistic,
               odeintVector, EulerVector,
               ImprovedEulerVector, RungeKuttaVector, TimeSpan,
               xBallistic(tMax),
               'Approximation of Projectile Motion of Launched Object',
               'X (meters)', 'Y (meters)')


# A similar equation to the ballistic one, except for the initial example
# Calculates and plots the numerical/analytical solution to the viscosity
# Problem
def ViscosityEquation():
    # First we initialize all the variables and assign the values using prompt
    global MASSLIQUID
    promptConstants(promptViscosity)
    INITIALVECTOR = [INITIALVX, INITIALVY, 0, 10]
    VOLUMEBALL = 4/3*np.pi*RADIUS**3                          # In meters cubed
    MASSLIQUID = (MASSBALL/VOLUMEBALL-DENSITYLIQUID)*VOLUMEBALL  # In kilograms

    # Then the time span is once again found analytically for this equation
    # Then applied to the minimum time, and number of points to find the step
    # And the time span vector.
    expParam = -MASSBALL*MASSLIQUID*GRAVITY
    expParam -= (6*np.pi*MASSBALL*RADIUS*VISCOSITY*INITIALVY)
    expParam -= 360*(np.pi*RADIUS*VISCOSITY)**2
    Wparam = (np.exp(expParam))/(MASSBALL*MASSLIQUID*GRAVITY)
    Wparam *= -GRAVITY*MASSLIQUID
    Wparam -= 6*np.pi*RADIUS*VISCOSITY*INITIALVY
    Wparam = (Wparam/(GRAVITY*MASSLIQUID))+1
    AnalyticalTMax = lambertw(Wparam)
    AnalyticalTMax *= MASSBALL*GRAVITY*MASSLIQUID
    AnalyticalTMax += (6*np.pi*MASSBALL*RADIUS*VISCOSITY*INITIALVY)
    AnalyticalTMax += 360*(np.pi*RADIUS*VISCOSITY)**2
    AnalyticalTMax /= (6*np.pi*GRAVITY*MASSLIQUID*RADIUS*VISCOSITY)
    tMax = (AnalyticalTMax).real    # In Seconds
    tMin = 0                        # In Seconds
    Points = 500
    Step = (tMax-tMin)/Points
    TimeSpan = np.arange(tMin, tMax, Step)

    # Finally the Numerical vectors are once again calculated and then used
    # To calculated the graphs of the motion. Each graph plots the odeint
    # Euler, improved Euler, and Runge-Kutta methods.
    odeintVector = odeint(differentialViscosity, INITIALVECTOR, TimeSpan)
    EulerVector = EulerMethod(differentialViscosity,
                              tMin, tMax, INITIALVECTOR, Step)
    ImprovedEulerVector = ImprovedEulerMethod(differentialViscosity,
                                              tMin, tMax, INITIALVECTOR, Step)
    RungeKuttaVector = RungeKuttaMethod(differentialViscosity,
                                        tMin, tMax, INITIALVECTOR, Step)
    plotGraphs(1, xViscosity, yViscosity,
               odeintVector, EulerVector,
               ImprovedEulerVector, RungeKuttaVector, TimeSpan,
               xViscosity(tMax),
               "Approximation of an Object's Movement through Viscous Liquids",
               'X (meters)', 'Y (meters)')


# This function observes the damped oscillations differential equation, a
# Different differential equation than the ones we have been looking at
def DampedEquation():
    # Again we first initialize and declare all our variables using the prompt
    # The solution coefficient is used to shorten the solution lines
    global VELOCITYCOEFFICIENT
    global POSITIONCOEFFICIENT
    global SOLUTIONCOEFFICIENT
    promptConstants(promptDamped)
    INITIALVECTOR = [0, INITIALX]
    VELOCITYCOEFFICIENT = 6*np.pi*VISCOSITY*RADIUS/MASS  # In Hertz
    POSITIONCOEFFICIENT = SPRINGCONSTANT/MASS            # In Hertz squared
    SOLUTIONCOEFFICIENT = POSITIONCOEFFICIENT-(VELOCITYCOEFFICIENT/2)**2
    # In Hertz sqaured

    # This equation does not have an end state so instead we load twenty
    # Oscillations as our max using the frequency. Then we calculated the
    # Minimum time, points, step and time span vector
    tMax = np.sqrt(np.abs(SOLUTIONCOEFFICIENT))  # In seconds
    tMin = 0                                        # In seconds
    Points = 250
    Step = (tMax-tMin)/Points
    TimeSpan = np.arange(tMin, tMax, Step)

    # Finally the Numerical vectors are once again calculated and then used
    # To calculated the graphs of the motion. Each graph plots the odeint
    # Euler, improved Euler, and Runge-Kutta methods. Now uses the two plot
    # Feature that we explained earlier
    odeintVector = odeint(differentialDamped, INITIALVECTOR, TimeSpan)
    EulerVector = EulerMethod(differentialDamped,
                              tMin, tMax, INITIALVECTOR, Step)
    ImprovedEulerVector = ImprovedEulerMethod(differentialDamped,
                                              tMin, tMax, INITIALVECTOR, Step)
    RungeKuttaVector = RungeKuttaMethod(differentialDamped,
                                        tMin, tMax, INITIALVECTOR, Step)
    plotGraphs(2, DampedPosition, DampedVelocity,
               odeintVector, EulerVector,
               ImprovedEulerVector, RungeKuttaVector, TimeSpan, tMax,
               'Approximation of Position in Damped Spring System',
               'Position (seconds)', 'Time (secnods)',
               'Approximation of Velocity in Damped Spring System',
               'Velocity (meters/second)', 'Time (seconds)')


# This function is once again similar to the previous one attacking the forced
# Undamped oscillation equations rather than the damped one
def ForcedUndampedEquation():
    # Once again is defining the constants using the prompt function
    promptConstants(promptForcedUndamped)
    INITIALVECTOR = [0, INITIALX]

    # Then we calculate the time we want to view as the time for ten
    # Oscillations of the spring, and then set up the time vector
    tMax = 10*np.sqrt(SPRINGCONSTANT/MASS)  # In seconds
    tMin = 0                                # In seconds
    Points = 250
    Step = (tMax-tMin)/Points
    TimeSpan = np.arange(tMin, tMax, Step)

    # Once again using all four numerical solutions we calculate our necessary
    # Arrays and then plot all the graphs that we need, using two plots
    odeintVector = odeint(differentialForcedUndamped, INITIALVECTOR, TimeSpan)
    EulerVector = EulerMethod(differentialForcedUndamped,
                              tMin, tMax, INITIALVECTOR, Step)
    ImprovedEulerVector = ImprovedEulerMethod(differentialForcedUndamped,
                                              tMin, tMax, INITIALVECTOR, Step)
    RungeKuttaVector = RungeKuttaMethod(differentialForcedUndamped,
                                        tMin, tMax, INITIALVECTOR, Step)
    plotGraphs(2, ForcedUndampedPosition, ForcedUndampedVelocity,
               odeintVector, EulerVector, ImprovedEulerVector,
               RungeKuttaVector, TimeSpan, tMax,
               'Approximation of Position in Forced Undamped Spring System',
               'Position (seconds)', 'Time (secnods)',
               'Approximation of Velocity in Forced Undamped Spring System',
               'Velocity (meters/second)', 'Time (seconds)')


# Lastly is our custom system of differential equations, which is much more
# Open than the last two functions and allows for more user input
def CustomEquation():
    # Once again beginning with the prompting for the system
    promptConstants(promptCustom)

    # Ask how long the system wants to be observed for and for how many points
    # Then calculates the step size and creates the time span vector
    timePrompt = 'How long would you like to observe this system of equations?'
    tMax = int(input(timePrompt+' '))
    tMin = 0
    Points = int(input('How many points would you like to observe? '))
    Step = (tMax-tMin)/Points
    TimeSpan = np.arange(tMin, tMax, Step)

    # Only uses odeint, Euler, Improved Euler, and Runge Kutta to calculate
    # Just numerical solutions and does not plot analytical solutions
    # Then calls the special custom plot function
    odeintVector = odeint(differentialCustom, CustomVector, TimeSpan)
    EulerVector = EulerMethod(differentialCustom,
                              tMin, tMax, CustomVector, Step)
    ImprovedEulerVector = ImprovedEulerMethod(differentialCustom,
                                              tMin, tMax, CustomVector, Step)
    RungeKuttaVector = RungeKuttaMethod(differentialCustom,
                                        tMin, tMax, CustomVector, Step)
    plotCustom(odeintVector, EulerVector, ImprovedEulerVector,
               RungeKuttaVector, TimeSpan)

# A list of the built-in physical systems that can be modelled using this code
BUILTINSYSTEMS = np.array(['Ballistic Motion',
                           'Motion through Viscous Liquids',
                           'Damped Harmonic Oscillations',
                           'Forced Harmonic Oscillations Without Damping',
                           'Custom Constant Coefficient System of Equations'])

# A series of initial values for the example problem
DRAG = 0.7
MASS = 0.1
GRAVITY = 9.81
INITIALVX = 10
INITIALVY = 10

# The function is run using the above initial conditions
BallisticEquation(first=True)

# Then the figure is saved to the desired file
figsave = '/Users/ryank/Desktop/Work/Python/PHYS210/'
figsave = figsave + 'Project 1-Ballistic/ballistic.pdf'
plt.savefig(figsave)

# Finally the data is analyzed and entered into the desired file
# Answers the questions of the maximum distance, maximum height, air time and
# The final velocity vector and magnitude of the object with conditions above
questionsave = '/Users/ryank/Desktop/Work/Python/PHYS210/'
questionsave = questionsave + 'Project 1-Ballistic/ballistic.txt'
file = open(questionsave, 'w')
file.write("The object has initial conditions with:\n")
file.write("\tDrag of {}kg/s\n".format(DRAG))
file.write("\tMass of {}kg\n".format(MASS))
file.write("\tGravitational acceleration of {}m/s^2\n".format(GRAVITY))
file.write("\tInitial x-direction velocity of {}m/s\n".format(INITIALVX))
file.write("\tInitial y-direction velocity of {}m/s\n\n".format(INITIALVY))
text = "The distance the object travels is {}m\n"
select = odeintVector[1:, 3] == min(abs(odeintVector[1:, 3]))
MaxX = odeintVector[np.where(select), 2][0, 0]
file.write(text.format(MaxX))
text = "The object has a maximum height of {}m\n"
MaxY = max(odeintVector[:, 3])
file.write(text.format(MaxY))
text = "The object has an air time of {}s\n"
MaxT = TimeSpan[np.where(odeintVector[1:, 3] == min(abs(odeintVector[1:, 3])))]
file.write(text.format(MaxT))
text = "The object has a final velocity of <{}, {}> m/s\n"
EndVX = odeintVector[np.where(select), 0]
EndVY = odeintVector[np.where(select), 1]
file.write(text.format(EndVX, EndVY))
text = "The object has a final velocity magnitude of {}m/s\n"
EndV = np.sqrt(EndVX**2+EndVY**2)
file.write(text.format(EndV))
file.close()

print('There are other differential equations in physics that we can look at.')
againPrompt = 'Would you like to look at different initial conditions or'
againPrompt = againPrompt + ' a different physical system? (Yes/No) '
SystemPrompt = 'What physical system would you like to look at? '
SystemPrompt += '(Enter List to view the list of systems or Cancel to exit) '
again = input(againPrompt)

while again.lower() == 'yes':
    print()
    System = input(SystemPrompt)

    if System.lower() == 'list':
        for indx in range(len(BUILTINSYSTEMS)):
            print(BUILTINSYSTEMS[indx])
    elif System.lower() == 'cancel':
        break
    elif System.lower() in map(lambda x: x.lower(), BUILTINSYSTEMS):
        lookupSystem(System)
        again = input(againPrompt)
    else:
        print('Input not understood. Please try again.')
