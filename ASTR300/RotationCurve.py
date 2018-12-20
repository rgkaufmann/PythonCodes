import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11
M = 1

def rotationCurve(R):
    return np.sqrt(G*M*R**2/(R**2+1**2)**(3/2))

def inclinedCurve(R, phi, i):
    return rotationCurve(R)*np.sin(i)*np.cos(phi)

RValues = np.linspace(0, 4, 1000)
RotationValues = rotationCurve(RValues)
RotationMax = rotationCurve(np.sqrt(2))
RotationValues = RotationValues/RotationMax

incline = np.radians(30)
Phi = np.linspace(0, 2*np.pi, 1000)
PhiMesh, RMesh = np.meshgrid(Phi, RValues)
inclinedRotations = inclinedCurve(RMesh, PhiMesh, incline)
inclinedRotations = inclinedRotations/(RotationMax*np.sin(incline))

ax1 = plt.subplot(121)
ax1.plot(RValues, RotationValues)
ax1.set_title('Rotation Curve as a Function of Radius from the Center')
ax1.set_xlabel('Radius in terms of r0')
ax1.set_ylabel('Rotation Velocity in terms of Maximum Velocity')

ax2 = plt.subplot(122, projection='polar')
PC = ax2.contour(PhiMesh, RMesh, inclinedRotations,
                 [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1],
                 linewidths=3)
ax2.clabel(PC, inline=1, fontsize=10)
ax2.grid(False)
ax2.set_title('Spider Diagram of Rotation Curves with Inclination Angle i=30deg')
plt.show()