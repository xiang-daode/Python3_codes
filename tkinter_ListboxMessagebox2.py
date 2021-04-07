from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("320x160") #界面大小,宽度与高度

#添加文本标签:
lbl = Label(top,text = "双击要执行的函数",bg='#FF0099')
lbl.pack()

#标签2:
L2 = Label(top, bd =2,text='........',bg='#FFFF88')
L2.pack(side = 'top')

#添加列表框:
listbox = Listbox(top)
listbox.insert(1, "fun1")
listbox.insert(2, "fun2")
listbox.insert(3, "fun3")
listbox.insert(4, "fun4")
listbox.pack(side='bottom')



#取出用户双击的项目:
def printlist(event):
    s=listbox.get(listbox.curselection())
    if s=='fun1':
       s99='五子登科'
       L2.config(text="大吉大利!  ---" + s)
       messagebox.showinfo(title='计算结果', message=s99)
    elif s=='fun2':
       s99 = '旗开得胜'
       L2.config(text="财源滚滚!  ---" + s)
       messagebox.showinfo(title='计算结果', message= s99)
    elif s=='fun3':
       s99 = '马到成功'
       L2.config(text="妙笔生花!  ---" + s)
       messagebox.showinfo(title='计算结果', message= s99)
    elif s=='fun4':
       s99 = '战无不胜'
       L2.config(text="前程无量!  ---" + s)
       messagebox.showinfo(title='计算结果', message= s99)
    else:
       s99='天方夜谭'
       L2.config(text="大吉大利!  ---" + s)
       messagebox.showinfo(title='计算结果', message=s99)



#绑定双击事件与处理函数:
listbox.bind('<Double-Button-1>',printlist)


top.mainloop()