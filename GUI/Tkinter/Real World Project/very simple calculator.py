from tkinter import *

# Functions will appear here
# We gonna use, button, entry, border, frame container

root = Tk()
root.title('Simple Calculator')  # Just type-in whatever you want

# Entry for user input
ent = Entry(root, borderwidth=3, bg='white', fg='blue', font=('times new roman', '8')).grid(row=0, column=0, padx=5,
                                                                                            pady=5)

# Buttons 1 to 9, try with loop, later.
btn0 = Button(root, text='0', padx=12, pady=8)
btn1 = Button(root, text='1', padx=12, pady=8)
btn2 = Button(root, text='2', padx=12, pady=8)
btn3 = Button(root, text='3', padx=12, pady=8)
btn4 = Button(root, text='4', padx=12, pady=8)
btn5 = Button(root, text='5', padx=12, pady=8)
btn6 = Button(root, text='6', padx=12, pady=8)
btn7 = Button(root, text='7', padx=12, pady=8)
btn8 = Button(root, text='8', padx=12, pady=8)
btn9 = Button(root, text='9', padx=12, pady=8)

# Operator buttons
plus = Button(root, text='+', padx=12, pady=8)
minus = Button(root, text='-', padx=12, pady=8)
multiplication = Button(root, text='*', padx=12, pady=8)
division = Button(root, text='÷', padx=12, pady=8)
root.mainloop()
