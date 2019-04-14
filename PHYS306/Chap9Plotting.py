import numpy as np
import matplotlib.pyplot as plt


def xfunc(t, vx, vy):
    return (1+vx*t)*np.cos(t)+(vy+1)*t*np.sin(t)


def yfunc(t, vx, vy):
    return -(1+vx*t)*np.sin(t)+(vy+1)*t*np.cos(t)


t = np.linspace(0, 15, 1000)

plt.figure(figsize=(9,9))
plt.plot(xfunc(t, 0.0, 1.0), yfunc(t, 0.0, 1.0), label="(0,1)")
plt.plot(xfunc(t, 0.0, 0.0), yfunc(t, 0.0, 0.0), label="(0,0)")
plt.plot(xfunc(t, 0.0, -1.0), yfunc(t, 0.0, -1.0), label="(0,-1)")
plt.plot(xfunc(t, -0.5, -0.5), yfunc(t, -0.5, -0.5), label="(-0.5,-0.5)")
plt.plot(xfunc(t, -0.7, -0.7), yfunc(t, -0.7, -0.7), label="(-0.7,-0.7)")
plt.plot(xfunc(t, 0.0, -0.1), yfunc(t, 0.0, -0.1), label="(0,-0.1)")
plt.legend(loc='best')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()

plt.figure(figsize=(9,9))
plt.plot(xfunc(t, 0.0, 1.0), yfunc(t, 0.0, 1.0), label="(0,1)")
plt.plot(xfunc(t, 0.0, 0.0), yfunc(t, 0.0, 0.0), label="(0,0)")
plt.plot(xfunc(t, 0.0, -1.0), yfunc(t, 0.0, -1.0), label="(0,-1)")
plt.plot(xfunc(t, -0.5, -0.5), yfunc(t, -0.5, -0.5), label="(-0.5,-0.5)")
plt.plot(xfunc(t, -0.7, -0.7), yfunc(t, -0.7, -0.7), label="(-0.7,-0.7)")
plt.plot(xfunc(t, 0.0, -0.1), yfunc(t, 0.0, -0.1), label="(0,-0.1)")
plt.legend(loc='best')
plt.xlim((-2, 3))
plt.ylim((-2, 3))
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()
