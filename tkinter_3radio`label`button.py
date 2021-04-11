# 在这里写上你的代码 :-)
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("First Window")
window.geometry("750x500")

selected = IntVar()
lbl = Label(window, text="Show selected Radiobutton Value")


rad1 = Radiobutton(window, text="First", value=1, variable=selected)
rad2 = Radiobutton(window, text="Second", value=2, variable=selected)
rad3 = Radiobutton(window, text="Third", value=3, variable=selected)

#按钮与交互:
def clicked():
    lbl.configure(text=selected.get())
btn = Button(window, text="Click Me", command=clicked)

#各控件布局:
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=4, row=0)
lbl.grid(column=0, row=1)

#运行主程序:
window.mainloop()
