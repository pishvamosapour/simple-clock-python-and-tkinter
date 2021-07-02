from tkinter import *
from tkinter.ttk import *

from time import strftime

win = Tk()
win.title('digital clock')
win.resizable(0, 0)


def time():
    string = strftime("%H:%M:%S:%p")
    label.config(text=string)
    label.after(1000, time)

label = Label(win, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack()
time()

win.mainloop()
