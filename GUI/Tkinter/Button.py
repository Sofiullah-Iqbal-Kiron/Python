from tkinter import *

# root is main Frame/JFrame/Top-Level-Window in Java.
root = Tk()
root.title('Top Label')

# padx: width, pady: height
# fg=foreground_colour_name_string
# bg=background_colour_name_string
# Colour name string: violet, indigo, blue, green, yellow, orange, red or hexa colour codes(6 digit) like #1abc9c.
# Copy colour codes from https://flatuicolors.com/palette/defo
button0 = Button(root, text='My Button!', padx=50, pady=30, bg='#95a5a6').grid(row=0, column=0)
button1 = Button(root, text='Disabled Button', state=DISABLED).grid(row=1, column=0)


def act_btn_cmd():
    label = Label(root, text='I clicked!').grid(row=3, column=0)


# A button with command to perform a specific action. command = fun_name (Without parenthesis).
# If you put parenthesis after function name the interpreter thinks that the function is called.
# But we not calling it, we just setting a command for the button.
act_btn = Button(root, text='Click Me', padx=30, pady=30, command=act_btn_cmd).grid(row=2, column=0)
# act_btn1 = Button(root, text='Clear Me', padx=20, pady=20, command=act_btn_cmd1).grid(row=4, column=0)

root.mainloop()
