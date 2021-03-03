import numpy as np
import matplotlib.pyplot as plt
import Atom_Class as AC

m0 = 4.9155e-32
BField = np.array([0, 0, 21])
Gyromagnetic = 42.577478518*2*np.pi

NumAtoms = int(1e3)
StepSize = 0.00001
Steps = int(2e3)
TimeArray = np.linspace(0, Steps+1, Steps+1)

FirstPiHalfRotation = 50
SecondPiHalfRotation = 700

AtomList = []
History = np.zeros((Steps + 1, 3))
M0Tot = np.zeros(Steps + 1)
MxTot = []
MyTot = []
MzTot = []

for num in range(NumAtoms):
    Mz = 1
    Mx = 0
    My = 0

    AtomList.append(AC.Atom(m0 * BField[2] * Mx, m0 * BField[2] * My, m0 * BField[2] * Mz))
    NonHomogeneous = np.array([0, 0, np.random.normal(0, 2)])

    XYDecay = AC.T2Decay(TimeArray, 500, AtomList[-1].get_vector())
    ZDecay = AC.T1Decay(TimeArray, 1000, AtomList[-1].get_vector())

    for step in range(1, FirstPiHalfRotation, 1):
        k1 = AC.MMRateofChange(AtomList[-1].get_vector(), Gyromagnetic, BField, NonHomogeneous)
        k2 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k1, Gyromagnetic, BField, NonHomogeneous)
        k3 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k2, Gyromagnetic, BField, NonHomogeneous)
        k4 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize * k3, Gyromagnetic, BField, NonHomogeneous)

        NewM = (AtomList[-1].get_vector() + 1 / 6 * StepSize * (k1 + 2 * k2 + 2 * k3 + k4))
        NewM[2] = ZDecay[step]
        AtomList[-1].next_vector(NewM)

    CurrentHistory = AtomList[-1].get_history()
    Phi, Theta = AC.GetAngle(CurrentHistory[0])
    CurrentHistory[0] = np.array([XYDecay[0] * np.cos(Phi), XYDecay[0] * np.sin(Phi), ZDecay[0]])
    M0Tot[0] = M0Tot[0] + np.linalg.norm(CurrentHistory[0])

    for step in range(1, FirstPiHalfRotation, 1):
        Phi, Theta = AC.GetAngle(CurrentHistory[step])
        CurrentHistory[step] = np.array(
            [XYDecay[step] * np.cos(Phi), XYDecay[step] * np.sin(Phi), CurrentHistory[step][2]])
        M0Tot[step] = M0Tot[step] + np.linalg.norm(CurrentHistory[step])

    AtomList[-1].set_history(CurrentHistory)
    NewM = np.matmul(AtomList[-1].get_vector(), np.array([[1, 0, 0],
                                                          [0, np.cos(np.pi / 2), -np.sin(np.pi / 2)],
                                                          [0, np.sin(np.pi / 2), np.cos(np.pi / 2)]]))
    ZDecay = AC.T1Decay(np.linspace(0 - FirstPiHalfRotation, Steps + 1 - FirstPiHalfRotation, Steps + 1), 1000,
                        [np.sqrt((m0 * BField[2]) ** 2 - NewM[2] ** 2), 0, NewM[2]])
    XYDecay = AC.T2Decay(np.linspace(0 - FirstPiHalfRotation, Steps + 1 - FirstPiHalfRotation, Steps + 1), 500, NewM)
    AtomList[-1].next_vector(np.array([NewM[0], NewM[1], ZDecay[FirstPiHalfRotation]]))

    for step in range(FirstPiHalfRotation + 1, SecondPiHalfRotation, 1):
        k1 = AC.MMRateofChange(AtomList[-1].get_vector(), Gyromagnetic, BField, NonHomogeneous)
        k2 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k1, Gyromagnetic, BField, NonHomogeneous)
        k3 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k2, Gyromagnetic, BField, NonHomogeneous)
        k4 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize * k3, Gyromagnetic, BField, NonHomogeneous)

        NewM = (AtomList[-1].get_vector() + 1 / 6 * StepSize * (k1 + 2 * k2 + 2 * k3 + k4))
        NewM[2] = ZDecay[step]
        AtomList[-1].next_vector(NewM)

    CurrentHistory = AtomList[-1].get_history()
    Phi, Theta = AC.GetAngle(CurrentHistory[FirstPiHalfRotation])
    CurrentHistory[FirstPiHalfRotation] = np.array([XYDecay[FirstPiHalfRotation] * np.cos(Phi),
                                                    XYDecay[FirstPiHalfRotation] * np.sin(Phi),
                                                    ZDecay[FirstPiHalfRotation]])
    M0Tot[FirstPiHalfRotation] = M0Tot[FirstPiHalfRotation] + np.linalg.norm(CurrentHistory[FirstPiHalfRotation])

    for step in range(FirstPiHalfRotation + 1, SecondPiHalfRotation, 1):
        Phi, Theta = AC.GetAngle(CurrentHistory[step])
        CurrentHistory[step] = np.array(
            [XYDecay[step] * np.cos(Phi), XYDecay[step] * np.sin(Phi), CurrentHistory[step][2]])
        M0Tot[step] = M0Tot[step] + np.linalg.norm(CurrentHistory[step])

    AtomList[-1].set_history(CurrentHistory)
    NewM = np.matmul(AtomList[-1].get_vector(), np.array([[1, 0, 0],
                                                          [0, np.cos(np.pi / 2), -np.sin(np.pi / 2)],
                                                          [0, np.sin(np.pi / 2), np.cos(np.pi / 2)]]))
    ZDecay = AC.T1Decay(np.linspace(0 - SecondPiHalfRotation, Steps + 1 - SecondPiHalfRotation, Steps + 1), 1000,
                        [np.sqrt((m0 * BField[2]) ** 2 - NewM[2] ** 2), 0, NewM[2]])
    XYDecay = AC.T2Decay(np.linspace(0 - SecondPiHalfRotation, Steps + 1 - SecondPiHalfRotation, Steps + 1), 500, NewM)
    AtomList[-1].next_vector(np.array([NewM[0], NewM[1], ZDecay[SecondPiHalfRotation]]))

    for step in range(SecondPiHalfRotation + 1, Steps + 1, 1):
        k1 = AC.MMRateofChange(AtomList[-1].get_vector(), Gyromagnetic, BField, NonHomogeneous)
        k2 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k1, Gyromagnetic, BField, NonHomogeneous)
        k3 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k2, Gyromagnetic, BField, NonHomogeneous)
        k4 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize * k3, Gyromagnetic, BField, NonHomogeneous)

        NewM = (AtomList[-1].get_vector() + 1 / 6 * StepSize * (k1 + 2 * k2 + 2 * k3 + k4))
        NewM[2] = ZDecay[step]
        AtomList[-1].next_vector(NewM)

    CurrentHistory = AtomList[-1].get_history()
    Phi, Theta = AC.GetAngle(CurrentHistory[SecondPiHalfRotation])
    CurrentHistory[SecondPiHalfRotation] = np.array([XYDecay[SecondPiHalfRotation] * np.cos(Phi),
                                                     XYDecay[SecondPiHalfRotation] * np.sin(Phi),
                                                     ZDecay[SecondPiHalfRotation]])
    M0Tot[SecondPiHalfRotation] = M0Tot[SecondPiHalfRotation] + np.linalg.norm(CurrentHistory[SecondPiHalfRotation])

    for step in range(SecondPiHalfRotation + 1, Steps + 1, 1):
        Phi, Theta = AC.GetAngle(CurrentHistory[step])
        CurrentHistory[step] = np.array(
            [XYDecay[step] * np.cos(Phi), XYDecay[step] * np.sin(Phi), CurrentHistory[step][2]])
        M0Tot[step] = M0Tot[step] + np.linalg.norm(CurrentHistory[step])

    AtomList[-1].set_history(CurrentHistory)
    History = History + AtomList[-1].get_history()

