from tkinter import *

# Functions will appear here
# We gonna use, button, entry, border, frame container

root = Tk()
root.title('Simple Calculator')  # Just type-in whatever you want
# OR, root.resizable(0/1/True, 0/1/True) or, root.resizable(width=none, height=none)
root.resizable(False, False)
root.configure(bg='gray')

# Entry for user input
ent = Entry(root, width=40, borderwidth=3, bg='white', fg='blue', font=('times new roman', '8')).grid(row=0, column=0,
                                                                                                      columnspan=3)

# Buttons 1 to 9, try with loop, later.
btn0 = Button(root, text='0', padx=12, pady=8)

btn7 = Button(root, text='7', padx=32, pady=25).grid(row=1, column=0)
btn8 = Button(root, text='8', padx=32, pady=25).grid(row=1, column=1)
btn9 = Button(root, text='9', padx=32, pady=25).grid(row=1, column=2)

btn4 = Button(root, text='4', padx=32, pady=25).grid(row=2, column=0)
btn5 = Button(root, text='5', padx=32, pady=25).grid(row=2, column=1)
btn6 = Button(root, text='6', padx=32, pady=25).grid(row=2, column=2)

btn1 = Button(root, text='1', padx=32, pady=25).grid(row=3, column=0)
btn2 = Button(root, text='2', padx=32, pady=25).grid(row=3, column=1)
btn3 = Button(root, text='3', padx=32, pady=25).grid(row=3, column=2)

# Operator buttons
plus = Button(root, text='+', padx=12, pady=8)
minus = Button(root, text='-', padx=12, pady=8)
multiplication = Button(root, text='*', padx=12, pady=8)
division = Button(root, text='÷', padx=12, pady=8)
root.mainloop()
