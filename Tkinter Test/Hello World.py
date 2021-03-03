# Import Statements:
from tkinter import *

########################################################################################################################
# Instantiating a Tk interface
# Root is a standard widget, a window with a title bar stylized by Windows, only create one for each program and before
# Anything else.
root = Tk()

# Create a label in the root window. This label is also a widget that is a 'Child' to the 'Parent' root window
# Label can display text or icons or images, here we use the text option to display text
# The pack method makes the label visible and fits the text to the widget
w = Label(root, text='Hello, world!')
w.pack()

# This loop create the window that we have made and makes it visible. The loop will end when we close the pop-up window.
# It handles everything such as user events, system events, and Tkinter events.
# So of these things include display updates and geometry management (such as the pack method)
root.mainloop()
