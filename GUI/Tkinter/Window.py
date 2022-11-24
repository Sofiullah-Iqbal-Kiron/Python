from tkinter import *

windowMain = Tk("")
windowMain.title("Window Demonstration")

Button(windowMain, text="Hello", padx=50, pady=50).grid(row=0, column=0)

windowMain.mainloop()
