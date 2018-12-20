import numpy as np                  # Importing necessary functions:
import matplotlib.pyplot as plt     # numpy for arrays, pyplot for plotting
from scipy.integrate import odeint  # odeint for differential equations


# Plots the oscillations of the the spring at three locations: above, below,
# And at resonance, including correct scales and titles.
def plotOscillations(Below, Above, At, Time):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    ax1.plot(Time, Below[:, 1])
    ax1.set_ylabel('X-Position (m)')
    ax1.set_title('Oscillations Below Resonance Frequency')
    ax1.set_ylim(-max(Below[:, 1])*1.1, max(Below[:, 1])*1.1)
    ax2.plot(Time, At[:, 1])
    ax2.set_ylabel('X-Position (m)')
    ax2.set_title('Oscillations At Resonance Frequency')
    ax2.set_ylim(-max(At[:, 1])*1.1, max(At[:, 1])*1.1)
    ax3.plot(Time, Above[:, 1])
    ax3.set_ylabel('X-Position (m)')
    ax3.set_title('Oscillations Above Resonance Frequency')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylim(-max(Above[:, 1])*1.1, max(Above[:, 1])*1.1)
    fig.subplots_adjust(hspace=.5)
    plt.savefig('Oscillations.pdf')
    plt.show()


# Plots the steady state amplitudes of various frequencies as a function of
# the ratio between the frequency and resonant frequency
def plotResonance(Amplitudes, Frequencies):
    plt.plot(Frequencies, Amplitudes)
    plt.title('Steady State Amplitudes at Various Frequencies')
    plt.xlabel('Frequency Ratio')
    plt.ylabel('Steady State Amplitude')
    plt.savefig('Resonance.pdf')
    plt.show()


# Prompts the user for the constants used in the calculation of the derivatives
# Time spans, and resonance
def promptForcedDamped():
    print('Please enter values between 0.1 and 100')
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


# The differential equation for the spring machanism
def differentialForcedDamped(Vector, Time, freq):
    velocity = Vector[0]
    position = Vector[1]
    acceleration = FORCE/MASS*np.cos(freq*Time)
    acceleration += -SPRINGCONSTANT/MASS*position-DAMPINGCONSTANT/MASS*velocity
    return [acceleration,
            velocity]


# Performs all necessary calculations and fuction calls for the differential
# Equations
def ForcedDampedEquation():
    # Receives the constants and calculates the resonance frequency, initial
    # Conditions of the equations, and the list of frequencies to be looked at
    promptForcedDamped()
    if DAMPINGCONSTANT**2/(2*MASS**2) > SPRINGCONSTANT/MASS:
        RESONANCE = np.sqrt(SPRINGCONSTANT/MASS)
    else:
        RESONANCE = np.sqrt(SPRINGCONSTANT/MASS-DAMPINGCONSTANT**2/(2*MASS**2))
    INITIALVECTOR = [INITIALV, INITIALX]
    frequencies = np.arange(1/4*RESONANCE, 3/2*RESONANCE, (5/4*RESONANCE)/100)

    # Creates all the time scales to view the oscillations and such
    tMax = (10*np.log(0.01)*2*MASS)/(-DAMPINGCONSTANT*2)  # In seconds
    tMin = 0                                              # In seconds
    Step = np.pi/(16*RESONANCE)
    TimeSpan = np.arange(tMin, tMax, Step)
    maxAmp = []
    SteadyState = int(np.ceil(tMax/(2*Step)))

    # Calculates and plots the amplitudes of the steady state solutions
    for frequency in frequencies:
        odeintVector = odeint(differentialForcedDamped, INITIALVECTOR,
                              TimeSpan, args=(frequency, ))
        maxAmp.append(np.max(odeintVector[SteadyState:, 1]))

    plotResonance(maxAmp, frequencies/RESONANCE)

    # Calculates and plots the solution to the position differential equation
    # Before, after, and at the resonance frequency
    odeintVectorBelow = odeint(differentialForcedDamped, INITIALVECTOR,
                               TimeSpan, args=(1/2*RESONANCE, ))
    odeintVectorAt = odeint(differentialForcedDamped, INITIALVECTOR,
                            TimeSpan, args=(RESONANCE, ))
    odeintVectorAbove = odeint(differentialForcedDamped, INITIALVECTOR,
                               TimeSpan, args=(2*RESONANCE, ))
    plotOscillations(odeintVectorBelow, odeintVectorAbove, odeintVectorAt,
                     TimeSpan)

# Repeatable call for calculations that lets various initial conditions to be
# Tried
again = 'Yes'
while again.lower() == 'yes':
    print()
    ForcedDampedEquation()
    again = input('Would you like observe another set of initial conditions? ')