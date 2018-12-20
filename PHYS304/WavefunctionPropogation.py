import scipy as sp
from scipy import constants, integrate, linalg
import matplotlib.pyplot as plt
from matplotlib import animation
### Paramters of interest ###
###############################################################################

# Function to create the n'th eigenstate
def spatial(x, a, n):
	return sp.sqrt(2/a)*sp.sin(n*sp.pi/a*x)

# Initial wavefunction (t=0)
def wavefunction(x, A, a, phi):
	return A/sp.sqrt(2)*(spatial(x, a, 1)+sp.exp(1j*phi)*spatial(x, a, 2)  )
num_states = 15	# Number of states in the basis
num_steps = 1000 # Number of steps in the animation
time_per_step = 10e3/num_steps # [s]

###############################################################################

### Specify the infinite square well domain
a = 1
 # Basis is (0 <= x <= a)
xs = sp.linspace(start=0, stop=a, num=int(1e3), endpoint=True)

### Initialize the wave function
A = 1 # set to 1 before normalization
# Initial probability density (t=0)
def probability(x, A, a):
	return abs(wavefunction(x, A, a, 0))**2

### Normalize the wavefunction
(y, abserr) = integrate.quad(func=probability, args=(A, a), a=0, b=a)
A = sp.sqrt(1/y)
print('Normalization Constant: {:0.3e}'.format(A))

###############################################################################

### Expand the wave function over energy eigenstates
# Function to generate a "basis" out of the first n eigenstates
def formBasis(x, a, num_states): 
	basis = sp.array([]).reshape(len(x), 0)
	for n in range(1, num_states+1):
		psi_n = spatial(x, a, n)
		basis = sp.hstack((basis, psi_n[:,sp.newaxis]))
	return basis

###############################################################################

# Create a basis to expand over
basisZero = formBasis(xs, a, num_states)
basisHalf = formBasis(xs, a, num_states)
basisAtPi = formBasis(xs, a, num_states)
basisThir = formBasis(xs, a, num_states)
basisSixt = formBasis(xs, a, num_states)
# Find the least-squares projection of wf_0 onto the basis
cnsZero = linalg.lstsq(basisZero, wavefunction(xs, A, a, 0))[0]
cnsHalf = linalg.lstsq(basisHalf, wavefunction(xs, A, a, sp.pi/2))[0]
cnsAtPi = linalg.lstsq(basisAtPi, wavefunction(xs, A, a, sp.pi))[0]
cnsThir = linalg.lstsq(basisThir, wavefunction(xs, A, a, sp.pi/3))[0]
cnsSixt = linalg.lstsq(basisSixt, wavefunction(xs, A, a, sp.pi/6))[0]
# Compare to Griffith's value
print('|c_1|^2 = {:0.6f}'.format(abs(cnsZero[0])**2))
print('|c_1|^2 = {:0.6f}'.format(abs(cnsHalf[0])**2))
print('|c_1|^2 = {:0.6f}'.format(abs(cnsAtPi[0])**2))
print('|c_1|^2 = {:0.6f}'.format(abs(cnsThir[0])**2))
print('|c_1|^2 = {:0.6f}'.format(abs(cnsSixt[0])**2))
# Ensure coefficient's sum to 1
print('Sum(|c_n|^2) = {:0.6f}'.format(sp.sum(abs(cnsZero)**2)))
print('Sum(|c_n|^2) = {:0.6f}'.format(sp.sum(abs(cnsHalf)**2)))
print('Sum(|c_n|^2) = {:0.6f}'.format(sp.sum(abs(cnsAtPi)**2)))
print('Sum(|c_n|^2) = {:0.6f}'.format(sp.sum(abs(cnsThir)**2)))
print('Sum(|c_n|^2) = {:0.6f}'.format(sp.sum(abs(cnsSixt)**2)))

###############################################################################

### Plot the initial wavefunction, its expansion, and the time evolved solution

fig, ax = plt.subplots(2, 3)
fig.suptitle('Initial, Expanded, and Time-Evolved Wavefunction At Various Values of Phi')

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

