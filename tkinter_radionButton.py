from tkinter import *


def selection():
    selection = "You selected the option " + str(radio.get())
    label.config(text=selection)


top = Tk()
top.geometry("600x450")
radio = IntVar()

#用于提示信息:
lbl = Label(text="你最擅长的编程语言是:\n============================================")
lbl.pack()

#以下N个单选钮:
R1 = Radiobutton(top, text="Python", variable=radio, value=1,command=selection)
R1.pack()

R2 = Radiobutton(top, text="C,C++,C#", variable=radio, value=2,command=selection)
R2.pack()

R3 = Radiobutton(top, text="Java", variable=radio, value=3,command=selection)
R3.pack()

R4 = Radiobutton(top, text="HTML,PHP", variable=radio, value=4,command=selection)
R4.pack()

#用于输出显示:
label = Label(top)
label.pack()

top.mainloop()