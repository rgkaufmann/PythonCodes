import scipy as sp
from scipy import constants, integrate, linalg
import matplotlib.pyplot as plt
from matplotlib import animation
### Paramters of interest ###
###############################################################################

num_states = 240	# Number of states in the basis
num_steps = 10000 # Number of steps in the animation
time_per_step = 5e3/num_steps # [s]
k = 0

# Function to create the n'th eigenstate
def spatial(x, a, n):
    return sp.sqrt(2/a)*sp.sin(n*sp.pi/a*x)

# Initial wavefunction (t=0)
def wavefunction(x, A, a, FWHM, average):
    sigma = FWHM/(2*sp.sqrt(2*sp.log(2)))
    constant = A*sp.sqrt(1/(sigma*sp.sqrt(2*sp.pi)))
    exponential = sp.exp(-0.5*((x-average)/(sigma))**2)
    complexAddition = sp.exp(1j*k*x)
    return constant*exponential*complexAddition

###############################################################################

### Specify the infinite square well domain
a = 1
 # Basis is (0 <= x <= a)
xs = sp.linspace(start=0, stop=a, num=int(1e3), endpoint=True)

### Initialize the wave function
A = 1 # set to 1 before normalization
# Initial probability density (t=0)
def probability(x, A, a):
	return abs(wavefunction(x, A, a, a/10, a/2))**2

### Normalize the wavefunction
(y, abserr) = integrate.quad(func=probability, args=(A, a), a=0, b=a)
A = sp.sqrt(1/y)
print('Normalization Constant: {:0.3e}'.format(A))

###############################################################################

### Expand the wave function over energy eigenstates
# Function to generate a "basis" out of the first n eigenstates
def formBasis(x, a, num_states, factor): 
	basis = sp.array([]).reshape(len(x), 0)
	for n in range(1, num_states+1):
		psi_n = spatial(x, a, n*factor)
		basis = sp.hstack((basis, psi_n[:,sp.newaxis]))
	return basis

###############################################################################

# Create a basis to expand over
basisQuarter = formBasis(xs, a, num_states, 0.25)
basisHalf = formBasis(xs, a, num_states, 0.5)
basisInteger = formBasis(xs, a, num_states, 1)
# Find the least-squares projection of wf_0 onto the basis
cnsQuarter = linalg.lstsq(basisQuarter, wavefunction(xs, A, a, a/10, a/2))[0]
cnsHalf = linalg.lstsq(basisHalf, wavefunction(xs, A, a, a/10, a/2))[0]
cnsInteger = linalg.lstsq(basisInteger, wavefunction(xs, A, a, a/10, a/2))[0]
# Compare to Griffith's value
print('|c_1|^2 (Quarter) = {:0.6f}'.format(abs(cnsQuarter[0])**2))
print('|c_1|^2 (Half) = {:0.6f}'.format(abs(cnsHalf[0])**2))
print('|c_1|^2 (Integer) = {:0.6f}'.format(abs(cnsInteger[0])**2))
# Ensure coefficient's sum to 1
print('Sum(|c_n|^2) (Quarter) = {:0.6f}'.format(sp.sum(abs(cnsQuarter)**2)))
print('Sum(|c_n|^2) (Half) = {:0.6f}'.format(sp.sum(abs(cnsHalf)**2)))
print('Sum(|c_n|^2) (Integer) = {:0.6f}'.format(sp.sum(abs(cnsInteger)**2)))

###############################################################################

### Plot the initial wavefunction, its expansion, and the time evolved solution
fig, ax = plt.subplots(2, 1)
ax[0].plot(xs, abs(wavefunction(xs, A, a, a/10, a/2)),
           label='$|\\mathrm{wf}_0|$')
ax[0].plot(xs, abs(sp.dot(basisInteger,cnsInteger)), label='$|\\mathrm{wf}_0$ Expansion|')
wf_t_pltQuarter, = ax[0].plot([], [], label='$|\\mathrm{wf}_{t}|$')
wf_t_pltHalf, = ax[0].plot([], [], label='$|\\mathrm{wf}_{t}|$')
wf_t_pltInteger, = ax[0].plot([], [], label='$|\\mathrm{wf}_{t}|$')
time_measure = ax[0].text(-0.01, 3, 'Time = ' + str(0) + 's')
ax[0].set_title('Initial, Expanded, and Time-Evolved Wavefunction')
ax[0].set_xlabel('x [m]')
ax[0].set_ylabel('$|\\Psi(x,t)|$')
ax[0].legend(loc='upper right')

###############################################################################

### plot magnitude-squard c_n values
ax[1].stem(
	sp.arange(1,len(cnsInteger)+1)*0.25,
	abs(cnsQuarter)**2,
	linefmt='C1-',
	markerfmt='C1o',
	basefmt='k')
ax[1].stem(
	sp.arange(1,len(cnsInteger)+1)*0.5,
	abs(cnsHalf)**2,
	linefmt='C1-',
	markerfmt='C1o',
	basefmt='k')
ax[1].stem(
	sp.arange(1,len(cnsInteger)+1),
	abs(cnsInteger)**2,
	linefmt='C1-',
	markerfmt='C1o',
	basefmt='k')
ax[1].set_title('Expansion Coefficients')
ax[1].set_xlabel('n')
ax[1].set_ylabel('$|c_n|^2$')
plt.tight_layout()

###############################################################################

### Propagate wavefucntion in time
# Function to create the time-dependence of the n'th eigenstate
def temporal(t, a, num_states, m, factor):
    n = sp.arange(1, num_states+1)*factor
    En = (n*sp.pi*constants.hbar/a)**2/(2*m)
    return sp.exp(-1j*En*t/constants.hbar)

def init(): # initialization function: plot the background of each frame
    wf_t_pltQuarter.set_data([], [])
    wf_t_pltHalf.set_data([], [])
    wf_t_pltInteger.set_data([], [])
    return wf_t_pltQuarter, wf_t_pltHalf, wf_t_pltInteger, time_measure,

def animate(i): # animation function.  This is called sequentially
    phi_t = temporal(i*time_per_step, a, num_states, constants.electron_mass,
                     0.25)
    wf_t = abs(sp.dot(basisQuarter, cnsQuarter*phi_t))
    wf_t_pltQuarter.set_data(xs, wf_t)
    phi_t = temporal(i*time_per_step, a, num_states, constants.electron_mass,
                     0.5)
    wf_t = abs(sp.dot(basisHalf, cnsHalf*phi_t))
    wf_t_pltHalf.set_data(xs, wf_t)
    phi_t = temporal(i*time_per_step, a, num_states, constants.electron_mass,
                     1)
    wf_t = abs(sp.dot(basisInteger, cnsInteger*phi_t))
    wf_t_pltInteger.set_data(xs, wf_t)
    time_measure.set_text('Time = ' + str(i*time_per_step) + 's')
    #The below commented code will save images at certain values of t
#    if i==0 or i==100 or i==200 or i==300 or i==400:
#        filename = 'LowkGuassianFrame{}PHYS304.pdf'.format(i)
#        plt.savefig(filename)
    return wf_t_pltQuarter, wf_t_pltHalf, wf_t_pltInteger, time_measure,

###############################################################################

### Call the animator.
### blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=(num_steps+1), interval=10, blit=True,
                               repeat=False)
### Show Plot
plt.show()

###############################################################################