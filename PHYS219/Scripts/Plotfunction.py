import numpy as np
import matplotlib.pyplot as plt

#LIST OF ALL INPUTS

# Enter the name and units for x and y axes  on the plot.
# labeled. e.g. x_name = 'Time', x_units = 'ms', y_name = 'Voltage', y_units
# = 'V'.
x_name = 'Voltage'
x_units = 'V'
y_name = 'Current'
y_units = 'microAmps'

# definition of the f(x,parameterlist)  whoch is this example is an exponetial
#plus   a constant 
def functionx(t):
#    """ exp function """
    return -1/3*(np.exp(-2*t))+4/3*(np.exp(t))

def functiony(t):
    return 10*(np.exp(t/(300*8.617*np.power(10., -5)))-1)

#define  a set a values  for the parameters  amplitude, tau and V_offset
#params= (50000, 224000)  
      
#define the domain of f(x)  from  xmin to xmax  with npoints  
tmin=-0.3
tmax=0.3
npoints=1000    
# define x as an array  of points  from 0, 100
t= np.linspace(tmin,tmax,npoints)
#dedfine y   as  f(x)
x= t
y= functiony(t)

# plots (x) 
# marker='.' : data points are not indicated by markers
# linestyle= '-' : a continuous line is drawn
# linewidth=2 : the line thickness is set to 2
# color='b' : the color of the line is set to black
# label=string : the string is shown in the legend
plt.plot(x,y,marker="",linestyle="-",linewidth=2,color="b",
         label=" function")
# add axis labels and title
plt.xlabel('{} [{}]'.format(x_name,x_units))
plt.ylabel('{} [{}]'.format(y_name,y_units))
plt.title(r'Graph for Equation 1: The I-V Curve')
# print out  a statement that the plot is being displayed
print ('Displaying plot 1')
# plt.show() may or may not need to be commented out depending on your python
# editor (spyder) settings.
plt.show()


###############################################################################
# plots residual and histogram of residual. Don't touch this par tof the code
###############################################################################

# residual is the difference between the data and theory
