for moment in History:
    MxTot.append(moment[0])
    MyTot.append(moment[1])
    MzTot.append(moment[2])

plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(M0Tot) / (m0 * BField[2] * NumAtoms),
         label=r'$|M|$')
plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MxTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_x$')
plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MyTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_y$')
plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MzTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_z$')
plt.legend(loc='best', ncol=2)
plt.title(r'Evolution of Sum of 1000 Magnetic Moments over Time in Magnetic Field $B_z\hat{z}$')
plt.ylabel('Magnetic Moment (Normalized to $|M_0|=1$)')
plt.xlabel('Time ($ns$)')
plt.ylim(-1.05, 1.05)
plt.xlim(0, StepSize * 1000 * Steps)
plt.show()

FirstPiHalfRotation = 50
SecondPiHalfRotation = 700

AtomList = []
History = np.zeros((Steps + 1, 3))
M0Tot = np.zeros(Steps + 1)
MxTot = []
MyTot = []
MzTot = []

for num in range(NumAtoms):
    Mz = 1
    Mx = 0
    My = 0

    AtomList.append(AC.Atom(m0 * BField[2] * Mx, m0 * BField[2] * My, m0 * BField[2] * Mz))
    NonHomogeneous = np.array([0, 0, np.random.normal(0, 2)])

    XYDecay = AC.T2Decay(TimeArray, 500, AtomList[-1].get_vector())
    ZDecay = AC.T1Decay(TimeArray, 1000, AtomList[-1].get_vector())

    for step in range(1, Steps + 1, 1):
        k1 = AC.MMRateofChange(AtomList[-1].get_vector(), Gyromagnetic, BField, NonHomogeneous)
        k2 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k1, Gyromagnetic, BField, NonHomogeneous)
        k3 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize / 2 * k2, Gyromagnetic, BField, NonHomogeneous)
        k4 = AC.MMRateofChange(AtomList[-1].get_vector() + StepSize * k3, Gyromagnetic, BField, NonHomogeneous)

        NewM = (AtomList[-1].get_vector() + 1 / 6 * StepSize * (k1 + 2 * k2 + 2 * k3 + k4))
        if step == FirstPiHalfRotation:
            NewM = np.matmul(NewM, np.array([[1, 0, 0],
                                             [0, np.cos(np.pi / 2), -np.sin(np.pi / 2)],
                                             [0, np.sin(np.pi / 2), np.cos(np.pi / 2)]]))
            ZDecay = AC.T1Decay(np.linspace(0 - FirstPiHalfRotation, Steps + 1 - FirstPiHalfRotation, Steps + 1), 1000,
                                [np.sqrt((m0 * BField[2]) ** 2 - NewM[2] ** 2), 0, NewM[2]])
        if step == SecondPiHalfRotation:
            NewM = np.matmul(NewM, np.array([[1, 0, 0],
                                             [0, np.cos(np.pi / 2), -np.sin(np.pi / 2)],
                                             [0, np.sin(np.pi / 2), np.cos(np.pi / 2)]]))
            ZDecay = AC.T1Decay(np.linspace(0 - SecondPiHalfRotation, Steps + 1 - SecondPiHalfRotation, Steps + 1),
                                1000,
                                [np.sqrt((m0 * BField[2]) ** 2 - NewM[2] ** 2), 0, NewM[2]])
        NewM[2] = ZDecay[step]
        AtomList[-1].next_vector(NewM)

    CurrentHistory = AtomList[-1].get_history()
    Phi, Theta = AC.GetAngle(CurrentHistory[0])
    CurrentHistory[0] = np.array([XYDecay[0] * np.cos(Phi), XYDecay[0] * np.sin(Phi), ZDecay[0]])
    M0Tot[0] = M0Tot[0] + np.linalg.norm(CurrentHistory[0])

    for step in range(1, Steps + 1, 1):
        if step == FirstPiHalfRotation:
            XYDecay = AC.T2Decay(np.linspace(0 - FirstPiHalfRotation, Steps + 1 - FirstPiHalfRotation, Steps + 1), 500,
                                 NewM)
        if step == SecondPiHalfRotation:
            XYDecay = AC.T2Decay(np.linspace(0 - SecondPiHalfRotation, Steps + 1 - SecondPiHalfRotation, Steps + 1),
                                 500, NewM)
        Phi, Theta = AC.GetAngle(CurrentHistory[step])
        CurrentHistory[step] = np.array(
            [XYDecay[step] * np.cos(Phi), XYDecay[step] * np.sin(Phi), CurrentHistory[step][2]])
        M0Tot[step] = M0Tot[step] + np.linalg.norm(CurrentHistory[step])

    AtomList[-1].set_history(CurrentHistory)
    History = History + AtomList[-1].get_history()

