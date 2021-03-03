# Import Statements
from tkinter import *

# Tkinter handles a lot that the user doesn't has to, but there is a great tool that we can use to take control
# Each widget has a bind function that can tie together python methods to events that Tkinter recognizes
# widget.bind(event, handler)      [Passes an object description to the handler function if event occurs]

# Instantiate a root widget
root = Tk()


# Create a function that prints the character of the key that is pressed
def key(event):
    print(1)
    print("Pressed {}".format(repr(event.char)))


# Create a function that prints the coordinates of a mouse click when called
# Also changes the focus to the frame so that keypresses can be used
def callback(event):
    frame.focus_set()
    print("Clicked at ({}, {})".format(event.x, event.y))


# Instantiates a frame with specified width and height
# Uses the new bind function that binds the callback function to an event called <Button-1> (Left mouse click)
# Uses the bind function to bind the key function to an event called <Key> (Any key press)
frame = Frame(root, width=300, height=300)
frame.bind("<Key>", key)
frame.bind('<Button-1>', callback)
frame.pack()

# Instantiates, visualizes, and maintains the window
root.mainloop()

# Events are always stylized in <modifier-type-detail>, where type is the most important as it specifies the kind of
# event, such as a mouse button press or a key press. The modifier and detail fields are used for additional information
# Here are a list of event formats and rules:
# <Button-1>        [Corresponds to a specific mouse button when pressed, (1 is Left, 2 is middle, 3 is right)]
# <ButtonPres-1>    [Same as above]
# <1>               [Same as above]
# <B1-Motion>       [Corresponds to a movement of the mouse when button 1 is pressed]
# <ButtonRelease-1> [Corresponds to the release of mouse button 1]
# <Double-Button-1> [Corresponds to when button 1 is double clicked]
# <Triple-Button-1> [Corresponds to when button 1 is triple clicked]
# <Enter>           [Corresponds to when the mouse cursor enters the widget space (Note, not the enter key)]
# <Leave>           [Corresponds to when the mouse cursor leaves the widget space]
# <FocusIn>         [Corresponds to when the keyboard focus was moved to this widget or one of its children]
# <FocusOut>        [Corresponds to when the keyboard focus was moved away from this widget]
# <Return>          [Corresponds to when the enter key is pressed]
# <Key>             [Corresponds to any key press]
# a                 [Corresponds to a specific printable character, exceptions are space and less-than (less)]
# <Shift-Up>        [Corresponds to holding the shift key and the up arrow, works with alt/shift/ctrl and any direction]
# <Configure>       [Corresponds to when the widget changed size and/or location]
# Note that other special keys include Cancel (Break), BackSpace, Tab, Shift_L, Control_L, Alt_L, Pause, Caps_Lock,
# Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4,
# F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, Scroll_Lock

# The events all have attributes that can be referenced in corresponding event functions. Some main ones include:
# widget            [The widget that generated this event]
# x, y              [The x and y coordinates of the current mouse position (in pixels)]
# x_root, y_root    [The current mouse position relative to the upper left corner of the screen (in pixels)]
# char              [The character code as a string]        {Keyboard events}
# keysym            [The key symbol]                        {Keyboard events}
# keycode           [The key code]                          {Keyboard events}
# num               [The button number]                     {Mouse Button events}
# width, height     [The new size of the widget in pixels]  {Configure events}
# type              [The event type]
