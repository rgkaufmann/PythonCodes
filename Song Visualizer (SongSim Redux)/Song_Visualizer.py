import warnings
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
warnings.simplefilter(action='ignore', category=FutureWarning)
again='Yes'

def prompt():
    print()
    SongTitle=input("What song would you like to visualize? ")
    SongWrite=input("Who is the artist that plays the song? ")
    return {"Title":SongTitle, "Writer":SongWrite}

def promptRestrict():
    Restrict=''
    while Restrict.lower() not in np.array(['none' ,'single', 'stopwords']):
        print()
        Restrict =input("Would you like to not show any patterns? (None/Single/Stopwords) ")
    return Restrict

def promptLyrics():
    print()
    Lyrics=input("We do not have this song on file. Please type the full lyrics. Cancel or End to research. ")
    return Lyrics

def findLyrics(SongInfo):
    KnownLyrics=np.genfromtxt("songlyrics.txt", dtype=np.str, delimiter=';')
    if SongInfo["Title"] in KnownLyrics[:,0] and SongInfo["Writer"] in KnownLyrics[:,1] and np.where(KnownLyrics[:,0]==SongInfo["Title"])==np.where(KnownLyrics[:,1]==SongInfo["Writer"]):
        return KnownLyrics[np.where(SongInfo["Title"]==KnownLyrics[:,0]),2], KnownLyrics
    else:
        NewLyrics=promptLyrics()
        if NewLyrics.lower()=='cancel' or NewLyrics.lower()=='end':
            return findLyrics(prompt())
        else:
            return NewLyrics, np.vstack((KnownLyrics, np.array([SongInfo["Title"], SongInfo['Writer'], NewLyrics])))

def lyricsArray(Lyrics):
    if " " not in Lyrics:
        return np.array(rmvPunc(Lyrics))
    else:
        Word=rmvPunc(Lyrics[:Lyrics.index(' ')])
        NextLyrics=Lyrics[Lyrics.index(' ')+1:]
        return np.append(np.array(Word), lyricsArray(NextLyrics))
    
def rmvPunc(Word):
    EndPunc=np.array(['.', ',', '?', '!', ':', '"', ';', '(', ')'])
    for punc in EndPunc:
        while punc in Word:
            Word=Word.replace(punc, '')
    return Word

def generateArray(LyricsArray, Restrict):
    Repetitions=np.ones((len(LyricsArray), len(LyricsArray)))*np.nan
    for rowindx in range(len(LyricsArray)):
        for colindx in range(len(LyricsArray)):
            if LyricsArray[rowindx]==LyricsArray[colindx]:
                Repetitions[rowindx][colindx]=0
    Repetitions=colorArray(Repetitions, LyricsArray)
    if Restrict.lower()=='stopwords':
        Repetitions=checkStopwords(Repetitions, LyricsArray)
    elif Restrict.lower()=='single':
        Repetitions=checkSingles(Repetitions)
    return Repetitions

def checkSingles(Repetitions):
    for rowindx in range(len(Repetitions)):
        for colindx in range(len(Repetitions)):
            if np.isnan(Repetitions[rowindx-1][colindx-1]) and (rowindx==len(Repetitions)-1 or colindx==len(Repetitions)-1):
                if colindx==len(Repetitions)-1 and np.isnan(Repetitions[rowindx-1][colindx]) and np.isnan(Repetitions[rowindx+1][colindx]):
                    Repetitions[rowindx][colindx]=np.nan
                elif rowindx==len(Repetitions)-1 and np.isnan(Repetitions[rowindx][colindx-1]) and np.isnan(Repetitions[rowindx][colindx+1]):
                    Repetitions[rowindx][colindx]=np.nan
            elif (colindx<(len(Repetitions)-1) and rowindx<(len(Repetitions)-1)) and np.isnan(Repetitions[rowindx][colindx-1]) and np.isnan(Repetitions[rowindx][colindx+1]) and np.isnan(Repetitions[rowindx-1][colindx]) and np.isnan(Repetitions[rowindx+1][colindx]) and np.isnan(Repetitions[rowindx+1][colindx+1]) and np.isnan(Repetitions[rowindx-1][colindx-1]):
                Repetitions[rowindx][colindx]=np.nan
    return Repetitions

