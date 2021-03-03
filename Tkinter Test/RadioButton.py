from tkinter import *

root = Tk()

v = StringVar()

CHARS = [('Aasimar', '7'), ('Goblin', '3')]

for text, mode in CHARS:
    b = Radiobutton(root, text=text, variable=v, value=mode, indicatoron=0)
    b.pack(anchor=W)

root.mainloop()
