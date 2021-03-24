# 判断n是否质数

def zs(x):
    f=0
    for i in range(2,x):
        if x%i==0:
            f=1
            break;
    if f==1:
        print("不是质数")
    else:
        print("是质数")

n=int(input())
zs(n)