# 在这里写上你的代码 :-)
import random

#建立列表对象:
a2=[] #姓名
newLines=[] #新的各行

#读取原文件,生成新newLines:
with open("学生成绩226行.TXT", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')  #去掉:列表中每一个元素的换行符
        if("姓名" in  line): #先记下表头行
           newLines.append(line)
        #第2行[含]以后,开始为各列表对象装载数据
        if(not "姓名" in  line):
            b=line.split('\t') #剥离各字段,放入元组b中
            nm0=b[2]  #原姓名,因为:0_班级,1_考号,2_姓名,...
            k1=random.randint(0x4e00,0x9fa5)#第一汉字码
            k2=random.randint(0x4e00,0x9fa5)#第二汉字码
            nm1=b[2][0]+chr(k1)+chr(k2)#合成新姓名:原姓氏+汉字1+汉字2
            newLn=line.replace(nm0,nm1)#各行替换成新姓名
            #print(nm0," --->> ",nm1,newLn)
            newLines.append(newLn)#加入到列表对象newLines中
    f.close() #文件关闭

#新内容写入文件中:
with open("学生成绩226行.TXT", "w") as f:
    for line in newLines:
        f.write(line+"\n") #补上:列表中每一个元素的换行符
    f.flush() #涌流
    f.close() #文件关闭



print("=======  OK,新内容已经写入文件中  ========")




