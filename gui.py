# import tkinter module and alias tk to simplify 
##import tkinter as tk  
##
##win1 = tk.Tk()
##win1.title('Python GUI')
##win1.mainloop() #start gui


# prevent the gui from being resized
##import tkinter as tk
##
##win2 = tk.Tk()
##win2.title('Python GUI')
##win2.resizable(0, 0)
##win2.mainloop()


# adding a label to GUI form
# ttk module has some advanced widgets that make GUI look greath
##import tkinter as tk
##from tkinter import ttk 
##
##win3  = tk.Tk()
##ttk.Label(win, text = 'A label').grid(column = 0, row = 0)
##win3.mainloop()


# creating buttons and changing their text property

##import tkinter as tk
##from tkinter import ttk
##
##win4 = tk.Tk()
##aLabel = ttk.Label(win4, text = 'A Label')
##aLabel.grid(column = 0, row = 0)
##
##def clickme():
##    action.configure(text = '** I have been Clicked! **')
##    aLabel.configure(foreground = 'red')
##
##action = ttk.Button(win4, text = 'Click me!', command = clickme)
##action.grid(column = 1 , row = 0)
##
##win4.mainloop()

# Text box widgets

##import tkinter as tk
##from  tkinter import ttk
##
##win5 = tk.Tk()
##win5.title('GUI')
##
##def clickme():
##    button_1.configure(text = 'Hello! ' + name.get())
##
### configure the Button
##button_1 = ttk.Button(win5, text = 'Click me', command = clickme) 
##button_1.grid(column = 1, row =1)
##
### configure the Label
##label_1 = ttk.Label(win5, text = 'Enter a name')
##label_1.grid(column = 0, row =0)
##
### configure the textbox entry widget
##name = tk.StringVar()
##tbEntery_1 = ttk.Entry(win5, width =12, textvariable = name)
##tbEntery_1.grid(column = 0, row =1)
##tbEntery_1.focus() # 当GUI出现时，cursor会出现在输入框
##
##win5.mainloop()


# combo bos widgets


















































    
