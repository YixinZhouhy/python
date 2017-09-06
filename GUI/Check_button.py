import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('hello')

EnterName = ttk.Label(win, text = 'Enter a name :')  # configure label
EnterName.grid(column = 0, row = 0)  # position

ChooseNumber = ttk.Label(win, text = 'Choose a number :')
ChooseNumber.grid(column = 1, row = 0) 

name = tk.StringVar()
Entery_EN = ttk.Entry(win, textvariable = name)
Entery_EN.grid(column = 0, row =1)
Entery_EN.focus() # cursor focus

number = tk.StringVar()
Combox_CN = ttk.Combobox(win, textvariable = number,
                         state = 'readonly', width = 12)  # configure combobox
Combox_CN['value'] = (1, 2, 3, 4) 
Combox_CN.grid(column = 1, row = 1)
Combox_CN.current(0)  # assign a default value to be displayed

# command function
def Click():
    ClickMe.configure(text = name.get() + ' ' + number.get(),
                      state = 'disabled')

ClickMe =  ttk.Button(win, text = 'ClickMe !', command = Click)
ClickMe.grid(column = 2, row = 1)

chVarDis = tk.IntVar()
check_1 = tk.Checkbutton(win, text = 'Disabled', variable = chVarDis,
                         state = 'disabled')
check_1.select()
check_1.grid(column = 0, row = 4, sticky = tk.W)
# tk.W :the widgets will be aligned to the west of the gird

chVarUn = tk.IntVar()
check_2 = tk.Checkbutton(win, text = 'Unchecked', variable = chVarUn)
check_2.deselect()  # do not place a checkmark into the Checkbutton
check_2.grid(column = 1, row = 4, sticky = tk.W)

chVarEn = tk.IntVar()
check_3 = tk.Checkbutton(win, text = 'Enabled', variable = chVarEn)
check_3.select()  # place a checkmark into the Checkbutton
check_3.grid(column = 2, row = 4, sticky = tk.W)

win.mainloop()
