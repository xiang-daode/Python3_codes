# 在这里写上你的代码 :-)

#建立各列表对象:
a0=[] #序号
a1=[] #姓名
a2=[] #年龄
a3=[] #性别
a4=[] #语文
a5=[] #数学
a6=[] #英语
a7=[] #科学
a8=[] #总分


with open("生成学生册.txt", "r") as f:

    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        #跳过第一行,开始为各列表对象装载数据
        if(line !="序号	姓名	年龄	性别	语文	数学	英语	科学"):
            b=line.split('\t')
            a0.append(int(b[0]))  #序号
            a1.append((b[1]))     #姓名
            a2.append(int(b[2]))  #年龄
            a3.append(int(b[3]))  #性别
            a4.append(int(b[4]))  #语文
            a5.append(int(b[5]))  #数学
            a6.append(int(b[6]))  #英语
            a7.append(int(b[7]))  #科学
            a8.append(int(b[4])+int(b[5])+int(b[6])+int(b[7]))  #总分
#====================================================
n=len(a0) #总人数
print("人数=",n)
print("平均年龄=",sum(a2)/n)
print("男生人数=",sum(a3))
print("语文[均分]=",sum(a4)/n)
print("数学[均分]=",sum(a5)/n)
print("英语[均分]=",sum(a6)/n)
print("科学[均分]=",sum(a7)/n)
print("总分[均分]=",sum(a8)/n)
print("总分[前五名均分]=",sorted(a8,reverse=True)[0:5])
print("总分[后五名均分]=",sorted(a8)[0:5])
maxID=a8.index(max(a8)) #取出最高分的下标[序]
print("第一名:",a0[maxID],a1[maxID],str(a8[maxID])+"分")

#第一名并列人数计算函数:
def count():
    num=0
    mx=max(a8)
    for x in a8 :
        if x==mx:
           num=num+1
    return num

print(count(),"---第一名并列人数")
#使用内置函数,计算第一名并列人数:
n2=a8.count(max(a8))
print(n2,"---第一名并列人数")
