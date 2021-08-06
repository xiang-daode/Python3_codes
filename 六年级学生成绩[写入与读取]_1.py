#生成文件:
import random

################    写入文件[覆盖原有文件]    ####################
'''
SA=['六零一','六零二','六零三','六零四','六零五','六零六','六零七','六零八','六零九'] #list列表
with open('六年级学生9个班成绩.txt',"w") as f:
    f.write('姓名 \t班级 \t语文 \t数学 \t英语 \t科学 \t社会 \t总分\n')
    for i in range(500): #模拟学生数=500
        s0=SA[i%9]            #s0=str(601+i%9)
        s1=str((int)(100*random.random()))
        s2=str((int)(100*random.random()))
        s3=str((int)(100*random.random()))
        s4=str((int)(100*random.random()))
        s5=str((int)(100*random.random()))
        sum=int(s1)+int(s2)+int(s3)+int(s4)+int(s5);
        nm=chr(0x4e00+(int)(20902*random.random()))+chr(0x4e00+(int)(20902*random.random()))
        f.write("项"+nm+" \t"+s0+" \t"+s1+" \t"+s2+" \t"+s3+" \t"+s4+" \t"+s5+" \t"+str(sum)+"\n")
f.close()
print('文件已经生成!')
'''
################    读取文件-1:直接扫描文件中的全文并输出    ####################
'''
with open('六年级学生9个班成绩.txt',"r") as fr:
    line=fr.read()
    print(line)
fr.close()
'''

################    读取文件-2:逐行读取两字段:姓名,英语    ####################
'''
with open('六年级学生9个班成绩.txt',"r") as fr:
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        print(s2[0],s2[4])
fr.close()
 '''
################    读取文件-3:逐行读取两字段:(姓名,英语)的常用统计,列表应用    ####################
'''
with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    nm=[];en=[]
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        print(s2[0],s2[4])
        if i>0: #跳过中文表头
            nm.append(s2[0])
            en.append(int(s2[4])) #转为整数,再添加到列表中
        i=i+1
fr.close()
print("人数:{0},总和:{1},最高:{2},最低:{3},平均:{4:0.2f}".format( len(en),sum(en),max(en),min(en),sum(en)/len(en)))
'''

################    读取文件-4:逐行读取两字段:(姓名,英语)的常用统计,字典应用    ####################
'''
with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    dt={}
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        print(s2[0],s2[4])
        if i>0: #跳过中文表头
            dt[s2[0]]=int(s2[4])
        i=i+1
fr.close()
print("人数:{0}".format(len(dt)))
#按英语成绩排序(从小到大),带姓名输出:
dt2=sorted(dt.items(), key=lambda d: d[1], reverse=False)
print(dt2)
#按英语成绩排序(从大到小),带姓名输出:
dt3=sorted(dt.items(), key=lambda d: d[1], reverse=True)
print(dt3)
#按姓氏内码(从大到小),带姓名输出:
dt4=sorted(dt.items(), key=lambda d: d[0])
print(dt4)
'''
################    读取文件-5:逐行读取两字段:(姓名,英语)的筛选与运算,字典应用    ####################
'''
with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    dt=dict() # 或: dt={}
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        #print(s2[0],s2[4])
        if i>0: #跳过中文表头
            dt[s2[0]]=int(s2[4])
        i=i+1
fr.close()

# 筛选出"值在(x>44 且 x<99)区间"的元素:
print("值在(x>44 且 x<99)区间中:")
for m in dt.items():
    #print(m)
    if m[1]>44 and m[1]<99:#m[0]:姓名(字符串), m[1]:成绩(整数)
        print("{}:{}".format(m[0],m[1]))

# 将各元素重新计算(如:乘以某一数字):
print("============将各元素重新计算-->生成新字典==================")
dt2={} #新字典
for m in dt.items():
    dt2[m[0]]=m[1]*10 #m[0]:姓名(字符串), m[1]:成绩(整数)
print(dt2)  #输出新字典
'''

################    读取文件-6:逐行读取两字段:(姓名,英语)的高级统计,列表应用    ####################
'''
with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    nm=[];MyList=[]
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        print(s2[0],s2[4])
        if i>0: #跳过中文表头
            nm.append(s2[0])
            MyList.append(int(s2[4])) #转为整数,再添加到列表中
        i=i+1
fr.close()

import numpy as np #依赖numpy库计算List

#计数与求和:
a_sum = np.sum(MyList)
print("个数=%d" % len(MyList),",和为：%0.2f" % a_sum)
#求均值:
a_mean = np.mean(MyList)
print("平均值为：%0.2f" % a_mean)
#求方差:
a_var = np.var(MyList)
print("方差为：%0.2f" % a_var)
#求标准差:
a_std = np.std(MyList,ddof=1)
print("标准差为:%0.6f" % a_std)
'''
################    读取文件-7:逐行读取各字段的高级统计,列表-->统计图表    ####################
'''
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
'''
