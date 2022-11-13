# Grids have rows and columns.
# Grid is a system for positioning widgets.

from tkinter import *

root = Tk()
label1 = Label(root, text='Hello,World!')
label2 = Label(root, text='New text here.')

# Labels will stay right where it is.
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

# We get the exact same thing if
# label1 = Label(root, text='Hello,World!').grid(row=0, column=0)
# label2 = Label(root, text='New text here.').grid(row=1, column=1)
# Cause python is object oriented.

root.mainloop()
