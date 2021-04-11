from tkinter import *


def selection():
    k=radio.get()
    #根据k的值,作分别处理:
    if k==1:
        s='十六进制是0xFFFFFF'
        label.config(text=s)
    if k==2:
        s='十六进制是0x000000'
        label.config(text=s)


top = Tk()
top.geometry("600x450")
radio = IntVar()

#用于输出显示:
label = Label(text="======  输出区域  =======",padx=10,pady=10)
label.config(bd=10,relief = SUNKEN)
'''
风格可选：
FLAT_平、SUNKEN_凹、RAISED_凸、GROOVE_槽、RIDGE_脊。默认为: FLAT_平。
'''
label.config(cursor='gumby')
'''
光标可选:
gumby_小绿人冈比、watch_手表、pencil_铅笔、crdss_十字、 hand2_手形2
'''
label.config(bg='#334466',fg='#ddeeff')
label.config(font=("Times", 20, "bold"))
label.pack()

#用于提示信息:
lbl = Label(text="请选择:")
lbl.pack(side='left')

#以下N个单选钮:
R1 = Radiobutton(top, text="白色", variable=radio, value=1,command=selection)
R1.pack(side='left')

R2 = Radiobutton(top, text="黑色", variable=radio, value=2,command=selection)
R2.pack(side='left')

top.mainloop()
