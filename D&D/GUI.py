from tkinter import *
from tkinter import filedialog
import DiceRoller
import numpy as np
from Constants import *


class StatsLabel(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=256)

        self.STRIntroLabel = Label(root, bd=1, relief=SUNKEN, anchor=CENTER, text='STR:', font=("Helvetica", 16))
        self.STRIntroLabel.place(x=1024, y=64, anchor=NE, height=32, width=128)
        self.STRLabel = Label(root, textvariable=STRText, bd=2, relief=SUNKEN, anchor=CENTER, font=("Helvetica", 16))
        self.STRLabel.place(x=1024, y=96, anchor=NE, height=32, width=128)
        self.DEXIntroLabel = Label(root, bd=1, relief=SUNKEN, anchor=CENTER, text='DEX:', font=("Helvetica", 16))
        self.DEXIntroLabel.place(x=1024, y=128, anchor=NE, height=32, width=128)
        self.DEXLabel = Label(root, textvariable=DEXText, bd=2, relief=SUNKEN, anchor=CENTER, font=("Helvetica", 16))
        self.DEXLabel.place(x=1024, y=160, anchor=NE, height=32, width=128)
        self.CONIntroLabel = Label(root, bd=1, relief=SUNKEN, anchor=CENTER, text='CON:', font=("Helvetica", 16))
        self.CONIntroLabel.place(x=1024, y=192, anchor=NE, height=32, width=128)
        self.CONLabel = Label(root, textvariable=CONText, bd=2, relief=SUNKEN, anchor=CENTER, font=("Helvetica", 16))
        self.CONLabel.place(x=1024, y=224, anchor=NE, height=32, width=128)
        self.WISIntroLabel = Label(root, bd=1, relief=SUNKEN, anchor=CENTER, text='WIS:', font=("Helvetica", 16))
        self.WISIntroLabel.place(x=1024, y=256, anchor=NE, height=32, width=128)
        self.WISLabel = Label(root, textvariable=WISText, bd=2, relief=SUNKEN, anchor=CENTER, font=("Helvetica", 16))
        self.WISLabel.place(x=1024, y=288, anchor=NE, height=32, width=128)
        self.INTIntroLabel = Label(root, bd=1, relief=SUNKEN, anchor=CENTER, text='INT:', font=("Helvetica", 16))
        self.INTIntroLabel.place(x=1024, y=320, anchor=NE, height=32, width=128)
        self.INTLabel = Label(root, textvariable=INTText, bd=2, relief=SUNKEN, anchor=CENTER, font=("Helvetica", 16))
        self.INTLabel.place(x=1024, y=352, anchor=NE, height=32, width=128)
        self.CHAIntroLabel = Label(root, bd=1, relief=SUNKEN, anchor=CENTER, text='CHA:', font=("Helvetica", 16))
        self.CHAIntroLabel.place(x=1024, y=384, anchor=NE, height=32, width=128)
        self.CHALabel = Label(root, textvariable=CHAText, bd=2, relief=SUNKEN, anchor=CENTER, font=("Helvetica", 16))
        self.CHALabel.place(x=1024, y=416, anchor=NE, height=32, width=128)

        self.StatRollButton = Button(root, text='Roll Stats', command=self.roll_stats, font=('Helvetica', 14))
        self.StatRollButton.place(x=1024, y=448, anchor=NE, height=32, width=128)

        self.RollWindow = Toplevel(root)
        self.RollWindow.title('Stat Rolling')
        self.RollWindow.geometry('420x120')
        self.RollWindow.resizable(0, 0)

        self.SubSTRIntroLabel = Label(self.RollWindow, anchor=CENTER, text='STR?', font=('Helvetica', 16))
        self.SubSTRIntroLabel.place(x=0, y=40, anchor=NW, height=40, width=70)
        self.SubSTRLabel = Label(self.RollWindow, anchor=CENTER, textvariable=STR, font=('Helvetica', 16))
        self.SubDEXIntroLabel = Label(self.RollWindow, anchor=CENTER, text='DEX?', font=('Helvetica', 16))
        self.SubDEXLabel = Label(self.RollWindow, anchor=CENTER, textvariable=DEX, font=('Helvetica', 16))
        self.SubCONIntroLabel = Label(self.RollWindow, anchor=CENTER, text='CON?', font=('Helvetica', 16))
        self.SubCONLabel = Label(self.RollWindow, anchor=CENTER, textvariable=CON, font=('Helvetica', 16))
        self.SubWISIntroLabel = Label(self.RollWindow, anchor=CENTER, text='WIS?', font=('Helvetica', 16))
        self.SubWISLabel = Label(self.RollWindow, anchor=CENTER, textvariable=WIS, font=('Helvetica', 16))
        self.SubINTIntroLabel = Label(self.RollWindow, anchor=CENTER, text='INT?', font=('Helvetica', 16))
        self.SubINTLabel = Label(self.RollWindow, anchor=CENTER, textvariable=INT, font=('Helvetica', 16))
        self.SubCHAIntroLabel = Label(self.RollWindow, anchor=CENTER, text='CHA?', font=('Helvetica', 16))
        self.SubCHALabel = Label(self.RollWindow, anchor=CENTER, textvariable=CHA, font=('Helvetica', 16))

        self.RollWindow.withdraw()

    def roll_stats(self):
        self.RollWindow.update()
        self.RollWindow.deiconify()

        self.SubSTRIntroLabel.config(text='STR?')
        self.SubSTRLabel.place_forget()
        self.SubDEXIntroLabel.config(text='DEX?')
        self.SubDEXIntroLabel.place_forget()
        self.SubDEXLabel.place_forget()
        self.SubCONIntroLabel.config(text='CON?')
        self.SubCONIntroLabel.place_forget()
        self.SubCONLabel.place_forget()
        self.SubWISIntroLabel.config(text='WIS?')
        self.SubWISIntroLabel.place_forget()
        self.SubWISLabel.place_forget()
        self.SubINTIntroLabel.config(text='INT?')
        self.SubINTIntroLabel.place_forget()
        self.SubINTLabel.place_forget()
        self.SubCHAIntroLabel.config(text='CHA?')
        self.SubCHAIntroLabel.place_forget()
        self.SubCHALabel.place_forget()

        Skills = DiceRoller.charactercreation()

        RollButton1 = Button(self.RollWindow, text=Skills[0], command=lambda: self.set_current_stat(RollButton1),
                             font=('Helvetica', 16))
        RollButton1.place(x=0, y=0, anchor=NW, height=40, width=70)
        RollButton2 = Button(self.RollWindow, text=Skills[1], command=lambda: self.set_current_stat(RollButton2),
                             font=('Helvetica', 16))
        RollButton2.place(x=70, y=0, anchor=NW, height=40, width=70)
        RollButton3 = Button(self.RollWindow, text=Skills[2], command=lambda: self.set_current_stat(RollButton3),
                             font=('Helvetica', 16))
        RollButton3.place(x=140, y=0, anchor=NW, height=40, width=70)
        RollButton4 = Button(self.RollWindow, text=Skills[3], command=lambda: self.set_current_stat(RollButton4),
                             font=('Helvetica', 16))
        RollButton4.place(x=210, y=0, anchor=NW, height=40, width=70)
        RollButton5 = Button(self.RollWindow, text=Skills[4], command=lambda: self.set_current_stat(RollButton5),
                             font=('Helvetica', 16))
        RollButton5.place(x=280, y=0, anchor=NW, height=40, width=70)
        RollButton6 = Button(self.RollWindow, text=Skills[5], command=lambda: self.set_current_stat(RollButton6),
                             font=('Helvetica', 16))
        RollButton6.place(x=350, y=0, anchor=NW, height=40, width=70)

    def set_current_stat(self, buttonpressed):
        if '?' in self.SubSTRIntroLabel.cget('text'):
            STR.set(int(buttonpressed.cget('text')))
            self.SubSTRIntroLabel.config(text='STR:')
            self.SubSTRLabel.place(x=0, y=80, anchor=NW, height=40, width=70)
            self.SubDEXIntroLabel.place(x=70, y=40, anchor=NW, height=40, width=70)
            buttonpressed.destroy()
        elif '?' in self.SubDEXIntroLabel.cget('text'):
            DEX.set(int(buttonpressed.cget('text')))
            self.SubDEXIntroLabel.config(text='DEX:')
            self.SubDEXLabel.place(x=70, y=80, anchor=NW, height=40, width=70)
            self.SubCONIntroLabel.place(x=140, y=40, anchor=NW, height=40, width=70)
            buttonpressed.destroy()
        elif '?' in self.SubCONIntroLabel.cget('text'):
            CON.set(int(buttonpressed.cget('text')))
            self.SubCONIntroLabel.config(text='CON:')
            self.SubCONLabel.place(x=140, y=80, anchor=NW, height=40, width=70)
            self.SubWISIntroLabel.place(x=210, y=40, anchor=NW, height=40, width=70)
            buttonpressed.destroy()
        elif '?' in self.SubWISIntroLabel.cget('text'):
            WIS.set(int(buttonpressed.cget('text')))
            self.SubWISIntroLabel.config(text='WIS:')
            self.SubWISLabel.place(x=210, y=80, anchor=NW, height=40, width=70)
            self.SubINTIntroLabel.place(x=280, y=40, anchor=NW, height=40, width=70)
            buttonpressed.destroy()
        elif '?' in self.SubINTIntroLabel.cget('text'):
            INT.set(int(buttonpressed.cget('text')))
            self.SubINTIntroLabel.config(text='INT:')
            self.SubINTLabel.place(x=280, y=80, anchor=NW, height=40, width=70)
            self.SubCHAIntroLabel.place(x=350, y=40, anchor=NW, height=40, width=70)
            buttonpressed.destroy()
        elif '?' in self.SubCHAIntroLabel.cget('text'):
            CHA.set(int(buttonpressed.cget('text')))
            self.SubCHAIntroLabel.config(text='CHA:')
            self.SubCHALabel.place(x=350, y=80, anchor=NW, height=40, width=70)
            buttonpressed.destroy()
            self.RollWindow.withdraw()
            self.StatRollButton.config(text='Re-Roll Stats')
            update_basestats()


