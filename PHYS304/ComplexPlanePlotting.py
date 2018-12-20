import numpy as np
import matplotlib.pyplot as plt

def wavefunc(x, t):
    m = 9.109383e-31
    w = 1
    h = 1.0545718e-34
    a0 = ((m*w)/(np.pi*h))**(1/4)
    a1 = np.sqrt(2)*a0
    psi0 = np.exp(-(m*w)/(2*h)*x**2)
    phi0 = np.exp(-(1j*t)/(2)*w)
    psi1 = np.sqrt(m*w/h)*x*np.exp(-(m*w)/(2*h)*x**2)
    phi1 = np.exp(-(3j*t)/(2)*w)
    return 1/np.sqrt(2)*(a0*psi0*phi0+a1*psi1*phi1), phi0, phi1

xValues = np.linspace(-0.04, 0.04, 10000)
tValues = (0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4,
           5*np.pi/6, np.pi, 7*np.pi/6, 5*np.pi/4, 4*np.pi/3, 3*np.pi/2,
           5*np.pi/3, 7*np.pi/4, 11*np.pi/6, 2*np.pi)

#for tval in tValues:
#    wave, phase1, phase2 = wavefunc(xValues, tval)
#    wavefuncsquared = np.abs(wave)**2
#    ax = plt.subplot(111)
#    ax.plot(xValues, wavefuncsquared)
#    ax.set_title("Probability at t={:.3f}".format(tval))
#    plt.show()
#    
#    ax = plt.subplot(111)
#    ax.set_title("Phasors at t={:.3f}".format(tval))
#    ax.quiver([0], [0], 10*np.real(phase1), 10*np.imag(phase1), label='Psi-naught', color='b', scale=30)
#    ax.quiver([0], [0], 10*np.real(phase2), 10*np.imag(phase2), label='Psi-one', color='r', scale=30)
#    ax.legend(loc='best')
#    plt.show()

wave, phase1, phase2 = wavefunc(xValues, 0)
wavefuncsquared = np.abs(wave)**2
ax1 = plt.subplot(241)
ax1.plot(xValues, wavefuncsquared)
ax1.set_title("Probability at t={:.3f}".format(0))
ax5 = plt.subplot(245)
ax5.set_title("Phasors at t={:.3f}".format(0))
ax5.quiver([0], [0], 10*np.real(phase1), 10*np.imag(phase1), label='Psi-naught', color='b', scale=30)
ax5.quiver([0], [0], 10*np.real(phase2), 10*np.imag(phase2), label='Psi-one', color='r', scale=30)
ax5.legend(loc='best')

wave, phase1, phase2 = wavefunc(xValues, np.pi/4)
wavefuncsquared = np.abs(wave)**2
ax2 = plt.subplot(242)
ax2.plot(xValues, wavefuncsquared)
ax2.set_title("Probability at t={:.3f}".format(np.pi/4))
ax6 = plt.subplot(246)
ax6.set_title("Phasors at t={:.3f}".format(np.pi/4))
ax6.quiver([0], [0], 10*np.real(phase1), 10*np.imag(phase1), label='Psi-naught', color='b', scale=30)
ax6.quiver([0], [0], 10*np.real(phase2), 10*np.imag(phase2), label='Psi-one', color='r', scale=30)
ax6.legend(loc='best')

wave, phase1, phase2 = wavefunc(xValues, np.pi/2)
wavefuncsquared = np.abs(wave)**2
ax3 = plt.subplot(243)
ax3.plot(xValues, wavefuncsquared)
ax3.set_title("Probability at t={:.3f}".format(np.pi/2))
ax7 = plt.subplot(247)
ax7.set_title("Phasors at t={:.3f}".format(np.pi/2))
ax7.quiver([0], [0], 10*np.real(phase1), 10*np.imag(phase1), label='Psi-naught', color='b', scale=30)
ax7.quiver([0], [0], 10*np.real(phase2), 10*np.imag(phase2), label='Psi-one', color='r', scale=30)
ax7.legend(loc='best')

wave, phase1, phase2 = wavefunc(xValues, 3*np.pi/4)
wavefuncsquared = np.abs(wave)**2
ax4 = plt.subplot(244)
ax4.plot(xValues, wavefuncsquared)
ax4.set_title("Probability at t={:.3f}".format(3*np.pi/4))
ax8 = plt.subplot(248)
ax8.set_title("Phasors at t={:.3f}".format(3*np.pi/4))
ax8.quiver([0], [0], 10*np.real(phase1), 10*np.imag(phase1), label='Psi-naught', color='b', scale=30)
ax8.quiver([0], [0], 10*np.real(phase2), 10*np.imag(phase2), label='Psi-one', color='r', scale=30)
ax8.legend(loc='best')

plt.show()