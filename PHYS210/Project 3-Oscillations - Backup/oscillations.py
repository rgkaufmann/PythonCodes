import numpy as np                  # Importing necessary functions:
import matplotlib.pyplot as plt     # numpy for arrays, pyplot for plotting
from scipy.integrate import odeint  # odeint for differential equations


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


def plotOscillations(Below, Above, At, Time):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    ax1.plot(Time, Below[:,1])
    ax1.set_ylabel('X-Position (m)')
    ax1.set_title('Oscillations Below Resonance Frequency')
    ax1.set_ylim(-max(Below[:,1])*1.1, max(Below[:,1])*1.1)
    ax2.plot(Time, At[:,1])
    ax2.set_ylabel('X-Position (m)')
    ax2.set_title('Oscillations At Resonance Frequency')
    ax2.set_ylim(-max(At[:,1])*1.1, max(At[:,1])*1.1)
    ax3.plot(Time, Above[:,1])
    ax3.set_ylabel('X-Position (m)')
    ax3.set_title('Oscillations Above Resonance Frequency')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylim(-max(Above[:,1])*1.1, max(Above[:,1])*1.1)
    plt.savefig('Oscillations.pdf')
    plt.show()


def plotResonance(Amplitudes, Frequencies):
    plt.plot(Frequencies, Amplitudes)
    plt.title('Steady State Amplitudes at Various Frequencies')
    plt.xlabel('Frequency Ratio')
    plt.ylabel('Steady State Amplitude')
    plt.savefig('Resonance.pdf')
    plt.show()


def promptConstants(SystemPrompt):
    print('Please enter values greater than 0')
    SystemPrompt()


def promptForcedDamped():
    promptSpring = 'What is the spring constant of the spring in kg/s^2? '
    promptDamp = 'What is the damping constant in kg/s? '
    promptForce = 'What is the magnitude of the external force in kg*m/s^2? '
    promptX = 'What is the initial position of the ball in m? '
    promptV = 'What is the initial velocity of the ball in m/s? '
    global FORCE            # In kilogram-meters per seconds squared
    global MASS             # In kilograms
    global SPRINGCONSTANT   # In kilograms per seconds squared
    global DAMPINGCONSTANT  # In kilograms per second
    global INITIALX         # In meters
    global INITIALV         # In meters per second
    try:
        FORCE = float(input(promptForce))
        MASS = float(input('What is the mass of the ball in kg? '))
        SPRINGCONSTANT = float(input(promptSpring))
        DAMPINGCONSTANT = float(input(promptDamp))
        INITIALX = float(input(promptX))
        INITIALV = float(input(promptV))
    except ValueError:
        print('Values are not numbers, please try again.')
        promptForcedDamped()


def differentialForcedDamped(Vector, Time, freq):
    velocity = Vector[0]
    position = Vector[1]
    acceleration = FORCE/MASS*np.cos(freq*Time)
    acceleration += -SPRINGCONSTANT/MASS*position-DAMPINGCONSTANT/MASS*velocity
    return [acceleration,
            velocity]


def ForcedDampedPosition(time):
    return 0


def ForcedDampedVelocity(time):
    return 0


def ForcedDampedEquation():
    promptConstants(promptForcedDamped)
    RESONANCE = np.sqrt(SPRINGCONSTANT/MASS)
    INITIALVECTOR = [INITIALV, INITIALX]
    
    frequencies = np.arange(1/8*RESONANCE, 3/2*RESONANCE, (11/8*RESONANCE)/100)

    tMax = 40*np.pi/np.sqrt(SPRINGCONSTANT/MASS)  # In seconds
    tMin = 0                                      # In seconds
    Points = 500
    Step = (tMax-tMin)/Points
    TimeSpan = np.arange(tMin, tMax, Step)
    maxAmp = []
    
    for frequency in frequencies:
        odeintVector = odeint(differentialForcedDamped, INITIALVECTOR,
                              TimeSpan, args=(frequency, ))
        maxAmp.append(np.max(odeintVector[300:,1]))

    plotResonance(maxAmp, frequencies/RESONANCE)
    
    odeintVectorBelow = odeint(differentialForcedDamped, INITIALVECTOR,
                               TimeSpan, args=(1/2*RESONANCE, ))
    odeintVectorAt = odeint(differentialForcedDamped, INITIALVECTOR,
                            TimeSpan, args=(RESONANCE, ))
    odeintVectorAbove = odeint(differentialForcedDamped, INITIALVECTOR,
                               TimeSpan, args=(2*RESONANCE, ))
    plotOscillations(odeintVectorBelow, odeintVectorAbove, odeintVectorAt,
                     TimeSpan)

again = 'Yes'
while again.lower() == 'yes':
    print()
    ForcedDampedEquation()
    again = input('Would you like observe another set of initial conditions? ')