def load_character():
    filename = filedialog.askopenfilename(parent=root)
    file = open(filename, 'r')
    count = len(file.readlines())
    file.close()
    file = open(filename, 'r')
    for linenum in range(1, count+1):
        if linenum == 1:
            print(file.readline()[:-1])
        elif linenum == 2:
            Race.set(file.readline()[:-1])
        elif linenum == 3:
            SubRace.set(file.readline()[:-1])
        elif linenum == 4:
            Class.set(file.readline()[:-1])
        elif linenum == 5:
            SubClass.set(file.readline()[:-1])
        elif linenum == 6:
            Alignment.set(file.readline()[:-1])
        elif linenum == 7:
            Experience.set(int(file.readline()[:-1]))
        elif linenum == 8:
            STR.set(int(file.readline()[:-1]))
        elif linenum == 9:
            DEX.set(int(file.readline()[:-1]))
        elif linenum == 10:
            CON.set(int(file.readline()[:-1]))
        elif linenum == 11:
            WIS.set(int(file.readline()[:-1]))
        elif linenum == 12:
            INT.set(int(file.readline()[:-1]))
        elif linenum == 13:
            CHA.set(int(file.readline()[:-1]))
    file.close()

    open_subrace()
    open_subclass()
    update_experience()
    update_basestats()
    Stats.StatRollButton.config(text='Re-Roll Stats')


