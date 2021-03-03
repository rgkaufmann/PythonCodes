from tkinter import *
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from scipy.integrate import quad

root = Tk()

MASS = 9.10938356E-31
BOLTZMANN = 1.38064852E-23
REDUCEDH = 6.62607015E-34 / (2.0 * np.pi)
N = 9.65E-6

Temperature = IntVar()
Temperature.set(10)


def update_plots(variable):
    IntegralFD = quad(FDDistribution, a=0, b=1000000, args=(int(variable), 1000))[0]
    IntegralMB = quad(MBDistribution, a=0, b=1000000, args=(int(variable),))[0]

    Plots.cla()
    Plots.plot(velocities, MBDistribution(velocities, int(variable)) / IntegralMB, label='Maxwell-Boltzmann')
    Plots.plot(velocities, FDDistribution(velocities, int(variable), 1000) / IntegralFD, label='Fermi-Dirac')
    Plots.legend()

    canvas.draw()


def MBDistribution(velocity, temperature):
    return N * (MASS / (2.0 * np.pi * BOLTZMANN * temperature)) ** (3.0 / 2.0) *\
           np.exp(-MASS * (velocity ** 2.0) / (2.0 * BOLTZMANN * temperature))


def FDDistribution(velocity, temperature, t0):
    return (MASS / REDUCEDH) ** 3.0 / (4.0 * np.pi ** 3.0) * 1 /\
           (np.exp((0.5 * MASS * velocity ** 2.0 - BOLTZMANN * t0) / BOLTZMANN * temperature) + 1.0)


PlotFrame = Frame(root, width=512, height=512)
PlotFrame.pack(side=TOP, fill=BOTH, expand=True)

f = Figure(figsize=(5, 5), dpi=100)
velocities = np.linspace(0, 500000, 500000)
Plots = f.add_subplot(111)
Plots.plot(velocities, MBDistribution(velocities, Temperature.get()), label='Maxwell-Boltzmann')
Plots.plot(velocities, FDDistribution(velocities, Temperature.get(), 1000), label='Fermi-Dirac')
Plots.legend()

canvas = FigureCanvasTkAgg(f, PlotFrame)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

Slider = Scale(root, length=512, sliderlength=15, from_=10, to=1000, orient=HORIZONTAL, variable=Temperature,
               label='Temperature', resolution=10, command=update_plots)
Slider.pack(side=BOTTOM, expand=1, fill=X)

root.mainloop()
