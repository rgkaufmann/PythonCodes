import numpy as np

SYMBOLS = np.loadtxt('Atomic_Symbols.txt', dtype=str)
R = 1.2                                                               # fm
MASSES = np.loadtxt('Nuclei_Masses.txt', delimiter=',') * 931.494102  # MeV
C = 2.998E23                                                          # fm / s
HBARC = 197.3                                                         # MeV * fm
E2 = 1.44                                                             # MeV * fm

def M0(Ad, Zd, Ap, Zp):
    Md = MASSES[Ad][Zd-1]
    Mp = MASSES[Ap][Zp-1]
    return (Md * Mp) / (Md + Mp)


def Gamma(Ad, Zd, Ap, Zp, Qp):
    Mred = M0(Ad, Zd, Ap, Zp)
    Rbratio = (R * (Ad + Ap) ** (1 / 3)) / ((Zp * Zd * E2) / Qp)
    return (2 * Zp) * np.sqrt(2 * Mred) * (E2 / HBARC) * (Zd / np.sqrt(Qp)) * \
           (np.arccos(np.sqrt(Rbratio)) - np.sqrt(Rbratio * (1 - Rbratio)))


def Vin(Ad, Zd, Ap, Zp, Qp):
    return np.sqrt((2 * Qp) / M0(Ad, Zd, Ap, Zp))


def LambdaDecay(Ad, Zd, Ap, Zp, Qp):
    return (Vin(Ad, Zd, Ap, Zp, Qp) * C) / (2 * R * (Ad + Ap) ** (1 / 3)) * \
           np.exp(-1 * Gamma(Ad, Zd, Ap, Zp, Qp))


def QValue(Ad, Zd, Ap, Zp):
    return MASSES[Ad+Ap][Zd+Zp-1] - MASSES[Ad][Zd-1] - MASSES[Ap][Zp-1]


def HalfLife(Ad, Zd, Ap, Zp):
    return np.log(2) / LambdaDecay(Ad, Zd, Ap, Zp, QValue(Ad, Zd, Ap, Zp))


ParentNuclei = input('Please input the total nucleon number and proton number ' + \
                     'of the parent nucleus in the form A,Z. ')
ReleasedNuclei = input('Please input the total nucleon number and proton number ' + \
                     'of the released nucleus in the form A,Z. ')
print()

AParent = int(ParentNuclei[:ParentNuclei.index(',')])
ZParent = int(ParentNuclei[ParentNuclei.index(',')+1:])
AReleased = int(ReleasedNuclei[:ReleasedNuclei.index(',')])
ZReleased = int(ReleasedNuclei[ReleasedNuclei.index(',')+1:])
ADaughter = AParent - AReleased
ZDaughter = ZParent - ZReleased

if ADaughter <= 0:
    print('The released particle has more or an equal number of nucleons ' + \
          'than the parent particle. This decay can not happen.')
elif ZDaughter <= 0:
    print('The released particle has more or an equal number of protons ' + \
          'than the parent particle. The decay either can not occur or ' + \
          'can not be calculated using our formalism.')
else:
    print('The reaction described is ' + SYMBOLS[ZParent-1] + '-' + \
          str(AParent) + ' --> ' + SYMBOLS[ZDaughter-1] + '-' + \
          str(ADaughter) + ' + ' + SYMBOLS[ZReleased-1] + '-' + \
          str(AReleased) + ' + Q.')
    print()

    QVal = QValue(ADaughter, ZDaughter, AReleased, ZReleased)
    if QVal <= 0:
        print('The q-value of the reaction is negative. This reaction will ' + \
              'not happen naturally and must be induced.')
    else:
        HL = HalfLife(ADaughter, ZDaughter, AReleased, ZReleased)
        print('The half life of this decay is {} seconds.'.format(HL))
        if HL >= 60:
            print('This is equivalent to {} minutes.'.format(HL / 60))
        if HL >= (60 * 60):
            print('This is equivalent to {} hours.'.format(HL / (60 * 60)))
        if HL >= (60 * 60 * 24):
            print('This is equivalent to {} days.'.format(HL / \
                  (60 * 60 * 24)))
        if HL >= (60 * 60 * 24 * 7):
            print('This is equivalent to {} weeks.'.format(HL / \
                  (60 * 60 * 24 * 7)))
        if HL >= (60 * 60 * 24 * 365):
            print('This is equivalent to {} years.'.format(HL / \
                  (60 * 60 * 24 * 365)))
        if HL >= (60 * 60 * 24 * 365 * 1000):
            print('This is equivalent to {} millennia.'.format(HL / \
                  (60 * 60 * 24 * 365 * 1000)))
        if HL >= (60 * 60 * 24 * 365 * 1E6):
            print('This is equivalent to {} Myrs.'.format(HL / \
                  (60 * 60 * 24 * 365 * 1E6)))
        if HL >= (60 * 60 * 24 * 365 * 1E9):
            print('This is equivalent to {} Gyrs.'.format(HL / \
                   (60 * 60 * 24 * 365 * 1E9)))

