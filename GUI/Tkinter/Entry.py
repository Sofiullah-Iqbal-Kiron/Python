from tkinter import *

root = Tk()
root.title('Entry Or TextField')

# Entry means entering or input data in a field.
# So, it can be called as, entry widget (TextField in Java for single
# line text input), we can write something stuff in it.
# Used to collect input from a user.
# width, fg, bg, borderwidth
ent = Entry(root, width=40, fg='blue', borderwidth=1)
ent.pack()

# Or the same thing is as:
Entry(root, width=40, bg='green').pack()


def whttypt():
    lbl=Label(root,text=ent.get())


btn = Button(root, command=whttypt).pack()

root.mainloop()
