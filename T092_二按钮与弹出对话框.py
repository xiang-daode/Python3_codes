# 在这里写上你的代码 :-)
from tkinter import messagebox
import tkinter as tk
top = tk.Tk()

#这里四个参数分别为：宽、高、左、上
top.geometry("600x400+50+50")
top.title("凡事要想一想")


def okCallBack1():
    tk.messagebox.askokcancel("title1","info1")
def okCallBack2():
    tk.messagebox.askokcancel("title2","info2")

btnOk = tk.Button(top,text='按钮1',command = okCallBack1)
btnOk.pack();

btnOk = tk.Button(top,text='按钮2',command = okCallBack2)
btnOk.pack();


top.mainloop();
