#生成data.txt数据文件
import tkinter as tk
import tkinter.messagebox as tb
root = tk.Tk();w = tk.Canvas(root, width = 800, height = 600);w.pack()
P=[]
def paint(event):
        x, y = event.x,event.y
        w.delete('poly1');w.delete('poly2');
        w.create_oval(x-2, y-2, x+2, y+2, fill = "#008",outline="#008")
        #w.create_oval(x-9, y-9, x+9, y+9, fill = "#E00",outline="#0E0")
        #w.create_oval(x-4, y-4, x+4, y+4, fill = "#0E0",outline="#00E")
        P.append([x,y]);#print(P)
        #实心的多边形:
        #w.create_polygon(P,outline='black', fill='#98BAD3', dash=(4,9),tag='poly1')
        #空心的多边形:
        #w.create_polygon(P,outline='#005', fill='', dash=(4,1),tag='poly2')
        w.update()
def save():
    with open("data.txt","w") as fw:
        for p in P:
            fw.write("{0},{1}\n".format(p[0],p[1]))
        print('data.txt ---OK')
        tb.showinfo('提示','data.txt ---保存就绪.')
def delAll():
    A=tb.askyesno('提示', '要执行此操作吗')#是/否，返回值true/false
    if A==True:
        P.clear()
        w.delete('all')
        print(A)
#===============================================
#w.bind("<Button-1>", paint)  #[左]键单击
w.bind("<B1-Motion>", paint)  #[左]键连续记录
tk.Button(root, text = "清空重画", command = (lambda: delAll())).pack(side='right')
tk.Button(root, text = '保存数据到"data.txt"中', command = (lambda: save())).pack(side='right')
tk.Label(root, text = "单击鼠标左键绘制绿色点").pack(side = "bottom")
root.mainloop()


