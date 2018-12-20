import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

zValues = np.linspace(-2*np.pi, 2*np.pi, 1000)
xValues = 2*np.abs(zValues)*np.cos(4*zValues)
yValues = np.abs(zValues)*np.sin(4*zValues)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(xValues, yValues, zs=zValues)
plt.show()

xValues = np.random.normal(0, 1, (100, 3))
yValues = np.random.normal(0, 1, (100, 3))
zValues = np.random.normal(0, 1, (100, 3))

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(xValues[:, 0], yValues[:, 0], zs=zValues[:, 0], marker='o', c='g')
ax.scatter(xValues[:, 1], yValues[:, 1], zs=zValues[:, 1], marker='^', c='r')
ax.scatter(xValues[:, 2], yValues[:, 2], zs=zValues[:, 2], marker='<', c='b')
ax.view_init(30, 75)
plt.show()

xValues = np.linspace(-5, 5, 1000)
yValues = np.linspace(-5, 5, 1000)
xValues, yValues = np.meshgrid(xValues, yValues)
zValues = np.sin(yValues)*np.cos(xValues)*np.exp(-xValues/5-yValues/5)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(xValues, yValues, zValues)
ax.view_init(50, 205)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xValues, yValues, zValues, color='r')
ax.view_init(40, 25)
plt.show()

xValues = np.linspace(-5, 5, 5)
yValues = np.linspace(-5, 5, 5)
zValues = np.linspace(-5, 5, 5)
xValues, yValues, zValues = np.meshgrid(xValues, yValues, zValues)
uValues = np.sin(xValues)*np.cos(yValues)
vValues = np.cos(xValues)*np.sin(yValues)
wValues = zValues/10

fig = plt.figure()
ax = Axes3D(fig)
ax.quiver(xValues, yValues, zValues, uValues, vValues, wValues)
plt.show()


def func(xVal):
    return np.sin(4*xVal)*np.exp(np.abs(xVal)/10)

xValues = np.linspace(-10, 10, 1000)
yValues = func(xValues)

plt.copper()
plt.axvline(-2*np.pi, ymin=-5, ymax=5, alpha=0.6, c='r', ls='--', lw=1,
            label='-2pi X-Line')
plt.axvline(2*np.pi, ymin=-5, ymax=5, alpha=0.6, c='r', ls='--', lw=1,
            label='2pi X-Line')
plt.axhline(-1.5, xmin=-10, xmax=10, alpha=0.4, c='g', ls='-.', lw=1,
            label='-1.5 Y-Line')
plt.axhline(1.5, xmin=-10, xmax=10, alpha=0.4, c='g', ls='-.', lw=1,
            label='1.5 Y-Line')
plt.plot(xValues, yValues, 'b-', label='Sine Wave')
plt.grid()
plt.legend(loc='best')
plt.xlim(xmin=-10, xmax=18)
plt.xlabel('This is an X label')
plt.ylim(ymin=-3, ymax=3)
plt.ylabel('This is an Y label')
plt.title('Some weird graphs')
plt.show()

xValues = np.random.normal(0, 1, 500)
yValues = np.random.normal(0, 1, 500)

plt.bone()
plt.subplot(223)
plt.hist(xValues, bins='auto', normed=True)
plt.subplot(224)
plt.hist(yValues, bins='auto', normed=True)
plt.subplot(211)
plt.hist2d(xValues, yValues, normed=True)
plt.show()

xValues = np.linspace(-10, 10, 1000)
yValues = np.linspace(-10, 10, 1000)
xValues, yValues = np.meshgrid(xValues, yValues)
zValues = np.sin(xValues)*np.cos(yValues*xValues)

plt.figure(figsize=(10, 10))
plt.inferno()
C = plt.contour(zValues)
plt.imshow(zValues, cmap='cool')
plt.show()