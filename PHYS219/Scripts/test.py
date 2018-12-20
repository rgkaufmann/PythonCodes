import numpy as np
import matplotlib.pyplot as plt
import math

def Euler_Method(t,yprev,tprev,h):
    y=(yprev+h*Derivative(tprev,yprev))
    coors = np.array([[tprev+h], [y]])
    if (tprev+h < t):
        return np.append(coors, Euler_Method(t,y,tprev+h,h), axis=1)
    else:
        return coors
    
def Improved_Euler_Method(t,yprev,tprev,h):
    m1=Derivative(tprev, yprev)
    m2=Derivative(tprev+h,yprev+h*m1)
    y=yprev+h*(m1+m2)/2
    coors = np.array([[tprev+h], [y]])
    if (tprev+h < t):
        return np.append(coors, Improved_Euler_Method(t,y,tprev+h,h), axis=1)
    else:
        return coors
    
def Derivative(t,y):
    return (2*y-2)/(math.pow((math.sin(t)),3)+2)

hof25 = np.append(np.array([[0],[1]]), Euler_Method(3,0,0,0.25), axis=1)
hof1  = np.append(np.array([[0],[1]]), Euler_Method(3,0,0,0.10), axis=1)
hof05 = np.append(np.array([[0],[1]]), Euler_Method(3,0,0,0.05), axis=1)

hof25i = np.append(np.array([[0],[1]]), Improved_Euler_Method(3,0,0,0.25), axis=1)
hof1i  = np.append(np.array([[0],[1]]), Improved_Euler_Method(3,0,0,0.10), axis=1)
hof05i = np.append(np.array([[0],[1]]), Improved_Euler_Method(3,0,0,0.05), axis=1)

for int in range(13):
    print("t={:.2f}\ty={:.3f}".format(hof25[0,int], hof25[1,int]))
    
print()
for int in range(31):
    print("t={:.2f}\ty={:.3f}".format(hof1[0,int], hof1[1,int]))

print()
for int in range(61):
    print("t={:.2f}\ty={:.3f}".format(hof05[0,int], hof05[1,int]))

print()
for int in range(13):
    print("t={:.2f}\ty={:.3f}".format(hof25i[0,int], hof25i[1,int]))
    
print()
for int in range(31):
    print("t={:.2f}\ty={:.3f}".format(hof1i[0,int], hof1i[1,int]))

print()
for int in range(61):
    print("t={:.2f}\ty={:.3f}".format(hof05i[0,int], hof05i[1,int]))

plt.plot(hof25[0,:], hof25[1,:], c='b', label="h=0.25")
plt.plot(hof1[0,:], hof1[1,:], c='r', label="h=0.1")
plt.plot(hof05[0,:], hof05[1,:], c='g', label="h=0.05")
plt.legend()
plt.xlabel('t')
plt.ylabel("y")
plt.title("Euler Approximations of the Derivative $y'(t)=(2y(t)-2)/(sin^3(t)+2)$")
plt.show()

plt.plot(hof25i[0,:], hof25i[1,:], c='b', label="h=0.25")
plt.plot(hof1i[0,:], hof1i[1,:], c='r', label="h=0.1")
plt.plot(hof05i[0,:], hof05i[1,:], c='g', label="h=0.05")
plt.legend()
plt.xlabel('t')
plt.ylabel("y")
plt.title("Improved Euler Approximations of the Derivative $y'(t)=(2y(t)-2)/(sin^3(t)+2)$")
plt.show()