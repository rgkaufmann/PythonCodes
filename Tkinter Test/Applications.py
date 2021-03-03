# Import statements
from tkinter import *


class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, formatting, *args):
        self.label.config(text=formatting % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


# A quick method that prints a statement
def callback():
    print("Called the callback!")


# Here we want to explore the use of multiple windows. We begin with our standard root window
root = Tk()

# Let us construct a menu. Here we can create a menu instance and make it a child of the root widget
# In order to display the menu, we pass it to the config of the root widget, and it is automatically updated to be on
# a menubar at the top of the root window.
menu = Menu(root)
root.config(menu=menu)

# We can then create a new menu and add it to original menu object by putting it in a cascade submenu
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
# Once the submenu is added, we can put in commands with a label and a function to call
filemenu.add_command(label='New', command=callback)
filemenu.add_command(label='Open...', command=callback)
# Separators are bar that are put in place in order to group menu entries
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

# We also make a help menu in a similar fashion
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About...', command=callback)

# In order to create a toolbar, we simply make a frame to put buttons into
toolbar = Frame(root)

# Note that the buttons are pushed to the left while the toolbar itself is pushed to the top. Additionally, we set the
# fill option to X and the widget is resized to cover the full parent widget
b = Button(toolbar, text="new", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text='open', width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

status = StatusBar(root)
status.pack(side=BOTTOM, fill=X)

# However, we can also create a new window using the Toplevel widget. Note that if we construct this new window, we
# don't need to call pack or any geometry to display it.
top = Toplevel()

# Here we can construct any child widgets to put into the toplevel window

# And of course we must run the main loop
root.mainloop()
