import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  

win = tk.Tk()
win.title('Radio Button')

EnterName = ttk.Label(win, text = 'Enter a name')
EnterName.grid(column = 0, row = 0)

ChooseNumber = ttk.Label(win, text = 'Choose  a name')
ChooseNumber.grid(column = 1, row = 0)

name = tk.StringVar()
Entry_EN = ttk.Entry(win, textvariable = name)
Entry_EN.grid(column = 0, row = 1)
Entry_EN.focus()

number = tk.StringVar()
Combox_CN = ttk.Combobox(win, textvariable = number,
                         state = '', width = 12)
Combox_CN.grid(column = 1, row = 1)
Combox_CN['value'] = (1, 2, 3, 4)
Combox_CN.current(0)

def Click():
    ClickMe.configure(text = name.get() + ' ' + number.get())
    
ClickMe = ttk.Button(win, text = 'Click Me !', command = Click)
ClickMe.grid(column = 2, row = 1)


chVarDis = tk.IntVar()
check_1 = tk.Checkbutton(win, text = 'Disabled', variable = chVarDis,
                         state = 'disabled')
check_1.select()
check_1.grid(column = 0, row = 4, sticky = tk.W)
# tk.W :the widgets will be aligned to the west of the gird

chVarUn = tk.IntVar()
Check_2 = tk.Checkbutton(win, text = 'Unchecked', variable = chVarUn)
Check_2.deselect()  # do not place a checkmark into the Checkbutton
Check_2.grid(column = 1, row = 4, sticky = tk.W)

chVarEn = tk.IntVar()
Check_3 = tk.Checkbutton(win, text = 'Enabled', variable = chVarEn)
Check_3.select()  # place a checkmark into the Checkbutton
Check_3.grid(column = 2, row = 4, sticky = tk.W)

Color1 = 'Blue'
Color2 = 'Gold'
Color3 = 'Red'

# radio button callback
# 单选项
def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background = Color1)
    elif radSel == 2:
        win.configure(background = Color2)
    elif radSel == 3:
        win.configure(background = Color3)

radVar = tk.IntVar()
RadioButton_1 = tk.Radiobutton(win, text = Color1, variable = radVar,
                               value = 1, command = radCall)
RadioButton_1.grid(column = 0, row = 5, sticky = tk.W)

RadioButton_2 = tk.Radiobutton(win, text = Color2, variable = radVar,
                               value = 2, command = radCall)
RadioButton_2.grid(column = 1, row = 5, sticky = tk.W)

RadioButton_3 = tk.Radiobutton(win, text = Color3, variable = radVar,
                               value= 3, command =radCall)
RadioButton_3.grid(column = 2, row = 5, sticky = tk.W)

# scrolled text widgets

ScrollWidth = 40  # magic number found by experimentation to work well
ScrollHeight = 3

# wrap = tk.WORD  : break line by words
ScrolledText_1 = scrolledtext.ScrolledText(win, width = ScrollWidth,
                                           height = ScrollHeight,
                                           wrap = tk.WORD)
ScrolledText_1.grid(column = 0, columnspan = 3)

# create a container to hold labels
LabelFrame = ttk.LabelFrame(win, text = 'Label in a Frame')
# use padding add space around widgets, padx  pady 
LabelFrame.grid(column = 0, row = 7, padx = 20, pady = 40)

#place labels into the container element
ttk.Label(LabelFrame, text = 'Label_1').grid(column = 0, row = 0)
ttk.Label(LabelFrame, text = 'Label_2').grid(column = 1, row = 0)
ttk.Label(LabelFrame, text = 'Label_3').grid(column = 2, row = 0)

win.mainloop()
