import numpy as np
import matplotlib.pyplot as plt

def giveRA(data):
    RA = np.zeros(len(data[:, 0]))
    for index in range(len(data[:, 0])):
        RA[index] = 15*data[index, 0]+15/60*data[index, 1]
        RA[index] += 15/3600*data[index, 2]
    return RA*np.pi/180

def giveDec(data):
    Dec = np.zeros(len(data[:, 3]))
    for index in range(len(data[:, 3])):
        Dec[index] = data[index, 3]+1/60*data[index, 4]+1/3600*data[index, 5]
    return Dec*np.pi/180

filename = "C:/Users/ryank/Desktop/Work/Classes/Python/ASTR205/Data/"
filename += "FullSkyCatalogue.txt"
Data = np.loadtxt(filename)

combinedData = np.zeros((len(Data[:, 0]), 3))
combinedData[:, 0] = giveRA(Data)
combinedData[:, 1] = giveDec(Data)
combinedData[:, 2] = Data[:, 6]
combinedData[(np.where(combinedData[:, 0]>np.pi)), 0] -= 2*np.pi
visibleData = combinedData[(np.where(combinedData[:, 2]<=6)), :][0]
#circumpolarData = combinedData[np.where(combinedData[:, 1]>=(90-49)*np.pi/180),
#                               :][0]
#circumpolarVisibleData = visibleData[np.where(visibleData[:, 1]>=(90-49)*np.pi/180)]

fig = plt.figure(num = 1, figsize=(10,5))
ax = fig.add_subplot(111, projection='mollweide')
ax.scatter(combinedData[:, 0], combinedData[:, 1], s=0.01, marker='.',
           color='red')
#plt.title('Full Catalogue of Stars as Seen From Earth')
plt.xlabel('Right Ascension')
plt.ylabel('Declination')
plt.show()

fig = plt.figure(num = 1, figsize=(10,5))
ax = fig.add_subplot(111, projection='mollweide')
ax.scatter(visibleData[:, 0], visibleData[:, 1], s=0.1, marker='.',
           color='green')
plt.title('Only Visible Stars as Seen From Earth')
plt.xlabel('Right Ascension')
plt.ylabel('Declination')
plt.show()
#
#fig = plt.figure(num = 1, figsize=(10,5))
#ax = fig.add_subplot(111, projection='mollweide')
#ax.scatter(combinedData[:, 0], combinedData[:, 1], s=0.01, marker='.',
#           color='red', label='Full Sky Catalogue')
#ax.scatter(visibleData[:, 0], visibleData[:, 1], s=0.1, marker='.',
#           color='green', label='Visible Stars')
#plt.title('Visible Stars Over Full Sky Catalogue as Seen From Earth')
#plt.xlabel('Right Ascension')
#plt.ylabel('Declination')
#plt.legend(loc='best', markerscale=100)
#plt.show()
#
#fig = plt.figure(num = 1, figsize=(10,5))
#ax = fig.add_subplot(111, projection='mollweide')
#ax.scatter(circumpolarData[:, 0], circumpolarData[:, 1], s=0.01, marker='.',
#           color='cyan')
#plt.title('Circumpolar Stars as Seen From Vancouver')
#plt.xlabel('Right Ascension')
#plt.ylabel('Declination')
#plt.show()
#
#fig = plt.figure(num = 1, figsize=(10,5))
#ax = fig.add_subplot(111, projection='mollweide')
#ax.scatter(combinedData[:, 0], combinedData[:, 1], s=0.01, marker='.',
#           color='red', label='Full Sky Catalogue')
#ax.scatter(visibleData[:, 0], visibleData[:, 1], s=0.1, marker='.',
#           color='green', label='Visible Stars')
#ax.scatter(circumpolarData[:, 0], circumpolarData[:, 1], s=0.01, marker='.',
#           color='cyan', label='Circumpolar Stars')
#plt.title('Circumpolar Stars From Vancouver Over Visible Stars and Full Sky Catalogue From Earth')
#plt.xlabel('Right Ascension')
#plt.ylabel('Declination')
#plt.legend(loc='best', markerscale=100)
#plt.show()