def checkStopwords(Repetitions, Lyrics):
    Stopwords=np.array(['a', 'about', 'and', 'but', 'so', 'the', 'an', 'to', 'on', 'in'])
    for rowindx in range(len(Repetitions)):
        for colindx in range(len(Repetitions)):
            if np.isnan(Repetitions[rowindx-1][colindx-1]) and (rowindx==len(Repetitions)-1 or colindx==len(Repetitions)-1) and Lyrics[rowindx] in Stopwords:
                if colindx==len(Repetitions)-1 and np.isnan(Repetitions[rowindx-1][colindx]) and np.isnan(Repetitions[rowindx+1][colindx]):
                    Repetitions[rowindx][colindx]=np.nan
                elif rowindx==len(Repetitions)-1 and np.isnan(Repetitions[rowindx][colindx-1]) and np.isnan(Repetitions[rowindx][colindx+1]):
                    Repetitions[rowindx][colindx]=np.nan
            elif (colindx<(len(Repetitions)-1) and rowindx<(len(Repetitions)-1)) and np.isnan(Repetitions[rowindx][colindx-1]) and np.isnan(Repetitions[rowindx][colindx+1]) and np.isnan(Repetitions[rowindx-1][colindx]) and np.isnan(Repetitions[rowindx+1][colindx]) and np.isnan(Repetitions[rowindx+1][colindx+1]) and np.isnan(Repetitions[rowindx-1][colindx-1]) and Lyrics[rowindx] in Stopwords:
                Repetitions[rowindx][colindx]=np.nan
    return Repetitions

def colorArray(Repetitions, LyricsArray):
    AlreadyFound=np.array([])
    for indx in range(len(LyricsArray)):
        if LyricsArray.item(indx) in AlreadyFound:
            Repetitions[indx][np.where(Repetitions[indx,:]==0)]=np.where(AlreadyFound==LyricsArray.item(indx))[0]+2
        elif 0 in Repetitions[indx][indx+1:]:
            AlreadyFound=np.append(AlreadyFound, np.array(LyricsArray.item(indx)))
            Repetitions[indx][np.where(Repetitions[indx,:]==0)]=np.where(AlreadyFound==LyricsArray.item(indx))[0]+2
    return Repetitions

def plotLyrics(Repetitions):
    fig, ax = plt.subplots(1,1,tight_layout=True)
    my_cmap = mpl.colors.ListedColormap(['#000000', '#f00000', '#f07800', '#f0f000', '#78f000', '#00f000', '#00f078', '#00f0f0', '#0078f0', '#0000f0', '#7800f0', '#f000f0', '#f00078'])
    my_cmap.set_bad(color='w', alpha=0)
    ax.imshow(Repetitions, interpolation='none', cmap=my_cmap, extent=[0, len(Repetitions), 0, len(Repetitions)], zorder=0)
    ax.axis('off')
    plt.show()

def writeLyrics(NewKnownLyrics):
    file=open("songlyrics.txt", 'w')
    text="{};{};{}\n"
    for indx in range(len(NewKnownLyrics)):
        file.write(text.format(NewKnownLyrics[indx,0], NewKnownLyrics[indx,1], NewKnownLyrics[indx,2]))
    file.close()

while again=='Yes':
    SongInfo=prompt()
    if SongInfo['Title']=='End':
        again='no';
        break
    Restrict=promptRestrict()
    Lyrics, NewKnownLyrics=findLyrics(SongInfo)
    if isinstance(Lyrics, np.ndarray):
        Lyrics=Lyrics.item(0)
    LyricsArray=lyricsArray(Lyrics.lower())
    Repeats=generateArray(LyricsArray, Restrict)
    plotLyrics(Repeats)
    writeLyrics(NewKnownLyrics)
    again=input("Would you like to display another song? (Yes/No) ")