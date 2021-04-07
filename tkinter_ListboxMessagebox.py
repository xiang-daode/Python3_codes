from tkinter import *
from tkinter import messagebox


top = Tk()
top.geometry("400x350")

#添加文本标签:
lbl = Label(top,text = "你要去哪一国家留学?")
lbl.pack()

#添加列表框:
listbox = Listbox(top)
listbox.insert(1,"India")
listbox.insert(2, "Franch")
listbox.insert(3, "Japan")
listbox.insert(4, "Austrelia")
listbox.insert(5, "England")
listbox.insert(6, "China")
listbox.insert(7, "USA")
listbox.pack()

#取出用户双击的项目:
def printlist(event):
    messagebox.showinfo(title='ha,ha,ha', message=listbox.get(listbox.curselection()))
     #print(listbox.get(listbox.curselection()))

#绑定双击事件与处理函数:
listbox.bind('<Double-Button-1>',printlist)

#this button will delete the selected item from the list:
btn = Button(top, text = "delete", command = lambda listbox=listbox: listbox.delete(ANCHOR))
btn.pack()

#this button will insert 'More':
btn = Button(top, text = "insert", command =  listbox.insert(END,'More'))
btn.pack()




top.mainloop()