# 在这里写上你的代码 :-)
from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("First Window")
window.geometry("750x400")

lbl = Label(window, text="=========Hello========")
lbl.grid(column=0, row=6)

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"请选择:")
combo.current(5)
combo.grid(column=1, row=1)

chk_state1 = BooleanVar()
chk_state1.set(True) # Set check state
chk_state2 = BooleanVar()
chk_state2.set(False) # Set check state

chk1 = Checkbutton(window, text="Choose1", var=chk_state1)
chk1.grid(column=2, row=1)
chk2 = Checkbutton(window, text="Choose2", var=chk_state2)
chk2.grid(column=3, row=1)


txt = Entry(window, width=10)
txt.grid(column=0, row=2)
txt.focus()


def f1():
    res = "Welcome to 1" +", "+ txt.get()+", "+str(chk_state1.get())+", "+str(chk_state2.get())+", "+combo.get()
    lbl.configure(text=res)

btn1 = Button(window, text="Click Me 1", command=f1)
btn1.grid(column=1, row=3)

def f2():
    res = "Welcome to 2" +", "+ txt.get()+", "+str(chk_state1.get())+", "+str(chk_state2.get())+", "+combo.get()
    lbl.configure(text=res)

btn2 = Button(window, text="Click Me 2", command=f2)
btn2.grid(column=2, row=3)

window.mainloop()
