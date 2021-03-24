# 计算n，m的最大公约数
def gys(x,y):
    if x>y:
        z=y
    else:
        z=x
    f=1
    for i in range(z-1,2,-1):
        if(x%i==0 and y%i==0):
            f=f*i
    print(f)

n=int(input())
m=int(input())
gys(n,m)