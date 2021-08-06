#枚举万以内各位数字之和等于十八的数
a=range(0,10000,1)
for m in a:
    if len(str(m))==4:
        b0=str(m)[0]
        b1=str(m)[1]
        b2=str(m)[2]
        b3=str(m)[3]
        s=int(b0)+int(b1)+int(b2)+int(b3)
        if s==18:
            print(m,end='_')
    if len(str(m))==3:
        b0=str(m)[0]
        b1=str(m)[1]
        b2=str(m)[2]
        s=int(b0)+int(b1)+int(b2)
        if s==18:
            print(m,end=',')
    if len(str(m))==2:
        b0=str(m)[0]
        b1=str(m)[1]
        s=int(b0)+int(b1)
        if s==18:
            print(m,end='*')


