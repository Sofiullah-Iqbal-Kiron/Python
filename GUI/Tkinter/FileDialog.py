from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File Dialog")

fd = filedialog.LoadFileDialog
filedialog.asksaveasfilename()
root.geometry("300x200")

root.mainloop()
