# 在这里写上你的代码 :-)
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

#窗体:
window = Tk()
window.title("First Window")
window.geometry("350x200")


def fun3():
    bar["value"] = 30

# 按钮1:
btn = Button(window, text="再来30%", command=fun3).pack(side='top')
#btn.grid(column=0, row=0)

def fun4():
    bar["value"] = 70

# 按钮2:
btn = Button(window, text="再来70%", command=fun4).pack(side='top')
#btn.grid(column=0, row=0)

#风格:
style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background="#447799")

bar = Progressbar(window, length=350, style="black.Horizontal.TProgressbar")
#进度条:
bar["value"] = 70  # 百分比
bar.pack(side='bottom')
#bar.grid(column=0, row=1)

# 运行主程序:
window.mainloop()
