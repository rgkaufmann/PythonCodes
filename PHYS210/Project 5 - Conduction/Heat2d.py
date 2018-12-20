import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import cProfile, pstats, io

pr = cProfile.Profile()
pr.enable()

# Constants
L = 0.01
D = 4.25e-6 #m^2s^-1
N=100
dx = L/N
dy = L/N
dtlist = [1e-3, 1e-4]

Tlo, Tmid, Thi = 200.0, 250., 400.0  # initial temperatures in K

# Choosen Times to make plots
t1, t2, t3, t4, t5 = 0.01, 0.1, 0.4, 1.0, 10.
listofTconverge = []
listofTdiverge = []

for dt in dtlist:
    T = np.empty((N+1, N+1), float)
    T[0, :] = Tlo
    T[N, :] = Tlo
    T[:, 0] = Thi
    T[:, N] = Thi
    T[1:N, 1:N] = Tmid
    T = T.T
    Tp = np.copy(T)
    t = 0
    c = dt*D/(dx**2)
    b = dt*D/(dy**2)
    epsilon = dt/1000
    tend = t5+epsilon
    while t<tend:
        # Calculates the new values of T at time t
        Tp[1:N, 1:N] = T[1:N, 1:N]
        Tp[1:N, 1:N] += (c*(np.roll(T, 1, axis=1) +
                            np.roll(T, -1, axis=1)-2*T))[1:N, 1:N]
        Tp[1:N, 1:N] += (b*(np.roll(T, 1, axis=0) +
                            np.roll(T, -1, axis=0)-2*T))[1:N, 1:N]
        T, Tp = Tp, T
        if abs(dt-dtlist[0]) <= epsilon:
            listofTdiverge.append(np.copy(T))
        if abs(dt-dtlist[1]) <= epsilon:
            listofTconverge.append(np.copy(T))
        print(t)
        t += dt

def updateHeat(num, data, multiple):
    print(num)
    Heat.set_data(data[num*multiple])

fig = plt.figure()
Heat = plt.imshow(listofTconverge[0], extent=[0, L, 0, L])
animation = anim.FuncAnimation(fig, updateHeat, frames=1000,
                               fargs=(listofTconverge, 100, ), repeat=False)
animation.save('heat2d_converged.mp4', fps=20)

fig = plt.figure()
Heat = plt.imshow(listofTdiverge[0], extent=[0, L, 0, L])
animation = anim.FuncAnimation(fig, updateHeat, frames=1000, fargs=(listofTdiverge, 10, ), repeat=False)
animation.save('heat2d_diverged.mp4', fps=20)

pr.disable()
file = open('HeatStats.txt', 'w')
s = io.StringIO()
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()