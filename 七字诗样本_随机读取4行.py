# 在这里写上你的代码 :-)
import random
import datetime
#建立时间对象:
dt=datetime.datetime.now()


#建立列表对象:
newLines=[] #新的各行

#读取原文件("UTF-8"),生成新newLines:
with open("七字诗样本.TXT", "r",-1,"UTF-8") as f:
    txt=f.read()
    newLines=txt.split(',')
    f.close() #文件关闭

#新内容写入文件中:
with open("七字诗样本_新四行.TXT", "w") as f:
    N=len(newLines)
    for i in range(3): #生成前三句
        rnd=random.randint(0,N-1)
        f.write(newLines[rnd]+"，\n") #补上:列表中每一个元素的换行符
    #最后一句使用句号：
    rnd=random.randint(0,N-1)
    f.write(newLines[rnd]+"。\n") #补上:列表中每一个元素的换行符
    f.write("--------- 作者： 项道德\n"+dt.strftime("%Y-%m-%d %H:%M:%S")) #补上:列表中每一个元素的换行符

    f.flush() #涌流
    f.close() #文件关闭

print("=======  OK,新内容已经写入文件中  ========")