def save_character():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.ddc')
    file.write('\n')
    file.write(Race.get() + '\n')
    file.write(SubRace.get() + '\n')
    file.write(Class.get() + '\n')
    file.write(SubClass.get() + '\n')
    file.write(Alignment.get() + '\n')
    file.write(str(Experience.get()) + '\n')
    file.write(str(STR.get()) + '\n')
    file.write(str(DEX.get()) + '\n')
    file.write(str(CON.get()) + '\n')
    file.write(str(WIS.get()) + '\n')
    file.write(str(INT.get()) + '\n')
    file.write(str(CHA.get()) + '\n')
    file.close()


def update_basestats():
    STRMod.set(np.floor((STR.get() + STRRacial.get() - 10)/2))
    DEXMod.set(np.floor((DEX.get() + DEXRacial.get() - 10)/2))
    CONMod.set(np.floor((CON.get() + CONRacial.get() - 10)/2))
    WISMod.set(np.floor((WIS.get() + WISRacial.get() - 10)/2))
    INTMod.set(np.floor((INT.get() + INTRacial.get() - 10)/2))
    CHAMod.set(np.floor((CHA.get() + CHARacial.get() - 10)/2))

    STRText.set('{} ({:+d})'.format(STR.get() + STRRacial.get(), STRMod.get()))
    DEXText.set('{} ({:+d})'.format(DEX.get() + DEXRacial.get(), DEXMod.get()))
    CONText.set('{} ({:+d})'.format(CON.get() + CONRacial.get(), CONMod.get()))
    WISText.set('{} ({:+d})'.format(WIS.get() + WISRacial.get(), WISMod.get()))
    INTText.set('{} ({:+d})'.format(INT.get() + INTRacial.get(), INTMod.get()))
    CHAText.set('{} ({:+d})'.format(CHA.get() + CHARacial.get(), CHAMod.get()))


