# 在这里写上你的代码 :-)
import random

#建立列表对象:
a2=[] #姓名
newLines=[] #新的各行

#读取原文件,生成新newLines:
with open("仿员工名册.TXT", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')  #去掉:列表中每一个元素的换行符
        if("姓名" in  line):
           newLines.append(line)
        #第2行[含]以后,开始为各列表对象装载数据
        if(not "姓名" in  line):
            b=line.split('\t') #剥离各字段,放入元组b中
            ##合成新姓名:
            k1=random.randint(0x4e00,0x9fa5)#第一汉字码
            k2=random.randint(0x4e00,0x9fa5)#第二汉字码
            nm1=b[1][0]+chr(k1)+chr(k2)#合成新姓名:原姓氏+汉字1+汉字2
            #原先单位改为大学:
            k3=random.randint(0x4e00,0x9fa5)#第3汉字码
            k4=random.randint(0x4e00,0x9fa5)#第4汉字码
            b4=chr(k3)+chr(k4)+"大学" #原先单位改为XX大学
            #合成新字符串:
            newLn='\t'.join([b[0],nm1,b[2],b[3],b4,b[5]]) #各行新内容
            #加入到列表对象newLines中:
            newLines.append(newLn)
    f.close() #文件关闭

#新内容写入文件中:
with open("仿员工名册.TXT", "w") as f:
    for line in newLines:
            f.write(line+"\n") #补上:列表中每一个元素的换行符
    f.flush() #涌流
    f.close() #文件关闭



print("=======  OK,新内容已经写入文件中  ========")




