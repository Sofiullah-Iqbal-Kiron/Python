import tkinter

from customtkinter import *

set_appearance_mode("dark")
set_default_color_theme("green")

root = CTk()
root.geometry("400X240")


def pressed():
    val = get_appearance_mode()
    if val == "Dark":
        set_appearance_mode("light")
    else:
        set_appearance_mode("dark")
    root.update()


button = CTkButton(master=root, text="Change Mode!", command=pressed)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