def update_experience():
    while Experience.get() >= EXPLEVELS[Level.get()]:
        Level.set(Level.get() + 1)
    ExperienceText.set('EXP: {}'.format(Experience.get()))
    LevelText.set('Level: {}'.format(Level.get()))


def update_race():
    if SubRace.get() == '':
        FullRace.set('Race: ' + Race.get())
    else:
        FullRace.set('Race: ' + SubRace.get() + ' ' + Race.get())

    if len(SUBRACES[Race.get()]) == 0:
        RaceFile = open('Races/' + Race.get().replace(' ', '_') + '.race', 'r')

        RaceFile.readline()
        STRRacial.set(int(RaceFile.readline()[:-1]))
        DEXRacial.set(int(RaceFile.readline()[:-1]))
        CONRacial.set(int(RaceFile.readline()[:-1]))
        WISRacial.set(int(RaceFile.readline()[:-1]))
        INTRacial.set(int(RaceFile.readline()[:-1]))
        CHARacial.set(int(RaceFile.readline()[:-1]))

        RaceFile.close()
        update_basestats()
    else:
        if not SubRace.get() == '':
            RaceFile = open('Races/' + Race.get().replace(' ', '_') + '/' + SubRace.get() + '.race', 'r')

            RaceFile.readline()
            STRRacial.set(int(RaceFile.readline()[:-1]))
            DEXRacial.set(int(RaceFile.readline()[:-1]))
            CONRacial.set(int(RaceFile.readline()[:-1]))
            WISRacial.set(int(RaceFile.readline()[:-1]))
            INTRacial.set(int(RaceFile.readline()[:-1]))
            CHARacial.set(int(RaceFile.readline()[:-1]))

            RaceFile.close()
            update_basestats()


def update_class():
    if SubClass.get() == '':
        FullClass.set('Class: ' + Class.get())
    else:
        FullClass.set('Class: ' + SubClass.get() + ' ' + Class.get())


