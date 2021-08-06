################    读取文件-7:逐行读取各字段的高级统计,列表-->统计图表    ####################

with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    #'姓名 \t班级 \t语文 \t数学 \t英语 \t科学 \t社会 \t总分\n'
    nm=[];bj=[];
    L2=[];L3=[];L4=[];L5=[];L6=[];L7=[]
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        #print(s2[0],s2[4])
        if i>0: #跳过中文表头
            L2.append(int(s2[2])) #转为整数,再添加到列表中
            L3.append(int(s2[3])) #转为整数,再添加到列表中
            L4.append(int(s2[4])) #转为整数,再添加到列表中
            L5.append(int(s2[5])) #转为整数,再添加到列表中
            L6.append(int(s2[6])) #转为整数,再添加到列表中
            L7.append(int(s2[7])) #转为整数,再添加到列表中
        i=i+1
fr.close()
#求均值:
import numpy as np #依赖numpy库计算List
L2_mean = np.mean(L2)
print("平均值为：%0.2f" % L2_mean)
L3_mean = np.mean(L3)
print("平均值为：%0.2f" % L3_mean)
L4_mean = np.mean(L4)
print("平均值为：%0.2f" % L4_mean)
L5_mean = np.mean(L5)
print("平均值为：%0.2f" % L5_mean)
L6_mean = np.mean(L6)
print("平均值为：%0.2f" % L6_mean)
L7_mean = np.mean(L7)
print("平均值为：%0.2f" % L7_mean)
#2--6合成新列表:
data=[L2_mean,L3_mean,L4_mean,L5_mean,L6_mean]

##################  生成条形统计图表 ###################
from turtle import *
from random import *

#坐标(x,y), 高度h,宽度w,红r,绿g,蓝b
def drawRect(x,y,h,w,r,g,b):
    pu();color(r,g,b);pencolor(0.5*r,0.5*g,0.5*b);pensize(2)
    goto(x,y);pd()
    begin_fill()
    for k in range(4):
      if k % 2 == 0:
        forward(w)
        left(90)
      else:
        forward(h)
        left(90)
    end_fill()

#将列表数据以条形统计图显示:
#data=[175,225,360,148,262,150,247,320,261,98,189,75,157]
ht();tracer(False)
n=len(data);ww=600 #ww:条形图总宽度
for i in range(n):
    h=5*data[i]
    r=random();g=random();b=random();
    drawRect(ww*(i-n/2)/n,-200,h,ww/n,r,g,b)
pu();goto(-300,-225);pd()
write("=== {0:0.2f} === {1:0.2f} === {2:0.2f} === {3:0.2f} === {4:0.2f} ===".format(data[0],data[1],data[2],data[3],data[4]), False, "left", font=("Arial", 18, "normal")) ;
pu();goto(-200,-250);pd()
write("======= By daode[设计]. 2021-08-05 =======", False, "left", font=("Arial", 12, "normal")) ;




