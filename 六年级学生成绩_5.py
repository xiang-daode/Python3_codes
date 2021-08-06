#生成HTML文件:
import random
SA=['六零一','六零二','六零三','六零四','六零五','六零六','六零七','六零八','六零九'] #list列表
with open('六年级学生9个班成绩.html',"w") as f:
    h0='<center><table border=1 bgcolor=#DFE width=60%><tr><td>'
    f.write(h0+'姓名@班级@语文@数学@英语@科学@社会@总分</tr>'.replace('@','</td><td>'))
    for i in range(100):
        s0=SA[i%9]
        s1=str((int)(100*random.random()))
        s2=str((int)(100*random.random()))
        s3=str((int)(100*random.random()))
        s4=str((int)(100*random.random()))
        s5=str((int)(100*random.random()))
        sum=int(s1)+int(s2)+int(s3)+int(s4)+int(s5);
        nm=chr(0x4e00+(int)(20902*random.random()))+chr(0x4e00+(int)(20902*random.random()))
        hi="\n<tr><td>项"+nm+"@"+s0+"@"+s1+"@"+s2+"@"+s3+"@"+s4+"@"+s5+"@"+str(sum)+"</tr>"
        f.write(hi.replace('@','</td><td>'))
f.close()
print('HTML文件已经生成!')
