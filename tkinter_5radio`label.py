# 在这里写上你的代码 :-)
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("First Window")
window.geometry("750x500")



# 按钮与交互:
def selected():
    k=str(rb.get())
    lbl.configure(text=k)
    #可依据k的值作分别的处理:
    #...



rb = IntVar()
rad1 = Radiobutton(window, text="111", value=1, variable=rb, command=selected)
rad2 = Radiobutton(window, text="222", value=2, variable=rb, command=selected)
rad3 = Radiobutton(window, text="333", value=3, variable=rb, command=selected)
rad4 = Radiobutton(window, text="444", value=4, variable=rb, command=selected)
rad5 = Radiobutton(window, text="555", value=5, variable=rb, command=selected)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)
rad5.grid(column=4, row=0)

lbl = Label(window, text="Show selected Radiobutton Value")
lbl.grid(column=0, row=1)

# 运行主程序:
window.mainloop()
