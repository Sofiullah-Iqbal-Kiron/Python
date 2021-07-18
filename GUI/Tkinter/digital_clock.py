from tkinter import *  # From tkinter package, import all (*) classes.
from tkinter.ttk import *
from time import strftime

# tkinter stands for interface toolkit. Running "python -m tkinter" from terminal
# should open a simple tkinter interface, letting you know that tkinter in properly installed on your system.
# Tk is a shared library.
# This class is very handy for application programmers.
# Importing tkinter will auto-import tkinter.constants
# Tk(): is a class instantiated without arguments.

# 'root' is a object instantiated by class Tk(). After instantiating, we can use all of it's methods to 'root'.
# Now, 'root' belongs to Tk().
# Tk.title(string)
# Tk.
root = Tk()
root.title('Digital Clock')


# Left 2 newlines before and after of all functions definition.
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')
time()
mainloop()
