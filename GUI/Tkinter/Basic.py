# Whatever is frame or component in Java, all of them called widget in Python.

from tkinter import *

root = Tk()

# Create a label with Label() widget. In other words, instantiate an object of Label class,
# it will done by constructor. Label goes to root widget.
myLabel = Label(root, text='Hello, World!')
myLabel.pack()  # Shoving it onto the screen.

# Anything we see on the screen is a loop. Every program is continuously looping that's why the program works.
root.mainloop() # in mainloop, L must be lowercase.
