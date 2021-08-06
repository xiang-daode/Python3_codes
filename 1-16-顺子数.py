# 挑选四位数从千开始各位间关系依次递增的数/计数
a=range(1000,10000,1)
k=0
for m in a:
    b0=str(m)[0]
    b1=str(m)[1]
    b2=str(m)[2]
    b3=str(m)[3]
    if b0<b1<b2<b3: #字符串可按ASCII码比较大小
        print(m,end=' ')
        k=k+1
print(k)