for moment in History:
    MxTot.append(moment[0])
    MyTot.append(moment[1])
    MzTot.append(moment[2])

plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(M0Tot) / (m0 * BField[2] * NumAtoms),
         label=r'$|M|$')
plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MxTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_x$')
plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MyTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_y$')
plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MzTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_z$')
plt.legend(loc='best', ncol=2)
plt.title(r'Evolution of Sum of 1000 Magnetic Moments over Time in Magnetic Field $B_z\hat{z}$')
plt.ylabel('Magnetic Moment (Normalized to $|M_0|=1$)')
plt.xlabel('Time ($ns$)')
plt.ylim(-1.05, 1.05)
plt.xlim(0, StepSize * 1000 * Steps)
plt.show()

plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MyTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_y$')
plt.plot(np.linspace(0, Steps + 1, Steps + 1) * 1000 * StepSize, np.array(MzTot) / (m0 * BField[2] * NumAtoms),
         label=r'$M_z$')
plt.legend(loc='best', ncol=2)
plt.title(r'Evolution of Sum of 1000 Magnetic Moments over Time in Magnetic Field $B_z\hat{z}$')
plt.ylabel('Magnetic Moment (Normalized to $|M_0|=1$)')
plt.xlabel('Time ($ns$)')
plt.ylim(-1.05, 1.05)
plt.xlim(0, StepSize * 1000 * Steps)
plt.show()