def open_subrace():
    if len(SubRace.get()) == 0 or SubRace.get() not in SUBRACES[Race.get()]:
        SubRace.set('')
    update_race()

    for button in RaceWindow.winfo_children():
        if button.cget('text') not in RACES and button.cget('text') != 'Confirm':
            button.destroy()

    if len(SUBRACES[Race.get()]) > 0:
        for row in range(int(np.ceil(len(SUBRACES[Race.get()]) / 2))):
            b = Radiobutton(RaceWindow, text=SUBRACES[Race.get()][row * 2], variable=SubRace, indicatoron=0,
                            value=SUBRACES[Race.get()][row * 2], command=update_race)
            b.place(x=496, y=row * 48, anchor=NW, height=48, width=96)
            if (2 * row + 1) < len(SUBRACES[Race.get()]):
                b = Radiobutton(RaceWindow, text=SUBRACES[Race.get()][row * 2 + 1], variable=SubRace, indicatoron=0,
                                value=SUBRACES[Race.get()][row * 2 + 1], command=update_race)
                b.place(x=592, y=row * 48, anchor=NW, height=48, width=96)
    else:
        SubRace.set('')


def open_subclass():
    if len(SubClass.get()) == 0 or SubClass.get() not in SUBCLASSES[Class.get()]:
        SubClass.set('')
    update_class()

    for button in ClassWindow.winfo_children():
        if button.cget('text') not in CLASSES and button.cget('text') != 'Confirm':
            button.destroy()

    if len(SUBCLASSES[Class.get()]) > 0:
        for row in range(int(np.ceil(len(SUBCLASSES[Class.get()]) / 3))):
            b = Radiobutton(ClassWindow, text=SUBCLASSES[Class.get()][row * 3], variable=SubClass, indicatoron=0,
                            value=SUBCLASSES[Class.get()][row * 3], command=update_class)
            b.place(x=208, y=row * 48, anchor=NW, height=48, width=96)
            if (3 * row + 1) < len(SUBCLASSES[Class.get()]):
                b = Radiobutton(ClassWindow, text=SUBCLASSES[Class.get()][row * 3 + 1], variable=SubClass,
                                indicatoron=0, value=SUBCLASSES[Class.get()][row * 3 + 1], command=update_class)
                b.place(x=304, y=row * 48, anchor=NW, height=48, width=96)
                if (3 * row + 2) < len(SUBCLASSES[Class.get()]):
                    b = Radiobutton(ClassWindow, text=SUBCLASSES[Class.get()][row * 3 + 2], variable=SubClass,
                                    indicatoron=0, value=SUBCLASSES[Class.get()][row * 3 + 2], command=update_class)
                    b.place(x=400, y=row * 48, anchor=NW, height=48, width=96)
    else:
        SubClass.set('')


def race_select():
    RaceWindow.update()
    RaceWindow.deiconify()


def class_select():
    ClassWindow.update()
    ClassWindow.deiconify()


def alignment_select():
    AlignmentWindow.update()
    AlignmentWindow.deiconify()

    for button in AlignmentWindow.winfo_children():
        if button.cget('text') in ALIGNMENTS:
            if Race.get() == '':
                button.config(fg='black')
            else:
                button.config(fg=STANDARDALIGNMENTS[Race.get()][ALIGNMENTS.index(button.cget('text'))])


def add_exp():
    EXPWindow = Toplevel(root)
    EXPWindow.title('EXP Additions')
    EXPWindow.geometry('192x48')
    EXPWindow.resizable(0, 0)

    EXPEntry = Entry(EXPWindow)
    EXPEntry.place(x=0, y=0, anchor=NW, height=24, width=192)

    def close_exp():
        try:
            Experience.set(Experience.get()+ int(EXPEntry.get()))
            ExperienceText.set('EXP: {}'.format(Experience.get()))
            while Experience.get() >= EXPLEVELS[Level.get()]:
                Level.set(Level.get() + 1)
            LevelText.set('Level: {}'.format(Level.get()))
            EXPWindow.destroy()
        except ValueError:
            EXPEntry.delete(0, END)
            EXPEntry.insert(0, 'Please enter a whole number.')

    Confirmation = Button(EXPWindow, text='Confirm', command=close_exp)
    Confirmation.place(x=64, y=24, anchor=NW, height=24, width=64)


