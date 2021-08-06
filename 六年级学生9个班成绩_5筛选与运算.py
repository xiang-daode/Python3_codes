################    读取文件-5:逐行读取两字段:(姓名,英语)的筛选与运算,字典应用    ####################

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
'''
print("值在(x>44 且 x<99)区间中:")
for m in dt.items():
    #print(m)
    if m[1]>44 and m[1]<99:#m[0]:姓名(字符串), m[1]:成绩(整数)
        print("{}:{}".format(m[0],m[1]))

#使用lambda表达式在字典中的数据筛选:
L5=list(filter(lambda x: x[1]>44 and x[1]<99,dt.items()))
print(L5[0:10])
'''

'''
# 将各元素重新计算(如:乘以某一数字):
print("============将各元素重新计算-->生成新字典==================")
dt2={} #新字典
for m in dt.items():
    dt2[m[0]]=m[1]*10 #m[0]:姓名(字符串), m[1]:成绩(整数)
print(dt2)  #输出新字典

#使用lambda表达式在字典中的数据运算(可加减乘除运算):
L5b=list(map(lambda x: x[1]*10,dt.items()))
print(L5b[0:5])

#使用lambda表达式在字典中的数据运算(乘以浮点数后取整):
L5c=list(map(lambda x: round(x[1]*2.71828,2),dt.items()))
print(L5c[0:5])

#使用lambda表达式在字典中的数据运算(姓名中第三个汉字的内码):
L5d=list(map(lambda x: hex(ord(x[0][2])),dt.items()))
print(L5d[0:5])

#使用lambda表达式在字典中的数据运算(整数-->二进制):
L5e=list(map(lambda x: bin(x[1]),dt.items()))
print(L5e[0:10])
'''

