# 在这里写上你的代码 :-)
'''
create_oval:指定左上角和右下角两个点的坐标绘制椭圆
create_rectangle:指定左上角和右下角两个点的坐标绘制矩形
create_arc：指定左上角和右下角两个点的坐标绘制弧。
create_bitmap：指定一个坐标点，用于指定目标元素的绘制位置绘制位图。
create_image：指定一个坐标点，用于指定目标元素的绘制位置绘制图片。
create_line()：指定左上角和右下角两个点的坐标绘制直线。
create_polygon：指定多个点的坐标来作为多边形的多个定点绘制多边形。
create_text：指定一个坐标点，用于指定目标元素的绘制位置绘制文字。
create_window：指定一个坐标点，用于指定目标元素的绘制位置绘制组件。
'''

from tkinter import *
# 创建窗口:
root = Tk()
# 创建并添加Canvas:
cv = Canvas(root, background='white')
cv.pack(fill=BOTH, expand=YES)

#矩形:
cv.create_rectangle(30, 30, 200, 200,
        outline='red', # 边框颜色
        stipple ='question', # 填充的位图
        fill="red", # 填充颜色
        width=5 # 边框宽度
        )

#椭圆:
cv.create_oval(240, 30, 330, 200,
        outline='yellow', # 边框颜色
        fill='pink', # 填充颜色
        width=4 # 边框宽度
        )
root.mainloop()
