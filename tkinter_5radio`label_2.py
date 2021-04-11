# 在这里写上你的代码 :-)
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("First Window")
window.geometry("900x700")

canvas =Canvas(width=895, height=650, bg='white')
canvas.grid(column=0, row=3, columnspan=5)

# 按钮与交互:
def selected():
    k=rb.get()
    lbl.configure(text=str(k)+'号图片已经就绪.   ----设计师:项道德,2021-04-10')
    #可依据k的值作分别的处理:
    #...
    if k==1:
        canvas.create_oval(400-100,300-100,400+100,300+100,fill='#7788FF')
    if k==2:
        canvas.create_oval(400-200,300-100,400+200,300+100,fill='#ff4899')
    if k==3:
        canvas.create_oval(400-160,300-100,400+160,300+100,fill='#77ffee')
    if k==4:
        canvas.create_oval(400-100,300-190,400+100,300+190,fill='#4488FF')
    if k==5:
        canvas.create_oval(400-100,300-100,400+100,300+100,fill='#ee44FF')


rb = IntVar()
rad1 = Radiobutton(window, text="画个图1", value=1, variable=rb, command=selected)
rad2 = Radiobutton(window, text="画个图2", value=2, variable=rb, command=selected)
rad3 = Radiobutton(window, text="画个图3", value=3, variable=rb, command=selected)
rad4 = Radiobutton(window, text="画个图4", value=4, variable=rb, command=selected)
rad5 = Radiobutton(window, text="画个图5", value=5, variable=rb, command=selected)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)
rad5.grid(column=4, row=0)

lbl = Label(window, text="---------  设计: 项道德  ----------------")
lbl.grid(column=0, row=4, columnspan=5)

# 运行主程序:
window.mainloop()
