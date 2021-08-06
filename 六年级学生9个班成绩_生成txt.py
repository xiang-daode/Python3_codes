#生成文件:
import random

################    写入文件[覆盖原有文件]    ####################
def mkNM():
    m1=chr(random.randint(0x4e00,0x9fa5))
    m2=chr(random.randint(0x4e00,0x9fa5))
    return m1+m2

SA=['六零一','六零二','六零三','六零四','六零五','六零六','六零七','六零八','六零九'] #list列表
with open('六年级学生9个班成绩.txt',"w") as f:
    f.write('姓名 \t班级 \t语文 \t数学 \t英语 \t科学 \t社会 \t总分\n')
    for i in range(500): #模拟学生数=500
        s0=SA[i%9]            #s0=str(601+i%9)
        s1=str(random.randint(30,100))
        s2=str(random.randint(5,100))
        s3=str(random.randint(10,100))
        s4=str(random.randint(0,100))
        s5=str(random.randint(30,100))
        sum=int(s1)+int(s2)+int(s3)+int(s4)+int(s5);
        nm=mkNM()
        f.write("项"+nm+" \t"+s0+" \t"+s1+" \t"+s2+" \t"+s3+" \t"+s4+" \t"+s5+" \t"+str(sum)+"\n")
f.close()
print('文件已经生成!')
