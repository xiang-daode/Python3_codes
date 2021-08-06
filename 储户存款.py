#生成文件:
import random

def mkPID():
    s1="330523"
    s2=random.randint(1920,2021)
    s3=random.randint(1,12)
    s4=random.randint(1,30)
    s5=random.randint(1000,9999)
    z2=str(s2)
    if s3<10:
       z3='0'+str(s3)
    else:
       z3=str(s3)
    if s4<10:
       z4='0'+str(s4)
    else:
       z4=str(s4)
    z5=str(s5)
    zz=s1+z2+z3+z4+z5
    return  zz


SA=['溷距小区','债烟小区','内苡小区','胃额小区','界尺小区','贻实小区','内涵小区','通顺小区','保山小区'] #list列表
with open('储户存款表.html',"w") as f:
    h0='<center><table border=1 bgcolor=#DEF width=80%><tr><td>'
    f.write(h0+'姓名@身份证@家庭住址@工商银行@建设银行@湖州银行@嘉兴银行@信用联社@总存款</td></tr>\n'.replace('@','</td><td>'))
    for i in range(50000):
        s0=SA[i%9]  #若用数字: s0=str(601+i%9)
        s1=str(round(999999*random.random(),2))
        s2=str(round(999999*random.random(),2))
        s3=str(round(999999*random.random(),2))
        s4=str(round(999999*random.random(),2))
        s5=str(round(999999*random.random(),2))
        sum=float(s1)+float(s2)+float(s3)+float(s4)+float(s5);
        sum=round(sum,2)
        nm=chr(0x4e00+(int)(20902*random.random()))+chr(0x4e00+(int)(20902*random.random()))
        hi="<tr><td>项"+nm+"@"+mkPID()+"@"+s0+"@"+s1+"@"+s2+"@"+s3+"@"+s4+"@"+s5+"@"+str(sum)+"</td></tr>\n"
        f.write(hi.replace('@','</td><td>'))
f.close()
print('HTML文件已经生成!')


