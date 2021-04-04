# 在这里写上你的代码 :-)
from tkinter import *

#题目072_tkinter`Listbox


def main():
    root = Tk()

    my_lb = Listbox(root,width =8, height = 15)
    my_lb.pack()

    my_list = ["星星", "贪狼", "巨门", "禄存", "文曲", "廉贞", "武曲", "破军", "左辅", "右弼"]

    Button(root, text = "删除'星星'", command = (lambda:my_lb.delete(0))).pack()
    Button(root, text = "添加'屁屁'", command = (lambda:my_lb.insert(END, '屁屁'))).pack()

    for item in my_list:
        my_lb.insert(END, item)

    # 删除索引值为 0 的元素 "星星":
    # my_lb.delete(0)



    mainloop()


if __name__ == '__main__':
    main()
