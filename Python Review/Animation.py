import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animate
#import matplotlib.image as mpimg

def Decay(x):
    return np.sin(6*x)*np.exp(-x/5)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated='True')
ani = animate(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init,
              blit=True, interval=1)
plt.show()

def update(frame):
    xdata.append(frame)
    ydata.append(Decay(frame))
    ln.set_data(xdata, ydata)
    return ln,

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r', animated='True')
ani = animate(fig, update, frames=np.linspace(0, 2*np.pi, 256, endpoint=False),
              init_func=init, blit=True, interval=25)
plt.show()

#def init():
#    ax.set_xlim(0, 1)
#    ax.set_ylim(0, 1)
#    return heat,
#
#def update(frame):
#    global lum_img
#    lum_img+=(2*np.random.random(lum_img.shape)-np.ones(lum_img.shape)).astype(int)
#    heat.set_data(lum_img)
#    return heat
#
#fig, ax = plt.subplots()
#img=mpimg.imread('/Users/ryank/Desktop/o_o.jpg')
#lum_img = np.copy(img[:,:,2]).astype(int)
#heat = plt.imshow(lum_img, cmap='Pastel1')
#ani = animate(fig, update, frames=200, init_func=init, blit=True, interval=200)
#plt.show()