########################################################################################################################
# Set up root
########################################################################################################################

root = Tk()
root.title('Dungeons and Dragons GUI Master Tool')
root.geometry('1024x512')
root.resizable(0, 0)

########################################################################################################################
# Set up menus
########################################################################################################################

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=load_character)
filemenu.add_command(label='Save', command=save_character)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_separator()
editmenu.add_command(label='Select Race', command=race_select)
editmenu.add_command(label='Select Class', command=class_select)
editmenu.add_command(label='Select Alignment', command=alignment_select)

optionmenu = Menu(menu)
menu.add_cascade(label='Options', menu=optionmenu)

########################################################################################################################
# Set up variables
########################################################################################################################

Race = StringVar()
SubRace = StringVar()
FullRace = StringVar()
Race.set('')
SubRace.set('')
FullRace.set('Race: ')

Class = StringVar()
SubClass = StringVar()
FullClass = StringVar()
Class.set('')
SubClass.set('')
FullClass.set('Class: ')

Name = StringVar()
Name.set('Name Goes Here')

Alignment = StringVar()
Alignment.set('Alignment')

Experience = IntVar()
Experience.set(0)
ExperienceText = StringVar()
ExperienceText.set('EXP: {}'.format(Experience.get()))

Level = IntVar()
Level.set(1)
LevelText = StringVar()
LevelText.set('Level: {}'.format(Level.get()))

STR = IntVar()
DEX = IntVar()
CON = IntVar()
WIS = IntVar()
INT = IntVar()
CHA = IntVar()
STR.set(0)
DEX.set(0)
CON.set(0)
WIS.set(0)
INT.set(0)
CHA.set(0)

STRRacial = IntVar()
DEXRacial = IntVar()
CONRacial = IntVar()
WISRacial = IntVar()
INTRacial = IntVar()
CHARacial = IntVar()
STRRacial.set(0)
DEXRacial.set(0)
CONRacial.set(0)
WISRacial.set(0)
INTRacial.set(0)
CHARacial.set(0)

STRMod = IntVar()
DEXMod = IntVar()
CONMod = IntVar()
WISMod = IntVar()
INTMod = IntVar()
CHAMod = IntVar()
STRMod.set(0)
DEXMod.set(0)
CONMod.set(0)
WISMod.set(0)
INTMod.set(0)
CHAMod.set(0)

STRText = StringVar()
DEXText = StringVar()
CONText = StringVar()
WISText = StringVar()
INTText = StringVar()
CHAText = StringVar()
STRText.set('{} ({:+d})'.format(STR.get(), STRMod.get()))
DEXText.set('{} ({:+d})'.format(DEX.get(), DEXMod.get()))
CONText.set('{} ({:+d})'.format(CON.get(), CONMod.get()))
WISText.set('{} ({:+d})'.format(WIS.get(), WISMod.get()))
INTText.set('{} ({:+d})'.format(INT.get(), INTMod.get()))
CHAText.set('{} ({:+d})'.format(CHA.get(), CHAMod.get()))

########################################################################################################################
# Set up Labels
########################################################################################################################

NameLabel = Label(root, textvariable=Name, anchor=W, font=("Helvetica", 24), bd=16)
NameLabel.place(x=0, y=0, anchor=NW, height=48, width=512)

RaceLabel = Label(root, textvariable=FullRace, anchor=W, font=('Helvetica', 10), bd=8)
RaceLabel.place(x=512, y=0, anchor=NW, height=24, width=256)

AlignmentLabel = Label(root, textvariable=Alignment, anchor=W, font=('Helvetica', 12), bd=8)
AlignmentLabel.place(x=768, y=0, anchor=NW, height=24, width=128)

