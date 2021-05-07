# 在这里写上你的代码 :-)

import tkinter as tk

root = tk.Tk()
w = tk.Canvas(root, width = 800, height = 600)
w.pack()
L1x=[];L1y=[];
L2x=[];L2y=[];
L3x=[];L3y=[];
def paint(event):
        x1, y1 = (event.x - 3), (event.y - 3)
        x2, y2 = (event.x + 3), (event.y + 3)
        w.create_oval(x1, y1, x2, y2, fill = "red")
        L1x.append(event.x);L1y.append(event.y);
def paint2(event):
        x1, y1 = (event.x - 4), (event.y - 4)
        x2, y2 = (event.x + 4), (event.y + 4)
        w.create_line(x1, y1, x2, y2, fill = "green")
        w.create_line(x1, y2, x2, y1, fill = "green")
        L2x.append(event.x);L2y.append(event.y);
def paint3(event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        w.create_rectangle(x1, y1, x2, y2, outline='#f040f0', fill = "#202060")
        L3x.append(event.x);L3y.append(event.y);

def deleteAll():
    w.delete('all')
    L1x=[];L1y=[];
    L2x=[];L2y=[];
    L3x=[];L3y=[];
def saveData():
    path = 'mouseData.py'
    with open(path,'w') as f:
        f.write('L1=[')
        for i in range(len(L1x)):
           f.write(str(L1x[i]-400)+","+str(300-L1y[i])+",")
        f.write(']\nL2=[')
        for i in range(len(L2x)):
           f.write(str(L2x[i]-400)+","+str(300-L2y[i])+",")
        f.write(']\nL3=[')
        for i in range(len(L3x)):
           f.write(str(L3x[i]-400)+","+str(300-L3y[i])+",")
        f.write(']')
w.bind("<B1-Motion>", paint) #[左]键
w.bind("<B2-Motion>", paint2) #[中]键
w.bind("<B3-Motion>", paint3) #[右]键
tk.Button(root, text = "清空重画", command = (lambda: deleteAll())).pack(side='right')
tk.Button(root, text = "保存所有数据", command = (lambda: saveData())).pack(side='right')
tk.Label(root, text = "按住鼠标[左|中|右]键并移动，开始绘制[三种颜色+三种花色]的图画").pack(side = "bottom")

root.mainloop()
