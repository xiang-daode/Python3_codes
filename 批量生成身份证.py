# 批量生成身份证
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

print(mkPID())
