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
# 创建窗口
root = Tk()
root.title('绘制图形项')
# 创建并添加Canvas
cv = Canvas(root, background='white', width=830, height=830)
cv.pack(fill=BOTH, expand=YES)
columnFont = ('微软雅黑', 18)
titleFont = ('微软雅黑', 20, 'bold')

# 使用循环绘制文字
for i, st in enumerate(['默认', '指定边宽', '指定填充', '边框颜色', '位图填充']):
    cv.create_text((130 + i * 140, 20),text = st,
    font = columnFont,
    fill='gray',
    anchor = W,
    justify = LEFT)


# 绘制文字
cv.create_text(10, 60, text = '绘制矩形',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义列表，每个元素的4个值分别指定边框宽度、填充色、边框颜色、位图填充
options = [(None, None, None, None),
(4, None, None, None),
(4, 'pink', None, None),
(4, 'pink', 'blue', None),
(4, 'pink', 'blue', 'error')]


# 采用循环绘制5个矩形
for i, op in enumerate(options):
    cv.create_rectangle(130 + i * 140, 50, 240 + i * 140, 120,
    width = op[0], # 边框宽度
    fill = op[1], # 填充颜色
    outline = op[2], # 边框颜色
    stipple = op[3]) # 使用位图填充

# 绘制文字
cv.create_text(10, 160, text = '绘制椭圆',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义列表，每个元素的4个值分别指定边框宽度、填充色、边框颜色、位图填充
options = [(None, None, None, None),
(4, None, None, None),
(4, 'pink', None, None),
(4, 'pink', 'blue', None),
(4, 'pink', 'blue', 'error')]

# 采用循环绘制5个椭圆
for i, op in enumerate(options):
    cv.create_oval(130 + i * 140, 150, 240 + i * 140, 220,
    width = op[0], # 边框宽度
    fill = op[1], # 填充颜色
    outline = op[2], # 边框颜色
    stipple = op[3]) # 使用位图填充

# 绘制文字
cv.create_text(10, 260, text = '绘制多边形',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义列表，每个元素的4个值分别指定边框宽度、填充色、边框颜色、位图填充
options = [(None, "", 'black', None),
(4, "", 'black', None),
(4, 'pink', 'black', None),
(4, 'pink', 'blue', None),
(4, 'pink', 'blue', 'error')]

# 采用循环绘制5个多边形
for i, op in enumerate(options):
    cv.create_polygon(130 + i * 140, 320, 185 + i * 140, 250, 240 + i * 140, 320,
    width = op[0], # 边框宽度
    fill = op[1], # 填充颜色
    outline = op[2], # 边框颜色
    stipple = op[3]) # 使用位图填充

# 绘制文字
cv.create_text(10, 360, text = '绘制扇形',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义列表，每个元素的4个值分别指定边框宽度、填充色、边框颜色、位图填充
options = [(None, None, None, None),
(4, None, None, None),
(4, 'pink', None, None),
(4, 'pink', 'blue', None),
(4, 'pink', 'blue', 'error')]

# 采用循环绘制5个扇形
for i, op in enumerate(options):
    cv.create_arc(130 + i * 140, 350, 240 + i * 140, 420,
    width = op[0], # 边框宽度
    fill = op[1], # 填充颜色
    outline = op[2], # 边框颜色
    stipple = op[3]) # 使用位图填充

# 绘制文字
cv.create_text(10, 460, text = '绘制弓形',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义列表，每个元素的4个值分别指定边框宽度、填充色、边框颜色、位图填充
options = [(None, None, None, None),
(4, None, None, None),
(4, 'pink', None, None),
(4, 'pink', 'blue', None),
(4, 'pink', 'blue', 'error')]

# 采用循环绘制5个弓形
for i, op in enumerate(options):
    cv.create_arc(130 + i * 140, 450, 240 + i * 140, 520,
    width = op[0], # 边框宽度
    fill = op[1], # 填充颜色
    outline = op[2], # 边框颜色
    stipple = op[3], # 使用位图填充
    start = 30, # 指定起始角度
    extent = 60, # 指定逆时针转过角度
    style = CHORD) # CHORD指定绘制弓

# 绘制文字
cv.create_text(10, 560, text = '仅绘弧',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义列表，每个元素的4个值分别指定边框宽度、填充色、边框颜色、位图填充
options = [(None, None, None, None),
(4, None, None, None),
(4, 'pink', None, None),
(4, 'pink', 'blue', None),
(4, 'pink', 'blue', 'error')]

# 采用循环绘制5个弧
for i, op in enumerate(options):
    cv.create_arc(130 + i * 140, 550, 240 + i * 140, 620,
    width = op[0], # 边框宽度
    fill = op[1], # 填充颜色
    outline = op[2], # 边框颜色
    stipple = op[3], # 使用位图填充
    start = 30, # 指定起始角度
    extent = 60, # 指定逆时针转过角度
    style = ARC) # ARC指定仅绘制弧

# 绘制文字
cv.create_text(10, 660, text = '绘制直线',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义列表，每个元素的5个值分别指定边框宽度、线条颜色、位图填充、箭头风格, 箭头形状
options = [(None, None, None, None, None),
(6, None, None, BOTH, (20, 40, 10)),
(6, 'pink', None, FIRST, (40, 40, 10)),
(6, 'pink', None, LAST, (60, 50, 10)),
(8, 'pink', 'error', None, None)]

# 采用循环绘制5个弧
for i, op in enumerate(options):
    cv.create_line(130 + i * 140, 650, 240 + i * 140, 720,
    width = op[0], # 边框宽度
    fill = op[1], # 填充颜色
    stipple = op[2], # 使用位图填充
    arrow = op[3], # 箭头风格
    arrowshape = op[4]) # 箭头形状

# 绘制文字
cv.create_text(10, 760, text = '绘制位图\n图片、组件',
font = titleFont,
fill='magenta',
anchor = W,
justify = LEFT)
# 定义包括create_bitmap, create_image, create_window三个方法的数组
funcs = [Canvas.create_bitmap, Canvas.create_image, Canvas.create_window,Canvas.create_window]


def myFun(n):
    print(n*n)


# 为上面4个方法定义选项
items = [
{'bitmap' : 'questhead'},
{'image':PhotoImage(file='按钮.png')},
{'window':Button(cv,text = '单击我1', padx=10, pady=5,command = lambda :print('按钮单击1')),'anchor': W},
{'window':Button(cv,text = '单击我2', padx=20, pady=5,command = lambda :myFun(8)),'anchor': W}
]

for i, func in enumerate(funcs):
    func(cv, 230 + i * 140, 780, **items[i])


root.mainloop()