ax[0, 0].plot(xs, abs(wavefunction(xs, A, a, 0)), label='$|\\mathrm{wf}_0|$')
ax[0, 0].plot(xs, abs(sp.dot(basisZero, cnsZero)),
           label='$|\\mathrm{wf}_0$ Expansion|')
waveFunctionZero, = ax[0, 0].plot([], [], label='$|\\mathrm{wf}_{t}|$')
timeMeasureZero = ax[0, 0].text(-0.01, 1.9, 'Time = ' + str(0) + 's')
ax[0, 0].set_xlim(-0.1, 1.1)
ax[0, 0].set_ylim(-0.1, 2)
ax[0, 0].set_title(r'$\phi=0$')
ax[0, 0].set_xlabel('x [m]')
ax[0, 0].set_ylabel('$|\\Psi(x,t)|$')
ax[0, 0].legend(loc='upper right')

ax[0, 1].plot(xs, abs(wavefunction(xs, A, a, sp.pi/2)), label='$|\\mathrm{wf}_0|$')
ax[0, 1].plot(xs, abs(sp.dot(basisHalf, cnsHalf)),
           label='$|\\mathrm{wf}_0$ Expansion|')
waveFunctionHalf, = ax[0, 1].plot([], [], label='$|\\mathrm{wf}_{t}|$')
timeMeasureHalf = ax[0, 1].text(-0.01, 1.9, 'Time = ' + str(0) + 's')
ax[0, 1].set_xlim(-0.1, 1.1)
ax[0, 1].set_ylim(-0.1, 2)
ax[0, 1].set_title(r'$\phi=\pi/2$')
ax[0, 1].set_xlabel('x [m]')
ax[0, 1].set_ylabel('$|\\Psi(x,t)|$')
ax[0, 1].legend(loc='upper right')

ax[0, 2].plot(xs, abs(wavefunction(xs, A, a, sp.pi)), label='$|\\mathrm{wf}_0|$')
ax[0, 2].plot(xs, abs(sp.dot(basisAtPi, cnsAtPi)),
           label='$|\\mathrm{wf}_0$ Expansion|')
waveFunctionAtPi, = ax[0, 2].plot([], [], label='$|\\mathrm{wf}_{t}|$')
timeMeasureAtPi = ax[0, 2].text(-0.01, 1.9, 'Time = ' + str(0) + 's')
ax[0, 2].set_xlim(-0.1, 1.1)
ax[0, 2].set_ylim(-0.1, 2)
ax[0, 2].set_title(r'$\phi=\pi$')
ax[0, 2].set_xlabel('x [m]')
ax[0, 2].set_ylabel('$|\\Psi(x,t)|$')
ax[0, 2].legend(loc='upper right')

###############################################################################

### plot magnitude-squard c_n values
ax[1, 0].stem(sp.arange(1,len(cnsZero)+1), abs(cnsZero)**2, linefmt='C1-',
           markerfmt='C1o', basefmt='k')
ax[1, 0].set_title('Expansion Coefficients')
ax[1, 0].set_xlabel('n')
ax[1, 0].set_ylabel('$|c_n|^2$')

ax[1, 1].plot(xs, abs(wavefunction(xs, A, a, sp.pi/3)), label='$|\\mathrm{wf}_0|$')
ax[1, 1].plot(xs, abs(sp.dot(basisThir, cnsThir)),
           label='$|\\mathrm{wf}_0$ Expansion|')
waveFunctionThir, = ax[1, 1].plot([], [], label='$|\\mathrm{wf}_{t}|$')
timeMeasureThir = ax[1, 1].text(-0.01, 1.9, 'Time = ' + str(0) + 's')
ax[1, 1].set_xlim(-0.1, 1.1)
ax[1, 1].set_ylim(-0.1, 2)
ax[1, 1].set_title(r'$\phi=\pi$/3')
ax[1, 1].set_xlabel('x [m]')
ax[1, 1].set_ylabel('$|\\Psi(x,t)|$')
ax[1, 1].legend(loc='upper right')

