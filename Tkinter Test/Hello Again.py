# Import statements
from tkinter import *


# Many applications, especially large ones can benefit from having a dedicated class for them. This being an example.
# The constructor method (or instantiation method) is called with a parent widget argument (master).
# The first thing we construct is a Frame widget, which is used as a container for other widges.
class App:
    def __init__(self, master):
        # Once again, to make the widget visible, we immediately pack the widget using the assigned local variable.
        # Note that where you pack things affects where they appear on the window
        frame = Frame(master)
        frame.pack()

        # Next we create two Button widgets which are children to the frame, which is a child of master
        # There are a number of options here that we have included. The first and easiest is text which is simply the
        # text that appears on the button
        # Next there is fg, shorthand for foreground, and sets the color of the foreground (in this case text)
        # Finally we have the command option which specifies a function that occurs when a button is clicked

        # For the QUIT button, the method that is called if frame.quit which exits the application, similar to pressing
        # The red X button in the top right of the application
        self.button = Button(frame, text='QUIT', fg='red', command=frame.quit)
        self.button.pack(side=LEFT)

        # For the Hello button, the method that is called is a static method in the class, say_hi, which simply prints a
        # statement to the console.
        self.hi_there = Button(frame, text='Hello', command=self.say_hi)
        # Additionally, we have added are argument to our pack method, side. This creates the widget flush with which
        # side is chosen, with respect to the parent. If no side is given, the default is TOP
        # Here, the buttons are both added to the LEFT side of the frame widget. The frame above is defaulted to the
        # top of the master widget
        self.hi_there.pack(side=LEFT)

        # Here is another test button that changes slightly some things about the code above so that it can be compared
        self.bye = Button(master, text='Bye', command=self.say_bye)
        self.bye.pack()

    # This static method is used to print a message to the console when the Hello button is pushed
    @staticmethod
    def say_hi():
        print('hi there, everyone!')

    # This static method is used to print a message to the console when the Bye button is pushed
    @staticmethod
    def say_bye():
        print('Goodbye, everyone!')


# Finally, we must create our root widget and an instance of the App class. When we pass our root variable to the class,
# we instantiate and visualize the frame and three buttons that are made in the App class.
root = Tk()

app = App(root)

# Once again, we then call the mainloop and the hard work is done for us
# The destroy method is only required under certain conditions and destroys the window after the main loop is finished
# Some environments won't terminate the python process until this method is called, so it is safe to include it here.
root.mainloop()
root.destroy()

# There are a few more things that may be interesting to discuss about this code.
# Firstly, there is this problem of widget references. Here, we use two different scopes in which to reference widgets,
# The local, which frame is on, and the class instance, which the buttons are on.
# However, there is no need to keep a reference of a widget instance since Tkinter maintains a tree with the parent and
# children attributes of each widget instance. However, if it should be removed, it can be explicitly using the destroy
# method. Alternatively, if as the coder, you want to do something with the created widget, you need a reference to it
# at the proper scope. It is always safer to keep some reference to a widget and pack on a separate line

# Secondly, there is a concern with widget names. Widget are all assigned a name, but often than not, the name that you
# use is not the name that is assigned to a widget. Tkinter automatically create the widget's name upon creation, mostly
# as a series of numbers. This is how Tkinter will reference these widgets, however, you can reference them by what you
# instantiate the name of the variable to be, for example frame. If you would like to get the name that Tkinter has
# created for the widget, you can simply apply the str function to the widget instance. Additionally, in the event that
# a widget needs to have a name specified, you can use the name option when created the widget. It is better to avoid
# conflicts with Tkinter by creating a name that is not only digits. Additionally, once a widget is named, it cannot
# be renamed.

# There are 15 core widgets in Tkinter:
# Button    Canvas  Checkbutton Entry   Frame   Label   Listbox Menu    Menubutton  Message Radiobutton Scale
# Scrollbar Text    Toplevel
# Tk 8.4 adds three more:
# LabelFrame    PanedWindow Spinbox

# There are many useful methods that are used by most if not all wigets:
# widgetclass(master, option=value, ...) => widget  [Instantiates a widget class as a child to a master]
# cget('option') => string                          [Returns the current value of an option]
# config(option=value, ...)                         [Sets an option(s) with the value given]
# configure(option=value, ...)                      [Same as above, note that set and get can also be used as a dict]
# keys() => list                                    [Returns a list of all options that can be set for a widget]
