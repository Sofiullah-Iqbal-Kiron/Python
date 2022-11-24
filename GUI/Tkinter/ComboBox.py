import tkinter
from tkinter import ttk
from tkinter import *

root = tkinter.Tk()
root.title("ComboBox Demonstration!")

values = StringVar()
cb = ttk.Combobox(root)
cb['values'] = ("1", "2")
cb.current(1)
cb.pack()
print(cb.get())

root.mainloop()
