import numpy as np


def MMRateofChange(MagMom, Gyromagnetic, BField, Nonhomogeneous=np.array([0, 0, 0])):
    return np.cross(Gyromagnetic * MagMom, BField + Nonhomogeneous)


def T1Decay(t, T1, Initial):
    return np.linalg.norm(Initial) - (np.linalg.norm(Initial) - Initial[2]) * np.exp(-t / T1)


def T2Decay(t, T2, Initial):
    return np.linalg.norm([Initial[0], Initial[1]]) * np.exp(-t / T2)


def Rotate(MagMom, Angle):
    return np.matmul(MagMom,
                     np.array([[1, 0, 0], [0, np.cos(Angle), -np.sin(Angle)], [0, np.sin(Angle), np.cos(Angle)]]))


def GetAngle(MagMom):
    Phi = np.arctan2(MagMom[1], MagMom[0])
    Theta = np.arccos(MagMom[2] / np.linalg.norm(MagMom))
    return Phi, Theta


class Atom:
    def __init__(self, MagMomX, MagMomY, MagMomZ):
        self.MagMomX = MagMomX
        self.MagMomY = MagMomY
        self.MagMomZ = MagMomZ

        self.MagMomVector = np.array([MagMomX, MagMomY, MagMomZ])
        self.MagMomMagnitude = np.linalg.norm(self.MagMomVector)
        self.MagMomHistory = [self.MagMomVector]

    def set_x(self, MagMomX):
        self.MagMomX = MagMomX
        self.MagMomVector = np.array([MagMomX, self.MagMomY, self.MagMomZ])
        self.MagMomMagnitude = np.linalg.norm(self.MagMomVector)

    def set_y(self, MagMomY):
        self.MagMomY = MagMomY
        self.MagMomVector = np.array([self.MagMomX, MagMomY, self.MagMomZ])
        self.MagMomMagnitude = np.linalg.norm(self.MagMomVector)

    def set_z(self, MagMomZ):
        self.MagMomZ = MagMomZ
        self.MagMomVector = np.array([self.MagMomX, self.MagMomY, MagMomZ])
        self.MagMomMagnitude = np.linalg.norm(self.MagMomVector)

    def set_vector(self, MagMomVector):
        self.MagMomX = MagMomVector[0]
        self.MagMomY = MagMomVector[1]
        self.MagMomZ = MagMomVector[2]

        self.MagMomVector = MagMomVector
        self.MagMomMagnitude = np.linalg.norm(MagMomVector)

    def set_history(self, MagMomHistory):
        self.MagMomX = MagMomHistory[-1][0]
        self.MagMomY = MagMomHistory[-1][1]
        self.MagMomZ = MagMomHistory[-1][2]

        self.MagMomVector = MagMomHistory[-1]
        self.MagMomMagnitude = np.linalg.norm(MagMomHistory[-1])
        self.MagMomHistory = MagMomHistory

    def next_vector(self, MagMomVector):
        self.MagMomX = MagMomVector[0]
        self.MagMomY = MagMomVector[1]
        self.MagMomZ = MagMomVector[2]

        self.MagMomVector = MagMomVector
        self.MagMomMagnitude = np.linalg.norm(MagMomVector)
        self.MagMomHistory.append(MagMomVector)

    def get_history(self):
        return self.MagMomHistory

    def get_vector(self):
        return self.MagMomVector