ax[1, 2].plot(xs, abs(wavefunction(xs, A, a, sp.pi/6)), label='$|\\mathrm{wf}_0|$')
ax[1, 2].plot(xs, abs(sp.dot(basisSixt, cnsSixt)),
           label='$|\\mathrm{wf}_0$ Expansion|')
waveFunctionSixt, = ax[1, 2].plot([], [], label='$|\\mathrm{wf}_{t}|$')
timeMeasureSixt = ax[1, 2].text(-0.01, 1.9, 'Time = ' + str(0) + 's')
ax[1, 2].set_xlim(-0.1, 1.1)
ax[1, 2].set_ylim(-0.1, 2)
ax[1, 2].set_title(r'$\phi=\pi/6$')
ax[1, 2].set_xlabel('x [m]')
ax[1, 2].set_ylabel('$|\\Psi(x,t)|$')
ax[1, 2].legend(loc='upper right')

plt.tight_layout()

###############################################################################

### Propagate wavefucntion in time
# Function to create the time-dependence of the n'th eigenstate
def temporal(t, a, num_states, m=1):
	n = sp.arange(1, num_states+1)
	En = (n*sp.pi*constants.hbar/a)**2/(2*m)
	return sp.exp(-1j*En*t/constants.hbar)

def init(): # initialization function: plot the background of each frame
    waveFunctionZero.set_data([], [])
    waveFunctionHalf.set_data([], [])
    waveFunctionAtPi.set_data([], [])
    waveFunctionThir.set_data([], [])
    waveFunctionSixt.set_data([], [])
    return waveFunctionZero, waveFunctionHalf, waveFunctionAtPi, waveFunctionThir, waveFunctionSixt, timeMeasureZero, timeMeasureHalf, timeMeasureAtPi, timeMeasureThir, timeMeasureSixt

def animate(i): # animation function.  This is called sequentially
    phi_t = temporal(i*time_per_step, a, num_states, m=constants.electron_mass)
    waveFunctionTemporalZero = abs(sp.dot(basisZero, cnsZero*phi_t))
    waveFunctionZero.set_data(xs, waveFunctionTemporalZero)
    waveFunctionTemporalHalf = abs(sp.dot(basisHalf, cnsHalf*phi_t))
    waveFunctionHalf.set_data(xs, waveFunctionTemporalHalf)
    waveFunctionTemporalAtPi = abs(sp.dot(basisAtPi, cnsAtPi*phi_t))
    waveFunctionAtPi.set_data(xs, waveFunctionTemporalAtPi)
    waveFunctionTemporalThir = abs(sp.dot(basisThir, cnsThir*phi_t))
    waveFunctionThir.set_data(xs, waveFunctionTemporalThir)
    waveFunctionTemporalSixt = abs(sp.dot(basisSixt, cnsSixt*phi_t))
    waveFunctionSixt.set_data(xs, waveFunctionTemporalSixt)
    timeMeasureZero.set_text('Time = ' + str(i*time_per_step) + 's')
    timeMeasureHalf.set_text('Time = ' + str(i*time_per_step) + 's')
    timeMeasureAtPi.set_text('Time = ' + str(i*time_per_step) + 's')
    timeMeasureThir.set_text('Time = ' + str(i*time_per_step) + 's')
    timeMeasureSixt.set_text('Time = ' + str(i*time_per_step) + 's')
    #The below commented code will save images at certain values of t
    if i==100:
        filename = 'MultiplePhiFrame{}PHYS304.pdf'.format(i)
        plt.savefig(filename)
    return waveFunctionZero, waveFunctionHalf, waveFunctionAtPi, waveFunctionThir, waveFunctionSixt, timeMeasureZero, timeMeasureHalf, timeMeasureAtPi, timeMeasureThir, timeMeasureSixt

###############################################################################

### Call the animator.
### blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=(num_steps+1), interval=20, blit=True,
                               repeat=False)
### Show Plot
plt.show()

###############################################################################