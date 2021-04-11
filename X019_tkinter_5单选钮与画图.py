# 在这里写上你的代码 :-)
from tkinter import *
#from tkinter.ttk import * #使用风格时就不用这行,否则风格无效的

window = Tk()
window.title("tkinter_canvas 绘图设计器     ---设计:daode1212")
window.geometry("900x720+300+20")

canvas =Canvas(width=895, height=650, bg='white')
canvas.grid(column=0, row=3, columnspan=5)

# 按钮与交互:
def selected():
    k=rb.get()
    lbl.configure(text=str(k)+'号图片已经就绪.   ----设计师: 项道德,  2021-04-10')
    #可依据k的值作分别的处理:
    #...
    if k==1:
        canvas.create_oval(200-100,200-100,400+100,300+100,fill='#7788FF')
    if k==2:
        canvas.create_oval(300-200,300-100,400+200,300+100,fill='#ff4899')
    if k==3:
        canvas.create_oval(400-160,300-100,400+160,300+100,fill='#77ffee')
    if k==4:
        canvas.create_oval(500-100,300-190,400+100,300+190,fill='#4488FF')
    if k==5:
        canvas.delete('all')
        #canvas.create_oval(400-100,300-100,400+100,300+100,fill='#ee44FF')


rb = IntVar()
rad1 = Radiobutton(window, text="画个图1", value=1, variable=rb, command=selected)
rad2 = Radiobutton(window, text="画个图2", value=2, variable=rb, command=selected)
rad3 = Radiobutton(window, text="画个图3", value=3, variable=rb, command=selected)
rad4 = Radiobutton(window, text="画个图4", value=4, variable=rb, command=selected)
rad5 = Radiobutton(window, text="全部清空", value=5, variable=rb, command=selected)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)
rad5.grid(column=4, row=0)

lbl = Label(window, text="---------  设计: 项道德  ----------------")
lbl.config(bd=5,relief = SUNKEN)
'''
风格可选：
FLAT_平、SUNKEN_凹、RAISED_凸、GROOVE_槽、RIDGE_脊。默认为: FLAT_平。
'''
lbl.config(cursor='gumby')
'''
光标可选:
gumby_小绿人冈比、watch_手表、pencil_铅笔、crdss_十字、 hand2_手形2
'''
lbl.config(bg='#334466',fg='#ddee44')
lbl.config(font=("Times", 12, "bold"))
lbl.grid(column=0, row=4, columnspan=5)

# 运行主程序:
window.mainloop()