LevelLabel = Label(root, textvariable=LevelText, anchor=W, font=('Helvetica', 12), bd=8)
LevelLabel.place(x=896, y=0, anchor=NW, height=24, width=128)

ClassLabel = Label(root, textvariable=FullClass, anchor=W, font=('Helvetica', 10), bd=8)
ClassLabel.place(x=512, y=24, anchor=NW, height=24, width=256)

ExperienceLabel = Label(root, textvariable=ExperienceText, anchor=W, font=('Helvetica', 12), bd=8)
ExperienceLabel.place(x=768, y=24, anchor=NW, height=24, width=192)

AddEXPButton = Button(root, text='Add EXP', command=add_exp)
AddEXPButton.place(x=960, y=24, anchor=NW, height=24, width=64)

Stats = StatsLabel(root)
Stats.place(x=1024, y=48, anchor=NE)

########################################################################################################################
# Set up RaceWindow
########################################################################################################################

RaceWindow = Toplevel(root)
RaceWindow.title('Race Select')
RaceWindow.geometry('688x336')
RaceWindow.resizable(0, 0)

for col in range(5):
    for row in range(7):
        b = Radiobutton(RaceWindow, text=RACES[col + row * 5], variable=Race, value=RACES[col + row * 5], indicatoron=0,
                        command=open_subrace)
        if RACES[col + row * 5] in MONSTERRACES:
            b.config(fg='red')
        else:
            b.config(fg='green')
        b.place(x=96*col, y=row*48, anchor=NW, height=48, width=96)

b = Button(RaceWindow, text='Confirm', command=RaceWindow.withdraw)
b.place(x=496, y=288, anchor=NW, height=48, width=192)

RaceWindow.withdraw()

########################################################################################################################
# Set up ClassWindow
########################################################################################################################

ClassWindow = Toplevel(root)
ClassWindow.title('Class Select')
ClassWindow.geometry('608x336')
ClassWindow.resizable(0, 0)

for col in range(2):
    for row in range(7):
        b = Radiobutton(ClassWindow, text=CLASSES[col + row * 2], variable=Class, value=CLASSES[col + row * 2],
                        indicatoron=0, command=open_subclass)
        if CLASSES[col + row * 2] in FULLCASTER:
            b.config(fg='red')
        elif CLASSES[col + row * 2] in HALFCASTER:
            b.config(fg='blue')
        else:
            b.config(fg='green')
        b.place(x=96*col, y=row*48, anchor=NW, height=48, width=96)

b = Button(ClassWindow, text='Confirm', command=ClassWindow.withdraw)
b.place(x=512, y=0, anchor=NW, height=336, width=96)

ClassWindow.withdraw()

########################################################################################################################
# Set up AlignmentWindow
########################################################################################################################

AlignmentWindow = Toplevel(root)
AlignmentWindow.title('Alignment Select')
AlignmentWindow.geometry('288x208')
AlignmentWindow.resizable(0, 0)

for col in range(3):
    for row in range(3):
        b = Radiobutton(AlignmentWindow, text=ALIGNMENTS[col * 3 + row], variable=Alignment,
                        value=ALIGNMENTS[col * 3 + row], indicatoron=0)
        if Race.get() != '':
            b.config(fg=STANDARDALIGNMENTS[Race.get()][col * 3 + row])
        b.place(x=96*col, y=row*48, anchor=NW, height=48, width=96)

b = Button(AlignmentWindow, text='Confirm', command=AlignmentWindow.withdraw)
b.place(x=0, y=160, anchor=NW, height=48, width=288)

AlignmentWindow.withdraw()

########################################################################################################################
# Set up Saving Throws
########################################################################################################################

SaveLabel = Label(root, text='Saving Throws')
SaveLabel.place(x=0, y=48, anchor=NW, height=24, width=128)

########################################################################################################################
# Initiate tkInter windows
########################################################################################################################

root.mainloop()
