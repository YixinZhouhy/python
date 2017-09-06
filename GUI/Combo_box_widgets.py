import tkinter as tk
from tkinter import ttk

def clickMe():
    clickMe_Button.configure(text = 'Hello ' + name_Entry.get() +
                             ' ' + number.get())
    clickMe_Button.configure(state = 'disabled')

win = tk.Tk()
win.title('The gui excerise')

clickMe_Button = ttk.Button(win, text = 'Click me', command = clickMe)
clickMe_Button.grid(column = 2, row = 1)

name_Label = ttk.Label(win, text = 'Enter your name')
name_Label.grid(column = 0, row = 0)

name_Entry = tk.StringVar()
name_Entry = ttk.Entry(win, width = 12, textvariable = name_Entry)
name_Entry.grid(column = 0, row = 1)
name_Entry.focus()  # cursor foucus


label_2 = ttk.Label(win, text = 'Choose a number:')
label_2.grid(column =1, row = 0)

number = tk.StringVar()
number_Combobox = ttk.Combobox(win, width = 12, textvariable = number,
                               state = 'readonly')
number_Combobox['values'] = (1, 2, 4, 42, 100)
number_Combobox.grid(column = 1, row = 1)
number_Combobox.current(0) # assign a default value to be displayed


win.mainloop()
