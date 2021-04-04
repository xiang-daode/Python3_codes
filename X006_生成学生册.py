# 在这里写上你的代码 :-)
# 生成学生册与成绩
import random #rnd=random.random()

# 创建新文件(原有文件被覆盖),并写入内容:
fo = open("生成学生册.txt", "w+")
fo.write('序号\t姓名\t年龄\t性别\t语文\t数学\t英语\t科学\n')


x="项"
for i in range(1,101):
    m1=0x4e00+(i^9753)
    m2=0x4e00+(i^2468)
    nm=x+chr(m1)+chr(m2)
    age=random.randint(8,16)
    sex=random.randint(0,1)
    sc1=random.randint(50,100)
    sc2=random.randint(10,100)
    sc3=random.randint(30,100)
    sc4=random.randint(40,100)
    print(i,nm,age,sex,sc1,sc2,sc3,sc4)
    fo.write("%d\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n"%(i,nm,age,sex,sc1,sc2,sc3,sc4))


fo.flush() #涌流[一并写入硬盘文件中]
fo.close()
print("----- 生成学生册.txt已经生成 -----")
