import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, iterate_structure, binary_erosion
from scipy.signal import stft
from scipy.io import wavfile
from os.path import exists

DEFAULT_AMP_MIN = 10
PEAK_NEIGHBORHOOD_SIZE = 20

NewWAV = 'y'

while NewWAV == 'y':
    try:
        FileName = input('What is the name of the WAV file?\n')
        print()
        if exists('Plots/' + FileName[:-4] + ' Spectrum.png') and exists('Plots/' + FileName[:-4] + ' Fingerprint.png'):
            print("Fingerprint analysis already completed.")
            print("Find the files in the plots folder.")
            print()
        else:
            DEFAULT_FS, AudioData = wavfile.read('WAV Files/' + FileName)

            Frequencies, Times, Spectrum = stft(AudioData[:, 0], fs=DEFAULT_FS)

            Spectrum = np.real(10 * np.log10(Spectrum))
            Spectrum[Spectrum == -np.inf] = 0

            plt.imshow(Spectrum, cmap='Spectral', extent=(min(Times), max(Times), min(Frequencies), max(Frequencies)),
                       origin='lower', aspect='auto')
            plt.show()
            plt.savefig('Plots/' + FileName[:-4] + ' Spectrum.png')

            Struct = generate_binary_structure(2, 1)
            Neighborhood = iterate_structure(Struct, PEAK_NEIGHBORHOOD_SIZE)

            LocalMax = maximum_filter(Spectrum, footprint=Neighborhood) == Spectrum
            Background = (Spectrum == 0)
            ErodedBackground = binary_erosion(Background, structure=Neighborhood, border_value=1)

            DetectedPeaks = LocalMax ^ ErodedBackground

            Amps = Spectrum[DetectedPeaks]
            JIndex, IIndex = np.where(DetectedPeaks)

            Amps = Amps.flatten()
            Peaks = zip(IIndex, JIndex, Amps)
            Peaks = filter(lambda x: x[2] > DEFAULT_AMP_MIN, Peaks)

            FrequencyIndices = []
            TimeIndices = []
            for Peak in Peaks:
                FrequencyIndices.append(Peak[1])
                TimeIndices.append(Peak[0])

            plt.clf()
            plt.imshow(np.real(Spectrum), cmap='Spectral', extent=(min(Times), max(Times),
                                                                   min(Frequencies), max(Frequencies)),
                       origin='lower', aspect='auto')
            plt.scatter(Times[TimeIndices], Frequencies[FrequencyIndices], s=3, c='k')
            plt.xlim(min(Times), max(Times))
            plt.ylim(min(Frequencies), max(Frequencies))
            plt.show()
            plt.savefig('Plots/' + FileName[:-4] + ' Fingerprint.png')
    except IOError:
        print('File not found.')
        Redo = input('Would you like to try again? (y/n)\n')
        print()
        while Redo is not None:
            if Redo == 'y':
                break
            elif Redo == 'n':
                exit()
            else:
                Redo = input("Character not understood, please enter 'y' or 'n'.\n")
                print()
        continue

    NewWAV = input('Would you like to try another WAV File? (y/n)\n')
    print()
    while NewWAV is not None:
        if NewWAV == 'y' or NewWAV == 'n':
            break
        else:
            NewWAV = input("Character not understood, please enter 'y' or 'n'.\n")
            print()
