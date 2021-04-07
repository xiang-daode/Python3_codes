from tkinter import *

#定义函数在先:
def selection():
    si =  str(radio.get())
    #label.config(text=si)
    if si=='1':
        label.config(text=si+',入门学习用,目前最流行!')
    elif si=='2':
        label.config(text=si+',是自动化工程师!')
    elif si=='3':
        label.config(text=si+',是互联网专家!')
    elif si=='4':
        label.config(text=si+',是互联网工程师!')
    else:
        pass

top = Tk()
top.geometry("600x250")
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
label = Label(top,text='============',bg='#FFEEAA')
label.pack()

top.mainloop()