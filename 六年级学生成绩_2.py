#生成文件:
import random

with open('六年级学生9个班成绩.txt',"w") as f:
    f.write('姓名 \t班级 \t语文 \t数学 \t英语 \t科学 \t社会 \t总分\n')
    for i in range(500):
        s1=str((int)(100*random.random()))
        s2=str((int)(100*random.random()))
        s3=str((int)(100*random.random()))
        s4=str((int)(100*random.random()))
        s5=str((int)(100*random.random()))
        sum=int(s1)+int(s2)+int(s3)+int(s4)+int(s5);
        f.write("项道德 \t600 \t"+s1+" \t"+s2+" \t"+s3+" \t"+s4+" \t"+s5+" \t"+str(sum)+"\n")
f.close()
print('文件已经生成!')
